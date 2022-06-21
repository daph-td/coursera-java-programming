public class ex1 {
    public static void main(String[] args) {
        System.out.println("\nPRINT AND COMMENTS");
        System.out.println("Hello \"World\"");
        // this is a single comment
        /* this is a multi-line comment */

        // variables and data types
        System.out.println("\nVARIABLES AND DATA TYPES");
        char nameChar = 'D';
        String fullName = "Daphne";
        int birthDay = 25;
        double birthDayDouble = (double) birthDay;
        System.out.println(birthDayDouble);
        double birthMonth = 1.0;
        int birthMonthInt = (int) birthMonth;
        System.out.println(birthMonthInt);
        boolean myBool = false;
        String message = fullName + " birthday is " + birthDay;
        System.out.println(message);
        String name1 = "Daphne ", name2 = "Alex ", name3 = "Luna ";
        System.out.println(name1 + name2 + name3);
        System.out.println("Start ...");

        // operators 
        System.out.println("\nOPERATORS");
        int x = 9;
        System.out.println(++x);
        int y = 20;
        y += 5;
        System.out.println(y);
        System.out.println(9 + 2);
        System.out.println(9 - 2);
        System.out.println(9 * 2);
        System.out.println(1.0 * 9 / 2);
        System.out.println(9 % 2);
        System.out.println(9.0 % 2.0);
        System.out.println(9 / 2);
        System.out.println(10 * (2 + 3) - 3);
    }
}


