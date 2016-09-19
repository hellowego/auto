#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
from baseHandler import BaseHandler
from tornado import gen
import uuid
sys.path.append("..")



class TestHandler(BaseHandler):
	def get(self):
		sessionId = str(uuid.uuid1())
		print sessionId

		self.set_session_id()
		self.render("test/mylogin.html")
		# self.render("test/dropload.html")


class TestCommentTreeHandler(BaseHandler):
	def get(self):
		self.render("test/comment.html")



class CommentTree:
	"""
	cids link 的所以comment id, 是一个list
	tree dict类型， key 是commnet id， value是改id所以儿子子节点，
	depth dict类型，key key 是commnet id， value是该id的层数，
	parents dict类型，key 是commnet id, value是该id的父节点的id
	num_children dict类型，key 是commnet id， value是改id所以儿子子节点的个数
	"""


	def __init__(self, cids, tree, depth, parents, num_children):
		# self.link = link
		self.cids = cids
		self.tree = tree
		self.depth = depth
		self.parents = parents
		self.num_children = num_children

	

	@classmethod
	def add_comments(cls, tree, comments):
		cids = tree.cids
		depth = tree.depth
		parents = tree.parents

		for comment in sorted(comments, key=lambda c: c._id):
		    # sort the comments by id so we'll process a parent comment before
		    # its child
		    cid = comment._id
		    p_id = comment.parent_id

		    # don't add a comment that is already in the tree
		    if cid in cids:
		        continue

		    if p_id and p_id not in cids:
		        # raise InconsistentCommentTreeError
		        print 'hi'

		    cids.append(cid)
		    tree.tree.setdefault(p_id, []).append(cid)
		    depth[cid] = depth[p_id] + 1 if p_id else 0
		    print p_id, '  ', depth[cid]
		    parents[cid] = p_id



class Comment(object):
	"""docstring for Comment"""
	def __init__(self, id, parent_id, name):
		super(Comment, self).__init__()
		self._id = id
		self.parent_id = parent_id
		self._name = name
		



		



if __name__ == "__main__":
	tree = CommentTree(cids=[], tree={}, depth={}, parents={}, num_children={})
	# comment1 = {}
	comment1 = Comment(1, None, "动物")
	comment2 = Comment(2, 1, "野生动物")
	comment3 = Comment(3, 2, "猫科动物")
	comment6 = Comment(6, 2, "犬科动物")
	comment4 = Comment(4, 3, "老虎")
	comment5 = Comment(5, 3, "狮子")

	comments = [comment1, comment2, comment3, comment4, comment5, comment6]
	# comments.append(comment1)	
	CommentTree.add_comments(tree, comments)
	print tree.cids, '  ', tree.depth, '  ', tree.parents, '  ', tree.tree
