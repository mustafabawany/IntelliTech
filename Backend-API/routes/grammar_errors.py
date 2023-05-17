# from flask import Flask, request, jsonify, Blueprint
# import language_tool_python
# tool = language_tool_python.LanguageTool('en-US')

# grammarErrors_bp = Blueprint('grammar_errors' , __name__)

# @grammarErrors_bp.route("/grammar", methods=["POST"])
# def Grammar_Errors(essays):
#     """
#     Checks Grammatical Errors in each Essay

#     Args:
#         essays: Essay of each student 

#     Returns: 
#         int
#     """
#     matches = tool.check(essays)
#     is_bad_rule = lambda rule: rule.category == 'GRAMMAR'
#     matches = [rule for rule in matches if is_bad_rule(rule)]
#     errors = []
#     for i in range(0, len(matches)):
#       errors.append(matches[i].ruleId)  # or category of the error (Misc, Whitespace, Typography)
    
#     return jsonify({
#        'error_count' : len(matches),
#        'error': errors
#     })