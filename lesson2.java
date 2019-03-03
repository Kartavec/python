import java.util.Arrays;

public class lesson2 {

    public static void main(String[] args) {

        getInvertArray(15);

        getIntArray(8);

        int[] arrayToCheck = {1, 5, 3, 2, 11, 4, 5, 2, 4, 8, 9, 1};
        multiplyArray(arrayToCheck);

        getSquareArray(5);

        int[] sourceArray = {1, 5, 3, 2, 11, 4, 5, 2, -4, 8, 9, -1};
        getMaxMinValue(sourceArray);

        int[] balancingArray = {1, 2, 3, 4, 4, 3, 2, 1};
        checkBalance(balancingArray);

        int[] originalArray = {1, 2, 3, 4, 5, 6, 7, 8};
        moveArray(originalArray, -20);

        getArrayOfOddNumbers();

        getArrayOfRandomVariables();

        сompareTwoArrays();
    }

    public static void getInvertArray(int amount) {
        int[] arr = new int[amount];
        for (int i = 0; i < amount; i++) {
            int j = (int) Math.round(Math.random());
            arr[i] = j;
        }
        System.out.println("Исходный массив:        " + Arrays.toString(arr));

        int[] arrInvert = arr;
        for (int i = 0; i < amount; i++) {
            if (arr[i] == 1) arrInvert[i] = 0;
            else arrInvert[i] = 1;
        }
        System.out.println("Инвертированный массив: " + Arrays.toString(arrInvert));
        System.out.println();
    }

    public static void getIntArray(int amount) {
        int[] arr = new int[amount];
        for (int i = 0; i < amount; i++) {
            arr[0] = 0;
            if (i > 0 && i < amount) arr[i] = arr[i - 1] + 3;
        }
        System.out.print("Массив арифметической прогрессии: ");
        System.out.println(Arrays.toString(arr));
        System.out.println();
    }

    public static void multiplyArray(int[] arrayToCheck) {
        System.out.print("Исходный массив:        ");
        System.out.println(Arrays.toString(arrayToCheck));
        for (int i = 0; i < arrayToCheck.length; i++) {
            if (arrayToCheck[i] < 6) arrayToCheck[i] *= 2;
        }
        System.out.print("Преобразованный массив: ");
        System.out.println(Arrays.toString(arrayToCheck));
        System.out.println();
    }

    public static void getSquareArray(int n) {
        int[][] arr = new int[n][n];
        System.out.println("Квадратный двумерный целочисленный массив: ");
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (i == j) arr[i][j] = 1;
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void getMaxMinValue(int[] sourceArray) {

        int max = sourceArray[0];
        int min = sourceArray[0];
        for (int i = 0; i < sourceArray.length; i++) {
            if (sourceArray[i] > max) max = sourceArray[i];
            if (sourceArray[i] < min) min = sourceArray[i];
        }
        System.out.println("Заданный массив: " + Arrays.toString(sourceArray));
        System.out.println("Максимальное значение массива: " + max + " Минимальное значение массива: " + min);
        System.out.println();
    }

    public static void checkBalance(int[] balancingArray) {

        int sumLeft = 0;
        int sumRight = 0;
        for (int i = 0; i < balancingArray.length; i++) sumRight += balancingArray[i];
        for (int i = 0; i < balancingArray.length; i++) {
            sumLeft += balancingArray[i];
            sumRight -= balancingArray[i];
            if (sumLeft == sumRight) System.out.println("Массив содержит баланс: " + true);
        }
        System.out.println();
    }

    public static void moveArray(int[] originalArray, int n) {

        System.out.println("Заданный массив: " + Arrays.toString(originalArray));

        if (Math.abs(n) >= originalArray.length) n = n % originalArray.length;

        int currentIndex, movedIndex, buffer;

        for (int i = 0; i < greatestCommonDivisor(n, originalArray.length); i++) {

            buffer = originalArray[i];

            currentIndex = i;

            if (n > 0) {
                while (true) {
                    movedIndex = currentIndex + n;
                    if (movedIndex >= originalArray.length) movedIndex = movedIndex - originalArray.length;
                    if (movedIndex == i) break;
                    originalArray[currentIndex] = originalArray[movedIndex];
                    currentIndex = movedIndex;
                }
            } else if (n < 0) {
                while (true) {
                    movedIndex = currentIndex + n;
                    if (movedIndex < 0) movedIndex = originalArray.length + movedIndex;
                    if (movedIndex == i) break;
                    originalArray[currentIndex] = originalArray[movedIndex];
                    currentIndex = movedIndex;
                }
            }

            originalArray[currentIndex] = buffer;
        }
        System.out.println("Итоговый массив: " + Arrays.toString(originalArray));
        System.out.println();
    }

    public static int greatestCommonDivisor(int a, int b) {
        if (b == 0) return Math.abs(a);
        else return greatestCommonDivisor(b, a % b);
    }

    public static void getArrayOfOddNumbers() {
        int count = 0;
        for (int i = 1; i < 100; i++) {
            if (i % 2 != 0) count += 1;
        }

        int[] arrayOfOddNumbers = new int[count];
        for (int i = 0; i < arrayOfOddNumbers.length; i++) {
            for (int j = 1; j <= 99; j++) {
                if (i == 0){
                    if (j % 2 != 0) {
                        arrayOfOddNumbers[i] = j;
                        break;
                        }
                }
                else {
                    if (j % 2 != 0 && arrayOfOddNumbers[i-1] < j){
                        arrayOfOddNumbers[i] = j;
                        break;
                    }
                }
            }
        }
        System.out.println("Массив нечетный значений от 1 до 99: " + Arrays.toString(arrayOfOddNumbers));
        System.out.println();
     }

    public static void getArrayOfRandomVariables(){
         int[] arr = new int[15];
         int count = 0;
         for (int i = 0; i < arr.length; i++) {
             int j = (int) Math.round(Math.random()*9);
             arr[i] = j;
             if (j%2 == 0) count += 1;
         }
         System.out.println("Массив рандомных значений от 0 до 9: " + Arrays.toString(arr));
         System.out.println("Количество четных элементов в массиве: " + count);
         System.out.println();
    }

    public static void сompareTwoArrays(){
        int[] arrFirst = new int[5];
        int[] arrSecond = new int[5];

        for (int i = 0; i < arrFirst.length; i++) arrFirst[i] = (int) Math.round(Math.random()*5);
        for (int i = 0; i < arrSecond.length; i++) arrSecond[i] = (int) Math.round(Math.random()*5);

        System.out.println("Массив № 1 рандомных значений от 0 до 5: " + Arrays.toString(arrFirst));
        System.out.println("Массив № 2 рандомных значений от 0 до 5: " + Arrays.toString(arrSecond));

        int sumFirst = 0;
        int sumSecond = 0;

        for (int i = 0; i < arrFirst.length; i++) sumFirst += arrFirst[i];
        for (int i = 0; i < arrSecond.length; i++) sumSecond += arrSecond[i];

        if (sumFirst/5.0 > sumSecond/5.0) System.out.println("Массив № 1 больше Массива № 2 по параметру: среднее арифметическое элементов");
        else if (sumFirst/5.0 < sumSecond/5.0) System.out.println("Массив № 1 меньше Массива № 2 по параметру: среднее арифметическое элементов");
        else System.out.println("Массив № 1 равен Массиву № 2 по параметру: среднее арифметическое элементов");
    }
}