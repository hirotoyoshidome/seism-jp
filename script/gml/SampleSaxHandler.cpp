#include "SampleSaxHandler.hpp"
#include <iostream>

using namespace std;
using namespace xercesc;

// when start tag.
void SampleSaxHandler::startElement(const XMLCh* const uri, const XMLCh* const localname,
                                    const XMLCh* const qname, const Attributes& attrs)
{
    char* name = XMLString::transcode(localname);
    cout << "start : " << name << endl;
    XMLString::release(&name);
}

// when end tag.
void SampleSaxHandler::endElement(const XMLCh* const uri, const XMLCh* const localname,
                                  const XMLCh* const qname)
{
    char* name = XMLString::transcode(localname);
    cout << "end : " << name << endl;
    XMLString::release(&name);
}

// when hit string that between tag.
void SampleSaxHandler::characters(const XMLCh* const chars, const XMLSize_t length)
{
    XMLCh* buffer = new XMLCh[XMLString::stringLen(chars)+1];
    XMLString::copyString(buffer, chars);
    XMLString::trim(buffer);
    char* text = XMLString::transcode(buffer);
    delete[] buffer;

    cout << "text : " << text << endl;
    XMLString::release(&text);
}
