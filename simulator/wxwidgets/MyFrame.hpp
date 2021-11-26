#ifndef MYFRAME_H
#define MYFRAME_H

#include <wx/wx.h>


class MyFrame : public wxFrame
{
public:
    wxButton* button;
    wxPanel* panel;
    wxTextCtrl* textbox;

public:
    // Constructor.
    MyFrame();

    // Destructor.
    virtual ~MyFrame();

    void onClose(wxCloseEvent& event);
    void click(wxCommandEvent& event);
    void onPaint(wxCommandEvent& event);
    void onEnter(wxCommandEvent& event);
};

#endif
