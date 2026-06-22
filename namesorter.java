import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
public class Name Sort
public static void main(String[] args) {
List<String> names = new ArrayList<>();
names.add("Gayuu");
names.add("Sakshi");
names.add("Rutuu");
names.add("Vedaa");
System.out.println("Unsorted names: " + names);
Collections.sort(names);
System.out.println("Sorted names: " + names);
}
}
