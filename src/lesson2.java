public class lesson2 {

    // задание 1

    public static void task1(int[] a) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] == 0) {
                a[i] = 1;
            } else {
                a[i] = 0;
            }
        }
    }

    // задание 2

    public static int[] task2() {
        int[] a = new int[8];
        for (int i = 0, j = 1; i < 8; i++, j += 3) {
            a[i] = j;
        }
        return a;
    }

    // задание 3

    public static void task3(int[] a) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] < 6) {
                a[i] *= 2;
            }
        }
    }

    // задание 4

    public static int min(int[] a) {
        int min = a[0];
        for (int value : a) {
            if (value < min) {
                min = value;
            }
        }
        return min;
    }
    public static int max(int[] a) {
        int max = a[0];
        for (int value : a) {
            if (value > max) {
                max = value;
            }
        }
        return max;
    }

    // *задание 5

    public static int[][] task5(int l) {
        int[][] a = new int[l][l];
        for (int i = 0; i < l; i++) {
            a[i][i] = 1;
            a[i][l - 1 - i] = 1;
        }
        return a;
    }

    // **задание 6

    public static int sum(int[] a, int from, int to) {
        int s = 0;
        for (int i = from; i < to; i++) {
            s = s + a[i];
        }
        return s;
    }

    public static void print(int[] a) {
        System.out.print("[");
        for (int i : a) {
            System.out.print(i + " ");
        }
        System.out.print("]");
    }

    public static boolean checkBalance(int[] a) {
        for (int i = 0; i < a.length; i++) {
            if (sum(a, 0, i) == sum(a, i, a.length)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] a = {1, 1, 0, 0, 1, 0, 1, 1, 0, 0};
        System.out.println("задание 1");
        print(a);
        System.out.println();
        task1(a);
        print(a);
        System.out.println();
        System.out.println("задание 2");
        print(task2());
        System.out.println();
        a = new int[]{1, 2, 3, 4, 5, 6, 78, 50, 1};
        System.out.println("задание 3");
        print(a);
        System.out.println();
        task3(a);
        print(a);
        System.out.println();
        System.out.println("задание 4");
        System.out.println("max=" + max(a));
        System.out.println("min=" + min(a));

        int[][] b = task5(7);
        System.out.println("Задание 5");
        for (int[] bs : b) {
            for (int i : bs) {
                System.out.print(i);
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("Задание 6");

        b = new int[][]{{1, 1, 1, 2, 1}, {2, 1, 1, 2, 1}, {10, 1, 2, 3, 4}};
        for (int[] bs : b) {
            print(bs);
            System.out.print(": " + checkBalance(bs));
            System.out.println();
        }

    }
}
