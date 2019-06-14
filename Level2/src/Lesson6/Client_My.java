package Lesson6.HW_ClientServer;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client_My {

    public static void main(String[] args) {

        Socket socket = null;

        try {
            socket = new Socket("localhost", 3443); // входящий поток
            Scanner in =  new Scanner(socket.getInputStream()); // исходящий поток
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true); // с консоли
            Scanner sc = new Scanner(System.in);

            //Получение сообщения от сервера
            new Thread(() -> {
                while (true) {
                    String msg = in.nextLine();
                    System.out.println("Server: " + msg);
                }
            }).start();

            //Отправление сообщения серверу
            while (true) {
                System.out.println("Write you message...");
                String msg = sc.nextLine();
                out.println(msg); //Сообщение отправилось серверу
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}