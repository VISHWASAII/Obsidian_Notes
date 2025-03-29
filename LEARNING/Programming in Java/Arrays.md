- A _Java Array_ is a collection of variables of the same type. For instance, an _array_ of `int` is a collection of variables of the type `int`. The variables in the array are ordered and each have an index. You will see how to index into an array later in this text.
```
MyClass[] myClassArray;

int[] intArray;
int   intArray[];

String[] stringArray;
String   stringArray[];

MyClass[] myClassArray;
MyClass   myClassArray[];
```

- ## Java Array Literals
- IF we dont know the size we need to of the array without the 0 index then we need to reduce the length

The Java programming language contains a shortcut for instantiating arrays of primitive types and strings. If you already know what values to insert into the array,
```
int[]   ints2 = new int[]{ 1,2,3,4,5,6,7,8,9,10 };
```

- All Array things
```import java.sql.SQLOutput;  
import java.util.Arrays;  
import java.util.List;  
import java.util.stream.Collectors;  
  
public class Main {  
    public static void main(String[] args) {  
        //Instance Array  
        Integer[] arr = new Integer[4];  
        Integer value = Math.toIntExact(Arrays.stream(arr).count());  
        System.out.println(value);  
  
        //Literals  
        int[] arrOfValues = new int[]{1,2,3,4,5,6,7,8};  
        int arryOfValues[] = {1,2,3,4,5,6,7};  
  
        //Add elements into array  
        String[] valuesOfString = new String[10];  
        for(int i=0; i<10; i++){  
            valuesOfString[i] = "Index " + i;  
        }  
       List<String> updatedString = Arrays.stream(valuesOfString).collect(Collectors.toList());  
        System.out.println(updatedString);  
  
        //For each Iteration  
        for(int x: arrOfValues){  
            System.out.print(x);  
        }  
  
        //using Stream  
        int sumOfArray = Arrays.stream(arrOfValues).sum();  
        System.out.println(sumOfArray);  
  
        //Multidimentional Array  
        int[][] intArrays = new int[10][20];  
  
        for(int i=0; i < intArrays.length; i++){  
            for(int j=0; j < intArrays[i].length; j++){  
                System.out.println("i: " + i + ", j: " + j);  
            }  
        }  
        //For dsa i need to take  
    }  
  
}
```