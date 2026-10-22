set -e
cat _p1 _p2 _p3 _p4 _p5 _p6 > _u.py
python3 _u.py
rm -f _p1 _p2 _p3 _p4 _p5 _p6 _u.py _probe.txt _update_readme.py
rm -rf .github/workflows
git config user.name QuakeBladesman
git config user.email c29932304@gmail.com
git add -A
git commit -m "docs: update Complete TODO List"
git push
