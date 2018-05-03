package tco;

import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.net.Socket;

import javax.swing.JFileChooser;

/**
 * �ͻ���
 */
public class myClient extends Socket {

	private static final String SERVER_IP = "127.0.0.1";
	private static final int SERVER_PORT = 2018;

	private Socket client;
	private FileInputStream fis;
	private DataOutputStream dos;

	public myClient() {
		try {
			try {
				client = new Socket(SERVER_IP, SERVER_PORT);
				// �����˴����ļ�

				JFileChooser fileChooser = new JFileChooser();
				int returnVal = fileChooser.showOpenDialog(fileChooser);

				String filePath = fileChooser.getSelectedFile()
						.getAbsolutePath();
				File file = new File(filePath);
				fis = new FileInputStream(file);
				dos = new DataOutputStream(client.getOutputStream());

				// �ļ����ͳ���
				dos.writeUTF(file.getName());
				dos.flush();
				dos.writeLong(file.length());
				dos.flush();

				// �����ļ�
				byte[] sendBytes = new byte[1024];
				int length = 0;
				while ((length = fis.read(sendBytes, 0, sendBytes.length)) > 0) {
					dos.write(sendBytes, 0, length);
					dos.flush();
				}
			} catch (Exception e) {
				e.printStackTrace();
			} finally {
				if (fis != null)
					fis.close();
				if (dos != null)
					dos.close();
				client.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) throws Exception {
		new myClient();
	}
}