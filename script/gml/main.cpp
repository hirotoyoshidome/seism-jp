#include "SampleSaxHandler.hpp"

#include <iostream>
#include <fstream>

#include <xercesc/sax2/SAX2XMLReader.hpp>
#include <xercesc/sax2/XMLReaderFactory.hpp>
#include <xercesc/util/PlatformUtils.hpp>

using namespace std;
using namespace xercesc;


void simpleReadFile(char* filepath)
{
    ifstream ifs(filepath);
    std::string contents;
    if (ifs.fail()) {
        std::cerr << "Failed to open file." << std::endl;
    } else {
        while (getline(ifs, contents)) {
            cout << contents << endl;
        }
    }
}

int main(int argc, char *argv[])
{
    cout << "start." << endl;

    // const char* xmlpath = argv[1];

    const char* xmlpath = "./data/codelists_2/LandUse_genChange.xml";

    // read file.
    // simpleReadFile(xmlpath);

    try {
        XMLPlatformUtils::Initialize();
        cout << "init." << endl;
    }
    catch (const XMLException& toCatch) {
        cerr << "init error." << endl;
        return 1;
    }

    SAX2XMLReader* parser = XMLReaderFactory::createXMLReader();
    cout << "parser init." << endl;

    try {
        SampleSaxHandler handler;
        cout << "hander init." << endl;
        parser->setContentHandler(&handler);
        cout << "parse start." << endl;
        parser->parse(xmlpath);
        cout << "parse end." << endl;
    } catch (...) {
        cerr << "load error." << endl;
    }

    delete parser;

    XMLPlatformUtils::Terminate();

    cout << "end." << endl;
    return 0;
}
