PROJECT_WORKSPACE="$HOME/workspace-python/python-commonutil"
export PYTHONPATH="$PROJECT_WORKSPACE/src:$PYTHONPATH"
python "$PROJECT_WORKSPACE/test/unit/testpyquery/testpyquery.py"
python "$PROJECT_WORKSPACE/test/unit/testlxml/testlxml.py"
python "$PROJECT_WORKSPACE/test/unit/testjsonpickle/testjsonpickle.py"
python "$PROJECT_WORKSPACE/test/unit/testpytz/testpytz.py"
python "$PROJECT_WORKSPACE/test/unit/testjieba/testjieba.py"

