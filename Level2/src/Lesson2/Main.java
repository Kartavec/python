package Lesson2;

public class Main {

    public static void main(String[] args) {

        //Корректный массив
        String[][] arr1 = new String[][]{{"1", "2", "3", "4"}, {"2", "2", "2", "3"}, {"1", "2", "2", "2"}, {"2", "2", "2", "2"}};

        //Массив с текстовыми данными
        String[][] arr2_1 = new String[][]{{"1", "2", "text", "4"}, {"2", "2", "2", "3"}, {"1", "2", "2", "2"}, {"2", "2", "2", "2"}};
        String[][] arr2_2 = new String[][]{{"1", "2", "99999", "4"}, {"2", "2", "2", "3"}, {"1", "2", "2", "2"}, {"2", "2", "2", "!"}};

        //Массивы с некорректным размером
        String[][] arr3_1 = new String[][]{{"1", "2", "3", "4"}, {"2", "2", "2", "3"}, {"1", "2", "2", "2"}};
        String[][] arr3_2 = new String[][]{{"1", "2", "3", "4"}, {"2", "2", "2", "3"}, {"1", "2", "2", "2"}, {"2", "2", "2", "2"}, {"2", "2", "2", "2"}};
        String[][] arr3_3 = new String[][]{{"1", "2", "3"}, {"2", "2", "2"}, {"1", "2", "2"}, {"2", "2", "2"}};


        //Выбираем массив, который будем проверять
        String[][] arr = arr2_2;

        try {
            try {
                int result = method(arr);
                System.out.println(result);
            } catch (MyArraySizeException e) {
                System.out.println("Некорректный размер массива! Ожидается массив 4х4.");
            }
        }
        catch (MyArrayDataException e) {
            System.out.println("Неправильное значение массива!");
            System.out.println("Ошибка в ячейке: " + e.i + "x" + e.j);
        }
    }

    public static int method(String[][] arr) throws MyArraySizeException, MyArrayDataException {
        int sum = 0;
        if (arr.length != 4) {
            throw new MyArraySizeException();
        }
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].length != 4) {
                throw new MyArraySizeException();
            }
            for (int j = 0; j < arr[i].length; j++) {
                try {
                    sum = sum + Integer.parseInt(arr[i][j]);
                }
                catch (NumberFormatException e) {
                    throw new MyArrayDataException(i, j);
                }
            }
        }
        return sum;
    }
}