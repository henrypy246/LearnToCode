package com.example.web;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class BeerSelect extends HttpServlet{

	public void doPost(HttpServletRequest request, HttpServletResponse response)
				throws IOException, ServletException{
		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		out.println("Beer Selection Advice<br/>");
		String color = request.getParameter("color");
		int volume = Integer.parseInt(request.getParameter("volume"));
		out.println("<br/> Got Beer color "+color);
		out.println("<br/> Got Beer volume "+ volume+ "ml");
	}
}