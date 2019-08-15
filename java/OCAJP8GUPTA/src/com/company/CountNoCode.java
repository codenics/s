package com.company;


//Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
//
//
//        countCode("aaacodebbb") → 1
//        countCode("codexxcode") → 2
//        countCode("cozexxcope") → 2

public class CountNoCode {

    public static void main (String [] args){

        System.out.println(count("Totalcodecode"));

    }
    static int count(String str){
        int total=0;
        String [] splitStr = str.split("c.{2}e");

        for (String name : splitStr) {
            System.out.println(name);
//            if(("c"+name).matches("co.{1}e")){
//                total++;
//            }
        }

        return total;
    }

}
