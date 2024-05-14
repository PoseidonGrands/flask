from flask import Blueprint, render_template, request

from qa_online.model import db, Question

qa = Blueprint('qa', __name__)

@qa.route('/')
@qa.route('/index')
def index():
    return render_template('qa/index.html')

@qa.route('/follow', methods=['GET'])
def follow():
    per_page = 20
    # 默认第一页
    page = request.args.get('page', 1)
    questions = Question.query.filter_by(is_valid=True).paginate(page=page, per_page=per_page)
    return render_template('qa/follow.html', questions=questions)


@qa.route('/write')
def write():
    return render_template('qa/write.html')

@qa.route('/mine')
def mine():
    return render_template('qa/mine.html')

@qa.route('/detail/<int:q_id>')
def detail(q_id):
    print('q_id is ', q_id)
    question = Question.query.filter_by(id=q_id).first()
    if not question.is_valid:
        error_handle()
    else:
        # 取出该问题的第一条回答
        answer = question.answer_list.filter_by(is_valid=True).first()
        return render_template('qa/detail.html', question=question, answer=answer)

@qa.route('/init_db')
def init_db():
    db.create_all()
    return 'init_db success...'

@qa.errorhandler(404)
def error_handle():
    return '404'