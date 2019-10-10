import sys
import argparse
import xml.etree.ElementTree as xmltree


def read_idea_dictionary(xml_file_path):
    """
    :param xml_file_path: Path to standard IDEA dictionary or user-defined XML dictionary file
    :return: list of dictionary items
    """
    idea_dictionary = []
    tree = xmltree.parse(xml_file_path)
    root = tree.getroot()

    for child in root.findall("./dictionary/words/w"):
        idea_dictionary.append(child.text)

    return idea_dictionary


def read_vassist_dictionary(text_file_path):
    """
    :param text_file_path: Path to Visual Assist dictionary or user-defined text dictionary file
    :return: list of dictionary items
    """
    with open(text_file_path) as f:
        text_dictionary = [item.strip() for item in f.readlines()]

    return text_dictionary


def main():
    """
    Uninstall applications based on list, or simply retrieve the list of installed applications
    :return: System return code
    """
    parser = argparse.ArgumentParser(description='Command-line params')
    parser.add_argument('--idea-dictionary',
                        help='Add XML-based IDEA dictionary as a merge source',
                        action='append',
                        nargs=1,
                        dest='idea_dictionary',
                        required=True)
    parser.add_argument('--visual-assist-dictionary',
                        help='Add plain text Visual Assist dictionary as a merge source',
                        action='append',
                        nargs=1,
                        dest='text_dictionary',
                        default='UserWords.txt',
                        required=False)

    args = parser.parse_args()

    merged_list = set()

    for idea_xml_file in args.idea_dictionary:
        print("IDEA dictionary file: %s" % idea_xml_file)
        merged_list.union(set(read_idea_dictionary(idea_xml_file)))
    
    for text_file in args.text_dictionary:
        print("User VAssist file: %s" % text_file)
        merged_list.union(set(read_vassist_dictionary(text_file)))

    print(merged_list)

    return 0


###########################################################################
if __name__ == '__main__':
    sys.exit(main())
