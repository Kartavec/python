package Lesson5;

import java.util.Arrays;

public class HW {

    static final int size = 100000000;
    static final int half = size / 2;

    private static float[] createArray () {
        float[] arr = new float[size];
        Arrays.fill(arr, 1); // вместо цикла for
        return arr;
    }

    static void addFirst(float[] arr) {
        long a = System.currentTimeMillis();
        calculate(arr);
        System.currentTimeMillis();
        System.out.println(System.currentTimeMillis() - a);
    }

    static void addSecond(float[] arr) {
        float[] arr1 = new float[half];
        float[] arr2 = new float[half];

        long b = System.currentTimeMillis();

        System.arraycopy(arr, 0, arr1, 0, half);
        System.arraycopy(arr, half, arr2, 0, half);

        calculate(arr1);
        calculate(arr2);

        System.arraycopy(arr1, 0, arr, 0, half);
        System.arraycopy(arr2, 0, arr, half, half);

        System.currentTimeMillis();
        System.out.println(System.currentTimeMillis() - b);
    }

synchronized static void calculate(float[] arr) {
        Thread calc = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < arr.length; i++) {
                    arr[i] = (float) (arr[i] * Math.sin(0.2f + i / 5) * Math.cos(0.2f + i / 5) * Math.cos(0.4f + i / 2));
                }
                }
        });
    calc.start();
    }

    public static void main(String[] args) {

        addFirst(createArray());
        addSecond(createArray());
    }

}
