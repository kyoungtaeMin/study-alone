package controller;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import entity.Notice;

@WebServlet("/notice/list")
public class NoticeListController extends HttpServlet {
  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    List<Notice> list = new ArrayList<>();

    String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
    String sql = "SELECT * FROM NOTICE";

    try {
      Class.forName("oracle.jdbc.driver.OracleDriver");
      Connection con = DriverManager.getConnection(url, "NEWLEC", "1234");
      Statement st = con.createStatement();
      ResultSet rs = st.executeQuery(sql);

      while (rs.next()) {
        int id = rs.getInt("ID");
        String title = rs.getString("TITLE");
        Date regDate = rs.getDate("REGDATE");
        String writerId = rs.getString("WRITER_ID");
        String hit = rs.getString("HIT");
        String files = rs.getString("FILES");
        String content = rs.getString("CONTENT");

        Notice notice = new Notice(id, title, regDate, writerId, hit, files, content);
        list.add(notice);
      }

      rs.close();
      st.close();
      con.close();
    } catch (ClassNotFoundException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (SQLException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }

    request.setAttribute("list", list);

    request.getRequestDispatcher("/WEB-INF/view/notice/list.jsp").forward(request, response);

  }
}
