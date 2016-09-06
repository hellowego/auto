#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
# from baseHandler import BaseHandler
from tornado import gen
import uuid
sys.path.append("..")



# class TestHandler(BaseHandler):
# 	def get(self):
# 		sessionId = str(uuid.uuid1())
# 		print sessionId

# 		self.set_session_id()
# 		# self.render("test/mylogin.html")
# 		self.render("test/dropload.html")



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
		        raise InconsistentCommentTreeError

		    cids.append(cid)
		    tree.tree.setdefault(p_id, []).append(cid)
		    depth[cid] = depth[p_id] + 1 if p_id else 0
		    parents[cid] = p_id






class TestCommentTreeHandler(object):
	def get(self):
		comment1 = {}
		comment1.parent_id = 0
		comment1._id = 0
		comment1._name = "动物"

		comment2.parent_id = 0
		comment2._id = 1
		comment2._name = "野生动物"

		comment3.parent_id = 1
		comment3._id = 2
		comment3._name = "猫科动物"

		comment4.parent_id = 2
		comment4._id = 3
		comment4._name = "老虎"

		comment5.parent_id = 2
		comment5._id = 4
		comment5._name = "狮子"

		# commentlist["生物"] = comment1


		# self.render("test/comment.html")

if __name__ == "__main__":
	tree = CommentTree(cids=[], tree={}, depth={}, parents={}, num_children={})
	comment1 = {}
	comment1.parent_id = 0
	comment1._id = 0
	comment1._name = "动物"
	CommentTree.add_comments(tree, comment1)
