#include <wx/wx.h>


class MyFrame : public wxFrame
{
public:
    MyFrame();
    virtual ~MyFrame();

    void OnClose(wxCloseEvent& event);
};
