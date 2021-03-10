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
import entity.NoticeView;
import service.NoticeService;

@WebServlet("/notice/list")
public class NoticeListController extends HttpServlet {
  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // list?f=title&q=a

    String field_ = request.getParameter("f");
    String query_ = request.getParameter("q");
    String page_ = request.getParameter("p");

    String field = "title";
    if (field_ != null && !field_.equals("")) {
      field = field_;
    }
    String query = "";
    if (query_ != null && !query_.equals("")) {
      query = query_;
    }
    int page = 1;
    if (page_ != null && !page_.equals("")) {
      page = Integer.parseInt(page_);
    }

    NoticeService service = new NoticeService();
    List<NoticeView> list = service.getNoticeList(field, query, page);
    int count = service.getNoticeCount(field, query);

    request.setAttribute("list", list);
    request.setAttribute("count", count);

    request.getRequestDispatcher("/WEB-INF/view/notice/list.jsp").forward(request, response);

  }
}
