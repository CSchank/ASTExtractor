from astextractor import *

ast_extractor = ASTExtractor("../target/ASTExtractor-0.5.jar", "../ASTExtractor.properties")

test = (
    "public WindowBuilder withSize(int width, int height) {\n"
    "    this.size = new Dimension(width, height);\n"
    "    return this;\n"
    "}"
 )

print(test)
print(ast_extractor.parse_string(test))