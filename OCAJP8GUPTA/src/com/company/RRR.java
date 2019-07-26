package com.company;

import java.util.ArrayList;

public class RRR {

    public static void main(String args[]){

        int a = 0;
        a = a++ + a;
        System.out.println("Sum = " + a);

        String string ;
        for (int i = 0; i < 6; i++)
            System.out.println(i);


        int[] aa = new int[10];
        int[] ab = aa;
        

        foo(aa);
        System.out.println(aa[0]+" "+ab[0]);
    }
    public static void foo(int[] x) {
        x[0] = x[0] + 1;
    };





}
