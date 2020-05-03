from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session
)

from tag_dh import db
from tag_dh.models import Account, Clash, Post

bp = Blueprint('clash', __name__)

@bp.route('/', methods=['GET'])
@bp.route("/clashes", methods=["GET"])
def index():
    return render_template('clashes/index.html')