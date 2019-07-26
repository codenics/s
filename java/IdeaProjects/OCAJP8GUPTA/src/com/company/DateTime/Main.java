package com.company.DateTime;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;
import java.util.ArrayList;
import java.util.Date;

public class Main {

    public static void main (String [] args){

        LocalDate localDate = LocalDate.now();
        LocalTime localTime = LocalTime.now();
        System.out.println(localDate.getChronology());
        System.out.println(localDate.getDayOfYear());
        System.out.println(localDate.getDayOfMonth());
        System.out.println(localDate.getDayOfWeek());
        System.out.println(localDate.getYear());
        System.out.println(localDate.getMonth());
        System.out.println(localDate.getMonthValue());

        System.out.println(LocalDate.now().toEpochDay());
        System.out.println(localTime);

        DateTimeFormatter formatter1 = DateTimeFormatter.ofLocalizedDate(FormatStyle.FULL);
        DateTimeFormatter formatter2 = DateTimeFormatter.ofLocalizedDate(FormatStyle.LONG);
        System.out.println(localDate.format(formatter2));
        ArrayList<String> str = new ArrayList<>();
        System.out.println(str);
        System.out.println("game".replace('a','Z').concat("Aa"));

        System.out.println();
    }
}
