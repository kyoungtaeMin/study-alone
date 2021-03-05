package ex1;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Date;

public class Jdbc01 {

  public static void main(String[] args) throws ClassNotFoundException, SQLException {

    String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
    String sql = "SELECT * FROM NOTICE WHERE HIT > 10";

    Class.forName("oracle.jdbc.driver.OracleDriver");
    Connection con = DriverManager.getConnection(url, "NEWLEC", "1234");
    Statement st = con.createStatement();
    ResultSet rs = st.executeQuery(sql);

    while (rs.next()) {
      int id = rs.getInt("ID");
      String title = rs.getString("TITLE");
      String writerId = rs.getString("WRITER_ID");
      String content = rs.getString("CONTENT");
      Date regDate = rs.getDate("REGDATE");
      int hit = rs.getInt("HIT");

      System.out.printf("id:%d, title:%s, writerId:%s, content:%s, regDate:%s," + "hit:%d\n", id, title, writerId,
          content, regDate, hit);
    }

    rs.close();
    st.close();
    con.close();

  }

}
