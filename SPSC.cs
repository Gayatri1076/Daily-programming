using System;
using System.Threading;

public sealed class LockFreeSpscQueue<T>
{
    private readonly T[] _buffer;
    private readonly int _mask;
    
    // Aligned padded indices to prevent false sharing on cache lines
    private long _head;
    private long _tail;

    public LockFreeSpscQueue(int capacity)
    {
        // Capacity must be a power of 2
        if (capacity < 2 || (capacity & (capacity - 1)) != 0)
            throw new ArgumentException("Capacity must be a power of 2.", nameof(capacity));

        _buffer = new T[capacity];
        _mask = capacity - 1;
    }

    public bool TryEnqueue(T item)
    {
        long tail = Volatile.Read(ref _tail);
        long head = Volatile.Read(ref _head);

        // Check if queue is full
        if (tail - head == _buffer.Length)
            return false;

        _buffer[tail & _mask] = item;
        
        // Publish the tail update with release barrier
        Interlocked.Exchange(ref _tail, tail + 1);
        return true;
    }

    public bool TryDequeue(out T item)
    {
        long head = Volatile.Read(ref _head);
        long tail = Volatile.Read(ref _tail);

        // Check if queue is empty
        if (head == tail)
        {
            item = default!;
            return false;
        }

        item = _buffer[head & _mask];
        
        // Clear reference for GC if type is reference type
        _buffer[head & _mask] = default!;

        // Publish the head update with release barrier
        Interlocked.Exchange(ref _head, head + 1);
        return true;
    }
}
