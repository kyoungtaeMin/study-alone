package jsp;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/mvcmodel")
public class MvcModel extends HttpServlet{
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		int num = 0;
		
		String num_ = request.getParameter("n");
		if(num_ != null && !num_.equals(""))
			num = Integer.parseInt(num_);
		
		String result;
		
		if(num % 2 != 0) 
			result = "È¦¼ö";
		else
			result = "Â¦¼ö";
		
		request.setAttribute("result", result);
		
		//redirect
		//forward
		RequestDispatcher dispatcher = request.getRequestDispatcher("MvcModel.jsp");
		dispatcher.forward(request, response);
	}
}
