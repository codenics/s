package com.company;

public class BankAccount {

    private int acctNum;
    private int acctType;
    public BankAccount (){
        acctNum = 000000;
        acctType = 0;
    }


    public boolean equals(Object obj){

        if (obj instanceof BankAccount){

            BankAccount b = (BankAccount) obj;
            return b.acctType == this.acctType &&
                    b.acctNum == this.acctNum;

        }else
            return false;
    }

    public int getAcctNum(){
        return acctNum;
    }

    public int getAcctType(){
        return acctType;
    }
    public void setAcctNum(int num){
        acctNum = num;
    }

    public void setAcctType(int num){
    acctType = num;

    }
}
