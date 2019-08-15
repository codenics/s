package com.company;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {

        String str = "My good";
        BankAccount b1 = new BankAccount();
        b1.setAcctType(2);
        b1.setAcctNum(889988);

        /*System.out.println(b1.equals(b2));
        System.out.println(str.equals(str));
*/
        ArrayList<BankAccount> list = new ArrayList<>();

        BankAccount b2 = new BankAccount();
        list.add(b1);
        b2.setAcctType(2);
        b2.setAcctNum(889988);

        System.out.println(list.contains(b2));



    }
}
