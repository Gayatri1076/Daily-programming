public class SquareNumber{
public static void main(String[]args){
if(args.length==0){
System.out.println("Please provide a number as acommand-line argument.");
return;
}
try{
double number=Double.parseDouble(args[0]);
double square=number*number;
System.out.println("The square of"+number+"is:"+square);
}
catch(NumberFormatException e){
System.out.println("Invalid input.Please enter a valid number:");
}
}
}