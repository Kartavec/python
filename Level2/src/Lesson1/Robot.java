package Lesson1;

public class Robot implements Actions {

    private int heightRestriction;
    private int lengthRestriction;

    String name;
    boolean active = true;

    public Robot(String name) {
        this.name = name;
        this.heightRestriction = 10;
        this.lengthRestriction = 40;
    }

    @Override
    public void run(int length) {
        if (length <= lengthRestriction) {
            System.out.println("Робот " + name + " успешно пробежал " + length + " метра(-ов)");
        }
        else {
            System.out.println("Робот " + name + " не смог пробежать " + length + " метра(-ов)");
            active = false;
        }
    }

    @Override
    public void jump(int height) {
        if (height <= heightRestriction) {
            System.out.println("Робот " + name + " успешно прыгнул на " + height + " метра(-ов)");
        }
        else {
            System.out.println("Робот " + name + " не смог прыгнуть на " + height + " метра(-ов)");
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
