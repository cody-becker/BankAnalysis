package com.mycompany.sample;

public class CalculatorLogic {

        // Calculator methods



    public static int add(int x, int y) {
        return x + y;
    }

    public static int subtract(int x, int y) {
        return x - y;
    }

    public static int multiply(int x, int y) {
        return x * y;
    }

    public static int divide(int x, int y) {
        if (y != 0) {
            return x / y;
        } else {
            throw new ArithmeticException("Division by zero is not allowed.");
        }
    }

    public static int modulus(int x, int y) {return x % y;
    }

    public static int square(int x) {
        return x * x;
    }

    public static int codyFormula(int x, int y) {
        return 2 * x + 3 * y;
    }
}

