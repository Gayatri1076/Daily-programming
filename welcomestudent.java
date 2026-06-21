public class WelcomeStudent{
public static void main(String[]args)
{
if(args.length!=2){
System.out.println("Please provide both name and surname as command line argument.");
return;
}
String name=args[0];
String surname=args[1];
System.out.println("Welcome,"+name+""+surname+"!");
}
}