#include <stdio.h>

int main() {
    int frames, pages, i, j, k;
    int page[50], frame[10], recent[10];
    int faults = 0, time = 0, pos;

    printf("Enter number of frames: ");
    scanf("%d", &frames);

    printf("Enter number of pages: ");
    scanf("%d", &pages);

    printf("Enter page reference string:\n");
    for(i = 0; i < pages; i++)
        scanf("%d", &page[i]);

    for(i = 0; i < frames; i++) {
        frame[i] = -1;
        recent[i] = 0;
    }

    for(i = 0; i < pages; i++) {

        int found = 0;

        for(j = 0; j < frames; j++) {
            if(frame[j] == page[i]) {
                found = 1;
                recent[j] = ++time;
                break;
            }
        }

        if(!found) {

            faults++;

            pos = 0;

            for(j = 1; j < frames; j++)
                if(recent[j] < recent[pos])
                    pos = j;

            frame[pos] = page[i];
            recent[pos] = ++time;
        }

        printf("\nFrames: ");
        for(k = 0; k < frames; k++) {
            if(frame[k] == -1)
                printf("- ");
            else
                printf("%d ", frame[k]);
        }
    }

    printf("\n\nTotal Page Faults = %d\n", faults);

    return 0;
}