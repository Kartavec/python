package Lesson6.HW_ClientServer;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server_My {

    public static void main(String[] args) {
        Server_My server = new Server_My();
    }

    public Server_My() {

        ServerSocket server = null;
        Socket socket = null;

        try {
            server = new ServerSocket(3443); //Порт, прослушивающий сервер
            System.out.println("Server is working...");
            socket = server.accept();
            System.out.println("New Client");
            Scanner in =  new Scanner(socket.getInputStream());  // входящий поток
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true); // исходящий поток
            Scanner sc = new Scanner(System.in); // с консоли

            //Отправление сообщения от сервера
            new Thread(() -> {
                    while (true) {
                        System.out.println("Server, write you message");
                        String msg = sc.nextLine();
                        System.out.println("The message was send");
                        out.println(msg);
                    }
            }).start();

            //Получение сообщения и ответ - эхо
            while (true) {
                String msg = in.nextLine();
                if (msg.equals("/end")) break;
                System.out.println("Client: " + msg);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                socket.close();
                server.close();
                System.out.println("Server closed");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
