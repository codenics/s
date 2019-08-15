package com.company.GameAndPractice;

import java.util.Scanner;

public class ReverseString {
    //This a program to take a String and display its reverse
    public static void main (String [] args){
        String inputString;
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter any String: ");
        inputString = input.nextLine();
        char[] rawString = inputString.toCharArray();
        char [] outputCharArr = new char[inputString.length()];
        int i, j;
        for (i = rawString.length-1,j = 0; i >= 0; i--, j++){
            outputCharArr[j] = rawString[i];
        }
        System.out.println(outputCharArr);
        System.out.println("TYJ");

        String dk = "dkd";
        System.out.println("containss");
        dk.contains("k");
        System.out.println(dk.substring(0,1));
        System.out.println(dk.contains("k"));
        String.valueOf('j'+'k');
        System.out.println(500%3);
    }
}

