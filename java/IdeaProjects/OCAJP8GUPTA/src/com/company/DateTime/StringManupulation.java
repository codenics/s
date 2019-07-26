package com.company.DateTime;

public class StringManupulation {

    public void StringManupulation(){

    }

    public static void main (String [] args){

        String valof = String.valueOf(6.79);
        System.out.println(valof);
        String [] splited = valof.split("[.]");

        for (int i = 0; i < splited.length ; i++) {
            System.out.println(splited[i]);

        }

        String s1 = "Welcome";
        String s2 = "welcome";
        s2 = s1.replace('e', 'E');
        System.out.println(s2);

        String wel = "Welcome to Java and HTML";
       String splitedWel [] = wel.split(" ");
       s1 = splitedWel[0];
       s2 = splitedWel[1];
       System.out.println("");
       System.out.println(s1);
       System.out.println(s2);


    }
    public static int m(String s){
        int count = 0;
        for (int i = 0; i < s.length(); i++)
            if (Character.isUpperCase(s.charAt(i)))
                count++;
        return count;
    }
}
