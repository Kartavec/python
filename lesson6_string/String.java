package lesson6_string;

public class String {

    public static void main(java.lang.String[] args) {

        //Создаем строку с исходными данными
        java.lang.String inputString = "Предложение    один      Предложение     два    Предложение    три  ";

        //Создаем массив только из слов исходной строки
        java.lang.String[] words = inputString.split("\\s*(\\s|,|!|\\.)\\s*");

        //Создаем результирующую строку
        StringBuilder result = new StringBuilder();

        /*
        Записываем данные в результирующую  строку

        Первое слово просто записывается
        Последующие слова сравниваются сам с собой в нижнем регистре
        и перед словом ставлится либо пробел, либо точка с пробелом
        К последнему слову добавляется точка в конце
         */
        for (int i = 0; i < words.length; i++) {
            if (i == 0) {
                result.append(words[i]);
            }
            else if (i > 0 && i < words.length - 1) {
                java.lang.String word = words[i];
                if (word.equals(word.toLowerCase())) {
                    result.append(" "+ words[i]);
                }
                else {
                    result.append(". " + words[i]);
                }
            }
            else {
                result.append(" " + words[i] + ".");
            }
        }
        System.out.println(result);
    }
}
