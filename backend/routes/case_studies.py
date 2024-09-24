from flask import Blueprint, jsonify
from models import CaseStudy

case_studies_bp = Blueprint('case_studies', __name__)

@case_studies_bp.route('/api/case-studies', methods=['GET'])
def get_case_studies():
    case_studies = CaseStudy.query.all()
    return jsonify([{
        'title': cs.title,
        'description': cs.description,
        'image_url': cs.image_url,
        'date': cs.date,
        'link': cs.link
    } for cs in case_studies])
