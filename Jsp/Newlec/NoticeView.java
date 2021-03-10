package entity;

import java.util.Date;

public class NoticeView extends Notice {

  private int cmtCount;

  public int getCmtCount() {
    return cmtCount;
  }

  public void setCmtCount(int cmtCount) {
    this.cmtCount = cmtCount;
  }

  public NoticeView() {

  }

  public NoticeView(int id, String title, Date regDate, String writerId, String hit, String files, int cmtCount) {
    super(id, title, regDate, writerId, hit, files, "");
    this.cmtCount = cmtCount;
  }

}
