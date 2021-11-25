import xml.etree.ElementTree as ET


# CONSTS
file_path = "../data/533946_2/brid/53394600_brid_6697_op2.gml"

gml = "{http://www.opengis.net/gml}"
grp = "{http://www.opengis.net/citygml/cityobjectgroup/2.0}"
core = "{http://www.opengis.net/citygml/2.0}"
pbase = "{http://www.opengis.net/citygml/profiles/base/2.0}"


def main():
    tree = ET.parse(file_path)
    root = tree.getroot()

    for i, child in enumerate(root):
        pass
        # if gml + "boundedBy" == child.tag:
        #     for c in child.iter():
        #         print(c)
        if core + "cityObjectMember" == child.tag:
            for c in child.iter():
                print(c)
            break
        else:
            pass
            # print(child.tag)
        if i > 20:
            break


if __name__ == "__main__":
    main()
