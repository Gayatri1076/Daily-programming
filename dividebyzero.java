public class DivideByZero {
public static void main(String[] args) {
int numerator = 10;
int denominator = 0;//This is where the error occurs
try {
if (denominator!=0){
int result=numerator/denominator;
System.out.println("Result of division: " + result);
}else{
System.out.println("Error:cannot divide by zero.");
}
} catch (ArithmeticException e) {
System.out.println("Exception caught:"+e.getMessage());
}
finally{
System.out.println("This block always executes, regardless of exceptions.");
}
}
}

