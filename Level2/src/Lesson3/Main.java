package Lesson3;

public class Main {

    public static void main(String[] args) {
        PhoneBook pb1 = new PhoneBook();
        pb1.add("Ivanov", "925-155-11-11");
        pb1.add("Ivanov", "925-155-11-22");
        pb1.add("Ivanov", "925-155-11-33");
        pb1.add("Suvorova", "925-155-22-11");

        pb1.get("Ivanov");
        pb1.get("Suvorova");
        pb1.get("Never");


    }
}
