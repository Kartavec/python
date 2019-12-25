package Lesson1;

public class Cat implements Actions {

    private int heightRestriction;
    private int lengthRestriction;

    String name;
    boolean active = true;

    public Cat(String name) {
        this.name = name;
        this.heightRestriction = 3;
        this.lengthRestriction = 25;
    }

    @Override
    public void run(int length) {
        if (length <= lengthRestriction) {
            System.out.println("Кошка " + name + "  успешно пробежала " + length + " метра(-ов)");
        }
        else {
            System.out.println("Кошка " + name + " не смогла пробежать " + length + " метра(-ов)");
            active = false;
        }
    }

    @Override
    public void jump(int height) {
        if (height <= heightRestriction) {
            System.out.println("Кошка " + name + " успешно прыгнула на " + height + " метра(-ов)");
        }
        else {
            System.out.println("Кошка " + name + " не смогла прыгнуть на " + height + " метра(-ов)");
            active = false;
        }
    }

    @Override
    public boolean isOnDistance() {
        return active;
    }

    @Override
    public void info() {
        System.out.println(name);
    }
}
