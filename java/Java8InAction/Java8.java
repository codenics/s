public class Java8{
    
        public static boolean isPalindrone(String string){
            for (int i = 0; i<string.length()/2; i++){
                    if(string.charAt(i) != string.charAt(string.length()-1-i))
                    return false;
        }
    return true;
    }
        public static boolean isPalindroneReverse(String string){
       String reversedString = "";
        for(int i = string.length()-1; i >= 0; i--){
            reversedString +=string.charAt(i);
        }
            System.out.println(reversedString);
        if(string.equals(reversedString))
            return true;
        
            return false;

    }
    
    public static void main(String... args){
        //System.out.printf("This is %0.3f\n" + Math.PI + " ");
        System.out.println(isPalindrone("ooddoo"));
        System.out.println(isPalindroneReverse("ooddoo"));

    }
    

}