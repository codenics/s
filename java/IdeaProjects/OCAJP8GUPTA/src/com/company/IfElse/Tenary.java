package com.company.IfElse;

public class Tenary {

    public static void main (String [] args){

        int balance = 679;

        double transfer = balance >= 500 ? balance - 500 : 0;
        System.out.println("Transfer is "+transfer);

    }
}
