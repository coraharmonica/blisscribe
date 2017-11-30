# -*- coding: utf-8 -*-
"""
BLISSNET:

    A module for representing Blissymbols in WordNet.
"""

from nltk.corpus import wordnet as wn


BLISSNET = {
    # squirrel
	"U+3201":	[wn.synset("squirrel.n.01")],

	# fire
	"U+3202":	[wn.synset("fire.n.03")],

	# mango
	"U+3203":	[wn.synset("mango.n.01"),
				wn.synset("mango.n.02")],

	# cloud
	"U+3205":	[wn.synset("cloud.n.02")],

	# water, fluid, liquid
	"U+3206":	[wn.synset("body_of_water.n.01"),
				wn.synset("fluid.n.01"),
				wn.synset("fluid.n.02"),
				wn.synset("liquid.n.01"),
				wn.synset("liquid.n.02"),
				wn.synset("liquid.n.03"),
				wn.synset("liquid.n.04"),
				wn.synset("urine.n.01"),
				wn.synset("water.n.01"),
				wn.synset("water.n.03"),
				wn.synset("water.n.06"),
				wn.synset("water_system.n.02")],

	# oil, lubricant
	"U+3207":	[wn.synset("oil.n.01")],

	# steam
	"U+3209":	[wn.synset("steam.v.02"),
				wn.synset("steam.v.03"),
				wn.synset("steamer.v.01")],

	# rain
	"U+320a":	[wn.synset("rain.n.01")],

	# hail
	"U+320b":	[wn.synset("hail.n.01")],

	# ice
	"U+320e":	[wn.synset("ice.n.01")],

	# pool, snooker
	"U+320f":	[wn.synset("consortium.n.01"),
				wn.synset("pond.n.01"),
				wn.synset("pool.n.01"),
				wn.synset("pool.n.03"),
				wn.synset("pool.n.05"),
				wn.synset("pool.n.06"),
				wn.synset("pool.n.07"),
				wn.synset("pool.n.08"),
				wn.synset("pool.n.09"),
				wn.synset("snooker.n.01")],

	# snow
	"U+3210":	[wn.synset("snow.n.01"),
				wn.synset("snow.n.02")],

	# snowflake
	"U+3211":	[wn.synset("snowflake.n.01")],

	# freeze, solidify
	"U+3212":	[wn.synset("freeze.v.08")],

	# rice
	"U+3214":	[wn.synset("rice.n.01")],

	# mud, clay
	"U+3215":	[wn.synset("mud.n.01")],

	# swamp, bog, marsh
	"U+3216":	[wn.synset("bog.n.01"),
				wn.synset("marsh.n.01"),
				wn.synset("marsh.n.02"),
				wn.synset("marsh.n.03"),
				wn.synset("swamp.n.01"),
				wn.synset("swamp.n.02")],

	# island
	"U+3217":	[wn.synset("island.n.01")],

	# medicine, medication, medical practice practice
	"U+3219":	[wn.synset("medicine.n.01"),
				wn.synset("medicine.n.03")],

	# sperm
	"U+321b":	[wn.synset("sperm.n.01")],

	# feeling, emotion, sensation
	"U+321f":	[wn.synset("emotion.n.01"),
				wn.synset("feeling.n.01")],

	# comfort, console
	"U+3221":	[wn.synset("comfort.v.01")],

	# discomfort
	"U+3222":	[wn.synset("discomfort.n.01")],

	# cloth, fabric, material, textile, net
	"U+3223":	[wn.synset("fabric.n.01")],

	# number
	"U+3224":	[wn.synset("act.n.04"),
				wn.synset("issue.n.02"),
				wn.synset("number.n.02"),
				wn.synset("number.n.08")],

	# garage
	"U+3226":	[wn.synset("garage.n.01")],

	# yard
	"U+3228":	[wn.synset("yard.n.02")],

	# fence, wall
	"U+3229":	[wn.synset("fence.n.01")],

	# chimney
	"U+322a":	[wn.synset("chimney.n.01")],

	# ear, spike, capitulum
	"U+322b":	[wn.synset("auricle.n.02"),
				wn.synset("capitulum.n.01"),
				wn.synset("capitulum.n.03"),
				wn.synset("ear.n.01"),
				wn.synset("ear.n.02"),
				wn.synset("ear.n.04"),
				wn.synset("ear.n.05"),
				wn.synset("spike.n.01"),
				wn.synset("spike.n.02"),
				wn.synset("spike.n.04"),
				wn.synset("spike.n.05"),
				wn.synset("spike.n.07"),
				wn.synset("spike.n.08"),
				wn.synset("spike.n.09"),
				wn.synset("spike.n.10"),
				wn.synset("spike.n.11"),
				wn.synset("spike_heel.n.01")],

	# sound
	"U+322c":	[wn.synset("sound.v.01")],

	# deafness
	"U+322d":	[wn.synset("deafness.n.01")],

	# continue, pass
	"U+322f":	[wn.synset("authorize.v.01"),
				wn.synset("communicate.v.01"),
				wn.synset("continue.v.01"),
				wn.synset("continue.v.02"),
				wn.synset("continue.v.03"),
				wn.synset("continue.v.06"),
				wn.synset("continue.v.07"),
				wn.synset("continue.v.10"),
				wn.synset("cover.v.03"),
				wn.synset("die.v.01"),
				wn.synset("elapse.v.01"),
				wn.synset("evanesce.v.01"),
				wn.synset("exceed.v.02"),
				wn.synset("excrete.v.01"),
				wn.synset("fall.v.21"),
				wn.synset("guide.v.05"),
				wn.synset("happen.v.01"),
				wn.synset("legislate.v.01"),
				wn.synset("pass.v.01"),
				wn.synset("pass.v.05"),
				wn.synset("pass.v.07"),
				wn.synset("pass.v.09"),
				wn.synset("pass.v.14"),
				wn.synset("pass.v.16"),
				wn.synset("pass.v.17"),
				wn.synset("pass.v.18"),
				wn.synset("pass.v.20"),
				wn.synset("pass.v.22"),
				wn.synset("proceed.v.02"),
				wn.synset("retain.v.02"),
				wn.synset("run.v.03"),
				wn.synset("sink.v.03"),
				wn.synset("spend.v.01"),
				wn.synset("stay.v.04"),
				wn.synset("travel_by.v.01")],

	# gas
	"U+3231":	[wn.synset("gas.n.01")],

	# bubble
	"U+3232":	[wn.synset("bubble.n.01")],

	# give, offer, provide, sacrifice
	"U+3233":	[wn.synset("offer.v.01"),
				wn.synset("offer.v.02"),
				wn.synset("offer.v.06"),
				wn.synset("offer.v.07"),
				wn.synset("offer.v.09"),
				wn.synset("sacrifice.v.02"),
				wn.synset("sacrifice.v.04"),
				wn.synset("volunteer.v.02")],

	# exchange, substitute, trade, substitution
	"U+3234":	[wn.synset("trade.v.04")],

	# forward
	"U+3236":	[wn.synset("forward.n.01"),
				wn.synset("forward.n.02")],

	# meet, encounter, see
	"U+3237":	[wn.synset("meet.v.01"),
				wn.synset("meet.v.02"),
				wn.synset("meet.v.08"),
				wn.synset("meet.v.10"),
				wn.synset("run_into.v.01")],

	# river, stream, current
	"U+3239":	[wn.synset("river.n.01")],

	# agreement, contract
	"U+323a":	[wn.synset("agreement.n.01")],

	# back and forth, backward and forward, to and fro
	"U+323b":	[wn.synset("back_and_forth.r.01"),
				wn.synset("up_and_down.r.01")],

	# through
	"U+323c":	[wn.synset("done.s.01"),
				wn.synset("through.r.01"),
				wn.synset("through.r.02"),
				wn.synset("through.r.03"),
				wn.synset("through.r.04"),
				wn.synset("through.r.05"),
				wn.synset("through.s.02"),
				wn.synset("trap.n.06")],

	# visit
	"U+323d":	[wn.synset("sojourn.n.01"),
				wn.synset("visit.n.01"),
				wn.synset("visit.n.02")],

	# understand, see
	"U+323e":	[wn.synset("understand.v.02")],

	# crush, squeeze
	"U+3240":	[wn.synset("beat.v.01"),
				wn.synset("break_down.v.01"),
				wn.synset("coerce.v.01"),
				wn.synset("compress.v.02"),
				wn.synset("crush.v.04"),
				wn.synset("crush.v.05"),
				wn.synset("crush.v.08"),
				wn.synset("embrace.v.02"),
				wn.synset("extort.v.02"),
				wn.synset("jam.v.03"),
				wn.synset("oppress.v.01"),
				wn.synset("pinch.v.01"),
				wn.synset("squash.v.01"),
				wn.synset("squeeze.v.02"),
				wn.synset("thrust.v.02"),
				wn.synset("wedge.v.02")],

	# push, shove, pushing
	"U+3241":	[wn.synset("energy.n.03"),
				wn.synset("push.n.01"),
				wn.synset("push.n.02"),
				wn.synset("push.n.05"),
				wn.synset("push_button.n.01")],

	# end, arrival, stop
	"U+3243":	[wn.synset("arrival.n.01"),
				wn.synset("arrival.n.02"),
				wn.synset("end.n.01"),
				wn.synset("end.n.02"),
				wn.synset("end.n.03"),
				wn.synset("end.n.05"),
				wn.synset("end.n.06"),
				wn.synset("goal.n.01")],

	# race, competition, contest
	"U+3244":	[wn.synset("competition.n.03"),
				wn.synset("contest.n.01")],

	# get, acquire, receive
	"U+3247":	[wn.synset("get.v.25"),
				wn.synset("receive.v.01"),
				wn.synset("receive.v.02")],

	# crash
	"U+3248":	[wn.synset("clang.n.01"),
				wn.synset("crash.n.02"),
				wn.synset("crash.n.03"),
				wn.synset("crash.n.04"),
				wn.synset("crash.n.05")],

	# mirror
	"U+324b":	[wn.synset("mirror.n.01")],

	# success
	"U+324d":	[wn.synset("success.n.01"),
				wn.synset("success.n.03")],

	# backward, back
	"U+324e":	[wn.synset("back.r.02"),
				wn.synset("back.r.04")],

	# gathering, assembly, meeting, conference
	"U+3251":	[wn.synset("meeting.n.01")],

	# explosive
	"U+3252":	[wn.synset("explosive.a.01")],

	# year
	"U+3253":	[wn.synset("year.n.01")],

	# atom
	"U+3255":	[wn.synset("atom.n.01")],

	# nucleus
	"U+3256":	[wn.synset("nucleus.n.02")],

	# rotate, circle, circulate, wind up
	"U+3257":	[wn.synset("revolve.v.01")],

	# mix, blend
	"U+3258":	[wn.synset("blend.v.03"),
				wn.synset("shuffle.v.03")],

	# jump
	"U+3259":	[wn.synset("blow_out.v.01"),
				wn.synset("cut.v.11"),
				wn.synset("explode.v.02"),
				wn.synset("hop.v.01"),
				wn.synset("hop.v.06"),
				wn.synset("jump.n.01"),
				wn.synset("jump.n.03"),
				wn.synset("jump.n.05"),
				wn.synset("jump.n.06"),
				wn.synset("jump.v.01"),
				wn.synset("jump.v.13"),
				wn.synset("leap.n.02"),
				wn.synset("leap.v.02"),
				wn.synset("startle.n.01"),
				wn.synset("vault.v.01"),
				wn.synset("vault.v.02")],

	# turn, turning, play
	"U+325a":	[wn.synset("turn.v.10")],

	# swing, swinging, sway, rock
	"U+325c":	[wn.synset("swing.n.02")],

	# tractor
	"U+325f":	[wn.synset("tractor.n.01"),
				wn.synset("tractor.n.02")],

	# wheel
	"U+3260":	[wn.synset("wheel.n.01")],

	# balloon
	"U+3264":	[wn.synset("balloon.n.01"),
				wn.synset("balloon.n.02")],

	# sun
	"U+3265":	[wn.synset("sun.n.01")],

	# north
	"U+3266":	[wn.synset("north.n.01"),
				wn.synset("north.n.03"),
				wn.synset("north.n.04"),
				wn.synset("north.n.05"),
				wn.synset("north.n.06"),
				wn.synset("north.n.07"),
				wn.synset("union.n.02")],

	# east
	"U+3267":	[wn.synset("east.n.01")],

	# south
	"U+3268":	[wn.synset("south.n.03")],

	# west
	"U+3269":	[wn.synset("west.n.02")],

	# weather
	"U+326a":	[wn.synset("weather.n.01")],

	# change, alteration, alter
	"U+326b":	[wn.synset("change.v.02"),
				wn.synset("change.v.03")],

	# development
	"U+326c":	[wn.synset("development.n.02")],

	# machine, appliance, engine, motor
	"U+326d":	[wn.synset("machine.n.01")],

	# ring
	"U+326e":	[wn.synset("band.n.12"),
				wn.synset("hoop.n.02"),
				wn.synset("ring.n.08")],

	# melon
	"U+326f":	[wn.synset("melon.n.01"),
				wn.synset("melon.n.02")],

	# light
	"U+3270":	[wn.synset("light.a.01")],

	# egg, fried egg, poached egg, ovum, boiled egg
	"U+3271":	[wn.synset("egg.n.02")],

	# head
	"U+3273":	[wn.synset("head.n.01")],

	# face
	"U+3274":	[wn.synset("face.n.01")],

	# chin
	"U+3275":	[wn.synset("chin.n.01")],

	# cheek
	"U+3276":	[wn.synset("cheek.n.01")],

	# forehead
	"U+3277":	[wn.synset("brow.n.01")],

	# beard
	"U+3278":	[wn.synset("beard.n.01")],

	# pimple, blemish
	"U+3279":	[wn.synset("pimple.n.01")],

	# raccoon
	"U+327b":	[wn.synset("raccoon.n.02")],

	# bear
	"U+327c":	[wn.synset("bear.n.01")],

	# day
	"U+327d":	[wn.synset("day.n.01")],

	# life
	"U+327e":	[wn.synset("life.n.03")],

	# death
	"U+327f":	[wn.synset("death.n.02")],

	# new
	"U+3280":	[wn.synset("new.a.01")],

	# pizza
	"U+3281":	[wn.synset("pizza.n.01")],

	# time
	"U+3283":	[wn.synset("time.n.03"),
				wn.synset("time.n.05")],

	# poetry
	"U+3285":	[wn.synset("poetry.n.01")],

	# metaphor
	"U+3286":	[wn.synset("metaphor.n.01")],

	# pretend, make believe believe
	"U+3287":	[wn.synset("dissemble.v.03"),
				wn.synset("feign.v.01"),
				wn.synset("guess.v.02"),
				wn.synset("make.v.42"),
				wn.synset("pretend.v.03"),
				wn.synset("profess.v.07")],

	# generalization
	"U+3289":	[wn.synset("abstraction.n.03")],

	# girl
	"U+328a":	[wn.synset("female_child.n.01")],

	# boy, lad
	"U+328b":	[wn.synset("boy.n.02"),
				wn.synset("male_child.n.01"),
				wn.synset("son.n.01")],

	# child, kid, youngster
	"U+328c":	[wn.synset("child.n.01"),
				wn.synset("child.n.02"),
				wn.synset("child.n.03")],

	# money, cash
	"U+328d":	[wn.synset("cash.n.01"),
				wn.synset("cash.n.02"),
				wn.synset("cash.n.03"),
				wn.synset("money.n.01"),
				wn.synset("money.n.02"),
				wn.synset("money.n.03")],

	# flower, bloom, blossom
	"U+328f":	[wn.synset("flower.n.01")],

	# stem, stalk
	"U+3290":	[wn.synset("stalk.n.02")],

	# garden
	"U+3291":	[wn.synset("garden.n.01")],

	# plant
	"U+3294":	[wn.synset("plant.n.02")],

	# park
	"U+3295":	[wn.synset("park.n.02")],

	# tennis, racket sport, racquet sport
	"U+3296":	[wn.synset("tennis.n.01")],

	# mouth, open mouth, gape
	"U+3297":	[wn.synset("gape.n.01"),
				wn.synset("gape.n.02"),
				wn.synset("mouth.n.01"),
				wn.synset("mouth.n.02"),
				wn.synset("mouth.n.03"),
				wn.synset("mouth.n.04"),
				wn.synset("mouth.n.05"),
				wn.synset("mouth.n.08"),
				wn.synset("mouthpiece.n.03"),
				wn.synset("sass.n.01")],

	# currants
	"U+3299":	[wn.synset("currant.n.01"),
				wn.synset("currant.n.02"),
				wn.synset("currant.n.03")],

	# spider
	"U+329a":	[wn.synset("spider.n.01")],

	# eye
	"U+329b":	[wn.synset("eye.n.01"),
				wn.synset("eye.n.02")],

	# eyelid
	"U+329c":	[wn.synset("eyelid.n.01")],

	# colour
	"U+329d":	[wn.synset("color.n.01")],

	# news
	"U+329e":	[wn.synset("news.n.01"),
				wn.synset("news.n.02"),
				wn.synset("news.n.04"),
				wn.synset("news_program.n.01"),
				wn.synset("newsworthiness.n.01")],

	# blind
	"U+32a0":	[wn.synset("blind.a.01")],

	# taste, gustation, sense of taste of taste
	"U+32a1":	[wn.synset("preference.n.01"),
				wn.synset("taste.n.06")],

	# food
	"U+32a2":	[wn.synset("food.n.01"),
				wn.synset("food.n.02"),
				wn.synset("food.n.03"),
				wn.synset("frozen_food.n.01")],

	# spread, paste
	"U+32a3":	[wn.synset("spread.n.05")],

	# be, am, are, is, exist
	"U+32a4":	[wn.synset("be.v.01"),
				wn.synset("exist.v.01")],

	# event, happening, occasion
	"U+32a5":	[wn.synset("event.n.01")],

	# nonspeaking
	"U+32a6":	[wn.synset("nonspeaking.a.01")],

	# name, label, term, title
	"U+32a7":	[wn.synset("name.n.01")],

	# language
	"U+32a8":	[wn.synset("language.n.01"),
				wn.synset("language.n.05"),
				wn.synset("speech.n.02")],

	# combination, connection
	"U+32a9":	[wn.synset("combination.n.01"),
				wn.synset("combination.n.03")],

	# spit
	"U+32aa":	[wn.synset("spit.v.01")],

	# kiss
	"U+32ab":	[wn.synset("kiss.n.01")],

	# grapes
	"U+32ac":	[wn.synset("grape.n.01")],

	# bow, fore, arc
	"U+32ad":	[wn.synset("arc.n.02"),
				wn.synset("bow.n.01"),
				wn.synset("bow.n.02"),
				wn.synset("bow.n.03"),
				wn.synset("bow.n.04"),
				wn.synset("bow.n.05"),
				wn.synset("bow.n.06"),
				wn.synset("bow.n.07"),
				wn.synset("bow.n.08"),
				wn.synset("bow.n.09"),
				wn.synset("discharge.n.05")],

	# berry
	"U+32ae":	[wn.synset("berry.n.01"),
				wn.synset("berry.n.02"),
				wn.synset("berry.n.03")],

	# strawberry
	"U+32af":	[wn.synset("strawberry.n.01"),
				wn.synset("strawberry.n.02"),
				wn.synset("strawberry.n.03")],

	# ball
	"U+32b2":	[wn.synset("ball.n.01"),
				wn.synset("ball.n.03"),
				wn.synset("testis.n.01")],

	# earphones, headphones
	"U+32b4":	[wn.synset("earphone.n.01"),
				wn.synset("headset.n.01")],

	# fruit
	"U+32b5":	[wn.synset("fruit.n.01")],

	# plum, drupe
	"U+32b7":	[wn.synset("plum.n.02")],

	# cherries
	"U+32b8":	[wn.synset("cherry.n.03")],

	# smoking
	"U+32ba":	[wn.synset("smoke.n.02"),
				wn.synset("smoke.n.07")],

	# cigarette
	"U+32bb":	[wn.synset("cigarette.n.01")],

	# pipe, smoking pipe pipe, hose, tube
	"U+32bc":	[wn.synset("hose.n.02"),
				wn.synset("hose.n.03"),
				wn.synset("hosiery.n.01"),
				wn.synset("metro.n.01"),
				wn.synset("organ_pipe.n.01"),
				wn.synset("pipe.n.01"),
				wn.synset("pipe.n.02"),
				wn.synset("pipe.n.03"),
				wn.synset("pipe.n.04"),
				wn.synset("tube.n.01"),
				wn.synset("tube.n.02"),
				wn.synset("tube.n.04")],

	# baby girl
	"U+32bd":	[wn.synset("baby.n.01")],

	# baby boy
	"U+32be":	[wn.synset("baby.n.01")],

	# scissors
	"U+32bf":	[wn.synset("scissors.n.01")],

	# baby, infant
	"U+32c1":	[wn.synset("baby.n.01")],

	# raspberry, blackberry, compound berry berry
	"U+32c4":	[wn.synset("raspberry.n.01"),
				wn.synset("raspberry.n.02")],

	# conscience
	"U+32c6":	[wn.synset("conscience.n.01")],

	# forgive, pardon
	"U+32c7":	[wn.synset("excuse.v.01"),
				wn.synset("forgive.v.01")],

	# moral, good, right
	"U+32c8":	[wn.synset("correct.a.01"),
				wn.synset("correct.s.02"),
				wn.synset("estimable.s.02"),
				wn.synset("full.s.06"),
				wn.synset("good.a.01"),
				wn.synset("good.a.03"),
				wn.synset("right.a.04"),
				wn.synset("right.a.05")],

	# immoral, bad, wrong
	"U+32c9":	[wn.synset("amiss.s.01"),
				wn.synset("bad.a.01"),
				wn.synset("bad.s.02"),
				wn.synset("bad.s.03"),
				wn.synset("bad.s.04"),
				wn.synset("bad.s.06"),
				wn.synset("bad.s.07"),
				wn.synset("bad.s.08"),
				wn.synset("bad.s.09"),
				wn.synset("bad.s.10"),
				wn.synset("bad.s.11"),
				wn.synset("bad.s.12"),
				wn.synset("bad.s.13"),
				wn.synset("bad.s.14"),
				wn.synset("base.s.04"),
				wn.synset("faulty.s.02"),
				wn.synset("ill-timed.s.01"),
				wn.synset("immoral.a.01"),
				wn.synset("improper.s.03"),
				wn.synset("incorrect.a.01"),
				wn.synset("regretful.a.01"),
				wn.synset("wrong.a.02"),
				wn.synset("wrong.a.05"),
				wn.synset("wrong.s.06"),
				wn.synset("wrong.s.07")],

	# mind, intellect, reason
	"U+32ca":	[wn.synset("intellectual.n.01"),
				wn.synset("mind.n.01"),
				wn.synset("mind.n.02"),
				wn.synset("mind.n.06"),
				wn.synset("mind.n.07"),
				wn.synset("thinker.n.01")],

	# wish, desire
	"U+32cb":	[wn.synset("wish.v.03")],

	# decision
	"U+32cd":	[wn.synset("decision.n.02")],

	# idea, thought
	"U+32ce":	[wn.synset("idea.n.01")],

	# opinion
	"U+32cf":	[wn.synset("opinion.n.01")],

	# observe
	"U+32d0":	[wn.synset("note.v.03"),
				wn.synset("watch.v.02")],

	# nonsense
	"U+32d1":	[wn.synset("nonsense.n.01")],

	# state of mind
	"U+32d2":	[wn.synset("cognitive_state.n.01"),
				wn.synset("emotional_state.n.01"),
				wn.synset("psychological_state.n.01"),
				wn.synset("state_of_mind.n.01")],

	# fact
	"U+32d3":	[wn.synset("fact.n.01")],

	# meaning, sense, significance
	"U+32d4":	[wn.synset("meaning.n.02")],

	# use
	"U+32d5":	[wn.synset("use.v.01"),
				wn.synset("use.v.02"),
				wn.synset("use.v.04")],

	# knowledge, class
	"U+32d6":	[wn.synset("cognition.n.01")],

	# forget
	"U+32d7":	[wn.synset("forget.v.02")],

	# kind, kindly
	"U+32d9":	[wn.synset("charitable.s.03"),
				wn.synset("kind.a.01"),
				wn.synset("kind.s.02"),
				wn.synset("kind.s.03"),
				wn.synset("kindly.s.02")],

	# fan
	"U+32da":	[wn.synset("fan.n.01"),
				wn.synset("fan.n.03"),
				wn.synset("sports_fan.n.01"),
				wn.synset("ventilator.n.01")],

	# good, well, fine, ok, okay, all right right
	"U+32db":	[wn.synset("good.a.01")],

	# science, body of learning of learning
	"U+32dc":	[wn.synset("science.n.01")],

	# truth
	"U+32dd":	[wn.synset("truth.n.01"),
				wn.synset("truth.n.03")],

	# mathematics, arithmetic, math
	"U+32de":	[wn.synset("mathematics.n.01")],

	# beetle
	"U+32df":	[wn.synset("beetle.n.01"),
				wn.synset("mallet.n.03")],

	# bad, wrong
	"U+32e1":	[wn.synset("bad.s.07")],

	# judge
	"U+32e2":	[wn.synset("evaluate.v.02"),
				wn.synset("judge.v.01"),
				wn.synset("pronounce.v.02")],

	# selfishness, egoism
	"U+32e3":	[wn.synset("egoism.n.01"),
				wn.synset("egoism.n.02"),
				wn.synset("selfishness.n.01")],

	# consideration, thoughtfulness
	"U+32e4":	[wn.synset("circumstance.n.03"),
				wn.synset("consideration.n.01"),
				wn.synset("consideration.n.03"),
				wn.synset("consideration.n.04"),
				wn.synset("consideration.n.06"),
				wn.synset("contemplation.n.02"),
				wn.synset("retainer.n.01"),
				wn.synset("thoughtfulness.n.03")],

	# doubt, uncertainty
	"U+32e5":	[wn.synset("doubt.n.02")],

	# interest
	"U+32e6":	[wn.synset("interest.n.01"),
				wn.synset("interest.n.03"),
				wn.synset("interest.n.04"),
				wn.synset("interest.n.05"),
				wn.synset("interest.n.06"),
				wn.synset("pastime.n.01"),
				wn.synset("sake.n.01")],

	# importance, significance
	"U+32e7":	[wn.synset("importance.n.01"),
				wn.synset("importance.n.02"),
				wn.synset("meaning.n.01"),
				wn.synset("significance.n.01"),
				wn.synset("significance.n.02")],

	# calculate
	"U+32e8":	[wn.synset("calculate.v.01")],

	# lead, direct, guide
	"U+32e9":	[wn.synset("jumper_cable.n.01"),
				wn.synset("lead.n.01"),
				wn.synset("lead.n.02"),
				wn.synset("lead.n.03"),
				wn.synset("lead.n.04"),
				wn.synset("lead.n.05"),
				wn.synset("lead.n.06"),
				wn.synset("lead.n.07"),
				wn.synset("lead.n.09"),
				wn.synset("lead.n.11"),
				wn.synset("lead.n.14"),
				wn.synset("lead.n.15"),
				wn.synset("lead.n.17"),
				wn.synset("leash.n.01"),
				wn.synset("spark_advance.n.01"),
				wn.synset("star.n.04"),
				wn.synset("tip.n.03")],

	# swan
	"U+32eb":	[wn.synset("swan.n.01")],

	# fish
	"U+32ec":	[wn.synset("fish.n.01"),
				wn.synset("fish.n.02")],

	# morning
	"U+32ed":	[wn.synset("morning.n.01")],

	# horizon
	"U+32ee":	[wn.synset("horizon.n.01")],

	# curve, curved line line
	"U+32ef":	[wn.synset("bend.n.03"),
				wn.synset("curve.n.01")],

	# container, bowl, holder, pouch, basket
	"U+32f0":	[wn.synset("basket.n.01"),
				wn.synset("basket.n.02"),
				wn.synset("basket.n.03"),
				wn.synset("basket.n.04"),
				wn.synset("bowl.n.01"),
				wn.synset("bowl.n.02"),
				wn.synset("bowl.n.03"),
				wn.synset("bowl.n.04"),
				wn.synset("bowl.n.07"),
				wn.synset("bowl.n.08"),
				wn.synset("bowling_ball.n.01"),
				wn.synset("container.n.01"),
				wn.synset("holder.n.01"),
				wn.synset("holder.n.02"),
				wn.synset("holder.n.03"),
				wn.synset("pouch.n.01"),
				wn.synset("pouch.n.02"),
				wn.synset("pouch.n.03"),
				wn.synset("roll.n.15"),
				wn.synset("stadium.n.01")],

	# float
	"U+32f1":	[wn.synset("float.v.01"),
				wn.synset("float.v.02"),
				wn.synset("float.v.03"),
				wn.synset("float.v.05"),
				wn.synset("float.v.09")],

	# sieve, colander, strainer
	"U+32f2":	[wn.synset("colander.n.01"),
				wn.synset("sieve.n.01"),
				wn.synset("strainer.n.01")],

	# take, bring, carry, move, transport, movement
	"U+32f3":	[wn.synset("bring.v.01"),
				wn.synset("lead.v.01")],

	# apple
	"U+32f7":	[wn.synset("apple.n.01")],

	# peach, nectarine
	"U+32f8":	[wn.synset("peach.n.03")],

	# cabbage
	"U+32f9":	[wn.synset("boodle.n.01"),
				wn.synset("cabbage.n.01"),
				wn.synset("cabbage.n.03")],

	# handbag
	"U+32fc":	[wn.synset("bag.n.04")],

	# dromedary
	"U+32fd":	[wn.synset("arabian_camel.n.01")],

	# camel
	"U+32fe":	[wn.synset("camel.n.01")],

	# mushroom
	"U+3300":	[wn.synset("mushroom.n.03")],

	# snake, grass snake, viper, boa
	"U+3301":	[wn.synset("snake.n.01")],

	# dolphin, porpoise
	"U+3304":	[wn.synset("dolphin.n.02")],

	# pig, boar
	"U+3306":	[wn.synset("hog.n.03")],

	# spiral, curl
	"U+3307":	[wn.synset("coil.n.01"),
				wn.synset("helix.n.01"),
				wn.synset("spiral.n.01"),
				wn.synset("spiral.n.03"),
				wn.synset("spiral.n.04"),
				wn.synset("spiral.n.06")],

	# gun, firearm
	"U+3309":	[wn.synset("gun.n.01")],

	# pliers
	"U+330b":	[wn.synset("pliers.n.01")],

	# dog, canine, canid
	"U+330c":	[wn.synset("dog.n.01")],

	# tail
	"U+330d":	[wn.synset("tail.n.01")],

	# pineapple
	"U+330f":	[wn.synset("pineapple.n.02")],

	# airplane, aeroplane, plane
	"U+3312":	[wn.synset("airplane.n.01")],

	# angel
	"U+3315":	[wn.synset("angel.n.01")],

	# fly
	"U+3316":	[wn.synset("fly.v.01")],

	# bird
	"U+3317":	[wn.synset("bird.n.01")],

	# bat
	"U+3319":	[wn.synset("bat.n.05")],

	# tree
	"U+331e":	[wn.synset("tree.n.01")],

	# branch
	"U+331f":	[wn.synset("branch.n.02")],

	# trunk, tree trunk
	"U+3320":	[wn.synset("trunk.n.01")],

	# evergreen tree, spruce, fir, fir tree
	"U+3321":	[wn.synset("evergreen.n.01"),
				wn.synset("fir.n.01"),
				wn.synset("fir.n.02"),
				wn.synset("spruce.n.01"),
				wn.synset("spruce.n.02")],

	# countryside, country
	"U+3322":	[wn.synset("country.n.04"),
				wn.synset("countryside.n.01")],

	# shamrock
	"U+3327":	[wn.synset("clover.n.01"),
				wn.synset("common_wood_sorrel.n.01"),
				wn.synset("hop_clover.n.02"),
				wn.synset("white_clover.n.01")],

	# corn
	"U+332a":	[wn.synset("corn.n.01"),
				wn.synset("corn.n.02"),
				wn.synset("corn.n.03"),
				wn.synset("corn.n.04"),
				wn.synset("corn.n.05"),
				wn.synset("corn.n.07"),
				wn.synset("corn_whiskey.n.01")],

	# celery
	"U+332b":	[wn.synset("celery.n.01"),
				wn.synset("celery.n.02")],

	# cheese
	"U+332d":	[wn.synset("cheese.n.01")],

	# grass
	"U+332e":	[wn.synset("grass.n.01")],

	# grain, cereal
	"U+332f":	[wn.synset("grain.n.02")],

	# field
	"U+3330":	[wn.synset("field.n.03"),
				wn.synset("field.n.05")],

	# iron, smoothing iron iron
	"U+3331":	[wn.synset("iron.n.04")],

	# beaver
	"U+3332":	[wn.synset("beaver.n.07")],

	# shellfish
	"U+3334":	[wn.synset("bivalve.n.01"),
				wn.synset("crustacean.n.01"),
				wn.synset("mollusk.n.01"),
				wn.synset("shellfish.n.01")],

	# past
	"U+3335":	[wn.synset("past.n.01")],

	# present
	"U+3336":	[wn.synset("present.n.01")],

	# moon
	"U+3337":	[wn.synset("lunar_month.n.01"),
				wn.synset("moon.n.01"),
				wn.synset("moon.n.02"),
				wn.synset("moon.n.05"),
				wn.synset("moon.n.06"),
				wn.synset("moonlight.n.01")],

	# banana
	"U+3338":	[wn.synset("banana.n.02")],

	# future
	"U+3339":	[wn.synset("future.n.01")],

	# bean, chick pea, kidney bean, pinto bean
	"U+333a":	[wn.synset("bean.n.01")],

	# peas
	"U+333b":	[wn.synset("pea.n.01")],

	# expectation, anticipation
	"U+333c":	[wn.synset("anticipation.n.04"),
				wn.synset("expectation.n.01")],

	# insurance
	"U+333d":	[wn.synset("indemnity.n.01")],

	# snowshoe
	"U+333e":	[wn.synset("snowshoe.n.01")],

	# leaf, flap
	"U+333f":	[wn.synset("leaf.n.01")],

	# turnip, rutabaga, vegetable
	"U+3340":	[wn.synset("rutabaga.n.01"),
				wn.synset("rutabaga.n.02"),
				wn.synset("turnip.n.01"),
				wn.synset("turnip.n.02"),
				wn.synset("vegetable.n.01"),
				wn.synset("vegetable.n.02")],

	# lemon
	"U+3341":	[wn.synset("gamboge.n.02"),
				wn.synset("lemon.n.01"),
				wn.synset("lemon.n.03"),
				wn.synset("lemon.n.04"),
				wn.synset("lemon.n.05")],

	# butterfly, moth
	"U+3342":	[wn.synset("butterfly.n.01")],

	# body, trunk
	"U+3343":	[wn.synset("body.n.01")],

	# chest
	"U+3344":	[wn.synset("breast.n.01"),
				wn.synset("chest.n.02"),
				wn.synset("chest_of_drawers.n.01"),
				wn.synset("thorax.n.02")],

	# breasts
	"U+3345":	[wn.synset("breast.n.02")],

	# crotch
	"U+3346":	[wn.synset("crotch.n.02"),
				wn.synset("fork.n.03"),
				wn.synset("genitalia.n.01")],

	# waist
	"U+3348":	[wn.synset("waist.n.01")],

	# shoulder
	"U+3349":	[wn.synset("shoulder.n.01")],

	# stomach, tummy, tum, abdomen, belly
	"U+334b":	[wn.synset("stomach.n.01")],

	# embryo
	"U+334c":	[wn.synset("embryo.n.02")],

	# pubic hair
	"U+334e":	[wn.synset("hair.n.01"),
				wn.synset("hair.n.06")],

	# uterus, womb
	"U+334f":	[wn.synset("uterus.n.01")],

	# vagina
	"U+3351":	[wn.synset("vagina.n.01")],

	# ago, then
	"U+3352":	[wn.synset("ago.r.01"),
				wn.synset("ago.s.01"),
				wn.synset("then.n.01"),
				wn.synset("then.r.01")],

	# now
	"U+3353":	[wn.synset("now.n.01")],

	# then, so, later
	"U+3354":	[wn.synset("belated.s.01"),
				wn.synset("by_and_by.r.01"),
				wn.synset("former.s.03"),
				wn.synset("late.a.01"),
				wn.synset("late.a.05"),
				wn.synset("late.a.06"),
				wn.synset("late.s.03"),
				wn.synset("late.s.04"),
				wn.synset("later.r.03"),
				wn.synset("later.s.01"),
				wn.synset("sol.n.03"),
				wn.synset("subsequently.r.01"),
				wn.synset("then.n.01"),
				wn.synset("then.r.01")],

	# olive
	"U+3355":	[wn.synset("olive.n.01"),
				wn.synset("olive.n.02"),
				wn.synset("olive.n.03"),
				wn.synset("olive.n.04"),
				wn.synset("olive.n.05")],

	# pear
	"U+3356":	[wn.synset("pear.n.01")],

	# avocado
	"U+3357":	[wn.synset("avocado.n.01"),
				wn.synset("avocado.n.02")],

	# bread, loaf of bread, loaf of sliced bread
	"U+3358":	[wn.synset("bread.n.01")],

	# toast
	"U+3359":	[wn.synset("crispen.v.01"),
				wn.synset("roast.v.01"),
				wn.synset("toast.v.02")],

	# pita
	"U+335a":	[wn.synset("pita.n.01")],

	# roll, bun
	"U+335b":	[wn.synset("bun.n.01")],

	# hair
	"U+3360":	[wn.synset("hair's-breadth.n.01"),
				wn.synset("hair.n.01"),
				wn.synset("hair.n.03"),
				wn.synset("hair.n.04"),
				wn.synset("hair.n.06"),
				wn.synset("haircloth.n.01"),
				wn.synset("mane.n.02")],

	# fur, coat, hair, jacket, jumper, sweater
	"U+3361":	[wn.synset("fur.n.01")],

	# pit, stone
	"U+3362":	[wn.synset("pit.v.01"),
				wn.synset("pit.v.03"),
				wn.synset("scar.v.01"),
				wn.synset("stone.v.01")],

	# enclosure
	"U+3363":	[wn.synset("enclosure.n.01"),
				wn.synset("enclosure.n.03")],

	# bottom, base, bottom of a thing of a thing
	"U+3364":	[wn.synset("bed.n.03"),
				wn.synset("buttocks.n.01")],

	# top, top of a thing of a thing
	"U+3366":	[wn.synset("acme.n.01"),
				wn.synset("circus_tent.n.01"),
				wn.synset("peak.n.04"),
				wn.synset("top.n.01"),
				wn.synset("top.n.02"),
				wn.synset("top.n.04"),
				wn.synset("top.n.06"),
				wn.synset("top.n.07"),
				wn.synset("top.n.08"),
				wn.synset("top.n.09"),
				wn.synset("top.n.10")],
	# out of, exit
	"U+336a":	[wn.synset("exit.n.01"),
				wn.synset("exit.n.03"),
				wn.synset("passing.n.02")],

	# camera
	"U+336b":	[wn.synset("camera.n.01")],

	# projector
	"U+336c":	[wn.synset("projector.n.02")],

	# secret
	"U+336d":	[wn.synset("secret.n.01")],

	# sleep
	"U+336e":	[wn.synset("sleep.n.01")],

	# window
	"U+3373":	[wn.synset("window.n.01"),
				wn.synset("window.n.08")],

	# all, every, everything, total, whole
	"U+3374":	[wn.synset("all.a.01"),
				wn.synset("all.s.02"),
				wn.synset("every.s.01"),
				wn.synset("every.s.02"),
				wn.synset("sum.n.02"),
				wn.synset("sum.n.05"),
				wn.synset("whole.n.01"),
				wn.synset("whole.n.02"),
				wn.synset("wholly.r.01")],

	# chest of drawers, bureau, dresser
	"U+3376":	[wn.synset("chest_of_drawers.n.01")],

	# drawer
	"U+3377":	[wn.synset("drawer.n.01")],

	# book
	"U+3378":	[wn.synset("book.n.01")],

	# cupboard, closet, wardrobe
	"U+3379":	[wn.synset("cabinet.n.03"),
				wn.synset("closet.n.04"),
				wn.synset("cupboard.n.01"),
				wn.synset("wardrobe.n.01"),
				wn.synset("wardrobe.n.02"),
				wn.synset("wardrobe.n.03"),
				wn.synset("water_closet.n.01")],

	# answer, reply
	"U+337a":	[wn.synset("answer.n.01")],

	# exit
	"U+337b":	[wn.synset("exit.v.01")],

	# postcard
	"U+337c":	[wn.synset("postcard.n.01")],

	# transport, transportation
	"U+337f":	[wn.synset("transportation.n.05")],

	# cart, carriage
	"U+3380":	[wn.synset("assiduity.n.01"),
				wn.synset("baby_buggy.n.01"),
				wn.synset("carriage.n.02"),
				wn.synset("carriage.n.03"),
				wn.synset("carriage.n.04"),
				wn.synset("diligence.n.01"),
				wn.synset("passenger_car.n.01"),
				wn.synset("stagecoach.n.01")],

	# thing, object
	"U+3382":	[wn.synset("object.n.01")],

	# goods, contents
	"U+3383":	[wn.synset("capacity.n.03"),
				wn.synset("commodity.n.01"),
				wn.synset("content.n.01"),
				wn.synset("content.n.03"),
				wn.synset("content.n.05"),
				wn.synset("contentedness.n.01"),
				wn.synset("contents.n.01"),
				wn.synset("good.n.01"),
				wn.synset("good.n.02"),
				wn.synset("good.n.03"),
				wn.synset("message.n.02"),
				wn.synset("subject.n.02")],

	# waste, garbage, rubbish, trash
	"U+3385":	[wn.synset("folderol.n.01"),
				wn.synset("garbage.n.01"),
				wn.synset("rubbish.n.01"),
				wn.synset("trash.n.02")],

	# block, brick, city block block
	"U+3388":	[wn.synset("auction_block.n.01"),
				wn.synset("block.n.01"),
				wn.synset("block.n.02"),
				wn.synset("block.n.03"),
				wn.synset("block.n.04"),
				wn.synset("block.n.05"),
				wn.synset("block.n.06"),
				wn.synset("block.n.07"),
				wn.synset("blockage.n.02"),
				wn.synset("blocking.n.01"),
				wn.synset("engine_block.n.01"),
				wn.synset("pulley.n.01")],

	# pull, drag, tow, tug, pulling
	"U+338a":	[wn.synset("pull.v.01")],

	# solid thing
	"U+338c":	[wn.synset("solid.n.01")],

	# kite
	"U+3391":	[wn.synset("kite.n.03")],

	# rectangle, oblong
	"U+3394":	[wn.synset("rectangle.n.01")],

	# parcel, package
	"U+3395":	[wn.synset("package.n.01")],

	# paper, card, page
	"U+3396":	[wn.synset("batting_order.n.01"),
				wn.synset("calling_card.n.02"),
				wn.synset("card.n.01"),
				wn.synset("card.n.02"),
				wn.synset("card.n.03"),
				wn.synset("card.n.04"),
				wn.synset("card.n.08"),
				wn.synset("circuit_board.n.01"),
				wn.synset("composition.n.08"),
				wn.synset("menu.n.01"),
				wn.synset("newspaper.n.01"),
				wn.synset("newspaper.n.02"),
				wn.synset("newspaper.n.03"),
				wn.synset("page.n.01"),
				wn.synset("page.n.02"),
				wn.synset("page.n.03"),
				wn.synset("page.n.04"),
				wn.synset("page.n.05"),
				wn.synset("page.n.06"),
				wn.synset("paper.n.01"),
				wn.synset("paper.n.04"),
				wn.synset("paper.n.05"),
				wn.synset("poster.n.01"),
				wn.synset("wag.n.01")],

	# door
	"U+3397":	[wn.synset("door.n.01")],

	# goal
	"U+3398":	[wn.synset("goal.n.04")],

	# shelf
	"U+3399":	[wn.synset("shelf.n.01")],

	# room
	"U+339a":	[wn.synset("room.n.01")],

	# ceiling
	"U+339b":	[wn.synset("ceiling.n.01")],

	# floor, storey, level, etage
	"U+339c":	[wn.synset("degree.n.01"),
				wn.synset("degree.n.02"),
				wn.synset("floor.n.01"),
				wn.synset("floor.n.02"),
				wn.synset("floor.n.03"),
				wn.synset("floor.n.04"),
				wn.synset("floor.n.05"),
				wn.synset("floor.n.06"),
				wn.synset("floor.n.07"),
				wn.synset("floor.n.08"),
				wn.synset("floor.n.09"),
				wn.synset("floor.n.10"),
				wn.synset("grade.n.02"),
				wn.synset("horizontal_surface.n.01"),
				wn.synset("level.n.04"),
				wn.synset("level.n.05"),
				wn.synset("level.n.07")],

	# floor covering, linoleum
	"U+339d":	[wn.synset("linoleum.n.01")],

	# wall
	"U+339e":	[wn.synset("wall.n.01"),
				wn.synset("wall.n.02")],

	# corner
	"U+339f":	[wn.synset("corner.n.03")],

	# steam bath
	"U+33a0":	[wn.synset("sauna.n.01")],

	# shower
	"U+33a1":	[wn.synset("lavish.v.01"),
				wn.synset("shower.v.02"),
				wn.synset("shower.v.03"),
				wn.synset("shower.v.04"),
				wn.synset("shower.v.05")],

	# opening
	"U+33a2":	[wn.synset("opening.n.01"),
				wn.synset("opening.n.02"),
				wn.synset("opening.n.03"),
				wn.synset("opening.n.05")],

	# fireplace
	"U+33a3":	[wn.synset("fireplace.n.01")],

	# freedom, liberty
	"U+33a4":	[wn.synset("freedom.n.01")],

	# awake
	"U+33a5":	[wn.synset("alert.s.03"),
				wn.synset("awake.a.01")],

	# question, be sceptical, doubt
	"U+33a6":	[wn.synset("interrogate.v.02")],

	# badge, shield
	"U+33a9":	[wn.synset("badge.n.01"),
				wn.synset("badge.n.02"),
				wn.synset("carapace.n.01"),
				wn.synset("shield.n.01"),
				wn.synset("shield.n.02")],

	# table
	"U+33aa":	[wn.synset("table.n.03")],

	# board, board of directors, executive
	"U+33ab":	[wn.synset("administrator.n.03"),
				wn.synset("board.n.01"),
				wn.synset("board.n.02"),
				wn.synset("board.n.03"),
				wn.synset("board.n.04"),
				wn.synset("board.n.09"),
				wn.synset("circuit_board.n.01"),
				wn.synset("control_panel.n.01"),
				wn.synset("dining_table.n.01"),
				wn.synset("directorate.n.01"),
				wn.synset("display_panel.n.01"),
				wn.synset("executive.n.01"),
				wn.synset("executive.n.02"),
				wn.synset("management.n.01")],

	# edge
	"U+33ac":	[wn.synset("boundary.n.02"),
				wn.synset("edge.n.01"),
				wn.synset("edge.n.03"),
				wn.synset("edge.n.04"),
				wn.synset("edge.n.05"),
				wn.synset("edge.n.06")],

	# pier
	"U+33af":	[wn.synset("pier.n.01")],

	# brush
	"U+33b1":	[wn.synset("brush.v.01"),
				wn.synset("brush.v.02"),
				wn.synset("brush.v.03"),
				wn.synset("brush.v.04"),
				wn.synset("brush.v.05"),
				wn.synset("brush.v.06")],

	# box, cube
	"U+33b2":	[wn.synset("box.n.01")],

	# comb
	"U+33b3":	[wn.synset("comb.n.01")],

	# shekel
	"U+33b4":	[wn.synset("shekel.n.01")],

	# pot, kettle, boiler, pan
	"U+33b5":	[wn.synset("pot.n.01"),
				wn.synset("pot.n.03")],

	# glass, drinking glass glass
	"U+33b6":	[wn.synset("glass.n.02"),
				wn.synset("glass.n.03")],

	# mug, cup
	"U+33b7":	[wn.synset("chump.n.01"),
				wn.synset("countenance.n.03"),
				wn.synset("cup.n.01"),
				wn.synset("cup.n.02"),
				wn.synset("cup.n.03"),
				wn.synset("cup.n.04"),
				wn.synset("cup.n.05"),
				wn.synset("cup.n.06"),
				wn.synset("cup.n.07"),
				wn.synset("cup.n.08"),
				wn.synset("mug.n.01"),
				wn.synset("mug.n.04")],

	# effect, result
	"U+33b9":	[wn.synset("consequence.n.01"),
				wn.synset("effect.n.03"),
				wn.synset("effect.n.05"),
				wn.synset("effect.n.06"),
				wn.synset("impression.n.02")],

	# make, manufacture, produce
	"U+33ba":	[wn.synset("produce.v.02")],

	# cause
	"U+33bb":	[wn.synset("campaign.n.02"),
				wn.synset("causal_agent.n.01"),
				wn.synset("cause.n.01"),
				wn.synset("cause.n.02"),
				wn.synset("lawsuit.n.01")],

	# therefore, so, so that that
	"U+33bc":	[wn.synset("consequently.r.02"),
				wn.synset("sol.n.03"),
				wn.synset("therefore.r.01")],

	# mountain
	"U+33bd":	[wn.synset("mountain.n.01")],

	# mine
	"U+33be":	[wn.synset("mine.n.01")],

	# stone, rock
	"U+33bf":	[wn.synset("rock.n.01"),
				wn.synset("rock.n.02"),
				wn.synset("rock.n.03"),
				wn.synset("rock.n.04"),
				wn.synset("rock.n.07"),
				wn.synset("rock_'n'_roll.n.01"),
				wn.synset("rock_candy.n.01")],

	# valley
	"U+33c1":	[wn.synset("valley.n.01")],

	# bone
	"U+33c5":	[wn.synset("bone.n.01")],

	# structure, construction
	"U+33c6":	[wn.synset("structure.n.01"),
				wn.synset("structure.n.02"),
				wn.synset("structure.n.03")],

	# joint
	"U+33c7":	[wn.synset("joint.n.01")],

	# over, above, superior
	"U+33c9":	[wn.synset("above.n.01"),
				wn.synset("above.r.01"),
				wn.synset("above.r.02"),
				wn.synset("lake_superior.n.01"),
				wn.synset("over.n.01"),
				wn.synset("superior.n.01"),
				wn.synset("superior.n.02"),
				wn.synset("superior.n.05"),
				wn.synset("superscript.n.01"),
				wn.synset("upstairs.r.01"),
				wn.synset("victor.n.01")],

	# division
	"U+33ca":	[wn.synset("class.n.05"),
				wn.synset("division.n.01"),
				wn.synset("division.n.03"),
				wn.synset("division.n.04"),
				wn.synset("division.n.05"),
				wn.synset("division.n.07"),
				wn.synset("division.n.08"),
				wn.synset("division.n.09"),
				wn.synset("division.n.10"),
				wn.synset("division.n.11"),
				wn.synset("division.n.12"),
				wn.synset("part.n.09")],

	# part, bit, piece, portion, part of of
	"U+33cb":	[wn.synset("bit.n.05"),
				wn.synset("morsel.n.02")],

	# dot
	"U+33cc":	[wn.synset("acid.n.02"),
				wn.synset("department_of_transportation.n.01"),
				wn.synset("dot.n.03"),
				wn.synset("period.n.07"),
				wn.synset("point.n.09")],

	# again
	"U+33cd":	[wn.synset("again.r.01")],

	# there
	"U+33ce":	[wn.synset("speed_of_light.n.01"),
				wn.synset("there.n.01")],

	# before, in front of, prior to
	"U+33cf":	[wn.synset("ahead.r.01"),
				wn.synset("earlier.r.01")],

	# around
	"U+33d0":	[wn.synset("about.r.02"),
				wn.synset("round.r.01")],

	# either
	"U+33d1":	[wn.synset("either.r.01"),
				wn.synset("o.n.02")],

	# that
	"U+33d3":	[wn.synset("such.s.01")],

	# powder, dust
	"U+33d5":	[wn.synset("powder.n.01")],

	# stamp
	"U+33d7":	[wn.synset("stamp.n.08")],

	# fold, folding, pleating, pleat
	"U+33d9":	[wn.synset("fold.v.01")],

	# space, dimension
	"U+33db":	[wn.synset("dimension.n.01"),
				wn.synset("dimension.n.03"),
				wn.synset("distance.n.05"),
				wn.synset("outer_space.n.01"),
				wn.synset("property.n.04"),
				wn.synset("proportion.n.02"),
				wn.synset("quad.n.03"),
				wn.synset("space.n.01"),
				wn.synset("space.n.02"),
				wn.synset("space.n.03"),
				wn.synset("space.n.05"),
				wn.synset("space.n.07"),
				wn.synset("space.n.08")],

	# arm
	"U+33dc":	[wn.synset("arm.n.01")],

	# wrist
	"U+33dd":	[wn.synset("wrist.n.01")],

	# elbow
	"U+33de":	[wn.synset("elbow.n.01")],

	# muscle
	"U+33df":	[wn.synset("muscle.n.01")],

	# strong, powerful
	"U+33e0":	[wn.synset("brawny.s.01"),
				wn.synset("firm.s.03"),
				wn.synset("hard.s.10"),
				wn.synset("herculean.s.01"),
				wn.synset("impregnable.s.01"),
				wn.synset("knock-down.s.01"),
				wn.synset("potent.a.03"),
				wn.synset("potent.s.01"),
				wn.synset("potent.s.02"),
				wn.synset("powerful.a.01"),
				wn.synset("solid.s.07"),
				wn.synset("strong.a.01"),
				wn.synset("strong.s.02"),
				wn.synset("strong.s.07"),
				wn.synset("strong.s.09")],

	# health
	"U+33e2":	[wn.synset("health.n.01")],

	# ride, drive
	"U+33e4":	[wn.synset("drive.v.01")],

	# tray
	"U+33e8":	[wn.synset("tray.n.01")],

	# buttocks, bottom, bum, rear, ass, back of a thing of a thing
	"U+33eb":	[wn.synset("buttocks.n.01")],

	# genitals, sex organs organs
	"U+33ec":	[wn.synset("genitalia.n.01")],

	# erection, erect penis penis
	"U+33ed":	[wn.synset("erecting.n.01"),
				wn.synset("erection.n.01")],

	# male, masculine
	"U+33ee":	[wn.synset("male.a.01"),
				wn.synset("male.s.02"),
				wn.synset("male.s.03"),
				wn.synset("masculine.a.01"),
				wn.synset("masculine.a.02"),
				wn.synset("masculine.s.03")],

	# penis
	"U+33ef":	[wn.synset("penis.n.01")],

	# left
	"U+33f0":	[wn.synset("left.a.01"),
				wn.synset("left.a.04"),
				wn.synset("left.s.03"),
				wn.synset("leftover.s.01")],

	# right
	"U+33f1":	[wn.synset("correct.a.01"),
				wn.synset("correct.s.02"),
				wn.synset("correct.s.03"),
				wn.synset("good.s.12"),
				wn.synset("proper.s.04"),
				wn.synset("right.a.01"),
				wn.synset("right.a.04"),
				wn.synset("right.a.05"),
				wn.synset("right.a.07"),
				wn.synset("right.n.02"),
				wn.synset("right.n.04"),
				wn.synset("right.n.05"),
				wn.synset("right.s.08"),
				wn.synset("right.s.09"),
				wn.synset("right.s.11"),
				wn.synset("right.s.12"),
				wn.synset("veracious.s.02")],

	# key, tonality
	"U+33f3":	[wn.synset("key.n.01"),
				wn.synset("key.n.04"),
				wn.synset("key.n.15")],

	# protection, shelter
	"U+33f5":	[wn.synset("protection.n.01"),
				wn.synset("protection.n.04"),
				wn.synset("protective_covering.n.01")],

	# harbour
	"U+33f6":	[wn.synset("seaport.n.01")],

	# clothing, clothes, garment
	"U+33f7":	[wn.synset("clothing.n.01")],

	# marriage, wedding
	"U+33f8":	[wn.synset("marriage.n.01"),
				wn.synset("marriage.n.03"),
				wn.synset("marriage.n.04"),
				wn.synset("wedding.n.01")],

	# cone, conifer cone, strobilus
	"U+33f9":	[wn.synset("cone.n.01"),
				wn.synset("cone.n.02"),
				wn.synset("cone.n.03"),
				wn.synset("cone.n.04")],

	# farm
	"U+33fa":	[wn.synset("farm.n.01")],

	# parent
	"U+33fb":	[wn.synset("parent.n.01")],

	# birth
	"U+33fc":	[wn.synset("birth.n.01"),
				wn.synset("birth.n.02"),
				wn.synset("birth.n.05"),
				wn.synset("parentage.n.02"),
				wn.synset("parturition.n.01")],

	# daughter
	"U+33fd":	[wn.synset("daughter.n.01")],

	# son
	"U+33fe":	[wn.synset("son.n.01")],

	# offspring, child
	"U+33ff":	[wn.synset("offspring.n.01")],

	# umbrella
	"U+3400":	[wn.synset("gamp.n.01"),
				wn.synset("umbrella.n.01"),
				wn.synset("umbrella.n.02"),
				wn.synset("umbrella.n.03")],

	# mother, mom, mommy, mum
	"U+3401":	[wn.synset("mother.n.01")],

	# father, dad, daddy, papa, pa, pop
	"U+3402":	[wn.synset("father.n.01"),
				wn.synset("father.n.03"),
				wn.synset("father.n.06"),
				wn.synset("forefather.n.01"),
				wn.synset("founder.n.02")],

	# relative, relation
	"U+3403":	[wn.synset("relation.n.01"),
				wn.synset("relation.n.04"),
				wn.synset("relation.n.06"),
				wn.synset("relation_back.n.01"),
				wn.synset("relative.n.01"),
				wn.synset("relative.n.02"),
				wn.synset("sexual_intercourse.n.01")],

	# wife
	"U+3404":	[wn.synset("wife.n.01")],

	# stepmother
	"U+3405":	[wn.synset("stepmother.n.01")],

	# grandparent
	"U+3406":	[wn.synset("grandparent.n.01")],

	# aunt
	"U+3407":	[wn.synset("aunt.n.01")],

	# uncle
	"U+3408":	[wn.synset("uncle.n.01")],

	# grandmother, grandma, granny
	"U+3409":	[wn.synset("grandma.n.01")],

	# grandfather, granddad, grandpa
	"U+340c":	[wn.synset("grandfather.n.01")],

	# illness, disease, sickness
	"U+3410":	[wn.synset("illness.n.01")],

	# purpose
	"U+3412":	[wn.synset("function.n.02"),
				wn.synset("purpose.n.01")],

	# opposition, counter purpose purpose
	"U+3417":	[wn.synset("confrontation.n.04"),
				wn.synset("enemy.n.02"),
				wn.synset("opposition.n.02"),
				wn.synset("opposition.n.04"),
				wn.synset("opposition.n.05"),
				wn.synset("opposition.n.06"),
				wn.synset("opposition.n.08"),
				wn.synset("resistance.n.01")],

	# crystal
	"U+3419":	[wn.synset("crystal.n.05")],

	# pointer
	"U+341b":	[wn.synset("arrow.n.01"),
				wn.synset("cursor.n.01"),
				wn.synset("pointer.n.02"),
				wn.synset("pointer.n.04")],

	# about, concerning, in relation to, of
	"U+341c":	[wn.synset("about.r.02"),
				wn.synset("about.r.03"),
				wn.synset("about.r.04"),
				wn.synset("about.r.05"),
				wn.synset("about.r.06"),
				wn.synset("about.r.07"),
				wn.synset("about.s.01"),
				wn.synset("along.r.01"),
				wn.synset("approximately.r.01"),
				wn.synset("concern.v.02"),
				wn.synset("on.a.01"),
				wn.synset("on.a.02"),
				wn.synset("on.r.02"),
				wn.synset("on.r.03"),
				wn.synset("refer.v.02")],

	# at
	"U+341e":	[wn.synset("above.r.01"),
				wn.synset("above.r.02"),
				wn.synset("astatine.n.01"),
				wn.synset("at.n.02"),
				wn.synset("up.r.01"),
				wn.synset("upstairs.r.01")],

	# here
	"U+341f":	[wn.synset("hera.n.01"),
				wn.synset("here.n.01")],

	# heat
	"U+3423":	[wn.synset("heat.v.01")],

	# cold, common cold cold
	"U+3424":	[wn.synset("cold.a.01"),
				wn.synset("cold.a.02")],

	# nuclear radiation, radioactivity
	"U+3425":	[wn.synset("radiation.n.04")],

	# or
	"U+3426":	[wn.synset("o.n.02"),
				wn.synset("operating_room.n.01"),
				wn.synset("oregon.n.01")],

	# against, opposed to to
	"U+3427":	[wn.synset("antonym.n.01"),
				wn.synset("contrary.n.02"),
				wn.synset("inverse.n.01"),
				wn.synset("reverse.n.01")],

	# person, human being, individual
	"U+3428":	[wn.synset("person.n.01")],

	# spouse, cohabitant, partner
	"U+342d":	[wn.synset("collaborator.n.03"),
				wn.synset("partner.n.03"),
				wn.synset("spouse.n.01")],

	# addition, gain
	"U+3431":	[wn.synset("summation.n.04")],

	# and, also, plus, too
	"U+3434":	[wn.synset("asset.n.01"),
				wn.synset("besides.r.02"),
				wn.synset("excessively.r.01"),
				wn.synset("summation.n.04")],

	# belongs to, of
	"U+3437":	[wn.synset("delaware.n.04")],

	# cross, Christianity
	"U+3438":	[wn.synset("cross.v.05"),
				wn.synset("intersect.v.01"),
				wn.synset("traverse.v.01")],

	# across, through
	"U+3439":	[wn.synset("across.r.01"),
				wn.synset("across.r.02"),
				wn.synset("done.s.01"),
				wn.synset("over.r.03"),
				wn.synset("short.r.03"),
				wn.synset("through.r.01"),
				wn.synset("through.r.02"),
				wn.synset("through.r.03"),
				wn.synset("through.r.04"),
				wn.synset("through.r.05"),
				wn.synset("through.s.02")],

	# multiplication
	"U+343a":	[wn.synset("multiplication.n.03")],

	# choice, selection, election
	"U+343c":	[wn.synset("choice.n.01"),
				wn.synset("choice.n.02"),
				wn.synset("option.n.02")],

	# more
	"U+343d":	[wn.synset("additionally.r.01"),
				wn.synset("again.r.01"),
				wn.synset("more.a.01"),
				wn.synset("more.a.02"),
				wn.synset("more.r.01"),
				wn.synset("more.r.02"),
				wn.synset("most.r.01"),
				wn.synset("most.r.02"),
				wn.synset("no.r.01"),
				wn.synset("no_longer.r.01"),
				wn.synset("plus_sign.n.01"),
				wn.synset("quite.r.01")],

	# much, many, very
	"U+343e":	[wn.synset("identical.s.02"),
				wn.synset("many.a.01"),
				wn.synset("much.a.01"),
				wn.synset("very.s.01")],

	# war
	"U+343f":	[wn.synset("war.n.01")],

	# wand
	"U+3442":	[wn.synset("baton.n.01"),
				wn.synset("scepter.n.02"),
				wn.synset("wand.n.01"),
				wn.synset("wand.n.02")],

	# star
	"U+3444":	[wn.synset("star.n.01")],

	# comet
	"U+3447":	[wn.synset("comet.n.01")],

	# knife, sword
	"U+3448":	[wn.synset("knife.n.01")],

	# plough
	"U+344a":	[wn.synset("plow.n.01")],

	# creation, nature
	"U+344b":	[wn.synset("creation.n.01"),
				wn.synset("creation.n.02")],

	# danger
	"U+344d":	[wn.synset("danger.n.01"),
				wn.synset("danger.n.03"),
				wn.synset("danger.n.04"),
				wn.synset("risk.n.02")],

	# pyramid
	"U+344e":	[wn.synset("pyramid.n.01")],

	# rocket, spaceship
	"U+3450":	[wn.synset("rocket.n.01"),
				wn.synset("rocket.n.02"),
				wn.synset("rocket.n.03"),
				wn.synset("rocket.n.04"),
				wn.synset("skyrocket.n.02"),
				wn.synset("starship.n.01")],

	# female, feminine
	"U+3451":	[wn.synset("female.a.01"),
				wn.synset("female.s.02"),
				wn.synset("female.s.03"),
				wn.synset("feminine.a.01"),
				wn.synset("feminine.a.02"),
				wn.synset("feminine.s.04"),
				wn.synset("womanly.a.01")],

	# tooth
	"U+3452":	[wn.synset("tooth.n.01"),
				wn.synset("tooth.n.05")],

	# teeth
	"U+3453":	[wn.synset("dentition.n.02"),
				wn.synset("tooth.n.01"),
				wn.synset("tooth.n.02"),
				wn.synset("tooth.n.03"),
				wn.synset("tooth.n.04"),
				wn.synset("tooth.n.05")],

	# cavity, caries
	"U+3454":	[wn.synset("cavity.n.03")],

	# action, act, deed, demonstrate, demonstration
	"U+3457":	[wn.synset("act.v.01"),
				wn.synset("act.v.02"),
				wn.synset("act.v.03"),
				wn.synset("act.v.04"),
				wn.synset("act.v.05"),
				wn.synset("act.v.06"),
				wn.synset("act.v.08"),
				wn.synset("act.v.10"),
				wn.synset("attest.v.01"),
				wn.synset("carry_through.v.01"),
				wn.synset("demonstrate.v.04"),
				wn.synset("dissemble.v.03"),
				wn.synset("enforce.v.01"),
				wn.synset("enforce.v.02"),
				wn.synset("execute.v.01"),
				wn.synset("execute.v.02"),
				wn.synset("execute.v.04"),
				wn.synset("execute.v.07"),
				wn.synset("perform.v.01"),
				wn.synset("perform.v.03"),
				wn.synset("prove.v.02"),
				wn.synset("run.v.19"),
				wn.synset("show.v.01"),
				wn.synset("work.v.03")],

	# hip
	"U+3459":	[wn.synset("hip.n.01"),
				wn.synset("hip.n.03"),
				wn.synset("hip.n.04"),
				wn.synset("hip.n.05"),
				wn.synset("pelvis.n.01")],

	# leg
	"U+345a":	[wn.synset("leg.n.01")],

	# heel
	"U+345b":	[wn.synset("heel.n.02")],

	# foot
	"U+345c":	[wn.synset("foot.n.02")],

	# kick
	"U+345d":	[wn.synset("complain.v.01"),
				wn.synset("kick.v.01"),
				wn.synset("kick.v.02"),
				wn.synset("kick.v.03"),
				wn.synset("kick.v.04"),
				wn.synset("kick.v.06"),
				wn.synset("kick.v.07"),
				wn.synset("kick_back.v.02")],

	# toe
	"U+345e":	[wn.synset("toe.n.01")],

	# evaluation, value
	"U+3461":	[wn.synset("value.n.01"),
				wn.synset("value.n.06")],

	# work, employment, job
	"U+3463":	[wn.synset("caper.n.03"),
				wn.synset("employment.n.01"),
				wn.synset("employment.n.02"),
				wn.synset("employment.n.03"),
				wn.synset("job.n.02"),
				wn.synset("job.n.03"),
				wn.synset("job.n.04"),
				wn.synset("job.n.05"),
				wn.synset("job.n.06"),
				wn.synset("job.n.07"),
				wn.synset("job.n.09"),
				wn.synset("job.n.10"),
				wn.synset("job.n.11"),
				wn.synset("job.n.12"),
				wn.synset("occupation.n.01"),
				wn.synset("oeuvre.n.01"),
				wn.synset("problem.n.01"),
				wn.synset("study.n.02"),
				wn.synset("use.n.01"),
				wn.synset("work.n.01"),
				wn.synset("work.n.02"),
				wn.synset("work.n.05"),
				wn.synset("workplace.n.01")],

	# gender, sex
	"U+3465":	[wn.synset("gender.n.01")],

	# insect, bug
	"U+3466":	[wn.synset("insect.n.01")],

	# electricity
	"U+3472":	[wn.synset("electricity.n.01"),
				wn.synset("electricity.n.02")],

	# hand
	"U+3474":	[wn.synset("hand.n.01")],

	# thumb
	"U+3475":	[wn.synset("thumb.n.01")],

	# finger
	"U+3476":	[wn.synset("finger.n.02")],

	# tool, instrument
	"U+3477":	[wn.synset("cock.n.01"),
				wn.synset("creature.n.03"),
				wn.synset("instrument.n.01"),
				wn.synset("instrument.n.02"),
				wn.synset("instrument.n.03"),
				wn.synset("instrumental_role.n.01"),
				wn.synset("legal_document.n.01"),
				wn.synset("musical_instrument.n.01"),
				wn.synset("tool.n.01")],

	# nose
	"U+347a":	[wn.synset("nose.n.01")],

	# road
	"U+347d":	[wn.synset("road.n.01")],

	# bus, coach
	"U+347f":	[wn.synset("bus.n.01")],

	# worm
	"U+3481":	[wn.synset("worm.n.01")],

	# sky
	"U+3482":	[wn.synset("sky.n.01")],

	# fog
	"U+3483":	[wn.synset("fog.n.01")],

	# environment
	"U+3484":	[wn.synset("environment.n.02")],

	# peace, peace of mind, serenity
	"U+3485":	[wn.synset("peace.n.01"),
				wn.synset("peace.n.02"),
				wn.synset("peace.n.03"),
				wn.synset("peace.n.05")],

	# disturbance, unrest
	"U+3486":	[wn.synset("affray.n.02"),
				wn.synset("agitation.n.02"),
				wn.synset("disturbance.n.02"),
				wn.synset("disturbance.n.03"),
				wn.synset("disturbance.n.05"),
				wn.synset("mental_disorder.n.01"),
				wn.synset("noise.n.03"),
				wn.synset("perturbation.n.03"),
				wn.synset("unrest.n.02"),
				wn.synset("worry.n.02")],

	# world
	"U+3487":	[wn.synset("earth.n.01"),
				wn.synset("populace.n.01"),
				wn.synset("universe.n.01"),
				wn.synset("world.n.02"),
				wn.synset("world.n.03"),
				wn.synset("world.n.06"),
				wn.synset("world.n.08"),
				wn.synset("worldly_concern.n.01")],

	# lightning
	"U+3489":	[wn.synset("lightning.n.01")],

	# air, atmosphere
	"U+348a":	[wn.synset("air.n.01")],

	# wind
	"U+348b":	[wn.synset("wind.n.01")],

	# subtraction, loss
	"U+348c":	[wn.synset("loss.n.01"),
				wn.synset("loss.n.02"),
				wn.synset("loss.n.03"),
				wn.synset("loss.n.04"),
				wn.synset("loss.n.05"),
				wn.synset("loss.n.06"),
				wn.synset("passing.n.02"),
				wn.synset("personnel_casualty.n.01"),
				wn.synset("subtraction.n.01"),
				wn.synset("subtraction.n.02")],

	# vehicle, carriage, railway car car
	"U+348d":	[wn.synset("vehicle.n.01")],

	# fill
	"U+3490":	[wn.synset("fill.v.01")],

	# sailboat, sailing boat, yacht
	"U+3491":	[wn.synset("sailboat.n.01")],

	# under, below, inferior
	"U+3492":	[wn.synset("below.r.01"),
				wn.synset("below.r.02"),
				wn.synset("below.r.03"),
				wn.synset("downstairs.r.01"),
				wn.synset("inferior.n.01"),
				wn.synset("nether.s.03"),
				wn.synset("subscript.n.01"),
				wn.synset("under.r.01"),
				wn.synset("under.r.02"),
				wn.synset("under.r.03"),
				wn.synset("under.r.04"),
				wn.synset("under.r.05"),
				wn.synset("under.r.06"),
				wn.synset("under.r.07"),
				wn.synset("under.r.08"),
				wn.synset("under.s.02")],

	# weight
	"U+3493":	[wn.synset("weight.n.01"),
				wn.synset("weight.n.04")],

	# animal, bovine, ovine, beast
	"U+3494":	[wn.synset("animal.n.01")],

	# paw
	"U+3495":	[wn.synset("paw.n.01")],

	# hippopotamus
	"U+3497":	[wn.synset("hippopotamus.n.01")],

	# claw
	"U+349c":	[wn.synset("claw.n.01"),
				wn.synset("claw.n.03"),
				wn.synset("claw.n.04"),
				wn.synset("hook.n.04")],

	# giraffe
	"U+349d":	[wn.synset("giraffe.n.01")],

	# horse
	"U+349e":	[wn.synset("horse.n.01"),
				wn.synset("knight.n.02")],

	# rhinoceros
	"U+349f":	[wn.synset("rhinoceros.n.01")],

	# horn, antler
	"U+34a0":	[wn.synset("antler.n.01"),
				wn.synset("automobile_horn.n.01"),
				wn.synset("cornet.n.01"),
				wn.synset("french_horn.n.01"),
				wn.synset("horn.n.01"),
				wn.synset("horn.n.02"),
				wn.synset("horn.n.03"),
				wn.synset("horn.n.04"),
				wn.synset("horn.n.06"),
				wn.synset("horn.n.07"),
				wn.synset("horn.n.08"),
				wn.synset("horn.n.09")],

	# place, area, location, space
	"U+34a3":	[wn.synset("place.n.02"),
				wn.synset("position.n.01"),
				wn.synset("topographic_point.n.01")],

	# bulb
	"U+34a5":	[wn.synset("bulb.n.01"),
				wn.synset("bulb.n.06"),
				wn.synset("light_bulb.n.01")],

	# onion, vegetable
	"U+34a6":	[wn.synset("onion.n.01"),
				wn.synset("onion.n.02"),
				wn.synset("onion.n.03")],

	# seed
	"U+34a8":	[wn.synset("seed.n.01"),
				wn.synset("semen.n.01")],

	# carrot, vegetable
	"U+34a9":	[wn.synset("carrot.n.01"),
				wn.synset("carrot.n.02"),
				wn.synset("carrot.n.03"),
				wn.synset("carrot.n.04"),
				wn.synset("vegetable.n.01"),
				wn.synset("vegetable.n.02")],

	# grave
	"U+34aa":	[wn.synset("grave.n.02")],

	# snail
	"U+34ab":	[wn.synset("snail.n.01")],

	# lawn, meadow
	"U+34ac":	[wn.synset("hayfield.n.01"),
				wn.synset("lawn.n.01")],

	# night
	"U+34ad":	[wn.synset("night.n.01")],

	# evening
	"U+34ae":	[wn.synset("evening.n.01")],

	# street
	"U+34b0":	[wn.synset("street.n.01")],

	# ski, runner
	"U+34b1":	[wn.synset("ski.n.01")],

	# skateboard
	"U+34b2":	[wn.synset("skateboard.n.01")],

	# adult, mature, grownup
	"U+34b4":	[wn.synset("adult.n.01")],

	# teenager, adolescent, youth
	"U+34b5":	[wn.synset("adolescent.n.01")],

	# eyebrow
	"U+34b6":	[wn.synset("eyebrow.n.01")],

	# temperature
	"U+34b8":	[wn.synset("temperature.n.01")],

	# most, maximum
	"U+34b9":	[wn.synset("maximal.a.01")],

	# high, tall
	"U+34ba":	[wn.synset("high.a.01"),
				wn.synset("high.a.02"),
				wn.synset("high.a.04"),
				wn.synset("tall.a.01")],

	# nail
	"U+34bb":	[wn.synset("nail.n.02")],

	# shovel, spade
	"U+34bc":	[wn.synset("shovel.n.01")],

	# dig
	"U+34bd":	[wn.synset("dig.v.01"),
				wn.synset("excavate.v.04")],

	# same, equal, equality
	"U+34bf":	[wn.synset("peer.n.01")],

	# different, other, difference
	"U+34c0":	[wn.synset("different.a.01"),
				wn.synset("different.s.02"),
				wn.synset("different.s.03"),
				wn.synset("different.s.05"),
				wn.synset("early.s.03"),
				wn.synset("other.a.01"),
				wn.synset("other.s.02"),
				wn.synset("other.s.04"),
				wn.synset("unlike.a.01")],

	# not, negative, no, don't, doesn't
	"U+34c1":	[wn.synset("negative.n.02"),
				wn.synset("no.n.01"),
				wn.synset("not.r.01")],

	# nowhere, no place place
	"U+34c2":	[wn.synset("beak.n.04"),
				wn.synset("nose.n.01"),
				wn.synset("nowhere.n.01")],

	# low, short
	"U+34c3":	[wn.synset("low.a.01"),
				wn.synset("low.a.02")],

	# pin
	"U+34c4":	[wn.synset("bowling_pin.n.01"),
				wn.synset("fall.n.10"),
				wn.synset("peg.n.02"),
				wn.synset("peg.n.06"),
				wn.synset("personal_identification_number.n.01"),
				wn.synset("pin.n.01"),
				wn.synset("pin.n.05"),
				wn.synset("pin.n.07"),
				wn.synset("pin.n.08"),
				wn.synset("pin.n.09"),
				wn.synset("pivot.n.02")],

	# love, affection
	"U+34c6":	[wn.synset("affection.n.01"),
				wn.synset("beloved.n.01"),
				wn.synset("love.n.01"),
				wn.synset("love.n.02"),
				wn.synset("love.n.04")],

	# but, except
	"U+34c7":	[wn.synset("demur.v.01"),
				wn.synset("exclude.v.01"),
				wn.synset("merely.r.01"),
				wn.synset("milliampere.n.01")],

	# break, crack, fracture, tear, teardrop, gap, cleft
	"U+34c8":	[wn.synset("tear.n.01")],

	# on
	"U+34ca":	[wn.synset("above.r.01"),
				wn.synset("above.r.02"),
				wn.synset("along.r.01"),
				wn.synset("on.a.01"),
				wn.synset("on.a.02"),
				wn.synset("on.r.02"),
				wn.synset("on.r.03"),
				wn.synset("upstairs.r.01")],

	# bridge, overpass
	"U+34cb":	[wn.synset("bridge.n.01")],

	# hole
	"U+34cc":	[wn.synset("hole.n.03"),
				wn.synset("hole.n.05")],

	# maple leaf, maple-leaf
	"U+34ce":	[wn.synset("maple-leaf.n.01")],

	# line, stripe, queue
	"U+34cf":	[wn.synset("queue.n.01")],

	# screw
	"U+34d0":	[wn.synset("fuck.n.01"),
				wn.synset("prison_guard.n.01"),
				wn.synset("screw.n.02"),
				wn.synset("screw.n.03"),
				wn.synset("screw.n.04")],

	# after, behind
	"U+34d1":	[wn.synset("after.r.02"),
				wn.synset("after.s.01"),
				wn.synset("buttocks.n.01"),
				wn.synset("subsequently.r.01")],

	# between
	"U+34d2":	[wn.synset("between.r.01"),
				wn.synset("between.r.02")],

	# attach
	"U+34d3":	[wn.synset("attach.v.01")],

	# parallel
	"U+34d4":	[wn.synset("latitude.n.03")],

	# other, another
	"U+34d5":	[wn.synset("another.s.01"),
				wn.synset("other.a.01"),
				wn.synset("other.s.02")],

	# copy, duplicate
	"U+34d6":	[wn.synset("copy.n.02"),
				wn.synset("copy.n.03"),
				wn.synset("copy.n.04"),
				wn.synset("duplicate.n.02"),
				wn.synset("extra.n.03"),
				wn.synset("transcript.n.02")],

	# thin, slim, narrow
	"U+34d7":	[wn.synset("thin.a.01")],

	# deep
	"U+34d9":	[wn.synset("bass.s.01"),
				wn.synset("deep.a.01"),
				wn.synset("deep.s.02"),
				wn.synset("deep.s.05")],

	# wide, broad
	"U+34db":	[wn.synset("across-the-board.s.01"),
				wn.synset("broad.s.03"),
				wn.synset("wide.a.01")],

	# broom
	"U+34dc":	[wn.synset("broom.n.01")],

	# perpendicular
	"U+34dd":	[wn.synset("perpendicular.n.01"),
				wn.synset("perpendicular.n.02"),
				wn.synset("perpendicular.n.04"),
				wn.synset("plumb_line.n.01")],

	# beginning, start
	"U+34de":	[wn.synset("beginning.n.02")],

	# month
	"U+34e0":	[wn.synset("calendar_month.n.01")],

	# needle
	"U+34e1":	[wn.synset("needle.n.03")],

	# account
	"U+34e3":	[wn.synset("account.n.03"),
				wn.synset("bill.n.02")],

	# commandments
	"U+34e5":	[wn.synset("commandment.n.01"),
				wn.synset("teaching.n.02")],

	# chair, seat
	"U+34e7":	[wn.synset("chair.n.01")],

	# toilet
	"U+34e8":	[wn.synset("toilet.n.01")],

	# wheelchair
	"U+34e9":	[wn.synset("wheelchair.n.01")],

	# armchair
	"U+34ea":	[wn.synset("armchair.n.01")],

	# bed
	"U+34eb":	[wn.synset("bed.n.01")],

	# pillow, cushion
	"U+34ec":	[wn.synset("cushion.n.03"),
				wn.synset("pillow.n.01")],

	# bottle, flask
	"U+34ed":	[wn.synset("bottle.n.01")],

	# woman, female
	"U+34ee":	[wn.synset("woman.n.01"),
				wn.synset("woman.n.02")],

	# man, male
	"U+34f4":	[wn.synset("man.n.01")],

	# citizen
	"U+34f8":	[wn.synset("citizen.n.01")],

	# husband
	"U+34f9":	[wn.synset("husband.n.01")],

	# stepfather
	"U+34fc":	[wn.synset("stepfather.n.01")],

	# boat, ship
	"U+3500":	[wn.synset("ship.n.01")],

	# sack, bag, dismiss
	"U+3501":	[wn.synset("displace.v.03")],

	# crab, shellfish
	"U+3502":	[wn.synset("crab.n.01")],

	# ankle
	"U+3504":	[wn.synset("ankle.n.01")],

	# knee
	"U+3505":	[wn.synset("knee.n.01")],

	# menorah
	"U+3506":	[wn.synset("menorah.n.01"),
				wn.synset("menorah.n.02")],

	# near, almost, close, nearly
	"U+3508":	[wn.synset("near.a.01")],

	# far, distant
	"U+350a":	[wn.synset("distant.a.01"),
				wn.synset("far.a.01")],

	# from
	"U+350b":	[wn.synset("delaware.n.04")],

	# length, longness
	"U+350d":	[wn.synset("length.n.03")],

	# measurement, measure
	"U+350e":	[wn.synset("bill.n.01"),
				wn.synset("measure.n.01"),
				wn.synset("measure.n.02"),
				wn.synset("measure.n.07"),
				wn.synset("measure.n.09"),
				wn.synset("measurement.n.01"),
				wn.synset("measuring_stick.n.01"),
				wn.synset("meter.n.03"),
				wn.synset("size.n.01"),
				wn.synset("standard.n.01")],

	# injection, inoculation, shot
	"U+350f":	[wn.synset("injection.n.03")],

	# short
	"U+3511":	[wn.synset("short.a.02")],

	# pepper
	"U+3512":	[wn.synset("capsicum.n.01"),
				wn.synset("pepper.n.04")],

	# it
	"U+3513":	[wn.synset("information_technology.n.01")],

	# until, till, to, toward, towards
	"U+3514":	[wn.synset("cashbox.n.01"),
				wn.synset("public_treasury.n.01"),
				wn.synset("so_far.r.01"),
				wn.synset("till.n.01")],

	# flag
	"U+3515":	[wn.synset("flag.n.01")],

	# country, state
	"U+3516":	[wn.synset("country.n.02"),
				wn.synset("state.n.02"),
				wn.synset("state.n.03"),
				wn.synset("state.n.04"),
				wn.synset("state_of_matter.n.01")],

	# sail
	"U+3517":	[wn.synset("sail.n.01")],

	# crown
	"U+3518":	[wn.synset("crown.n.04")],

	# shallow
	"U+3519":	[wn.synset("shallow.a.01")],

	# fight, combat
	"U+351a":	[wn.synset("battle.n.01"),
				wn.synset("fight.n.02")],

	# soft
	"U+351b":	[wn.synset("soft.a.01")],

	# etrog
	"U+351d":	[wn.synset("citron.n.01"),
				wn.synset("citron.n.02"),
				wn.synset("citronwood.n.01")],

	# ladder
	"U+3520":	[wn.synset("ladder.n.01")],

	# help, aid, assistance, support, assist, serve
	"U+3524":	[wn.synset("help.v.01"),
				wn.synset("help.v.02")],

	# sport stick
	"U+3526":	[wn.synset("baton.n.01"),
				wn.synset("cane.n.01"),
				wn.synset("cane.n.02"),
				wn.synset("cane.n.03"),
				wn.synset("fishing_rod.n.01"),
				wn.synset("pole.n.02"),
				wn.synset("reed.n.01"),
				wn.synset("staff.n.06"),
				wn.synset("stick.n.06"),
				wn.synset("walking_stick.n.01"),
				wn.synset("walking_stick.n.02")],

	# helicopter
	"U+352c":	[wn.synset("helicopter.n.01")],

	# seesaw, teeter totter, teeter board
	"U+352d":	[wn.synset("seesaw.n.01")],

	# energy
	"U+3530":	[wn.synset("energy.n.02")],

	# fuel
	"U+3531":	[wn.synset("fuel.n.01")],

	# microwave oven
	"U+3532":	[wn.synset("microwave.n.02")],

	# power, powerfulness
	"U+3533":	[wn.synset("ability.n.02"),
				wn.synset("baron.n.03"),
				wn.synset("exponent.n.03"),
				wn.synset("important_person.n.01"),
				wn.synset("might.n.01"),
				wn.synset("office.n.04"),
				wn.synset("power.n.01"),
				wn.synset("power.n.02"),
				wn.synset("power.n.05"),
				wn.synset("world_power.n.01")],

	# saw
	"U+3535":	[wn.synset("saw.n.02")],

	# tank
	"U+3537":	[wn.synset("tank.n.01")],

	# destroy, annul, cancel, cross out, delete
	"U+3538":	[wn.synset("delete.v.01"),
				wn.synset("destroy.v.01"),
				wn.synset("destroy.v.02"),
				wn.synset("erase.v.03")],

	# angle, right angle
	"U+3539":	[wn.synset("angle.n.01"),
				wn.synset("angle.n.03"),
				wn.synset("slant.n.01")],

	# cannon, gun
	"U+353a":	[wn.synset("cannon.n.01")],

	# fork
	"U+353e":	[wn.synset("fork.n.01")],

	# hammer, gavel, mallet
	"U+353f":	[wn.synset("gavel.n.01"),
				wn.synset("hammer.n.01"),
				wn.synset("hammer.n.02"),
				wn.synset("hammer.n.05"),
				wn.synset("hammer.n.06"),
				wn.synset("hammer.n.07"),
				wn.synset("hammer.n.08"),
				wn.synset("mallet.n.01"),
				wn.synset("mallet.n.02"),
				wn.synset("mallet.n.03"),
				wn.synset("malleus.n.01")],

	# the
	"U+3540":	[wn.synset("la.n.03")],

	# spoon
	"U+3543":	[wn.synset("spoon.n.01")],

	# pen, pencil
	"U+3545":	[wn.synset("pen.n.01"),
				wn.synset("pen.n.02"),
				wn.synset("pen.n.05"),
				wn.synset("pencil.n.01"),
				wn.synset("pencil.n.02"),
				wn.synset("pencil.n.03"),
				wn.synset("pencil.n.04"),
				wn.synset("penitentiary.n.01"),
				wn.synset("playpen.n.01")],

	# couch, chesterfield, sofa
	"U+3547":	[wn.synset("sofa.n.01")],

	# pitcher, jug, kettle, pot
	"U+3548":	[wn.synset("jug.n.01"),
				wn.synset("jug.n.02"),
				wn.synset("pitcher.n.02")],

	# wagon, cart, truck, lorry
	"U+3549":	[wn.synset("truck.n.01")],

	# hedgehog
	"U+354a":	[wn.synset("hedgehog.n.02")],

	# soup, broth
	"U+354f":	[wn.synset("soup.n.01")],

	# salad
	"U+3550":	[wn.synset("salad.n.01")],

	# dish, plate, platter
	"U+3551":	[wn.synset("plate.n.04")],

	# cereal
	"U+3552":	[wn.synset("cereal.n.01"),
				wn.synset("cereal.n.03"),
				wn.synset("grain.n.02")],

	# what, question mark mark
	"U+3555":	[wn.synset("bet.n.02")],

	# command, order
	"U+3557":	[wn.synset("arrange.v.07"),
				wn.synset("command.v.01"),
				wn.synset("command.v.02"),
				wn.synset("command.v.03"),
				wn.synset("control.v.01"),
				wn.synset("dominate.v.05"),
				wn.synset("ordain.v.02"),
				wn.synset("order.v.01"),
				wn.synset("order.v.02"),
				wn.synset("order.v.03"),
				wn.synset("order.v.05"),
				wn.synset("order.v.06"),
				wn.synset("rate.v.01"),
				wn.synset("regulate.v.02")],

	# comma
	"U+3559":	[wn.synset("comma.n.01")],

	# colon
	"U+355a":	[wn.synset("colon.n.05")],

	# exclamation mark
	"U+355d":	[wn.synset("exclamation_mark.n.01")],

	# zero, 0
	"U+355f":	[wn.synset("nothing.n.01"),
				wn.synset("zero.n.02"),
				wn.synset("zero.n.03"),
				wn.synset("zero.n.04")],

	# one, 1
	"U+3560":	[wn.synset("one.n.01")],

	# self, oneself, ego
	"U+3561":	[wn.synset("self.n.01")],

	# two, 2
	"U+3562":	[wn.synset("deuce.n.04"),
				wn.synset("two.n.01")],

	# three, 3
	"U+3563":	[wn.synset("three.n.01"),
				wn.synset("trey.n.02")],

	# four, 4
	"U+3564":	[wn.synset("four.n.01")],

	# five, 5
	"U+3565":	[wn.synset("five.n.01")],

	# six, 6
	"U+3566":	[wn.synset("six.n.01")],

	# seven, 7
	"U+3567":	[wn.synset("seven-spot.n.01"),
				wn.synset("seven.n.01")],

	# eight, 8
	"U+3568":	[wn.synset("ashcan_school.n.01"),
				wn.synset("eight-spot.n.01"),
				wn.synset("eight.n.01")],

	# nine, 9
	"U+3569":	[wn.synset("nine.n.01")],

	# difficult, hard
	"U+3576":	[wn.synset("difficult.a.01")],

	# ATB, all terrain bike-terrain bike
	"U+3577":	[wn.synset("mountain_bike.n.01"),
				wn.synset("trail_bike.n.01")],

	# bicycle
	"U+3578":	[wn.synset("bicycle.n.01")],

	# yellow
	"U+3579":	[wn.synset("yellow.n.01")],

	# forest, bush, wood, woods, shrub, lumber, timber
	"U+357d":	[wn.synset("forest.n.01")],

	# Olympics, Olympic games games
	"U+3580":	[wn.synset("olympic_games.n.01")],

	# garbage can, rubbish bin, trash can
	"U+3583":	[wn.synset("ashcan.n.01")],

	# conjure, turn to, transform
	"U+3584":	[wn.synset("bid.v.03"),
				wn.synset("raise.v.07"),
				wn.synset("transform.v.02"),
				wn.synset("translate.v.02")],

	# short message system, text message
	"U+3585":	[wn.synset("literally.r.01"),
				wn.synset("literally.r.02"),
				wn.synset("verbatim.r.01")],

	# letter, mail, post
	"U+3586":	[wn.synset("letter.n.01"),
				wn.synset("letter.n.02"),
				wn.synset("letter.n.04"),
				wn.synset("mail.n.02")],

	# telephone
	"U+3587":	[wn.synset("telephone.n.01")],

	# sexual abuse, sexual assault, sexual violence
	"U+3589":	[wn.synset("rape.n.03")],

	# abuse, assault, violence
	"U+358a":	[wn.synset("abuse.n.02"),
				wn.synset("assault.n.01"),
				wn.synset("assault.n.02"),
				wn.synset("assault.n.03"),
				wn.synset("ferocity.n.01"),
				wn.synset("maltreatment.n.01"),
				wn.synset("misuse.n.01"),
				wn.synset("rape.n.03"),
				wn.synset("violence.n.01"),
				wn.synset("violence.n.03")],

	# taco, taco shell shell
	"U+358e":	[wn.synset("greaser.n.01"),
				wn.synset("taco.n.02")],

	# shell, crust
	"U+358f":	[wn.synset("crust.n.01")],

	# wake up
	"U+3590":	[wn.synset("wake_up.v.02")],

	# Euro
	"U+3592":	[wn.synset("euro.n.01")],

	# water flower, water lily
	"U+3594":	[wn.synset("water_lily.n.01")],

	# prize, award, trophy
	"U+3595":	[wn.synset("trophy.n.02")],

	# win
	"U+3596":	[wn.synset("win.v.01")],

	# sport
	"U+3598":	[wn.synset("sport.n.01")],

	# car, automobile, motor vehicle vehicle
	"U+3599":	[wn.synset("car.n.01")],

	# rent, lease, hire, charter, let
	"U+359a":	[wn.synset("lease.v.03"),
				wn.synset("rent.v.01"),
				wn.synset("rent.v.04")],

	# limited time, interval, period, awhile, for a while
	"U+359b":	[wn.synset("time_period.n.01")],

	# tired, exhausted, weary, worn out out, raddled
	"U+359d":	[wn.synset("exhausted.a.02"),
				wn.synset("exhausted.s.01"),
				wn.synset("exhausted.s.03"),
				wn.synset("tired.a.01")],

	# rest, comfort
	"U+359e":	[wn.synset("respite.n.04"),
				wn.synset("rest.n.02")],

	# bacon
	"U+35a0":	[wn.synset("bacon.n.01")],

	# pork, ham
	"U+35a1":	[wn.synset("ham.n.01"),
				wn.synset("ham.n.02"),
				wn.synset("ham.n.03"),
				wn.synset("ham.n.04"),
				wn.synset("pork.n.01"),
				wn.synset("pork_barrel.n.01")],

	# linear thing, bar, pole
	"U+35a2":	[wn.synset("perch.n.02"),
				wn.synset("perch.n.03"),
				wn.synset("pole.n.01"),
				wn.synset("pole.n.02"),
				wn.synset("pole.n.03"),
				wn.synset("pole.n.06"),
				wn.synset("pole.n.07"),
				wn.synset("pole.n.09"),
				wn.synset("pole.n.10"),
				wn.synset("terminal.n.02")],

	# second
	"U+35a3":	[wn.synset("second.n.01")],

	# infertile, sterile
	"U+35ac":	[wn.synset("aseptic.s.01"),
				wn.synset("sterile.a.01"),
				wn.synset("sterile.s.03")],

	# tuft of grass, tussock
	"U+35ae":	[wn.synset("tuft.n.01")],

	# collection, pile, tussock
	"U+35af":	[wn.synset("atomic_pile.n.01"),
				wn.synset("batch.n.02"),
				wn.synset("collection.n.01"),
				wn.synset("collection.n.02"),
				wn.synset("collection.n.04"),
				wn.synset("down.n.05"),
				wn.synset("pile.n.01"),
				wn.synset("pile.n.03"),
				wn.synset("pile.n.06"),
				wn.synset("pile.n.07"),
				wn.synset("solicitation.n.02"),
				wn.synset("tuft.n.01"),
				wn.synset("voltaic_pile.n.01")],

	# shirt, blouse
	"U+35b1":	[wn.synset("blouse.n.01"),
				wn.synset("shirt.n.01")],

	# tooth fairy
	"U+35b2":	[wn.synset("tooth_fairy.n.01")],

	# fairy, fairy godmother godmother
	"U+35b3":	[wn.synset("fairy.n.01")],

	# forgetting, amnesia
	"U+35b4":	[wn.synset("amnesia.n.01")],

	# thunder
	"U+35b6":	[wn.synset("thunder.n.02")],

	# cooking, cookery, preparation, readying, readiness, preparedness
	"U+35b7":	[wn.synset("cooking.n.01")],

	# hero
	"U+35ba":	[wn.synset("hero.n.02")],

	# heroic
	"U+35bb":	[wn.synset("epic.s.01"),
				wn.synset("heroic.a.02")],

	# herb, spice plant plant
	"U+35bc":	[wn.synset("herb.n.02")],

	# smash, grind, shatter, splinter
	"U+35bd":	[wn.synset("bang_up.v.01"),
				wn.synset("bankrupt.v.01"),
				wn.synset("crunch.v.02"),
				wn.synset("crush.v.05"),
				wn.synset("grate.v.04"),
				wn.synset("grind.v.04"),
				wn.synset("grind.v.05"),
				wn.synset("grind.v.06"),
				wn.synset("grind.v.07"),
				wn.synset("jam.v.03"),
				wn.synset("labor.v.02"),
				wn.synset("secede.v.01"),
				wn.synset("shatter.v.01"),
				wn.synset("shatter.v.02"),
				wn.synset("shatter.v.03"),
				wn.synset("sliver.v.01"),
				wn.synset("smash.v.01"),
				wn.synset("smash.v.02"),
				wn.synset("smash.v.04"),
				wn.synset("smash.v.07"),
				wn.synset("smash.v.08"),
				wn.synset("smash.v.09"),
				wn.synset("smash.v.10"),
				wn.synset("splinter.v.03")],

	# he, she, him, her, one, himself
	"U+35c6":	[wn.synset("he.n.02"),
				wn.synset("helium.n.01"),
				wn.synset("id.n.03"),
				wn.synset("one.n.01"),
				wn.synset("one.n.02")],

	# pancreas
	"U+35c7":	[wn.synset("pancreas.n.01")],

	# gland
	"U+35c8":	[wn.synset("gland.n.01")],

	# insulin
	"U+35c9":	[wn.synset("insulin.n.01")],

	# substance
	"U+35ca":	[wn.synset("kernel.n.03"),
				wn.synset("meaning.n.02"),
				wn.synset("means.n.03"),
				wn.synset("message.n.02"),
				wn.synset("substance.n.01"),
				wn.synset("substance.n.04"),
				wn.synset("substance.n.07")],

	# material, raw material, stuff
	"U+35cb":	[wn.synset("material.n.01"),
				wn.synset("material.n.02")],

	# low tide, ebb
	"U+35cc":	[wn.synset("ebb.n.01"),
				wn.synset("ebb.n.02"),
				wn.synset("low_tide.n.01")],

	# tide
	"U+35cd":	[wn.synset("tide.n.01")],

	# physiotherapy
	"U+35cf":	[wn.synset("physical_therapy.n.01")],

	# neurologist
	"U+35d0":	[wn.synset("neurologist.n.01")],

	# doctor, physician, hab)
	"U+35d1":	[wn.synset("doctor.n.01"),
				wn.synset("doctor.n.04"),
				wn.synset("doctor_of_the_church.n.01")],

	# central nervous system, CNS
	"U+35d2":	[wn.synset("central_nervous_system.n.01")],

	# military, armed forces, armed services
	"U+35d3":	[wn.synset("military.n.01")],

	# group
	"U+35d4":	[wn.synset("group.n.03")],

	# deletion, cancellation, destruction
	"U+35d5":	[wn.synset("destruction.n.01"),
				wn.synset("destruction.n.02"),
				wn.synset("end.n.06")],

	# roadrunner
	"U+35d7":	[wn.synset("roadrunner.n.01")],

	# little, small
	"U+35d9":	[wn.synset("little.s.03"),
				wn.synset("minor.s.10"),
				wn.synset("small.a.01")],

	# divide
	"U+35da":	[wn.synset("divide.v.01")],

	# stern
	"U+35db":	[wn.synset("stern.n.01")],

	# oil lamp
	"U+35dc":	[wn.synset("oil_lamp.n.01")],

	# cheating
	"U+35de":	[wn.synset("cheat.n.05"),
				wn.synset("shoddy.n.01")],

	# activity, male gender gender
	"U+35df":	[wn.synset("action.n.02")],

	# Sagittarius
	"U+35e0":	[wn.synset("sagittarius.n.01"),
				wn.synset("sagittarius.n.02"),
				wn.synset("sagittarius.n.03"),
				wn.synset("sagittarius.n.04")],

	# constellation of stars
	"U+35e1":	[wn.synset("constellation.n.02")],

	# music
	"U+35e3":	[wn.synset("music.n.01")],

	# passport
	"U+35e4":	[wn.synset("passport.n.02")],

	# permission, allowance
	"U+35e5":	[wn.synset("license.n.04"),
				wn.synset("permission.n.01")],

	# travel
	"U+35e7":	[wn.synset("travel.v.02"),
				wn.synset("travel.v.05")],

	# fall asleep
	"U+35ea":	[wn.synset("fall_asleep.v.01")],

	# asleep
	"U+35eb":	[wn.synset("asleep.a.01"),
				wn.synset("asleep.s.02"),
				wn.synset("asleep.s.03"),
				wn.synset("sleepy.s.01")],

	# divine, holy
	"U+35ec":	[wn.synset("holy.a.01")],

	# God
	"U+35ed":	[wn.synset("deity.n.01")],

	# holiness
	"U+35ee":	[wn.synset("holiness.n.01")],

	# calling, vocation, profession, career
	"U+35f0":	[wn.synset("career.n.01")],

	# hurt, pain, suffer, suffering
	"U+35f1":	[wn.synset("hurt.v.02")],

	# injure, hurt
	"U+35f2":	[wn.synset("injure.v.01")],

	# meteorologist
	"U+35f4":	[wn.synset("meteorologist.n.01")],

	# meteorology
	"U+35f5":	[wn.synset("meteorology.n.02")],

	# earth, globe, world, ground, land
	"U+35f6":	[wn.synset("background.n.02"),
				wn.synset("country.n.02"),
				wn.synset("domain.n.02"),
				wn.synset("earth.n.01"),
				wn.synset("earth.n.02"),
				wn.synset("earth.n.04"),
				wn.synset("earth.n.05"),
				wn.synset("estate.n.02"),
				wn.synset("farming.n.02"),
				wn.synset("flat_coat.n.01"),
				wn.synset("footing.n.02"),
				wn.synset("ground.n.05"),
				wn.synset("ground.n.08"),
				wn.synset("ground.n.09"),
				wn.synset("ground.n.10"),
				wn.synset("kingdom.n.01"),
				wn.synset("land.n.01"),
				wn.synset("land.n.02"),
				wn.synset("land.n.04"),
				wn.synset("land.n.10"),
				wn.synset("nation.n.02"),
				wn.synset("reason.n.01"),
				wn.synset("soil.n.02"),
				wn.synset("state.n.04"),
				wn.synset("worldly_concern.n.01")],

	# hold, contain
	"U+35f7":	[wn.synset("accommodate.v.04"),
				wn.synset("agree.v.01"),
				wn.synset("apply.v.02"),
				wn.synset("bear.v.11"),
				wn.synset("carry.v.33"),
				wn.synset("check.v.18"),
				wn.synset("contain.v.04"),
				wn.synset("contain.v.05"),
				wn.synset("control.v.02"),
				wn.synset("declare.v.04"),
				wn.synset("deem.v.01"),
				wn.synset("defend.v.03"),
				wn.synset("defy.v.01"),
				wn.synset("halt.v.01"),
				wn.synset("harbor.v.01"),
				wn.synset("have.v.01"),
				wn.synset("hold.v.02"),
				wn.synset("hold.v.03"),
				wn.synset("hold.v.10"),
				wn.synset("hold.v.11"),
				wn.synset("hold.v.13"),
				wn.synset("hold.v.14"),
				wn.synset("hold.v.16"),
				wn.synset("hold.v.17"),
				wn.synset("hold.v.22"),
				wn.synset("hold.v.23"),
				wn.synset("hold.v.26"),
				wn.synset("hold.v.28"),
				wn.synset("hold.v.29"),
				wn.synset("hold.v.31"),
				wn.synset("hold.v.33"),
				wn.synset("hold.v.36"),
				wn.synset("incorporate.v.02"),
				wn.synset("keep.v.01"),
				wn.synset("oblige.v.02"),
				wn.synset("prevail.v.02"),
				wn.synset("reserve.v.04"),
				wn.synset("restrain.v.03"),
				wn.synset("retain.v.03")],

	# prepare, set, set up, ready, gear up, fix up, mend, repair
	"U+35f8":	[wn.synset("repair.v.01")],

	# unit, example, sample
	"U+35f9":	[wn.synset("unit.n.02"),
				wn.synset("unit_of_measurement.n.01")],

	# fast
	"U+35fc":	[wn.synset("fast.n.01")],

	# unfair, unjust
	"U+35fe":	[wn.synset("inequitable.a.01"),
				wn.synset("unfair.a.01"),
				wn.synset("unjust.a.02")],

	# artillery
	"U+3600":	[wn.synset("artillery.n.01"),
				wn.synset("artillery.n.02")],

	# sauce, gravy, relish, dressing
	"U+3603":	[wn.synset("sauce.n.01")],

	# chocolate, cocoa, cacao
	"U+3604":	[wn.synset("chocolate.n.02")],

	# currency
	"U+3605":	[wn.synset("currency.n.01")],

	# want, desire
	"U+3606":	[wn.synset("desire.v.01")],

	# trip, journey, travel, voyage
	"U+3607":	[wn.synset("journey.n.01"),
				wn.synset("trip.n.01"),
				wn.synset("trip.n.02")],

	# tropical rain forest, jungle
	"U+3608":	[wn.synset("hobo_camp.n.01"),
				wn.synset("jungle.n.01"),
				wn.synset("jungle.n.03")],

	# grove
	"U+3609":	[wn.synset("grove.n.01"),
				wn.synset("grove.n.02")],

	# equator
	"U+360a":	[wn.synset("equator.n.01")],

	# panpipe
	"U+360b":	[wn.synset("panpipe.n.01")],

	# who, that, which, whom
	"U+360e":	[wn.synset("world_health_organization.n.01")],

	# hot, spicy, peppery
	"U+360f":	[wn.synset("blistering.s.03"),
				wn.synset("blue.s.05"),
				wn.synset("hot.a.01"),
				wn.synset("hot.a.03"),
				wn.synset("hot.s.02"),
				wn.synset("hot.s.04"),
				wn.synset("hot.s.05"),
				wn.synset("hot.s.06"),
				wn.synset("hot.s.08"),
				wn.synset("hot.s.09"),
				wn.synset("hot.s.10"),
				wn.synset("hot.s.11"),
				wn.synset("hot.s.12"),
				wn.synset("hot.s.13"),
				wn.synset("hot.s.14"),
				wn.synset("hot.s.15"),
				wn.synset("hot.s.16"),
				wn.synset("hot.s.17"),
				wn.synset("hot.s.18"),
				wn.synset("hot.s.19"),
				wn.synset("hot.s.20"),
				wn.synset("hot.s.21"),
				wn.synset("peppery.s.01"),
				wn.synset("piquant.s.01")],

	# hop
	"U+3610":	[wn.synset("bounce.v.03"),
				wn.synset("hop.v.01"),
				wn.synset("hop.v.02"),
				wn.synset("hop.v.03"),
				wn.synset("hop.v.04"),
				wn.synset("hop.v.05"),
				wn.synset("hop.v.06")],

	# intensity
	"U+3614":	[wn.synset("intensity.n.02")],

	# right turn, right
	"U+3615":	[wn.synset("right.n.01"),
				wn.synset("right.n.02"),
				wn.synset("right.n.04"),
				wn.synset("right.n.05"),
				wn.synset("right.n.06"),
				wn.synset("right.n.07"),
				wn.synset("right.n.08"),
				wn.synset("right_field.n.01")],

	# beauty
	"U+3617":	[wn.synset("beauty.n.01")],

	# happiness, fun, joy, pleasure
	"U+3618":	[wn.synset("fun.n.01"),
				wn.synset("fun.n.02"),
				wn.synset("fun.n.03"),
				wn.synset("happiness.n.01"),
				wn.synset("happiness.n.02"),
				wn.synset("joy.n.01"),
				wn.synset("joy.n.02"),
				wn.synset("playfulness.n.02"),
				wn.synset("pleasure.n.01"),
				wn.synset("pleasure.n.03"),
				wn.synset("pleasure.n.04"),
				wn.synset("pleasure.n.05")],

	# opossum, possum
	"U+361c":	[wn.synset("opossum.n.02")],

	# bad conscience
	"U+361f":	[wn.synset("conscience.n.01")],

	# incorrect, bad, inaccurate, wrong
	"U+3620":	[wn.synset("incorrect.a.01")],

	# wash up, do the dishes
	"U+3623":	[wn.synset("wash_up.v.03")],

	# glassware
	"U+3625":	[wn.synset("glass.n.07"),
				wn.synset("glassware.n.01")],

	# baggage, bag, luggage, suitcase
	"U+3626":	[wn.synset("baggage.n.01")],

	# wing
	"U+3628":	[wn.synset("wing.n.01"),
				wn.synset("wing.n.02")],

	# fart, wind
	"U+3629":	[wn.synset("fart.n.01")],

	# wrap, wind
	"U+362a":	[wn.synset("envelop.v.01"),
				wn.synset("hoist.v.01"),
				wn.synset("scent.v.02"),
				wn.synset("weave.v.04"),
				wn.synset("wind.v.02"),
				wn.synset("wind.v.03"),
				wn.synset("wind.v.05"),
				wn.synset("wrap.v.01"),
				wn.synset("wrap.v.04"),
				wn.synset("wreathe.v.03")],

	# wine
	"U+362b":	[wn.synset("wine.n.01")],

	# alcoholic drink, alcoholic beverage, liquor
	"U+362c":	[wn.synset("liquor.n.01")],

	# limit, limitation, restriction, restrict, restrain, confine
	"U+362d":	[wn.synset("restrict.v.03")],

	# virus
	"U+3630":	[wn.synset("virus.n.03")],

	# eye makeup
	"U+3631":	[wn.synset("mascara.n.01")],

	# butcher
	"U+3633":	[wn.synset("butcher.n.01")],

	# meat, dried meat, minced meat, ground meat, frozen meat, diced meat, chunks of meat
	"U+3634":	[wn.synset("kernel.n.01"),
				wn.synset("meat.n.01")],

	# fidelity, loyalty, solidarity
	"U+3635":	[wn.synset("fidelity.n.02")],

	# attachment, appendix, annex, cecum, caecum
	"U+3636":	[wn.synset("appendix.n.02")],

	# playhouse, play house house
	"U+3638":	[wn.synset("playhouse.n.01")],

	# house, building, dwelling, residence
	"U+3639":	[wn.synset("house.n.01")],

	# play, recreation
	"U+363a":	[wn.synset("play.n.02")],

	# lifeline
	"U+363c":	[wn.synset("lifeline.n.02"),
				wn.synset("lifeline.n.03"),
				wn.synset("lifeline.n.04"),
				wn.synset("line_of_life.n.01")],

	# strap, string, velcro, rope, cord
	"U+363d":	[wn.synset("bowed_stringed_instrument.n.01"),
				wn.synset("chain.n.10"),
				wn.synset("cord.n.01"),
				wn.synset("cord.n.02"),
				wn.synset("cord.n.03"),
				wn.synset("cord.n.04"),
				wn.synset("drawstring.n.01"),
				wn.synset("r-2.n.01"),
				wn.synset("rope.n.01"),
				wn.synset("strap.n.01"),
				wn.synset("strap.n.02"),
				wn.synset("strap.n.03"),
				wn.synset("strap.n.04"),
				wn.synset("string.n.01"),
				wn.synset("string.n.03"),
				wn.synset("string.n.04"),
				wn.synset("string.n.05"),
				wn.synset("string.n.07"),
				wn.synset("string.n.08"),
				wn.synset("string.n.09"),
				wn.synset("velcro.n.01")],

	# string
	"U+363e":	[wn.synset("bowed_stringed_instrument.n.01"),
				wn.synset("chain.n.10"),
				wn.synset("drawstring.n.01"),
				wn.synset("string.n.01"),
				wn.synset("string.n.03"),
				wn.synset("string.n.04"),
				wn.synset("string.n.05"),
				wn.synset("string.n.07"),
				wn.synset("string.n.08"),
				wn.synset("string.n.09")],

	# rope, hawser
	"U+3640":	[wn.synset("rope.n.01")],

	# backpack, rucksack
	"U+3642":	[wn.synset("backpack.n.01")],

	# back
	"U+3643":	[wn.synset("back.n.01"),
				wn.synset("back.n.03"),
				wn.synset("back.n.04"),
				wn.synset("back.n.07"),
				wn.synset("back.n.08"),
				wn.synset("back.n.09"),
				wn.synset("binding.n.05"),
				wn.synset("rear.n.05"),
				wn.synset("spinal_column.n.01")],

	# covered, hidden
	"U+3644":	[wn.synset("concealed.s.01"),
				wn.synset("covered.a.01"),
				wn.synset("hidden.s.02"),
				wn.synset("hidden.s.03")],

	# invisible
	"U+3645":	[wn.synset("invisible.a.01")],

	# repetition, copying, duplication, replication
	"U+3646":	[wn.synset("repeat.n.01")],

	# blanket, duvet, quilt
	"U+3649":	[wn.synset("blanket.n.01")],

	# detachment, separation, breakup
	"U+364a":	[wn.synset("detachment.n.02"),
				wn.synset("detachment.n.04"),
				wn.synset("dissolution.n.05"),
				wn.synset("insulation.n.01"),
				wn.synset("interval.n.03"),
				wn.synset("legal_separation.n.02"),
				wn.synset("separation.n.01"),
				wn.synset("separation.n.02"),
				wn.synset("separation.n.04"),
				wn.synset("separation.n.05"),
				wn.synset("separation.n.06"),
				wn.synset("separation.n.07"),
				wn.synset("separation.n.09"),
				wn.synset("withdrawal.n.04")],

	# minus, no, without
	"U+364b":	[wn.synset("minus_sign.n.01"),
				wn.synset("no.n.01"),
				wn.synset("nobelium.n.01"),
				wn.synset("subtraction.n.01")],

	# fastener, gripper, velcro, zipper
	"U+364c":	[wn.synset("fastener.n.02")],

	# interrupt
	"U+3650":	[wn.synset("interrupt.v.03")],

	# interruption
	"U+3651":	[wn.synset("break.n.13"),
				wn.synset("interruption.n.02"),
				wn.synset("pause.n.01")],

	# silver
	"U+3653":	[wn.synset("silver.n.01")],

	# metal
	"U+3654":	[wn.synset("metallic_element.n.01")],

	# be caused by
	"U+3655":	[wn.synset("be_due.v.01"),
				wn.synset("derive.v.03"),
				wn.synset("derive.v.04"),
				wn.synset("derive.v.05")],

	# move bowels, defecate, stool, shit, ca ca
	"U+3656":	[wn.synset("denounce.v.04"),
				wn.synset("stool.v.01"),
				wn.synset("stool.v.02"),
				wn.synset("stool.v.03"),
				wn.synset("stool.v.04")],

	# bowel movement, defecation, shitting, feces, shit, poop
	"U+3657":	[wn.synset("defecation.n.01")],

	# rouge, blusher
	"U+3658":	[wn.synset("rouge.n.01")],

	# arrow
	"U+3659":	[wn.synset("arrow.n.02")],

	# volcano
	"U+365a":	[wn.synset("volcano.n.02")],

	# burial
	"U+365b":	[wn.synset("burial.n.01")],

	# ceremony
	"U+365c":	[wn.synset("ceremony.n.01")],

	# telescope
	"U+365e":	[wn.synset("telescope.n.01")],

	# harmony, harmoniousness, concord, concordance
	"U+3660":	[wn.synset("harmony.n.01"),
				wn.synset("harmony.n.02"),
				wn.synset("harmony.n.03"),
				wn.synset("harmony.n.04")],

	# lawn bowling, bowls
	"U+3661":	[wn.synset("bowl.n.01"),
				wn.synset("bowl.n.02"),
				wn.synset("bowl.n.03"),
				wn.synset("bowl.n.04"),
				wn.synset("bowl.n.07"),
				wn.synset("bowl.n.08"),
				wn.synset("bowling_ball.n.01"),
				wn.synset("lawn_bowling.n.01"),
				wn.synset("roll.n.15"),
				wn.synset("stadium.n.01")],

	# bowling
	"U+3662":	[wn.synset("bowling.n.01"),
				wn.synset("bowling.n.02"),
				wn.synset("bowling.n.03")],

	# roof, cover
	"U+3664":	[wn.synset("roof.n.01")],

	# existence, being
	"U+3666":	[wn.synset("being.n.01")],

	# message, content
	"U+3668":	[wn.synset("message.n.01")],

	# information
	"U+3669":	[wn.synset("information.n.01")],

	# communication
	"U+366a":	[wn.synset("communication.n.01"),
				wn.synset("communication.n.02"),
				wn.synset("communication.n.03")],

	# lymph node, lymph gland
	"U+366c":	[wn.synset("lymph_node.n.01")],

	# organ, pipe organ organ, inner organ, inner body part
	"U+366d":	[wn.synset("harmonium.n.01"),
				wn.synset("organ.n.01"),
				wn.synset("organ.n.02"),
				wn.synset("organ.n.05")],

	# lymph
	"U+366e":	[wn.synset("lymph.n.01")],

	# vascular system
	"U+366f":	[wn.synset("bloodstream.n.01")],

	# blood
	"U+3671":	[wn.synset("blood.n.01")],

	# encourage
	"U+3672":	[wn.synset("encourage.v.03")],

	# encouragement
	"U+3673":	[wn.synset("boost.n.01"),
				wn.synset("encouragement.n.01"),
				wn.synset("encouragement.n.03")],

	# foundation, base, fundament
	"U+3674":	[wn.synset("base.n.11"),
				wn.synset("foundation.n.01")],

	# sheet, bedclothes, bed linen
	"U+3676":	[wn.synset("sheet.n.03")],

	# guess, estimate, estimation
	"U+3677":	[wn.synset("guess.v.04")],

	# knit
	"U+3679":	[wn.synset("knit.v.01")],

	# enormous
	"U+367b":	[wn.synset("enormous.s.01")],

	# huge
	"U+367c":	[wn.synset("huge.s.01")],

	# shuttlecock, birdie
	"U+367d":	[wn.synset("birdie.n.01"),
				wn.synset("shuttlecock.n.01")],

	# wash, bathe, bath, washing
	"U+3681":	[wn.synset("bath.n.01"),
				wn.synset("bath.n.02"),
				wn.synset("bath.n.04"),
				wn.synset("bath.n.05"),
				wn.synset("bathroom.n.01"),
				wn.synset("bathtub.n.01"),
				wn.synset("laundry.n.01"),
				wn.synset("sink.n.01"),
				wn.synset("wash.n.02"),
				wn.synset("washbasin.n.02")],

	# teach, instruct
	"U+3682":	[wn.synset("teach.v.01")],

	# clearness, clarity, transparency, transparence
	"U+3687":	[wn.synset("clarity.n.01"),
				wn.synset("clearness.n.02")],

	# basketball
	"U+3688":	[wn.synset("basketball.n.01")],

	# service
	"U+3689":	[wn.synset("avail.n.01"),
				wn.synset("military_service.n.01"),
				wn.synset("overhaul.n.01"),
				wn.synset("serve.n.01"),
				wn.synset("service.n.01"),
				wn.synset("service.n.02"),
				wn.synset("service.n.03"),
				wn.synset("service.n.04"),
				wn.synset("service.n.05"),
				wn.synset("service.n.07"),
				wn.synset("service.n.09"),
				wn.synset("service.n.11"),
				wn.synset("service.n.13"),
				wn.synset("service.n.15"),
				wn.synset("servicing.n.01")],

	# plan, design, method, system
	"U+368a":	[wn.synset("design.v.02"),
				wn.synset("design.v.03"),
				wn.synset("design.v.04"),
				wn.synset("design.v.05"),
				wn.synset("design.v.06"),
				wn.synset("design.v.07"),
				wn.synset("plan.v.01"),
				wn.synset("plan.v.02"),
				wn.synset("plan.v.03")],

	# constructional blocks, lego
	"U+368b":	[wn.synset("lego.n.01")],

	# together, attached, appended, fastened, joined
	"U+368c":	[wn.synset("add.v.02"),
				wn.synset("affiliated.s.01"),
				wn.synset("append.v.01"),
				wn.synset("append.v.02"),
				wn.synset("attached.a.02"),
				wn.synset("attached.a.03"),
				wn.synset("attached.s.04"),
				wn.synset("buttoned.a.01"),
				wn.synset("coupled.s.02"),
				wn.synset("fastened.a.01"),
				wn.synset("joined.s.01"),
				wn.synset("jointly.r.02"),
				wn.synset("tied.a.03"),
				wn.synset("together.r.04"),
				wn.synset("together.s.01")],

	# engagement
	"U+368d":	[wn.synset("battle.n.01"),
				wn.synset("betrothal.n.01"),
				wn.synset("date.n.03"),
				wn.synset("employment.n.03"),
				wn.synset("engagement.n.05"),
				wn.synset("engagement.n.06"),
				wn.synset("engagement.n.07")],

	# Roman Catholicism, Roman Catholic Church
	"U+368e":	[wn.synset("romanism.n.01")],

	# religion, naturalism, theology, philosophy of religion
	"U+368f":	[wn.synset("theology.n.01")],

	# Vatican, Vatican City
	"U+3690":	[wn.synset("vatican.n.01")],

	# hijacker, coup maker
	"U+3691":	[wn.synset("highjacker.n.01"),
				wn.synset("highjacker.n.02")],

	# coup, coup d'etat d'etat, hijack, takeover
	"U+3692":	[wn.synset("hijack.n.01")],

	# hijack, make a coup a coup
	"U+3693":	[wn.synset("commandeer.v.01"),
				wn.synset("hijack.v.02"),
				wn.synset("kidnap.v.01")],

	# necessary, necessarily, needed
	"U+3695":	[wn.synset("necessary.a.01")],

	# need
	"U+3696":	[wn.synset("want.v.02")],

	# bitter
	"U+3697":	[wn.synset("acerb.s.02"),
				wn.synset("acrimonious.s.01"),
				wn.synset("biting.s.02"),
				wn.synset("bitter.s.02"),
				wn.synset("bitter.s.04"),
				wn.synset("bitter.s.05"),
				wn.synset("bitter.s.06")],

	# down, downward
	"U+3698":	[wn.synset("down.r.01")],

	# hear, listen
	"U+3699":	[wn.synset("hear.v.01"),
				wn.synset("hear.v.03"),
				wn.synset("hear.v.04"),
				wn.synset("heed.v.01"),
				wn.synset("learn.v.02"),
				wn.synset("listen.v.01"),
				wn.synset("listen.v.02")],

	# infiniteness, boundlessness, limitlessness
	"U+369a":	[wn.synset("infiniteness.n.01")],

	# potholder, oven mitt mitt
	"U+369c":	[wn.synset("handle.n.01"),
				wn.synset("holder.n.01"),
				wn.synset("potholder.n.01")],

	# crawl
	"U+369d":	[wn.synset("crawl.v.01"),
				wn.synset("crawl.v.02"),
				wn.synset("crawl.v.03"),
				wn.synset("crawl.v.05"),
				wn.synset("fawn.v.01")],

	# coward
	"U+369f":	[wn.synset("coward.n.01"),
				wn.synset("coward.n.02")],

	# cowardice
	"U+36a0":	[wn.synset("coward.n.01"),
				wn.synset("cowardice.n.01")],

	# werewolf
	"U+36a1":	[wn.synset("werewolf.n.01")],

	# wolf, dingo, wild dog dog
	"U+36a3":	[wn.synset("wolf.n.01")],

	# quickness, rapidity, speediness
	"U+36a4":	[wn.synset("adeptness.n.01"),
				wn.synset("celerity.n.01"),
				wn.synset("cursorily.r.01"),
				wn.synset("express.n.02"),
				wn.synset("fast.a.01"),
				wn.synset("fast.r.01"),
				wn.synset("mental_quickness.n.01"),
				wn.synset("promptly.r.01"),
				wn.synset("quick.s.01"),
				wn.synset("quickly.r.01")],

	# imprint, depression, trace, track
	"U+36a8":	[wn.synset("cut.n.08"),
				wn.synset("depression.n.08"),
				wn.synset("imprint.n.01"),
				wn.synset("imprint.n.03"),
				wn.synset("imprint.n.04"),
				wn.synset("imprint.n.05"),
				wn.synset("lead.n.03"),
				wn.synset("path.n.04"),
				wn.synset("racetrack.n.01"),
				wn.synset("touch.n.03"),
				wn.synset("trace.n.01"),
				wn.synset("trace.n.02"),
				wn.synset("trace.n.05"),
				wn.synset("trace.n.06"),
				wn.synset("tracing.n.02"),
				wn.synset("track.n.03"),
				wn.synset("track.n.06"),
				wn.synset("track.n.07"),
				wn.synset("track.n.08"),
				wn.synset("track.n.09"),
				wn.synset("track.n.10"),
				wn.synset("track.n.11")],

	# depression
	"U+36a9":	[wn.synset("depression.n.01")],

	# eagerness, keenness, willingness
	"U+36ab":	[wn.synset("acuteness.n.02"),
				wn.synset("eagerness.n.01"),
				wn.synset("enthusiasm.n.01"),
				wn.synset("readiness.n.02"),
				wn.synset("sharpness.n.05"),
				wn.synset("willingness.n.01")],

	# altruism, selflessness
	"U+36ad":	[wn.synset("altruism.n.01"),
				wn.synset("selflessness.n.02")],

	# urinate, make water, pass water, micturate, pee, piddle, piss, wee
	"U+36af":	[wn.synset("make.v.49")],

	# urine, piss, pee, piddle, weewee, water
	"U+36b0":	[wn.synset("urine.n.01")],

	# kidnap
	"U+36b1":	[wn.synset("kidnap.v.01")],

	# theft
	"U+36b2":	[wn.synset("larceny.n.01")],

	# escalator, moving stairs
	"U+36b3":	[wn.synset("escalator.n.02"),
				wn.synset("escalator_clause.n.01")],

	# stairs, steps
	"U+36b4":	[wn.synset("dance_step.n.01"),
				wn.synset("footfall.n.01"),
				wn.synset("footprint.n.01"),
				wn.synset("footstep.n.03"),
				wn.synset("gradation.n.01"),
				wn.synset("measure.n.01"),
				wn.synset("stairs.n.01"),
				wn.synset("stairway.n.01"),
				wn.synset("step.n.03"),
				wn.synset("step.n.04"),
				wn.synset("step.n.06"),
				wn.synset("step.n.10"),
				wn.synset("steps.n.02"),
				wn.synset("tone.n.09")],

	# concrete, cement
	"U+36b6":	[wn.synset("concrete.n.01")],

	# sport lesson
	"U+36b8":	[wn.synset("agitation.n.05"),
				wn.synset("athletic_contest.n.01"),
				wn.synset("calisthenics.n.01"),
				wn.synset("calisthenics.n.02"),
				wn.synset("exercise.n.01"),
				wn.synset("gymnastics.n.01"),
				wn.synset("sport.n.01")],

	# lesson, lecture, class
	"U+36b9":	[wn.synset("lesson.n.01")],

	# responsible
	"U+36ba":	[wn.synset("creditworthy.s.01"),
				wn.synset("responsible.a.01"),
				wn.synset("responsible.s.02")],

	# responsibility
	"U+36bb":	[wn.synset("duty.n.01"),
				wn.synset("responsibility.n.03")],

	# hum
	"U+36bc":	[wn.synset("hum.v.01"),
				wn.synset("hum.v.02"),
				wn.synset("hum.v.03"),
				wn.synset("hum.v.04")],

	# word
	"U+36be":	[wn.synset("parole.n.01"),
				wn.synset("word.n.01")],

	# Lakshmi
	"U+36bf":	[wn.synset("lakshmi.n.01")],

	# stirrup
	"U+36c0":	[wn.synset("stapes.n.01"),
				wn.synset("stirrup.n.01")],

	# support
	"U+36c1":	[wn.synset("support.n.01"),
				wn.synset("support.n.10")],

	# riding, horseback riding
	"U+36c2":	[wn.synset("riding.n.02")],

	# shall, will
	"U+36c3":	[wn.synset("bequeath.v.01"),
				wn.synset("crave.v.01"),
				wn.synset("desire.v.01"),
				wn.synset("feel_like.v.01"),
				wn.synset("hope.v.01"),
				wn.synset("like.v.05"),
				wn.synset("want.v.04"),
				wn.synset("will.v.01"),
				wn.synset("will.v.02"),
				wn.synset("wish.v.01"),
				wn.synset("wish.v.02"),
				wn.synset("wish.v.04")],

	# toy
	"U+36c5":	[wn.synset("plaything.n.01")],

	# infinite, limitless
	"U+36c6":	[wn.synset("infinite.a.01")],

	# open
	"U+36c7":	[wn.synset("open.a.01"),
				wn.synset("open.a.02"),
				wn.synset("open.s.04"),
				wn.synset("overt.a.01")],

	# addict
	"U+36c8":	[wn.synset("addict.n.01"),
				wn.synset("addict.n.02"),
				wn.synset("drug_addict.n.01"),
				wn.synset("drug_user.n.01")],

	# addiction
	"U+36c9":	[wn.synset("addiction.n.01"),
				wn.synset("addiction.n.02"),
				wn.synset("addiction.n.03")],

	# dryness, drought
	"U+36ca":	[wn.synset("dryness.n.01")],

	# dry
	"U+36cc":	[wn.synset("dry.v.01")],

	# bedbug, wall louse
	"U+36cd":	[wn.synset("bedbug.n.01")],

	# louse, stinging insect
	"U+36ce":	[wn.synset("bird_louse.n.01"),
				wn.synset("louse.n.01"),
				wn.synset("plant_louse.n.01"),
				wn.synset("worm.n.02")],

	# indoor, indoors
	"U+36d0":	[wn.synset("indoor.a.01"),
				wn.synset("indoor.s.02"),
				wn.synset("inside.n.01"),
				wn.synset("inside.n.02")],

	# pacifier, dummy
	"U+36d1":	[wn.synset("comforter.n.04")],

	# singer
	"U+36d2":	[wn.synset("singer.n.01")],

	# Christian love
	"U+36d3":	[wn.synset("love.n.02")],

	# Christian
	"U+36d4":	[wn.synset("christian.n.01")],

	# group of, much of, many of, quantity of
	"U+36d5":	[wn.synset("blood_group.n.01"),
				wn.synset("bunch.n.01"),
				wn.synset("crowd.n.02"),
				wn.synset("group.n.01"),
				wn.synset("group.n.03")],

	# camp
	"U+36d6":	[wn.synset("camp.n.01"),
				wn.synset("camp.n.02"),
				wn.synset("camp.n.03"),
				wn.synset("camp.n.05"),
				wn.synset("camp.n.06"),
				wn.synset("camp.n.07"),
				wn.synset("camp.n.08"),
				wn.synset("clique.n.01")],

	# yell, scream
	"U+36d7":	[wn.synset("shout.v.02")],

	# bomb, explosive
	"U+36da":	[wn.synset("bomb.n.01")],

	# explosion, detonation, blowup
	"U+36db":	[wn.synset("explosion.n.01")],

	# gauge
	"U+36dc":	[wn.synset("gauge.n.02")],

	# scale, measurement
	"U+36dd":	[wn.synset("measurement.n.01"),
				wn.synset("plate.n.14"),
				wn.synset("scale.n.01"),
				wn.synset("scale.n.02"),
				wn.synset("scale.n.03"),
				wn.synset("scale.n.04"),
				wn.synset("scale.n.05"),
				wn.synset("scale.n.06"),
				wn.synset("scale.n.07"),
				wn.synset("scale.n.08"),
				wn.synset("scale.n.10"),
				wn.synset("size.n.01")],

	# participate
	"U+36de":	[wn.synset("participate.v.01")],

	# participation, involvement
	"U+36df":	[wn.synset("engagement.n.07"),
				wn.synset("involvement.n.02")],

	# fatal, lethal
	"U+36e1":	[wn.synset("fatal.a.01")],

	# drug addict
	"U+36e2":	[wn.synset("drug_addict.n.01"),
				wn.synset("drug_user.n.01")],

	# drug addiction
	"U+36e3":	[wn.synset("drug_addiction.n.01")],

	# vasectomy
	"U+36e4":	[wn.synset("vasectomy.n.01")],

	# operation
	"U+36e5":	[wn.synset("operation.n.06")],

	# grunt
	"U+36e7":	[wn.synset("grunt.v.01")],

	# excavator, digger, power shovel shovel
	"U+36e9":	[wn.synset("digger.n.01"),
				wn.synset("excavator.n.01"),
				wn.synset("power_shovel.n.01")],

	# digging, excavation
	"U+36ea":	[wn.synset("dig.n.01")],

	# underpants, briefs, panties
	"U+36ed":	[wn.synset("underpants.n.01")],

	# pants, jeans, slacks, trousers
	"U+36ee":	[wn.synset("bloomers.n.01"),
				wn.synset("denim.n.02"),
				wn.synset("gasp.n.01"),
				wn.synset("jean.n.01"),
				wn.synset("mire.n.01"),
				wn.synset("pant.n.01"),
				wn.synset("slack.n.01"),
				wn.synset("slack.n.03"),
				wn.synset("slack.n.05"),
				wn.synset("slack.n.06"),
				wn.synset("slacks.n.01"),
				wn.synset("slump.n.01"),
				wn.synset("trouser.n.01"),
				wn.synset("trouser.n.02")],

	# Mother's Day
	"U+36ef":	[wn.synset("mother's_day.n.01")],

	# maturation
	"U+36f0":	[wn.synset("maturation.n.01")],

	# home run
	"U+36f2":	[wn.synset("bell_ringer.n.03"),
				wn.synset("channel.n.05"),
				wn.synset("circuit.n.01"),
				wn.synset("circuit.n.03"),
				wn.synset("circuit.n.05"),
				wn.synset("tour.n.01")],

	# fixing, fix, mending, mend, repair, reparation
	"U+36f3":	[wn.synset("fastener.n.02"),
				wn.synset("fix.n.01"),
				wn.synset("fix.n.02"),
				wn.synset("fix.n.04"),
				wn.synset("fixation.n.04"),
				wn.synset("haunt.n.01"),
				wn.synset("localization.n.01"),
				wn.synset("mend.n.01"),
				wn.synset("mending.n.01"),
				wn.synset("neutering.n.01"),
				wn.synset("repair.n.01"),
				wn.synset("repair.n.02"),
				wn.synset("reparation.n.01"),
				wn.synset("reparation.n.02"),
				wn.synset("reparation.n.04")],

	# puddle, pool
	"U+36f5":	[wn.synset("consortium.n.01"),
				wn.synset("pond.n.01"),
				wn.synset("pool.n.01"),
				wn.synset("pool.n.03"),
				wn.synset("pool.n.05"),
				wn.synset("pool.n.06"),
				wn.synset("pool.n.07"),
				wn.synset("pool.n.08"),
				wn.synset("pool.n.09"),
				wn.synset("puddle.n.01")],

	# home
	"U+36f7":	[wn.synset("dwelling.n.01"),
				wn.synset("family.n.01"),
				wn.synset("home.n.03")],

	# pocket
	"U+36f8":	[wn.synset("pocket.n.01"),
				wn.synset("pouch.n.03")],

	# boathouse
	"U+36f9":	[wn.synset("boathouse.n.01")],

	# seat, sitting
	"U+36fa":	[wn.synset("seat.n.03")],

	# liquid
	"U+36fb":	[wn.synset("liquid.n.01"),
				wn.synset("liquid.n.03")],

	# jaguar
	"U+36fc":	[wn.synset("jaguar.n.01")],

	# spot, mark
	"U+36fd":	[wn.synset("blot.n.02"),
				wn.synset("smudge.n.02"),
				wn.synset("spot.n.05")],

	# stocking, sock, pantyhose, tights
	"U+36fe":	[wn.synset("sock.n.01")],

	# disaster, catastrophe
	"U+3700":	[wn.synset("calamity.n.01")],

	# just, fair
	"U+3701":	[wn.synset("average.s.03"),
				wn.synset("bonny.s.01"),
				wn.synset("clean.s.11"),
				wn.synset("equitable.a.01"),
				wn.synset("fair.a.01"),
				wn.synset("fair.a.04"),
				wn.synset("fair.s.02"),
				wn.synset("fair.s.06"),
				wn.synset("fair.s.09"),
				wn.synset("fair.s.10"),
				wn.synset("good.s.07"),
				wn.synset("honest.s.07"),
				wn.synset("just.a.01")],

	# judgement, law
	"U+3702":	[wn.synset("judgment.n.03"),
				wn.synset("law.n.01"),
				wn.synset("law.n.02"),
				wn.synset("law.n.03"),
				wn.synset("law.n.04"),
				wn.synset("opinion.n.04")],

	# weather forecast
	"U+3706":	[wn.synset("weather_forecast.n.01")],

	# greater than
	"U+3707":	[wn.synset("relationship.n.02")],

	# outcome, result
	"U+3708":	[wn.synset("consequence.n.01"),
				wn.synset("result.n.03"),
				wn.synset("resultant_role.n.01"),
				wn.synset("solution.n.02")],

	# fail
	"U+3709":	[wn.synset("fail.v.02")],

	# failure
	"U+370a":	[wn.synset("bankruptcy.n.02"),
				wn.synset("fail.v.02"),
				wn.synset("failure.n.01"),
				wn.synset("failure.n.02"),
				wn.synset("failure.n.03"),
				wn.synset("failure.n.04"),
				wn.synset("failure.n.05"),
				wn.synset("failure.n.07"),
				wn.synset("miss.v.07"),
				wn.synset("stumble.v.04")],

	# pot stand, trivet
	"U+370b":	[wn.synset("trivet.n.02")],

	# best
	"U+370c":	[wn.synset("adept.s.01"),
				wn.synset("beneficial.s.01"),
				wn.synset("best.a.01"),
				wn.synset("better.s.03"),
				wn.synset("dear.s.02"),
				wn.synset("dependable.s.04"),
				wn.synset("effective.s.04"),
				wn.synset("estimable.s.02"),
				wn.synset("full.s.06"),
				wn.synset("good.a.01"),
				wn.synset("good.a.03"),
				wn.synset("good.s.06"),
				wn.synset("good.s.07"),
				wn.synset("good.s.09"),
				wn.synset("good.s.12"),
				wn.synset("good.s.13"),
				wn.synset("good.s.15"),
				wn.synset("good.s.16"),
				wn.synset("good.s.17"),
				wn.synset("good.s.18"),
				wn.synset("good.s.19"),
				wn.synset("good.s.20"),
				wn.synset("good.s.21")],

	# Purim
	"U+370d":	[wn.synset("purim.n.01")],

	# holiday, festival
	"U+370e":	[wn.synset("festival.n.01"),
				wn.synset("festival.n.02"),
				wn.synset("holiday.n.02"),
				wn.synset("vacation.n.01")],

	# score
	"U+370f":	[wn.synset("mark.n.01"),
				wn.synset("score.n.03")],

	# water tower
	"U+3710":	[wn.synset("water_tower.n.01")],

	# tower
	"U+3711":	[wn.synset("tower.n.01")],

	# yogurt, yoghurt
	"U+3712":	[wn.synset("yogurt.n.01")],

	# milk
	"U+3713":	[wn.synset("milk.n.01")],

	# pirate
	"U+3719":	[wn.synset("pirate.n.02"),
				wn.synset("pirate.n.03"),
				wn.synset("plagiarist.n.01")],

	# sailor
	"U+371a":	[wn.synset("sailor.n.01")],

	# receiving
	"U+371b":	[wn.synset("experience.v.03"),
				wn.synset("get.v.25"),
				wn.synset("meet.v.11"),
				wn.synset("pick_up.v.09"),
				wn.synset("receive.v.01"),
				wn.synset("receive.v.02"),
				wn.synset("receive.v.05"),
				wn.synset("receive.v.06"),
				wn.synset("receive.v.08"),
				wn.synset("receive.v.10"),
				wn.synset("receive.v.12"),
				wn.synset("receive.v.13"),
				wn.synset("welcome.v.02")],

	# keep, preserve, save
	"U+371c":	[wn.synset("keep.v.03")],

	# wage, pay, salary, spend
	"U+371e":	[wn.synset("pay.v.01")],

	# for, in order to
	"U+371f":	[wn.synset("by.r.01")],

	# precious thing, treasure
	"U+3721":	[wn.synset("treasure.n.04")],

	# precious, treasured
	"U+3722":	[wn.synset("cherished.s.01"),
				wn.synset("cute.s.02"),
				wn.synset("precious.s.02"),
				wn.synset("valuable.a.01"),
				wn.synset("valued.s.02")],

	# vestment
	"U+3723":	[wn.synset("chasuble.n.01"),
				wn.synset("vestment.n.01")],

	# accident, chance event event
	"U+3724":	[wn.synset("accident.n.01")],

	# incense
	"U+3726":	[wn.synset("incense.n.01")],

	# smoke
	"U+3727":	[wn.synset("smoke.n.01"),
				wn.synset("smoke.n.02")],

	# smell, give off odour off odour, odour, sense of smell, olfaction
	"U+3728":	[wn.synset("olfactory_property.n.01"),
				wn.synset("smell.n.04")],

	# argue, dispute, quarrel, row
	"U+3729":	[wn.synset("course.n.08"),
				wn.synset("quarrel.n.01"),
				wn.synset("quarrel.n.02"),
				wn.synset("row.n.01"),
				wn.synset("row.n.03"),
				wn.synset("row.n.05"),
				wn.synset("row.n.06"),
				wn.synset("rowing.n.01")],

	# argument, dispute, quarrel
	"U+372a":	[wn.synset("dispute.n.01"),
				wn.synset("quarrel.n.01")],

	# card
	"U+372c":	[wn.synset("batting_order.n.01"),
				wn.synset("calling_card.n.02"),
				wn.synset("card.n.01"),
				wn.synset("card.n.02"),
				wn.synset("card.n.03"),
				wn.synset("card.n.04"),
				wn.synset("card.n.08"),
				wn.synset("circuit_board.n.01"),
				wn.synset("menu.n.01"),
				wn.synset("poster.n.01"),
				wn.synset("wag.n.01")],

	# gopher, ground hog hog
	"U+372d":	[wn.synset("goffer.n.01"),
				wn.synset("gopher.n.04"),
				wn.synset("gopher_tortoise.n.01"),
				wn.synset("ground_squirrel.n.02"),
				wn.synset("minnesotan.n.01"),
				wn.synset("rodent.n.01")],

	# horse trailer, horsebox
	"U+372f":	[wn.synset("horsebox.n.01")],

	# trailer, container transport
	"U+3730":	[wn.synset("dawdler.n.01"),
				wn.synset("preview.n.01"),
				wn.synset("trailer.n.03"),
				wn.synset("trailer.n.04")],

	# pregnancy
	"U+3732":	[wn.synset("pregnancy.n.01")],

	# conception, fertilization, fertilized egg
	"U+3733":	[wn.synset("conception.n.02")],

	# missal, liturgical book
	"U+3734":	[wn.synset("missal.n.01")],

	# true, truly, truthful, truthfully
	"U+3735":	[wn.synset("dependable.s.02"),
				wn.synset("genuine.s.02"),
				wn.synset("in_truth.r.01"),
				wn.synset("on-key.s.01"),
				wn.synset("real.a.01"),
				wn.synset("rightfully.r.01"),
				wn.synset("sincerely.r.01"),
				wn.synset("true.a.01"),
				wn.synset("true.s.02"),
				wn.synset("true.s.03"),
				wn.synset("true.s.05"),
				wn.synset("true.s.08"),
				wn.synset("true.s.09"),
				wn.synset("true.s.10"),
				wn.synset("true.s.12"),
				wn.synset("truly.r.01"),
				wn.synset("truthful.a.01"),
				wn.synset("truthful.s.02"),
				wn.synset("truthfully.r.01")],

	# wind instrument
	"U+3736":	[wn.synset("kazoo.n.01"),
				wn.synset("wind_instrument.n.01")],

	# musical instrument
	"U+3737":	[wn.synset("bowed_stringed_instrument.n.01"),
				wn.synset("stringed_instrument.n.01")],

	# lighthouse
	"U+3738":	[wn.synset("beacon.n.03")],

	# grocery store, food store, supermarket
	"U+3739":	[wn.synset("supermarket.n.01")],

	# store, shop
	"U+373a":	[wn.synset("shop.n.01")],

	# union
	"U+373b":	[wn.synset("union.n.07")],

	# horseradish
	"U+373c":	[wn.synset("horseradish.n.01"),
				wn.synset("horseradish.n.02"),
				wn.synset("horseradish.n.03")],

	# fry, saute
	"U+373d":	[wn.synset("fry.v.02")],

	# nail polish, nail varnish
	"U+373f":	[wn.synset("nail_polish.n.01")],

	# saliva, spit
	"U+3740":	[wn.synset("phlegm.n.02"),
				wn.synset("saliva.n.01"),
				wn.synset("spit.n.01"),
				wn.synset("spit.n.03"),
				wn.synset("spit.n.04")],

	# spitting
	"U+3741":	[wn.synset("spit.n.04")],

	# rotisserie, spit
	"U+3742":	[wn.synset("rotisserie.n.02")],

	# rotation, circulation, orbit, lap, circle, round, circular
	"U+3743":	[wn.synset("beat.n.01"),
				wn.synset("circle.n.01"),
				wn.synset("circle.n.03"),
				wn.synset("circle.n.07"),
				wn.synset("circle.n.08"),
				wn.synset("circulation.n.01"),
				wn.synset("circulation.n.02"),
				wn.synset("circulation.n.03"),
				wn.synset("circulation.n.04"),
				wn.synset("circulation.n.05"),
				wn.synset("circulation.n.06"),
				wn.synset("cycle.n.01"),
				wn.synset("eye_socket.n.01"),
				wn.synset("lap.n.01"),
				wn.synset("lap.n.02"),
				wn.synset("lap.n.03"),
				wn.synset("lap.n.04"),
				wn.synset("lap.n.05"),
				wn.synset("lick.n.02"),
				wn.synset("orbit.n.01"),
				wn.synset("orbit.n.04"),
				wn.synset("r-2.n.01"),
				wn.synset("rotation.n.01"),
				wn.synset("rotation.n.02"),
				wn.synset("rotation.n.03"),
				wn.synset("rotation.n.04"),
				wn.synset("round.n.01"),
				wn.synset("round.n.04"),
				wn.synset("round.n.06"),
				wn.synset("round.n.08"),
				wn.synset("round.n.09"),
				wn.synset("round.n.10"),
				wn.synset("round.n.11"),
				wn.synset("round.n.12"),
				wn.synset("round_of_golf.n.01"),
				wn.synset("rung.n.01"),
				wn.synset("scope.n.01"),
				wn.synset("set.n.05"),
				wn.synset("sphere.n.01"),
				wn.synset("traffic_circle.n.01"),
				wn.synset("turn.n.09")],

	# eastern
	"U+3744":	[wn.synset("easterly.s.01"),
				wn.synset("eastern.a.04"),
				wn.synset("eastern.s.01")],

	# Poland
	"U+3745":	[wn.synset("poland.n.01")],

	# worker
	"U+3746":	[wn.synset("worker.n.01")],

	# circumcision
	"U+3747":	[wn.synset("circumcision.n.02"),
				wn.synset("circumcision.n.03")],

	# foreskin
	"U+3749":	[wn.synset("prepuce.n.02")],

	# elevator, lift, raise, grow, bring up, cultivate
	"U+374a":	[wn.synset("raise.v.02")],

	# hoist, lift
	"U+374b":	[wn.synset("aerodynamic_lift.n.01"),
				wn.synset("airlift.n.01"),
				wn.synset("elevation.n.01"),
				wn.synset("elevator.n.01"),
				wn.synset("face_lift.n.01"),
				wn.synset("hoist.n.01"),
				wn.synset("lift.n.01"),
				wn.synset("lift.n.04"),
				wn.synset("lift.n.06"),
				wn.synset("lift.n.07"),
				wn.synset("lift.n.11"),
				wn.synset("lift.n.12"),
				wn.synset("ski_tow.n.01")],

	# aid, device, support
	"U+374c":	[wn.synset("accompaniment.n.02"),
				wn.synset("aid.n.01"),
				wn.synset("aid.n.02"),
				wn.synset("aid.n.03"),
				wn.synset("care.n.01"),
				wn.synset("device.n.01"),
				wn.synset("device.n.02"),
				wn.synset("device.n.03"),
				wn.synset("device.n.04"),
				wn.synset("device.n.05"),
				wn.synset("documentation.n.03"),
				wn.synset("support.n.01"),
				wn.synset("support.n.02"),
				wn.synset("support.n.03"),
				wn.synset("support.n.04"),
				wn.synset("support.n.06"),
				wn.synset("support.n.07"),
				wn.synset("support.n.08"),
				wn.synset("support.n.10"),
				wn.synset("support.n.11")],

	# up, upward
	"U+374d":	[wn.synset("up.r.01")],

	# tail lift, lift
	"U+374e":	[wn.synset("elevator.n.01")],

	# platform, stage
	"U+374f":	[wn.synset("chopine.n.01"),
				wn.synset("degree.n.02"),
				wn.synset("phase.n.01"),
				wn.synset("platform.n.01"),
				wn.synset("platform.n.02"),
				wn.synset("platform.n.03"),
				wn.synset("platform.n.04"),
				wn.synset("stage.n.03"),
				wn.synset("stage.n.04"),
				wn.synset("stage.n.06"),
				wn.synset("stage.n.07"),
				wn.synset("stage.n.08"),
				wn.synset("stagecoach.n.01")],

	# prostitution
	"U+3750":	[wn.synset("prostitution.n.01")],

	# sexual intercourse, intercourse, copulation
	"U+3751":	[wn.synset("sexual_intercourse.n.01")],

	# business, economy, commerce, trade
	"U+3752":	[wn.synset("commerce.n.03"),
				wn.synset("trade.n.01"),
				wn.synset("trade.n.02")],

	# voltmeter
	"U+3753":	[wn.synset("voltmeter.n.01")],

	# voltage
	"U+3754":	[wn.synset("electric_potential.n.01"),
				wn.synset("voltage.n.01")],

	# life jacket, life-jacket
	"U+3755":	[wn.synset("life_jacket.n.01")],

	# canoeing
	"U+3756":	[wn.synset("canoe.v.01")],

	# paddle, oar
	"U+3757":	[wn.synset("oar.n.01"),
				wn.synset("paddle.n.01"),
				wn.synset("paddle.n.02"),
				wn.synset("paddle.n.03"),
				wn.synset("paddle.n.04"),
				wn.synset("soupspoon.n.01")],

	# key guard
	"U+3758":	[wn.synset("pegboard.n.01")],

	# keyboard
	"U+3759":	[wn.synset("keyboard.n.01"),
				wn.synset("keyboard.n.02")],

	# eyeliner, kohl
	"U+375a":	[wn.synset("kohl.n.01")],

	# horse box, stall
	"U+375b":	[wn.synset("stall.n.01")],

	# bricklayer
	"U+375c":	[wn.synset("bricklayer.n.01")],

	# toaster
	"U+375e":	[wn.synset("toaster.n.02")],

	# a, an, any
	"U+3760":	[wn.synset("a.n.06"),
				wn.synset("a.n.07"),
				wn.synset("adenine.n.01"),
				wn.synset("ampere.n.02"),
				wn.synset("angstrom.n.01"),
				wn.synset("any.r.01"),
				wn.synset("any.s.01"),
				wn.synset("associate_in_nursing.n.01"),
				wn.synset("deoxyadenosine_monophosphate.n.01"),
				wn.synset("one.n.01"),
				wn.synset("vitamin_a.n.01")],

	# some, any
	"U+3763":	[wn.synset("a_few.s.01"),
				wn.synset("any.s.01"),
				wn.synset("some.a.01"),
				wn.synset("some.s.02"),
				wn.synset("some.s.03"),
				wn.synset("some.s.04")],

	# occupational therapy
	"U+3764":	[wn.synset("occupational_therapy.n.01")],

	# therapy
	"U+3765":	[wn.synset("therapy.n.01")],

	# ownership, possession
	"U+3766":	[wn.synset("possession.n.01")],

	# supper, dinner
	"U+3767":	[wn.synset("dinner.n.01"),
				wn.synset("supper.n.01"),
				wn.synset("supper.n.02")],

	# meal
	"U+3768":	[wn.synset("meal.n.01")],

	# underground station, subway station
	"U+3769":	[wn.synset("subway_station.n.01")],

	# station
	"U+376a":	[wn.synset("station.n.01")],

	# tune, melody
	"U+376b":	[wn.synset("melody.n.02"),
				wn.synset("tune.n.01"),
				wn.synset("tune.n.02"),
				wn.synset("tune.n.03")],

	# shelter, refuge
	"U+376d":	[wn.synset("consignment.n.03"),
				wn.synset("cupboard.n.01"),
				wn.synset("protection.n.04"),
				wn.synset("recourse.n.01"),
				wn.synset("recourse.n.02"),
				wn.synset("refuge.n.03"),
				wn.synset("remittance.n.01"),
				wn.synset("safety.n.02"),
				wn.synset("shelter.n.01"),
				wn.synset("shelter.n.02"),
				wn.synset("shelter.n.05"),
				wn.synset("storehouse.n.01"),
				wn.synset("storeroom.n.01"),
				wn.synset("tax_shelter.n.01"),
				wn.synset("throw-in.n.01")],

	# scientist, academic, researcher
	"U+376e":	[wn.synset("scientist.n.01")],

	# coldness, cold
	"U+376f":	[wn.synset("coldness.n.03")],

	# juridical
	"U+3770":	[wn.synset("judicial.a.03")],

	# moo, bellow
	"U+3772":	[wn.synset("moo.v.01")],

	# cow
	"U+3773":	[wn.synset("cow.n.01")],

	# sleepy
	"U+3775":	[wn.synset("sleepy.s.01")],

	# costume, disguise
	"U+3776":	[wn.synset("costume.n.01"),
				wn.synset("costume.n.04")],

	# make believe, pretend, imaginary
	"U+3777":	[wn.synset("fanciful.s.02"),
				wn.synset("make-believe.s.01")],

	# dress up, disguise
	"U+3778":	[wn.synset("disguise.v.01")],

	# caregiver, protector, defender, guard
	"U+3779":	[wn.synset("caregiver.n.02"),
				wn.synset("defender.n.01"),
				wn.synset("defender.n.02"),
				wn.synset("health_professional.n.01")],

	# care, protection, defence, protect, defend
	"U+377a":	[wn.synset("defend.v.03"),
				wn.synset("defend.v.06")],

	# preceding, previous, former, earlier
	"U+377b":	[wn.synset("former.s.03")],

	# first, primary
	"U+377c":	[wn.synset("first.a.01")],

	# position
	"U+377f":	[wn.synset("military_position.n.01"),
				wn.synset("position.n.06"),
				wn.synset("status.n.01")],

	# boot, trunk, roof box, luggage compartment
	"U+3780":	[wn.synset("boot.n.01")],

	# ease, easiness, simplicity
	"U+3781":	[wn.synset("chasteness.n.01"),
				wn.synset("ease.n.01"),
				wn.synset("ease.n.02"),
				wn.synset("ease.n.04"),
				wn.synset("easiness.n.01"),
				wn.synset("easiness.n.03"),
				wn.synset("relief.n.02"),
				wn.synset("rest.n.02"),
				wn.synset("simplicity.n.01"),
				wn.synset("simplicity.n.02"),
				wn.synset("simplicity.n.03")],

	# hay
	"U+3784":	[wn.synset("hay.n.01")],

	# innocent, not guilty
	"U+3785":	[wn.synset("innocent.a.01")],

	# innocence
	"U+3786":	[wn.synset("innocence.n.03")],

	# prison, jail
	"U+3787":	[wn.synset("jail.n.01"),
				wn.synset("prison.n.01")],

	# hat, cap, hood
	"U+3789":	[wn.synset("hat.n.01")],

	# goodbye, farewell
	"U+378b":	[wn.synset("adieu.n.01"),
				wn.synset("farewell.n.01"),
				wn.synset("farewell.n.02")],

	# hello, greetings
	"U+378c":	[wn.synset("greeting.n.01"),
				wn.synset("hello.n.01")],

	# at one's destination, there
	"U+378d":	[wn.synset("there.n.01"),
				wn.synset("there.r.01"),
				wn.synset("there.r.02"),
				wn.synset("there.r.03")],

	# scrotum
	"U+378e":	[wn.synset("scrotum.n.01")],

	# testicle
	"U+378f":	[wn.synset("testis.n.01")],

	# sweet, confection
	"U+3790":	[wn.synset("angelic.s.03"),
				wn.synset("dulcet.s.02"),
				wn.synset("fresh.a.06"),
				wn.synset("fresh.s.09"),
				wn.synset("gratifying.s.01"),
				wn.synset("odoriferous.s.03"),
				wn.synset("sugared.s.01"),
				wn.synset("sweet.a.01"),
				wn.synset("sweet.a.07"),
				wn.synset("sweet.s.04")],

	# disagreement, discord
	"U+3791":	[wn.synset("disagreement.n.01")],

	# possible
	"U+3792":	[wn.synset("potential.a.01")],

	# possibility
	"U+3793":	[wn.synset("hypothesis.n.02"),
				wn.synset("possibility.n.01"),
				wn.synset("possibility.n.02"),
				wn.synset("possibility.n.04")],

	# maybe, perhaps, possibly
	"U+3794":	[wn.synset("possibly.r.01")],

	# fetus
	"U+3795":	[wn.synset("fetus.n.01")],

	# shadow, shade
	"U+3796":	[wn.synset("apparition.n.03"),
				wn.synset("darkness.n.02"),
				wn.synset("ghost.n.01"),
				wn.synset("nuance.n.01"),
				wn.synset("shade.n.01"),
				wn.synset("shade.n.02"),
				wn.synset("shade.n.03"),
				wn.synset("shade.n.05"),
				wn.synset("shade.n.08"),
				wn.synset("shadow.n.01"),
				wn.synset("shadow.n.04"),
				wn.synset("shadow.n.06"),
				wn.synset("shadow.n.07"),
				wn.synset("shadow.n.09"),
				wn.synset("tad.n.01"),
				wn.synset("tail.n.05"),
				wn.synset("trace.n.02")],

	# shape, form
	"U+3797":	[wn.synset("condition.n.05"),
				wn.synset("form.n.01"),
				wn.synset("form.n.03"),
				wn.synset("form.n.07"),
				wn.synset("form.n.10"),
				wn.synset("form.n.11"),
				wn.synset("form.n.14"),
				wn.synset("shape.n.01"),
				wn.synset("shape.n.02")],

	# ruin, wreck, wreckage, castle ruin
	"U+3798":	[wn.synset("ruin.n.02")],

	# destroyed, ruined, demolished, deleted, erased, cancelled
	"U+3799":	[wn.synset("delete.v.01"),
				wn.synset("demolished.s.01"),
				wn.synset("destroyed.a.01"),
				wn.synset("destroyed.s.02"),
				wn.synset("done_for.s.02"),
				wn.synset("edit.v.04"),
				wn.synset("erase.v.01"),
				wn.synset("erase.v.02"),
				wn.synset("erase.v.03"),
				wn.synset("finished.s.05"),
				wn.synset("off.a.03")],

	# church ruin, temple ruin, wreck, wreckage, temple, mosque
	"U+379a":	[wn.synset("crash.n.02"),
				wn.synset("shipwreck.n.03"),
				wn.synset("synagogue.n.01"),
				wn.synset("temple.n.01"),
				wn.synset("temple.n.02"),
				wn.synset("temple.n.03"),
				wn.synset("wreck.n.01"),
				wn.synset("wreck.n.04"),
				wn.synset("wreckage.n.01")],

	# church, mosque, temple
	"U+379b":	[wn.synset("church.n.02")],

	# sliced
	"U+379d":	[wn.synset("chopped.s.01"),
				wn.synset("sliced.s.02")],

	# slice
	"U+379e":	[wn.synset("break.v.43"),
				wn.synset("carve.v.02"),
				wn.synset("cut.n.05"),
				wn.synset("cut.v.01"),
				wn.synset("cut_off.v.03"),
				wn.synset("dilute.v.01"),
				wn.synset("divide.v.01"),
				wn.synset("edit.v.03"),
				wn.synset("interrupt.v.01"),
				wn.synset("mow.v.01"),
				wn.synset("piece.n.08"),
				wn.synset("reduce.v.01"),
				wn.synset("slash.v.01"),
				wn.synset("slash.v.03"),
				wn.synset("slash.v.04"),
				wn.synset("slice.n.01"),
				wn.synset("slice.n.04"),
				wn.synset("slice.n.05"),
				wn.synset("slice.n.06"),
				wn.synset("slice.v.04"),
				wn.synset("slit.v.01"),
				wn.synset("snip.v.02"),
				wn.synset("traverse.v.01")],

	# medical tube, catheter, cannula
	"U+37a0":	[wn.synset("cannula.n.01"),
				wn.synset("catheter.n.01")],

	# catheter
	"U+37a1":	[wn.synset("catheter.n.01")],

	# cannula
	"U+37a2":	[wn.synset("cannula.n.01")],

	# pavement, sidewalk
	"U+37a3":	[wn.synset("sidewalk.n.01")],

	# opposite meaning, opposite of, opposite
	"U+37a4":	[wn.synset("antonym.n.01"),
				wn.synset("inverse.n.01"),
				wn.synset("opposition.n.04"),
				wn.synset("reverse.n.01")],

	# Swedish
	"U+37a7":	[wn.synset("swedish.n.01")],

	# class
	"U+37a8":	[wn.synset("class.n.08")],

	# correct, accurate, good, right
	"U+37a9":	[wn.synset("correct.a.01")],

	# positive
	"U+37aa":	[wn.synset("positive.n.01"),
				wn.synset("positive.n.02")],

	# good conscience
	"U+37ab":	[wn.synset("conscience.n.01")],

	# old, elderly
	"U+37ac":	[wn.synset("old.a.01"),
				wn.synset("old.a.02")],

	# young
	"U+37ad":	[wn.synset("young.a.01")],

	# people, tribe, clan, folk
	"U+37ae":	[wn.synset("kin.n.02")],

	# go ashore
	"U+37b0":	[wn.synset("disembark.v.01"),
				wn.synset("get_off.v.01")],

	# debarkation, disembarkation
	"U+37b1":	[wn.synset("debarkation.n.01")],

	# trombone
	"U+37b6":	[wn.synset("trombone.n.01")],

	# brass instrument
	"U+37b7":	[wn.synset("brass.n.02"),
				wn.synset("cornet.n.01")],

	# leader, director, guide
	"U+37b9":	[wn.synset("conductor.n.01"),
				wn.synset("director.n.01"),
				wn.synset("director.n.02"),
				wn.synset("director.n.03"),
				wn.synset("drawing_card.n.02"),
				wn.synset("film_director.n.01"),
				wn.synset("guide.n.02"),
				wn.synset("guide.n.06"),
				wn.synset("guidebook.n.01"),
				wn.synset("leader.n.01"),
				wn.synset("scout.n.04"),
				wn.synset("template.n.01"),
				wn.synset("usher.n.03")],

	# harassment
	"U+37ba":	[wn.synset("agony.n.01"),
				wn.synset("anguish.n.01"),
				wn.synset("harassment.n.01"),
				wn.synset("harassment.n.02"),
				wn.synset("mistreatment.n.01"),
				wn.synset("pest.n.03")],

	# sociology
	"U+37bc":	[wn.synset("sociology.n.01")],

	# okra, lady's finger's finger
	"U+37bd":	[wn.synset("okra.n.02")],

	# practise, practice, drill, exercise, rehearse, work out out
	"U+37c0":	[wn.synset("drill.v.03"),
				wn.synset("exercise.v.04"),
				wn.synset("exert.v.01"),
				wn.synset("practice.v.01")],

	# fox
	"U+37c1":	[wn.synset("fox.n.01")],

	# creative
	"U+37c4":	[wn.synset("creative.a.01")],

	# tornado
	"U+37c7":	[wn.synset("tornado.n.01")],

	# gale
	"U+37c8":	[wn.synset("gale.n.01")],

	# apartment, flat, unit
	"U+37c9":	[wn.synset("apartment.n.01")],

	# sprout, germinate
	"U+37ca":	[wn.synset("shoot.v.19")],

	# growth, growing
	"U+37cc":	[wn.synset("emergence.n.01"),
				wn.synset("growing.n.02"),
				wn.synset("growth.n.01"),
				wn.synset("growth.n.02"),
				wn.synset("growth.n.04"),
				wn.synset("growth.n.06"),
				wn.synset("growth.n.07"),
				wn.synset("increase.n.03")],

	# trampoline
	"U+37ce":	[wn.synset("trampoline.n.01")],

	# tumble drier, tumble dryer
	"U+37d0":	[wn.synset("tumble-dryer.n.01")],

	# pudding, cream
	"U+37d2":	[wn.synset("cream.n.01"),
				wn.synset("cream.n.02"),
				wn.synset("cream.n.03"),
				wn.synset("pudding.n.01"),
				wn.synset("pudding.n.02"),
				wn.synset("pudding.n.03")],

	# gutter, eaves trough trough
	"U+37d3":	[wn.synset("gutter.n.01")],

	# eaves
	"U+37d4":	[wn.synset("eaves.n.01")],

	# mountain berry, cowberry, lingonberry
	"U+37d5":	[wn.synset("cowberry.n.01")],

	# fruit juice, juice
	"U+37d6":	[wn.synset("juice.n.01"),
				wn.synset("juice.n.02"),
				wn.synset("juice.n.03"),
				wn.synset("juice.n.04")],

	# drink, beverage
	"U+37d7":	[wn.synset("beverage.n.01")],

	# Valentine
	"U+37d8":	[wn.synset("valentine.n.01"),
				wn.synset("valentine.n.02")],

	# hoof
	"U+37da":	[wn.synset("hoof.n.01")],

	# storeroom
	"U+37db":	[wn.synset("storeroom.n.01")],

	# seaplane
	"U+37dc":	[wn.synset("seaplane.n.01")],

	# roti, chapati, flatbread
	"U+37dd":	[wn.synset("chapatti.n.01"),
				wn.synset("flatbread.n.01"),
				wn.synset("grid.n.05"),
				wn.synset("grill.n.02")],

	# disc, disk
	"U+37de":	[wn.synset("disk.n.01"),
				wn.synset("magnetic_disk.n.01")],

	# yen
	"U+37df":	[wn.synset("yen.n.02")],

	# Scotland
	"U+37e1":	[wn.synset("scotland.n.01")],

	# sow
	"U+37e2":	[wn.synset("sow.n.01")],

	# Woden
	"U+37e4":	[wn.synset("odin.n.01"),
				wn.synset("woden.n.01")],

	# Nordic God
	"U+37e5":	[wn.synset("deity.n.01"),
				wn.synset("god.n.03"),
				wn.synset("godhead.n.01")],

	# watch tower, observation tower
	"U+37e6":	[wn.synset("barbican.n.01"),
				wn.synset("watchtower.n.01")],

	# observation
	"U+37e7":	[wn.synset("observation.n.02")],

	# happy, glad, gladly, happily
	"U+37e8":	[wn.synset("beaming.s.01"),
				wn.synset("felicitous.s.02"),
				wn.synset("glad.a.01"),
				wn.synset("glad.s.02"),
				wn.synset("glad.s.03"),
				wn.synset("gladly.r.01"),
				wn.synset("happily.r.01"),
				wn.synset("happily.r.02"),
				wn.synset("happy.a.01"),
				wn.synset("happy.s.04")],

	# ice hockey
	"U+37e9":	[wn.synset("ice_hockey.n.01"),
				wn.synset("puck.n.02")],

	# oppressed, unfree
	"U+37eb":	[wn.synset("unfree.a.01")],

	# oppression, captivity, slavery
	"U+37ec":	[wn.synset("bondage.n.02"),
				wn.synset("captivity.n.01"),
				wn.synset("enslavement.n.01"),
				wn.synset("oppression.n.01"),
				wn.synset("oppression.n.02"),
				wn.synset("oppression.n.03"),
				wn.synset("slavery.n.02"),
				wn.synset("slavery.n.03")],

	# giving, gift
	"U+37ef":	[wn.synset("afford.v.04"),
				wn.synset("bear.v.05"),
				wn.synset("bestow.v.02"),
				wn.synset("breathe.v.03"),
				wn.synset("endowment.n.01"),
				wn.synset("establish.v.05"),
				wn.synset("find.v.01"),
				wn.synset("get.v.19"),
				wn.synset("gift.n.01"),
				wn.synset("give.v.01"),
				wn.synset("give.v.03"),
				wn.synset("give.v.04"),
				wn.synset("give.v.05"),
				wn.synset("give.v.08"),
				wn.synset("give.v.09"),
				wn.synset("give.v.10"),
				wn.synset("give.v.20"),
				wn.synset("give.v.21"),
				wn.synset("give.v.29"),
				wn.synset("give.v.31"),
				wn.synset("give.v.34"),
				wn.synset("give.v.37"),
				wn.synset("give.v.41"),
				wn.synset("give.v.44"),
				wn.synset("give_away.v.01"),
				wn.synset("giving.n.01"),
				wn.synset("giving.n.02"),
				wn.synset("giving.n.03"),
				wn.synset("go.v.25"),
				wn.synset("grant.v.05"),
				wn.synset("hit.v.09"),
				wn.synset("hit.v.15"),
				wn.synset("hold.v.03"),
				wn.synset("pass.v.05"),
				wn.synset("sacrifice.v.01"),
				wn.synset("strike.v.05"),
				wn.synset("yield.v.10")],

	# shoot
	"U+37f0":	[wn.synset("blast.v.07")],

	# tape recorder
	"U+37f1":	[wn.synset("recorder.n.01")],

	# congratulations, best of luck, mazel tov
	"U+37f3":	[wn.synset("congratulation.n.01"),
				wn.synset("congratulation.n.02"),
				wn.synset("praise.n.01")],

	# luck, fortune
	"U+37f4":	[wn.synset("fortune.n.02"),
				wn.synset("luck.n.02"),
				wn.synset("luck.n.03")],

	# in, inside, interior, internal
	"U+37f5":	[wn.synset("inside.n.01"),
				wn.synset("inside.n.02")],

	# tie, bind together, lash necktie
	"U+37f6":	[wn.synset("tie.v.01")],

	# knot
	"U+37f7":	[wn.synset("knot.n.02"),
				wn.synset("knot.n.03"),
				wn.synset("knot.n.04")],

	# powerful, mighty
	"U+37f9":	[wn.synset("powerful.a.01")],

	# passenger
	"U+37fa":	[wn.synset("passenger.n.01")],

	# adopt
	"U+37fc":	[wn.synset("adopt.v.05")],

	# adoption
	"U+37fd":	[wn.synset("adoption.n.02")],

	# anyone, anybody, somebody, someone
	"U+37ff":	[wn.synset("person.n.01")],

	# Sif
	"U+3801":	[wn.synset("sif.n.01")],

	# Thor
	"U+3802":	[wn.synset("thor.n.01")],

	# crutches
	"U+3804":	[wn.synset("crutch.n.01"),
				wn.synset("crutch.n.02")],

	# medical, medically
	"U+3806":	[wn.synset("medical.a.01")],

	# relay
	"U+3807":	[wn.synset("relay.n.04")],

	# dotted
	"U+380a":	[wn.synset("dotted.s.01")],

	# glacier
	"U+380c":	[wn.synset("glacier.n.01")],

	# actor
	"U+380d":	[wn.synset("actor.n.01")],

	# flood
	"U+380e":	[wn.synset("flood.n.01")],

	# republic
	"U+3810":	[wn.synset("republic.n.02")],

	# princess
	"U+3812":	[wn.synset("princess.n.01")],

	# leek
	"U+3813":	[wn.synset("leek.n.01")],

	# steamship
	"U+3814":	[wn.synset("steamer.n.03")],

	# height, tallness, altitude
	"U+3815":	[wn.synset("acme.n.01"),
				wn.synset("altitude.n.01"),
				wn.synset("height.n.01"),
				wn.synset("stature.n.02"),
				wn.synset("tallness.n.02")],

	# taxi driver, cab driver
	"U+3817":	[wn.synset("taxidriver.n.01")],

	# taxi, cab
	"U+3818":	[wn.synset("cab.n.03")],

	# lettuce, leafy vegetable vegetable
	"U+3819":	[wn.synset("lettuce.n.02")],

	# electric circuit
	"U+381b":	[wn.synset("circuit.n.01")],

	# tahini, sesame seed spread seed spread
	"U+381c":	[wn.synset("tahini.n.01")],

	# white
	"U+381d":	[wn.synset("white.n.01")],

	# mummy
	"U+381e":	[wn.synset("mummy.n.02")],

	# dead, deceased
	"U+381f":	[wn.synset("all_in.s.01"),
				wn.synset("asleep.s.03"),
				wn.synset("dead.a.01"),
				wn.synset("dead.a.02"),
				wn.synset("dead.s.04"),
				wn.synset("dead.s.05"),
				wn.synset("dead.s.06"),
				wn.synset("dead.s.07"),
				wn.synset("dead.s.08"),
				wn.synset("dead.s.09"),
				wn.synset("dead.s.10"),
				wn.synset("dead.s.11"),
				wn.synset("dead.s.12"),
				wn.synset("dead.s.13"),
				wn.synset("dead.s.14"),
				wn.synset("dead.s.15"),
				wn.synset("dead.s.16"),
				wn.synset("dead.s.17")],

	# all powerful
	"U+3821":	[wn.synset("almighty.s.01")],

	# ability, capability, capacity, potential
	"U+3822":	[wn.synset("ability.n.01")],

	# quantity
	"U+3825":	[wn.synset("quantity.n.03")],

	# multitude
	"U+3826":	[wn.synset("battalion.n.02")],

	# wind turbine
	"U+3827":	[wn.synset("wind_turbine.n.01")],

	# windmill
	"U+3828":	[wn.synset("windmill.n.01"),
				wn.synset("windmill.n.02")],

	# peacock
	"U+3829":	[wn.synset("peacock.n.02")],

	# chain
	"U+382a":	[wn.synset("chain.n.03")],

	# alligator, crocodile
	"U+382b":	[wn.synset("crocodile.n.01")],

	# avalanche
	"U+382c":	[wn.synset("avalanche.n.01")],

	# skiing
	"U+382d":	[wn.synset("skiing.n.01")],

	# skis
	"U+382e":	[wn.synset("ski.n.01")],

	# dog sled
	"U+3830":	[wn.synset("dogsled.n.01")],

	# ballet
	"U+3832":	[wn.synset("ballet.n.01")],

	# crater
	"U+3833":	[wn.synset("crater.n.03")],

	# sunscreen, sunblock, sun lotion lotion
	"U+3834":	[wn.synset("sunscreen.n.01")],

	# persevere
	"U+3835":	[wn.synset("persevere.v.01")],

	# perseverance
	"U+3836":	[wn.synset("doggedness.n.01"),
				wn.synset("perseverance.n.02")],

	# icing
	"U+3837":	[wn.synset("frost.n.03"),
				wn.synset("frosting.n.01"),
				wn.synset("icing.n.03")],

	# recipe
	"U+383a":	[wn.synset("recipe.n.01")],

	# embark, board
	"U+383e":	[wn.synset("board.v.01"),
				wn.synset("board.v.02"),
				wn.synset("board.v.03"),
				wn.synset("board.v.04"),
				wn.synset("embark.v.01"),
				wn.synset("embark.v.02"),
				wn.synset("venture.v.01")],

	# mourn
	"U+3840":	[wn.synset("mourn.v.01"),
				wn.synset("mourn.v.02")],

	# sadness, sorrow, unhappiness
	"U+3841":	[wn.synset("sadness.n.01")],

	# loss
	"U+3842":	[wn.synset("loss.n.01"),
				wn.synset("loss.n.06")],

	# minute
	"U+3843":	[wn.synset("minute.n.01")],

	# digital processing, artificial intelligence, AI
	"U+3846":	[wn.synset("army_intelligence.n.01"),
				wn.synset("artificial_insemination.n.01"),
				wn.synset("artificial_intelligence.n.01"),
				wn.synset("three-toed_sloth.n.01")],

	# digits
	"U+3847":	[wn.synset("bit.n.06"),
				wn.synset("digit.n.01"),
				wn.synset("digit.n.03"),
				wn.synset("finger.n.02")],

	# tricycle
	"U+3849":	[wn.synset("tricycle.n.01")],

	# drop
	"U+384a":	[wn.synset("drop.n.01")],

	# Kali
	"U+384b":	[wn.synset("kali.n.02")],

	# black
	"U+384c":	[wn.synset("black.n.01")],

	# bottle nipple, teat, bottle
	"U+384d":	[wn.synset("bottle.n.02"),
				wn.synset("bottle.n.03"),
				wn.synset("nipple.n.01")],

	# bottleneck, bottle opening opening
	"U+384e":	[wn.synset("bottleneck.n.02"),
				wn.synset("constriction.n.01")],

	# go, depart, leave
	"U+3850":	[wn.synset("depart.v.03"),
				wn.synset("depart.v.04"),
				wn.synset("exit.v.01"),
				wn.synset("go.v.28"),
				wn.synset("leave.v.01"),
				wn.synset("sidetrack.v.01")],

	# departure
	"U+3851":	[wn.synset("departure.n.01")],

	# subway, metro, underground, tube
	"U+3852":	[wn.synset("metro.n.01")],

	# tunnel, subway, underpass
	"U+3853":	[wn.synset("tunnel.n.01")],

	# team
	"U+3854":	[wn.synset("team.n.01")],

	# bonfire, barbeque, campfire
	"U+3855":	[wn.synset("barbecue.n.01"),
				wn.synset("barbecue.n.02"),
				wn.synset("barbecue.n.03"),
				wn.synset("bonfire.n.01"),
				wn.synset("campfire.n.01")],

	# rat, rodent, gnawer, gnawing animal
	"U+3856":	[wn.synset("informer.n.01"),
				wn.synset("rat.n.01"),
				wn.synset("rat.n.05"),
				wn.synset("rodent.n.01"),
				wn.synset("rotter.n.01"),
				wn.synset("scab.n.01")],

	# attic
	"U+3857":	[wn.synset("attic.n.02"),
				wn.synset("attic.n.03"),
				wn.synset("attic.n.04"),
				wn.synset("loft.n.02")],

	# fingernail, nail
	"U+3858":	[wn.synset("nail.n.01")],

	# farness, remoteness, farawayness
	"U+3859":	[wn.synset("aloofness.n.02"),
				wn.synset("farness.n.01")],

	# sign, advertisement, signal, broadcast, transmitting
	"U+385a":	[wn.synset("ad.n.01"),
				wn.synset("augury.n.01"),
				wn.synset("polarity.n.02"),
				wn.synset("sign.n.01"),
				wn.synset("sign.n.02"),
				wn.synset("sign.n.06"),
				wn.synset("sign.n.09"),
				wn.synset("sign.n.10"),
				wn.synset("sign.n.11"),
				wn.synset("sign_of_the_zodiac.n.01"),
				wn.synset("signal.n.01"),
				wn.synset("signboard.n.01")],

	# attention
	"U+385b":	[wn.synset("attention.n.01"),
				wn.synset("attention.n.03"),
				wn.synset("attention.n.05")],

	# sign language
	"U+385c":	[wn.synset("sign_language.n.01")],

	# crescent
	"U+385e":	[wn.synset("crescent.n.01")],

	# hot dog, frankfurter
	"U+3860":	[wn.synset("frank.n.02")],

	# long
	"U+3861":	[wn.synset("long.a.01"),
				wn.synset("long.a.02")],

	# sausage, frankfurter, hotdog, hot dog
	"U+3862":	[wn.synset("sausage.n.01")],

	# parachuting
	"U+3863":	[wn.synset("jump.n.05")],

	# parachute
	"U+3864":	[wn.synset("parachute.n.01")],

	# headset
	"U+3865":	[wn.synset("headset.n.01")],

	# earmuffs
	"U+3866":	[wn.synset("earmuff.n.01")],

	# thaw, melt
	"U+3867":	[wn.synset("dissolve.v.09")],

	# thawing, melting
	"U+3868":	[wn.synset("thaw.n.01"),
				wn.synset("thaw.n.02")],

	# current
	"U+386a":	[wn.synset("current.a.01")],

	# geography
	"U+386b":	[wn.synset("geography.n.01")],

	# jury
	"U+386d":	[wn.synset("jury.n.01"),
				wn.synset("jury.n.02")],

	# peer
	"U+386e":	[wn.synset("peer.n.01"),
				wn.synset("peer.n.02")],

	# legal
	"U+386f":	[wn.synset("legal.a.01")],

	# funeral
	"U+3870":	[wn.synset("funeral.n.01")],

	# empty, evacuate, throw away, void
	"U+3871":	[wn.synset("empty.v.01"),
				wn.synset("empty.v.02")],

	# emptying, voidance, evacuation
	"U+3872":	[wn.synset("elimination.n.02"),
				wn.synset("emptying.n.01"),
				wn.synset("evacuation.n.02")],

	# understanding, comprehension
	"U+3875":	[wn.synset("sympathy.n.01")],

	# magnetism
	"U+3876":	[wn.synset("magnetism.n.02")],

	# metal bar
	"U+3877":	[wn.synset("metallic_element.n.01")],

	# address
	"U+3879":	[wn.synset("address.n.02"),
				wn.synset("address.n.06")],

	# alone, just, only, solitary
	"U+387a":	[wn.synset("alone.s.01"),
				wn.synset("alone.s.02"),
				wn.synset("alone.s.03"),
				wn.synset("alone.s.04"),
				wn.synset("equitable.a.01"),
				wn.synset("fair.a.01"),
				wn.synset("good.s.07"),
				wn.synset("just.a.01"),
				wn.synset("lone.s.02"),
				wn.synset("lone.s.03"),
				wn.synset("lonely.s.04"),
				wn.synset("nongregarious.s.01")],

	# reclaim
	"U+387d":	[wn.synset("domesticate.v.02"),
				wn.synset("drain.v.03"),
				wn.synset("reclaim.v.01"),
				wn.synset("reclaim.v.02"),
				wn.synset("reclaim.v.04"),
				wn.synset("reform.v.02")],

	# land
	"U+387f":	[wn.synset("bring.v.05"),
				wn.synset("down.v.04"),
				wn.synset("land.v.01"),
				wn.synset("land.v.02"),
				wn.synset("land.v.04"),
				wn.synset("land.v.05"),
				wn.synset("land.v.06")],

	# radish
	"U+3882":	[wn.synset("radish.n.03")],

	# August
	"U+3883":	[wn.synset("august.n.01")],

	# employed, working
	"U+3885":	[wn.synset("employed.a.01"),
				wn.synset("employed.s.02"),
				wn.synset("running.s.06"),
				wn.synset("working.s.01"),
				wn.synset("working.s.02"),
				wn.synset("working.s.03"),
				wn.synset("working.s.05")],

	# angry, angrily, mad
	"U+3886":	[wn.synset("angry.a.01")],

	# wicket
	"U+3887":	[wn.synset("wicket.n.01"),
				wn.synset("wicket.n.02"),
				wn.synset("wicket.n.03"),
				wn.synset("wicket.n.04")],

	# prosecutor
	"U+3888":	[wn.synset("prosecutor.n.01")],

	# legal person
	"U+3889":	[wn.synset("judge.n.01"),
				wn.synset("jurist.n.01"),
				wn.synset("lawyer.n.01")],

	# dichotomy, duality
	"U+388b":	[wn.synset("dichotomy.n.01"),
				wn.synset("duality.n.02"),
				wn.synset("duality.n.03")],

	# clitoris
	"U+388c":	[wn.synset("clitoris.n.01")],

	# apparent, clear, evident, obvious, plain, transparent
	"U+388f":	[wn.synset("absolved.s.01"),
				wn.synset("apparent.s.01"),
				wn.synset("apparent.s.02"),
				wn.synset("clean.s.02"),
				wn.synset("clean.s.03"),
				wn.synset("clear.a.01"),
				wn.synset("clear.a.04"),
				wn.synset("clear.a.11"),
				wn.synset("clear.s.02"),
				wn.synset("clear.s.03"),
				wn.synset("clear.s.05"),
				wn.synset("clear.s.06"),
				wn.synset("clear.s.08"),
				wn.synset("clear.s.09"),
				wn.synset("clear.s.13"),
				wn.synset("clear.s.14"),
				wn.synset("clear.s.15"),
				wn.synset("clear.s.17"),
				wn.synset("discernible.s.03"),
				wn.synset("homely.s.01"),
				wn.synset("obvious.a.01"),
				wn.synset("plain.a.02"),
				wn.synset("plain.a.03"),
				wn.synset("plain.s.04"),
				wn.synset("plain.s.05"),
				wn.synset("plain.s.06"),
				wn.synset("well-defined.a.02")],

	# intestine, bowel, gut
	"U+3890":	[wn.synset("intestine.n.01")],

	# Pope
	"U+3893":	[wn.synset("pope.n.01")],

	# lumberjack
	"U+3894":	[wn.synset("lumberman.n.01")],

	# fantasy, phantasy, imagination, illusion
	"U+3896":	[wn.synset("delusion.n.03"),
				wn.synset("fantasy.n.01"),
				wn.synset("fantasy.n.02"),
				wn.synset("illusion.n.01"),
				wn.synset("illusion.n.02"),
				wn.synset("imagination.n.01")],

	# abortion
	"U+389a":	[wn.synset("abortion.n.01")],

	# miscarriage, abortion
	"U+389b":	[wn.synset("spontaneous_abortion.n.01")],

	# believer
	"U+389d":	[wn.synset("believer.n.02")],

	# agreed, in agreement, harmonious
	"U+389e":	[wn.synset("agreed.s.01"),
				wn.synset("harmonious.a.01"),
				wn.synset("harmonious.s.02"),
				wn.synset("harmonious.s.03"),
				wn.synset("harmonious.s.04"),
				wn.synset("unresentful.a.01")],

	# with
	"U+38a0":	[wn.synset("iodine.n.01")],

	# meeting, assembly, conference, encounter
	"U+38a2":	[wn.synset("assembly.n.04"),
				wn.synset("assembly.n.06"),
				wn.synset("conference.n.01"),
				wn.synset("meeting.n.01"),
				wn.synset("meeting.n.04")],

	# parting
	"U+38a4":	[wn.synset("farewell.n.02")],

	# matzo
	"U+38a6":	[wn.synset("matzo.n.01")],

	# sled, sledge, sleigh, toboggan
	"U+38a7":	[wn.synset("maul.n.01"),
				wn.synset("sled.n.01"),
				wn.synset("toboggan.n.01")],

	# boules
	"U+38a8":	[wn.synset("boulle.n.01"),
				wn.synset("lawn_bowling.n.01")],

	# winter
	"U+38aa":	[wn.synset("winter.n.01")],

	# Sukkot
	"U+38ac":	[wn.synset("succoth.n.01")],

	# divided
	"U+38ad":	[wn.synset("divided.s.03")],

	# file, data file file
	"U+38ae":	[wn.synset("file.n.01"),
				wn.synset("file.n.02"),
				wn.synset("file.n.03"),
				wn.synset("file.n.04")],

	# elephant
	"U+38af":	[wn.synset("elephant.n.01")],

	# bracha, berakah, prayer
	"U+38b0":	[wn.synset("entreaty.n.01"),
				wn.synset("prayer.n.01"),
				wn.synset("prayer.n.02"),
				wn.synset("prayer.n.04"),
				wn.synset("prayer.n.05")],

	# laundromat, launderette, laundry
	"U+38b1":	[wn.synset("launderette.n.01"),
				wn.synset("laundry.n.01"),
				wn.synset("laundry.n.02")],

	# explorer, enquirer
	"U+38b2":	[wn.synset("explorer.n.01"),
				wn.synset("inquirer.n.01"),
				wn.synset("internet_explorer.n.01")],

	# explore
	"U+38b3":	[wn.synset("explore.v.02"),
				wn.synset("explore.v.03"),
				wn.synset("explore.v.04"),
				wn.synset("research.v.02")],

	# data
	"U+38b5":	[wn.synset("corpus.n.02"),
				wn.synset("data.n.01"),
				wn.synset("datum.n.01")],

	# stress
	"U+38b6":	[wn.synset("stress.v.01"),
				wn.synset("stress.v.02"),
				wn.synset("try.v.07")],

	# sandbox, sandpit, sandtray
	"U+38b8":	[wn.synset("sandbox.n.02")],

	# sand
	"U+38b9":	[wn.synset("sand.n.01")],

	# Islam
	"U+38bc":	[wn.synset("islam.n.01"),
				wn.synset("islam.n.02")],

	# Muslim, Moslem, Islamic
	"U+38bd":	[wn.synset("muslim.a.01")],

	# archeologist
	"U+38be":	[wn.synset("archeologist.n.01")],

	# archeology
	"U+38bf":	[wn.synset("archeology.n.01")],

	# synthetic speech, text to speech, tts
	"U+38c0":	[wn.synset("micronesia.n.01"),
				wn.synset("palau.n.01"),
				wn.synset("terrestrial_time.n.01")],

	# speech
	"U+38c1":	[wn.synset("address.n.03")],

	# long for, yearn
	"U+38c2":	[wn.synset("hanker.v.01")],

	# longing, yearning
	"U+38c3":	[wn.synset("longing.n.01")],

	# descend, go down down
	"U+38c5":	[wn.synset("fall.v.32")],

	# accordion
	"U+38c6":	[wn.synset("accordion.n.01")],

	# apron, coverall, smock, overall
	"U+38c7":	[wn.synset("apron.n.01")],

	# insomnia
	"U+38c8":	[wn.synset("insomnia.n.01")],

	# nation
	"U+38c9":	[wn.synset("nation.n.02"),
				wn.synset("state.n.04")],

	# forced, compelled, obliged
	"U+38ca":	[wn.synset("compel.v.01"),
				wn.synset("compel.v.02"),
				wn.synset("constrained.s.01"),
				wn.synset("duty-bound.s.01"),
				wn.synset("forced.a.01"),
				wn.synset("forced.s.02"),
				wn.synset("forced.s.03")],

	# must, have to, be forced to
	"U+38cb":	[wn.synset("must.n.01"),
				wn.synset("must.n.02"),
				wn.synset("must.s.01"),
				wn.synset("mustiness.n.01"),
				wn.synset("owe.v.03")],

	# ketchup
	"U+38cd":	[wn.synset("catsup.n.01")],

	# tomato sauce
	"U+38ce":	[wn.synset("tomato_sauce.n.01")],

	# fisherman
	"U+38cf":	[wn.synset("fisherman.n.01")],

	# quarter, one quarter quarter
	"U+38d0":	[wn.synset("one-fourth.n.01")],

	# ironing board
	"U+38d2":	[wn.synset("ironing_board.n.01")],

	# turtle, tortoise
	"U+38d3":	[wn.synset("turtle.n.02")],

	# square
	"U+38d5":	[wn.synset("hearty.s.02"),
				wn.synset("square.a.01"),
				wn.synset("square.s.04"),
				wn.synset("square.s.05"),
				wn.synset("square.s.06"),
				wn.synset("straight.a.06")],

	# Tyrannosaurus Rex
	"U+38d6":	[wn.synset("tyrannosaur.n.01")],

	# dinosaur
	"U+38d7":	[wn.synset("dinosaur.n.01")],

	# receipt
	"U+38d8":	[wn.synset("prescription.n.01"),
				wn.synset("receipt.n.02"),
				wn.synset("reception.n.04"),
				wn.synset("recipe.n.01"),
				wn.synset("remedy.n.02")],

	# woodcraft
	"U+38d9":	[wn.synset("carpentry.n.01"),
				wn.synset("woodcraft.n.01"),
				wn.synset("woodcraft.n.02")],

	# craft
	"U+38da":	[wn.synset("craft.n.02"),
				wn.synset("craft.n.03"),
				wn.synset("craft.n.04"),
				wn.synset("craft.n.05"),
				wn.synset("trade.n.02")],

	# district, neighbourhood, city district
	"U+38dc":	[wn.synset("district.n.01"),
				wn.synset("neighborhood.n.02"),
				wn.synset("vicinity.n.01")],

	# city, metropolis
	"U+38dd":	[wn.synset("city.n.01")],

	# airforce, air force force
	"U+38de":	[wn.synset("air_force.n.01")],

	# examination, investigation
	"U+38df":	[wn.synset("examen.n.01"),
				wn.synset("examination.n.01"),
				wn.synset("examination.n.02"),
				wn.synset("examination.n.05"),
				wn.synset("interrogation.n.03"),
				wn.synset("investigation.n.02"),
				wn.synset("probe.n.01")],

	# fundamental law
	"U+38e1":	[wn.synset("fundamental_law.n.01")],

	# law, The Law Law
	"U+38e2":	[wn.synset("law.n.01"),
				wn.synset("law.n.02"),
				wn.synset("law.n.03"),
				wn.synset("law.n.04")],

	# fundamental, basic
	"U+38e3":	[wn.synset("basic.a.01"),
				wn.synset("basic.s.02"),
				wn.synset("basic.s.03"),
				wn.synset("basic.s.04"),
				wn.synset("cardinal.s.01"),
				wn.synset("fundamental.s.02"),
				wn.synset("fundamental.s.03")],

	# internet
	"U+38e4":	[wn.synset("internet.n.01")],

	# Saturn
	"U+38e6":	[wn.synset("saturn.n.01")],

	# gas planet
	"U+38e7":	[wn.synset("planet.n.01")],

	# barber, hairdresser
	"U+38e8":	[wn.synset("barber.n.02")],

	# inhaler
	"U+38ea":	[wn.synset("inhaler.n.01")],

	# breath
	"U+38ec":	[wn.synset("breath.n.01"),
				wn.synset("breath.n.02")],

	# pennywhistle, tin whistle whistle
	"U+38ed":	[wn.synset("pennywhistle.n.01")],

	# soprano
	"U+38ef":	[wn.synset("soprano.n.01")],

	# South Africa
	"U+38f0":	[wn.synset("south_africa.n.01")],

	# springbok
	"U+38f1":	[wn.synset("gazelle.n.01"),
				wn.synset("springbok.n.01")],

	# ostrich
	"U+38f2":	[wn.synset("ostrich.n.02")],

	# aboard, on board board
	"U+38f3":	[wn.synset("aboard.r.01"),
				wn.synset("aboard.r.02"),
				wn.synset("aboard.r.03"),
				wn.synset("aboard.r.04"),
				wn.synset("piggyback.r.01")],

	# Brazil
	"U+38f5":	[wn.synset("brazil.n.01")],

	# intuition
	"U+38f6":	[wn.synset("intuition.n.01"),
				wn.synset("intuition.n.02")],

	# audiologist
	"U+38f7":	[wn.synset("audiology.n.01")],

	# therapist
	"U+38f8":	[wn.synset("therapist.n.01")],

	# track
	"U+38fa":	[wn.synset("cut.n.08"),
				wn.synset("lead.n.03"),
				wn.synset("path.n.04"),
				wn.synset("racetrack.n.01"),
				wn.synset("track.n.03"),
				wn.synset("track.n.06"),
				wn.synset("track.n.07"),
				wn.synset("track.n.08"),
				wn.synset("track.n.09"),
				wn.synset("track.n.10"),
				wn.synset("track.n.11")],

	# train
	"U+38fb":	[wn.synset("train.n.01")],

	# ATM, cash machine machine
	"U+38fc":	[wn.synset("asynchronous_transfer_mode.n.01"),
				wn.synset("cash_machine.n.01"),
				wn.synset("standard_atmosphere.n.01")],

	# pushboat
	"U+38fe":	[wn.synset("tugboat.n.01")],

	# cloakroom, walk in closet-in closet
	"U+3902":	[wn.synset("cloakroom.n.02")],

	# habitation, dwelling place, site
	"U+3903":	[wn.synset("dwelling.n.01"),
				wn.synset("habitation.n.01"),
				wn.synset("inhabitancy.n.01"),
				wn.synset("site.n.01"),
				wn.synset("site.n.02"),
				wn.synset("web_site.n.01")],

	# live, dwell, reside
	"U+3904":	[wn.synset("populate.v.01")],

	# hard rock
	"U+3905":	[wn.synset("rock_'n'_roll.n.01")],

	# town, city
	"U+3906":	[wn.synset("city.n.01")],

	# goldfish, guppy, pet fish fish
	"U+3908":	[wn.synset("goldfish.n.01"),
				wn.synset("guppy.n.01")],

	# Monday
	"U+3909":	[wn.synset("monday.n.01")],

	# bite
	"U+390b":	[wn.synset("bite.v.01")],

	# point, indicate, tip, peak
	"U+390c":	[wn.synset("acme.n.01"),
				wn.synset("bill.n.09"),
				wn.synset("compass_point.n.01"),
				wn.synset("decimal_point.n.01"),
				wn.synset("degree.n.02"),
				wn.synset("detail.n.01"),
				wn.synset("distributor_point.n.01"),
				wn.synset("extremum.n.02"),
				wn.synset("flower.n.03"),
				wn.synset("gratuity.n.01"),
				wn.synset("item.n.01"),
				wn.synset("peak.n.04"),
				wn.synset("period.n.07"),
				wn.synset("point.n.01"),
				wn.synset("point.n.02"),
				wn.synset("point.n.03"),
				wn.synset("point.n.06"),
				wn.synset("point.n.07"),
				wn.synset("point.n.08"),
				wn.synset("point.n.09"),
				wn.synset("point.n.10"),
				wn.synset("point.n.11"),
				wn.synset("point.n.13"),
				wn.synset("point.n.14"),
				wn.synset("point.n.15"),
				wn.synset("point.n.17"),
				wn.synset("point.n.18"),
				wn.synset("point.n.20"),
				wn.synset("point.n.22"),
				wn.synset("point.n.23"),
				wn.synset("point.n.24"),
				wn.synset("point.n.25"),
				wn.synset("tip.n.01"),
				wn.synset("tip.n.03"),
				wn.synset("vertex.n.02")],

	# filled, stuffed
	"U+390e":	[wn.synset("filled.a.02"),
				wn.synset("filled.s.01"),
				wn.synset("filled.s.03"),
				wn.synset("stuffed.s.01"),
				wn.synset("stuffed.s.02")],

	# filling, fill, fullness
	"U+390f":	[wn.synset("comprehensiveness.n.01"),
				wn.synset("fill.n.01"),
				wn.synset("filling.n.01"),
				wn.synset("filling.n.02"),
				wn.synset("filling.n.03"),
				wn.synset("filling.n.05"),
				wn.synset("filling.n.06"),
				wn.synset("fullness.n.02"),
				wn.synset("fullness.n.03"),
				wn.synset("fullness.n.04"),
				wn.synset("woof.n.01")],

	# paper money, bill
	"U+3910":	[wn.synset("bill.n.03")],

	# drugstore, pharmacy
	"U+3911":	[wn.synset("drugstore.n.01")],

	# baking tin, baking pan, ovenware
	"U+3912":	[wn.synset("ovenware.n.01")],

	# starfish
	"U+3914":	[wn.synset("starfish.n.01")],

	# water creature
	"U+3915":	[wn.synset("marine_animal.n.01")],

	# man made item, artefact, artifact, product
	"U+3917":	[wn.synset("artifact.n.01"),
				wn.synset("intersection.n.04"),
				wn.synset("merchandise.n.01"),
				wn.synset("product.n.02"),
				wn.synset("product.n.03"),
				wn.synset("product.n.04"),
				wn.synset("product.n.05")],

	# making, production, fashioning
	"U+3918":	[wn.synset("production.n.02"),
				wn.synset("production.n.07")],

	# boyfriend
	"U+391b":	[wn.synset("boyfriend.n.01")],

	# iceberg
	"U+391c":	[wn.synset("iceberg.n.01")],

	# delicious, scrumptious, yummy
	"U+391d":	[wn.synset("delectable.s.01"),
				wn.synset("delightful.s.01")],

	# tasty, good, appetizing
	"U+391e":	[wn.synset("adept.s.01"),
				wn.synset("appetizing.a.01"),
				wn.synset("beneficial.s.01"),
				wn.synset("dear.s.02"),
				wn.synset("dependable.s.04"),
				wn.synset("effective.s.04"),
				wn.synset("estimable.s.02"),
				wn.synset("full.s.06"),
				wn.synset("good.a.01"),
				wn.synset("good.a.03"),
				wn.synset("good.s.06"),
				wn.synset("good.s.07"),
				wn.synset("good.s.09"),
				wn.synset("good.s.12"),
				wn.synset("good.s.13"),
				wn.synset("good.s.15"),
				wn.synset("good.s.16"),
				wn.synset("good.s.17"),
				wn.synset("good.s.18"),
				wn.synset("good.s.19"),
				wn.synset("good.s.20"),
				wn.synset("good.s.21"),
				wn.synset("tasty.a.01")],

	# summary, abstract
	"U+3920":	[wn.synset("summary.n.01")],

	# shiny, glossy
	"U+3922":	[wn.synset("bright.s.05"),
				wn.synset("glazed.a.03"),
				wn.synset("glistening.s.01"),
				wn.synset("glossy.s.01"),
				wn.synset("glossy.s.03")],

	# shine, beam
	"U+3923":	[wn.synset("glitter.v.01")],

	# medical treatment, medical care
	"U+3924":	[wn.synset("checkup.n.01"),
				wn.synset("treatment.n.02")],

	# janitor, caretaker
	"U+3925":	[wn.synset("caretaker.n.01"),
				wn.synset("caretaker.n.02"),
				wn.synset("janitor.n.01")],

	# see, look, watch, wristwatch
	"U+3926":	[wn.synset("see.v.01")],

	# discussion, conversation, debate, chat
	"U+3927":	[wn.synset("discussion.n.02")],

	# sad, sadly, unhappily, unhappy
	"U+3928":	[wn.synset("sad.a.01")],

	# say, speak, talk, tell, express
	"U+3929":	[wn.synset("speak.v.03"),
				wn.synset("talk.v.01"),
				wn.synset("talk.v.02")],

	# sap
	"U+392a":	[wn.synset("blackjack.n.02"),
				wn.synset("fool.n.01"),
				wn.synset("sap.n.01")],

	# flavouring, condiment, seasoning
	"U+392b":	[wn.synset("flavorer.n.01")],

	# handmade object, handicraft
	"U+392c":	[wn.synset("handicraft.n.01"),
				wn.synset("handicraft.n.02")],

	# handmade figure, handicraft
	"U+392d":	[wn.synset("handicraft.n.01"),
				wn.synset("handicraft.n.02")],

	# wink, blink
	"U+392e":	[wn.synset("blink.v.01"),
				wn.synset("flash.v.01"),
				wn.synset("wink.v.01"),
				wn.synset("wink.v.04")],

	# Jewish
	"U+392f":	[wn.synset("jewish.a.01")],

	# Tishri
	"U+3931":	[wn.synset("tishri.n.01")],

	# shofar
	"U+3932":	[wn.synset("shofar.n.01")],

	# zoo
	"U+3933":	[wn.synset("menagerie.n.02")],

	# portability
	"U+3934":	[wn.synset("portability.n.01")],

	# printer, typewriter
	"U+3936":	[wn.synset("printer.n.02")],

	# two storey building
	"U+3937":	[wn.synset("building.n.01")],

	# crochet
	"U+3938":	[wn.synset("crochet.v.01"),
				wn.synset("crochet.v.02")],

	# hook, hanger
	"U+3939":	[wn.synset("hook.n.05")],

	# kneeling
	"U+393a":	[wn.synset("kneel.n.01")],

	# sacrament of baptism
	"U+393b":	[wn.synset("baptism.n.01"),
				wn.synset("baptize.v.01"),
				wn.synset("christening.n.01"),
				wn.synset("dub.v.01"),
				wn.synset("name.v.01")],

	# sacrament
	"U+393c":	[wn.synset("sacrament.n.01")],

	# sale
	"U+393d":	[wn.synset("sale.n.01"),
				wn.synset("sale.n.05")],

	# salt
	"U+393f":	[wn.synset("salt.n.02")],

	# bright
	"U+3941":	[wn.synset("bright.a.01"),
				wn.synset("bright.s.02"),
				wn.synset("bright.s.03"),
				wn.synset("bright.s.04"),
				wn.synset("bright.s.05"),
				wn.synset("bright.s.06"),
				wn.synset("bright.s.08"),
				wn.synset("bright.s.09"),
				wn.synset("bright.s.10"),
				wn.synset("satiny.s.01"),
				wn.synset("undimmed.a.01")],

	# smart, bright, clever, intelligent
	"U+3942":	[wn.synset("intelligent.a.01")],

	# smartness, brightness, cleverness, intelligence
	"U+3943":	[wn.synset("able.a.01"),
				wn.synset("alacrity.n.01"),
				wn.synset("brainy.s.01"),
				wn.synset("brightness.n.01"),
				wn.synset("brightness.n.02"),
				wn.synset("brilliant.s.01"),
				wn.synset("chic.n.01"),
				wn.synset("entertaining.s.01"),
				wn.synset("ingenuity.n.02"),
				wn.synset("intelligence.n.01"),
				wn.synset("intelligence.n.02"),
				wn.synset("intelligence.n.03"),
				wn.synset("intelligence.n.05"),
				wn.synset("intelligent.a.01"),
				wn.synset("inventiveness.n.01"),
				wn.synset("luminosity.n.01"),
				wn.synset("news.n.01"),
				wn.synset("smart.n.01")],

	# fiber, fibre, fibril, filament, strand
	"U+3949":	[wn.synset("fiber.n.01")],

	# slow, slowly
	"U+394b":	[wn.synset("slow.a.01")],

	# spill, slop
	"U+394c":	[wn.synset("spill.v.02")],

	# dirt, soil
	"U+394d":	[wn.synset("crap.n.01"),
				wn.synset("dirt.n.02"),
				wn.synset("land.n.02"),
				wn.synset("scandal.n.01"),
				wn.synset("soil.n.02"),
				wn.synset("territory.n.03")],

	# day before holiday
	"U+394e":	[wn.synset("eve.n.02"),
				wn.synset("eve.n.03")],

	# Tarzan
	"U+394f":	[wn.synset("tarzan.n.01"),
				wn.synset("tarzan.n.02")],

	# liberation
	"U+3952":	[wn.synset("liberation.n.01")],

	# field hockey, hockey
	"U+3953":	[wn.synset("field_hockey.n.01")],

	# dressing gown, housecoat, robe
	"U+3955":	[wn.synset("dressing_gown.n.01"),
				wn.synset("gown.n.05"),
				wn.synset("negligee.n.01"),
				wn.synset("robe.n.01")],

	# cleaning cloth
	"U+3956":	[wn.synset("dishrag.n.01"),
				wn.synset("dishtowel.n.01"),
				wn.synset("rag.n.01")],

	# helper, aide, assistant, personal assistant assistant
	"U+3958":	[wn.synset("assistant.n.01")],

	# freezing, hardening, solidifying
	"U+3959":	[wn.synset("freeze.n.01"),
				wn.synset("hardening.n.01"),
				wn.synset("hardening.n.02"),
				wn.synset("hardening.n.03")],

	# rule, regulation
	"U+3960":	[wn.synset("rule.n.01")],

	# swimming, swim
	"U+3962":	[wn.synset("swimming.n.01")],

	# artist
	"U+3963":	[wn.synset("artist.n.01")],

	# art
	"U+3964":	[wn.synset("art.n.02")],

	# borrow
	"U+3965":	[wn.synset("adopt.v.02"),
				wn.synset("borrow.v.01"),
				wn.synset("lend.v.02")],

	# snowsuit, winter clothing clothing
	"U+3968":	[wn.synset("snowsuit.n.01")],

	# bindi, tika
	"U+3969":	[wn.synset("bandage.n.01"),
				wn.synset("tie.n.07")],

	# pancake, crepe, tortilla
	"U+396a":	[wn.synset("pancake.n.01")],

	# vision, apparition
	"U+396b":	[wn.synset("apparition.n.01"),
				wn.synset("apparition.n.02"),
				wn.synset("apparition.n.03"),
				wn.synset("sight.n.03"),
				wn.synset("vision.n.01"),
				wn.synset("vision.n.05")],

	# supernatural
	"U+396c":	[wn.synset("supernatural.a.01")],

	# sight, vision, visual sense sense
	"U+396d":	[wn.synset("sight.n.03")],

	# masseur
	"U+3970":	[wn.synset("massager.n.01"),
				wn.synset("masseur.n.01")],

	# diver
	"U+3972":	[wn.synset("diver.n.01"),
				wn.synset("diver.n.02"),
				wn.synset("loon.n.02")],

	# diving, activity under water under water
	"U+3973":	[wn.synset("dive.n.02"),
				wn.synset("diving.n.01")],

	# reading
	"U+3975":	[wn.synset("interpretation.n.01"),
				wn.synset("reading.n.01"),
				wn.synset("reading.n.02"),
				wn.synset("reading.n.03"),
				wn.synset("reading.n.04"),
				wn.synset("reading.n.06"),
				wn.synset("reading.n.08"),
				wn.synset("recitation.n.02")],

	# towboat, tugboat
	"U+3976":	[wn.synset("tugboat.n.01")],

	# fundamental rule
	"U+3977":	[wn.synset("constitution.n.02"),
				wn.synset("constitution.n.04"),
				wn.synset("fundamental_law.n.01")],

	# lamb, mutton
	"U+3978":	[wn.synset("mouton.n.01")],

	# sheep
	"U+3979":	[wn.synset("sheep.n.01")],

	# drug dependency
	"U+397a":	[wn.synset("drug_addiction.n.01")],

	# drug, mind altering drug-altering drug
	"U+397c":	[wn.synset("drug.n.01")],

	# rickshaw
	"U+397d":	[wn.synset("jinrikisha.n.01")],

	# Thai
	"U+397e":	[wn.synset("thai.n.02")],

	# Thailand
	"U+397f":	[wn.synset("thailand.n.01")],

	# Bible
	"U+3980":	[wn.synset("bible.n.01")],

	# holy book
	"U+3981":	[wn.synset("bible.n.01"),
				wn.synset("bible.n.02")],

	# bicycle helmet, crash helmet
	"U+3982":	[wn.synset("helmet.n.02")],

	# helmet
	"U+3983":	[wn.synset("helmet.n.02")],

	# vertical
	"U+3984":	[wn.synset("handstand.n.01"),
				wn.synset("headstand.n.01"),
				wn.synset("upright.n.01"),
				wn.synset("vertical.n.01")],

	# spark
	"U+3985":	[wn.synset("spark.n.06")],

	# flame
	"U+3986":	[wn.synset("fire.n.03")],

	# defend, legal)
	"U+3987":	[wn.synset("defend.v.03"),
				wn.synset("defend.v.06")],

	# defence
	"U+3988":	[wn.synset("defense.n.01"),
				wn.synset("defense.n.02"),
				wn.synset("defense.n.04"),
				wn.synset("defense.n.07"),
				wn.synset("defense.n.09"),
				wn.synset("defensive_structure.n.01")],

	# mane
	"U+3989":	[wn.synset("man.n.01"),
				wn.synset("mane.n.01"),
				wn.synset("mane.n.02")],

	# credit card
	"U+398b":	[wn.synset("credit_card.n.01")],

	# credit
	"U+398c":	[wn.synset("credit.n.02")],

	# designer, planner
	"U+398e":	[wn.synset("architect.n.01"),
				wn.synset("couturier.n.01"),
				wn.synset("designer.n.04"),
				wn.synset("graphic_designer.n.01"),
				wn.synset("interior_designer.n.01"),
				wn.synset("planner.n.01"),
				wn.synset("planner.n.02")],

	# ophthalmologist, oculist
	"U+3990":	[wn.synset("ophthalmologist.n.01")],

	# homosexuality, lesbianism
	"U+3991":	[wn.synset("homosexuality.n.01")],

	# couple
	"U+3992":	[wn.synset("couple.n.01")],

	# slip, petticoat, half slip, underskirt
	"U+3993":	[wn.synset("petticoat.n.01")],

	# dress, wear
	"U+3994":	[wn.synset("break.v.42"),
				wn.synset("dress.v.01"),
				wn.synset("dress.v.02"),
				wn.synset("dress.v.03"),
				wn.synset("dress.v.04"),
				wn.synset("dress.v.06"),
				wn.synset("dress.v.07"),
				wn.synset("dress.v.09"),
				wn.synset("dress.v.10"),
				wn.synset("dress.v.12"),
				wn.synset("dress.v.13"),
				wn.synset("dress.v.14"),
				wn.synset("dress.v.15"),
				wn.synset("dress.v.16"),
				wn.synset("preen.v.03"),
				wn.synset("snip.v.02"),
				wn.synset("tire.v.02"),
				wn.synset("trim.v.06"),
				wn.synset("wear.v.01"),
				wn.synset("wear.v.02"),
				wn.synset("wear.v.03"),
				wn.synset("wear.v.04"),
				wn.synset("wear.v.05"),
				wn.synset("wear.v.06"),
				wn.synset("wear.v.09")],

	# boar
	"U+3995":	[wn.synset("boar.n.02"),
				wn.synset("wild_boar.n.01")],

	# boss, supervisor
	"U+3996":	[wn.synset("foreman.n.01")],

	# stretch
	"U+3997":	[wn.synset("elongate.v.01"),
				wn.synset("stretch.v.02"),
				wn.synset("unfold.v.03")],

	# vacation, holiday
	"U+3999":	[wn.synset("holiday.n.02"),
				wn.synset("vacation.n.01"),
				wn.synset("vacation.n.02")],

	# unemployment
	"U+399a":	[wn.synset("unemployment.n.01")],

	# singalong
	"U+399b":	[wn.synset("singalong.n.01")],

	# song
	"U+399c":	[wn.synset("song.n.01")],

	# carve
	"U+399d":	[wn.synset("carve.v.01")],

	# mountain climbing
	"U+399e":	[wn.synset("mountain_climbing.n.01")],

	# clerk, legal aid aid
	"U+39a0":	[wn.synset("clerk.n.01"),
				wn.synset("salesclerk.n.01")],

	# Joseph, Saint Joseph Joseph
	"U+39a1":	[wn.synset("joseph.n.02"),
				wn.synset("joseph.n.03")],

	# newspaper, bulletin, newsletter
	"U+39a3":	[wn.synset("newspaper.n.01"),
				wn.synset("newspaper.n.02"),
				wn.synset("newspaper.n.03")],

	# girth, cinch
	"U+39a4":	[wn.synset("cinch.n.02")],

	# canoe
	"U+39a5":	[wn.synset("canoe.n.01")],

	# touch screen
	"U+39a6":	[wn.synset("touch_screen.n.01")],

	# computer screen, monitor
	"U+39a7":	[wn.synset("monitor.n.04")],

	# engaged
	"U+39a9":	[wn.synset("booked.s.01"),
				wn.synset("boyfriend.n.01"),
				wn.synset("busy.s.05"),
				wn.synset("engaged.s.01"),
				wn.synset("engaged.s.02"),
				wn.synset("engaged.s.05"),
				wn.synset("engaged.s.06"),
				wn.synset("engaged.s.07")],

	# technology
	"U+39aa":	[wn.synset("engineering.n.02"),
				wn.synset("technology.n.01")],

	# cafe, coffee house, snack bar
	"U+39ad":	[wn.synset("cafe.n.01")],

	# snack
	"U+39ae":	[wn.synset("bite.n.04")],

	# hearing impaired, hearing-impaired
	"U+39af":	[wn.synset("hard-of-hearing.s.01")],

	# gelding
	"U+39b1":	[wn.synset("gelding.n.01")],

	# stallion, entire
	"U+39b2":	[wn.synset("stallion.n.01")],

	# I, me, myself
	"U+39b4":	[wn.synset("ego.n.03"),
				wn.synset("i.n.03"),
				wn.synset("one.n.01")],

	# deflate, let out air out air
	"U+39b6":	[wn.synset("deflate.v.01"),
				wn.synset("deflate.v.02"),
				wn.synset("deflate.v.03"),
				wn.synset("deflate.v.04"),
				wn.synset("deflate.v.05"),
				wn.synset("deflate.v.06"),
				wn.synset("leak.v.03")],

	# cheers
	"U+39b7":	[wn.synset("cheer.n.01"),
				wn.synset("cheerfulness.n.01")],

	# teetotalism
	"U+39b8":	[wn.synset("abstinence.n.01"),
				wn.synset("teetotaling.n.01")],

	# alcohol, ethanol
	"U+39b9":	[wn.synset("alcohol.n.01")],

	# Loki
	"U+39bb":	[wn.synset("loki.n.01")],

	# lie
	"U+39bc":	[wn.synset("lie.n.01")],

	# veal
	"U+39bd":	[wn.synset("veal.n.01")],

	# summer
	"U+39c1":	[wn.synset("summer.n.01")],

	# creature, being
	"U+39c2":	[wn.synset("animal.n.01"),
				wn.synset("being.n.01"),
				wn.synset("creature.n.02")],

	# steamer
	"U+39c3":	[wn.synset("soft-shell_clam.n.01"),
				wn.synset("soft-shell_clam.n.02"),
				wn.synset("steamer.n.02"),
				wn.synset("steamer.n.03")],

	# disperse, disseminate, scatter, spread
	"U+39c4":	[wn.synset("disperse.v.02"),
				wn.synset("spread.v.02"),
				wn.synset("spread.v.07")],

	# dispersion, dissemination, scattering, spread, spreading
	"U+39c5":	[wn.synset("banquet.n.02"),
				wn.synset("bedspread.n.01"),
				wn.synset("dispersion.n.01"),
				wn.synset("dispersion.n.03"),
				wn.synset("dissemination.n.01"),
				wn.synset("dissemination.n.02"),
				wn.synset("distribution.n.02"),
				wn.synset("gap.n.01"),
				wn.synset("ranch.n.01"),
				wn.synset("scatter.n.01"),
				wn.synset("scatter.n.02"),
				wn.synset("scattering.n.01"),
				wn.synset("scattering.n.02"),
				wn.synset("scattering.n.03"),
				wn.synset("spread.n.01"),
				wn.synset("spread.n.05"),
				wn.synset("spread.n.07"),
				wn.synset("spread.n.08"),
				wn.synset("spread.n.10")],

	# mandolin
	"U+39c9":	[wn.synset("mandolin.n.01")],

	# continuance, continuation
	"U+39cd":	[wn.synset("continuance.n.01"),
				wn.synset("duration.n.01"),
				wn.synset("duration.n.02"),
				wn.synset("good_continuation.n.01"),
				wn.synset("lengthiness.n.02"),
				wn.synset("sequel.n.02")],

	# dart
	"U+39ce":	[wn.synset("dart.n.01"),
				wn.synset("dart.n.02"),
				wn.synset("flit.n.01")],

	# dark
	"U+39cf":	[wn.synset("dark.a.01"),
				wn.synset("dark.a.02"),
				wn.synset("dark.s.06"),
				wn.synset("dark.s.08")],

	# traffic
	"U+39d0":	[wn.synset("traffic.n.01")],

	# bandage, dressing
	"U+39d1":	[wn.synset("bandage.n.01")],

	# dare
	"U+39d4":	[wn.synset("dare.v.02"),
				wn.synset("defy.v.03"),
				wn.synset("make_bold.v.01")],

	# brave, courageous
	"U+39d5":	[wn.synset("brave.a.01")],

	# fiance, groom to be-to-be
	"U+39d7":	[wn.synset("fiance.n.01")],

	# oyster, clam
	"U+39d8":	[wn.synset("oyster.n.01")],

	# stranger, unknown
	"U+39da":	[wn.synset("stranger.n.01"),
				wn.synset("stranger.n.02"),
				wn.synset("unknown.n.01"),
				wn.synset("unknown.n.03")],

	# strange
	"U+39db":	[wn.synset("strange.a.01"),
				wn.synset("strange.s.02")],

	# Halloween, All Saint's Day Saint's Day
	"U+39dc":	[wn.synset("halloween.n.01")],

	# ghost, phantom
	"U+39dd":	[wn.synset("apparition.n.01"),
				wn.synset("apparition.n.03"),
				wn.synset("ghost.n.01"),
				wn.synset("ghost.n.03"),
				wn.synset("ghostwriter.n.01"),
				wn.synset("touch.n.03")],

	# tsunami
	"U+39df":	[wn.synset("tsunami.n.01")],

	# metal craft
	"U+39e2":	[wn.synset("metalworking.n.01")],

	# applaud, clap
	"U+39e3":	[wn.synset("applaud.v.01"),
				wn.synset("applaud.v.02")],

	# applause, clapping
	"U+39e4":	[wn.synset("applause.n.01")],

	# meeting room, auditorium
	"U+39e5":	[wn.synset("auditorium.n.01")],

	# pickled
	"U+39e8":	[wn.synset("acerb.s.01"),
				wn.synset("bitter.s.06"),
				wn.synset("cutting.s.03"),
				wn.synset("pickled.s.01"),
				wn.synset("unpalatable.a.01")],

	# sharp, acid, sour
	"U+39e9":	[wn.synset("abrupt.s.03"),
				wn.synset("acerb.s.02"),
				wn.synset("acid.s.03"),
				wn.synset("acidic.s.02"),
				wn.synset("acuate.s.01"),
				wn.synset("acute.s.03"),
				wn.synset("astute.s.01"),
				wn.synset("crisp.s.01"),
				wn.synset("dark.s.06"),
				wn.synset("false.s.08"),
				wn.synset("off.s.04"),
				wn.synset("sharp.a.08"),
				wn.synset("sharp.a.09"),
				wn.synset("sharp.a.10"),
				wn.synset("sharp.s.05"),
				wn.synset("sharp.s.11"),
				wn.synset("sharp.s.12"),
				wn.synset("shrill.s.01"),
				wn.synset("sour.a.02"),
				wn.synset("sour.s.01"),
				wn.synset("sour.s.03")],

	# lava, magma
	"U+39ea":	[wn.synset("lava.n.01")],

	# wireless connection, WiFi
	"U+39eb":	[wn.synset("wireless_local_area_network.n.01")],

	# lobster
	"U+39ed":	[wn.synset("lobster.n.01"),
				wn.synset("lobster.n.02")],

	# big, large
	"U+39ef":	[wn.synset("large.a.01")],

	# noon
	"U+39f0":	[wn.synset("noon.n.01")],

	# hour, o'clock'clock
	"U+39f1":	[wn.synset("hour.n.01"),
				wn.synset("hour.n.02")],

	# tuba
	"U+39f3":	[wn.synset("bass_horn.n.01")],

	# trumpet, horn, cornet
	"U+39f4":	[wn.synset("cornet.n.01"),
				wn.synset("horn.n.02"),
				wn.synset("horn.n.06"),
				wn.synset("horn.n.07")],

	# bass
	"U+39f6":	[wn.synset("bass.n.03"),
				wn.synset("bass.n.06"),
				wn.synset("bass.n.07")],

	# no speech, anarthria
	"U+39f7":	[wn.synset("anarthria.n.01")],

	# control
	"U+39f9":	[wn.synset("command.n.06"),
				wn.synset("control.n.01"),
				wn.synset("control.n.02"),
				wn.synset("control.n.03"),
				wn.synset("control.n.05"),
				wn.synset("dominance.n.02"),
				wn.synset("restraint.n.02")],

	# intimate, close, enclose, shut
	"U+39fa":	[wn.synset("close.v.01")],

	# intimacy, closeness
	"U+39fb":	[wn.synset("affair.n.02"),
				wn.synset("closeness.n.01"),
				wn.synset("familiarity.n.03")],

	# balance, poise, sense of balance of balance, standing)
	"U+39fc":	[wn.synset("proportion.n.05")],

	# fall, drop, spill, tumble
	"U+39fd":	[wn.synset("drop.n.06"),
				wn.synset("fall.n.05"),
				wn.synset("fall.n.06"),
				wn.synset("spill.n.04")],

	# leadership, guidance
	"U+39fe":	[wn.synset("leadership.n.01")],

	# side
	"U+3a00":	[wn.synset("english.n.04"),
				wn.synset("side.n.01"),
				wn.synset("side.n.02"),
				wn.synset("side.n.03"),
				wn.synset("side.n.04"),
				wn.synset("side.n.05"),
				wn.synset("side.n.06"),
				wn.synset("side.n.07"),
				wn.synset("side.n.08"),
				wn.synset("side.n.09"),
				wn.synset("side.n.10"),
				wn.synset("slope.n.01")],

	# do, act
	"U+3a04":	[wn.synset("act.v.01"),
				wn.synset("perform.v.01")],

	# mean, cruel, signify
	"U+3a05":	[wn.synset("average.s.01"),
				wn.synset("barbarous.s.01"),
				wn.synset("base.s.05"),
				wn.synset("bastardly.s.02"),
				wn.synset("beggarly.s.01"),
				wn.synset("beggarly.s.02"),
				wn.synset("hateful.s.02"),
				wn.synset("mean.s.04"),
				wn.synset("mean.s.06")],

	# curling
	"U+3a06":	[wn.synset("curling.n.01")],

	# burning
	"U+3a07":	[wn.synset("burning.s.01")],

	# picture, image, icon, painting
	"U+3a08":	[wn.synset("painting.n.01")],

	# man doll
	"U+3a09":	[wn.synset("doll.n.01")],

	# apologize, apologise, regret
	"U+3a0a":	[wn.synset("apologize.v.01"),
				wn.synset("apologize.v.02"),
				wn.synset("regret.v.02"),
				wn.synset("regret.v.03"),
				wn.synset("regret.v.04"),
				wn.synset("repent.v.02")],

	# racket, racquet
	"U+3a0d":	[wn.synset("racket.n.04")],

	# can opener
	"U+3a0e":	[wn.synset("can_opener.n.01")],

	# opener
	"U+3a0f":	[wn.synset("opener.n.01"),
				wn.synset("opener.n.03"),
				wn.synset("undoer.n.02")],

	# can, tin, jar, be able able
	"U+3a10":	[wn.synset("can.n.01")],

	# harpsichord
	"U+3a11":	[wn.synset("harpsichord.n.01")],

	# hen
	"U+3a12":	[wn.synset("hen.n.01")],

	# chicken, poultry
	"U+3a13":	[wn.synset("chicken.n.01"),
				wn.synset("chicken.n.02"),
				wn.synset("chicken.n.04"),
				wn.synset("wimp.n.01")],

	# finish, complete
	"U+3a15":	[wn.synset("complete.v.01"),
				wn.synset("complete.v.02"),
				wn.synset("complete.v.04"),
				wn.synset("complete.v.05"),
				wn.synset("dispatch.v.02"),
				wn.synset("eat_up.v.01"),
				wn.synset("end.v.01"),
				wn.synset("end.v.02"),
				wn.synset("finish.v.04"),
				wn.synset("finish.v.06"),
				wn.synset("finish_up.v.02")],

	# finished, complete, completed
	"U+3a17":	[wn.synset("complete.s.05")],

	# cake, bread with sugar with sugar
	"U+3a18":	[wn.synset("cake.n.03")],

	# game
	"U+3a1a":	[wn.synset("game.n.01"),
				wn.synset("game.n.02"),
				wn.synset("game.n.03")],

	# takeoff, take off, airplane take off
	"U+3a1b":	[wn.synset("parody.n.01"),
				wn.synset("parody.n.02"),
				wn.synset("takeoff.n.01"),
				wn.synset("takeoff.n.02")],

	# camper, caravan, mobile home home
	"U+3a1c":	[wn.synset("van.n.04")],

	# anti virus program, anti-virus program
	"U+3a1d":	[wn.synset("anti-virus_program.n.01")],

	# beautiful, attractive, good looking, handsome, pretty-looking
	"U+3a1f":	[wn.synset("beautiful.a.01")],

	# hurry, rush, hurried, rushed
	"U+3a20":	[wn.synset("haste.n.01"),
				wn.synset("haste.n.02"),
				wn.synset("hurry.n.01")],

	# rags
	"U+3a21":	[wn.synset("rag.n.01"),
				wn.synset("rag.n.02"),
				wn.synset("rag.n.05"),
				wn.synset("ragtime.n.01"),
				wn.synset("tabloid.n.02")],

	# usage, use
	"U+3a22":	[wn.synset("custom.n.01"),
				wn.synset("use.n.01"),
				wn.synset("use.n.03")],

	# dirty, soiled
	"U+3a23":	[wn.synset("dirty.a.01")],

	# agree
	"U+3a24":	[wn.synset("agree.v.01"),
				wn.synset("agree.v.02"),
				wn.synset("agree.v.05"),
				wn.synset("agree.v.06"),
				wn.synset("agree.v.07"),
				wn.synset("harmonize.v.01"),
				wn.synset("match.v.01")],

	# gong
	"U+3a25":	[wn.synset("gong.n.01")],

	# fear, fright, concern, be afraid, dread
	"U+3a27":	[wn.synset("fear.n.01")],

	# certain, sure
	"U+3a28":	[wn.synset("certain.a.02"),
				wn.synset("certain.a.03"),
				wn.synset("certain.a.04"),
				wn.synset("certain.s.01"),
				wn.synset("sure.s.04"),
				wn.synset("sure.s.06")],

	# Thursday
	"U+3a29":	[wn.synset("thursday.n.01")],

	# still, calm, peaceful, tranquil, continuously, lull, serene, continuing, ongoing
	"U+3a2b":	[wn.synset("calm.a.02"),
				wn.synset("calm.s.01"),
				wn.synset("passive.s.02"),
				wn.synset("peaceful.a.01"),
				wn.synset("serene.s.02")],

	# chocolate flavouring
	"U+3a2c":	[wn.synset("cacao.n.01"),
				wn.synset("cacao_bean.n.01"),
				wn.synset("cocoa.n.02")],

	# coconut
	"U+3a2d":	[wn.synset("coconut.n.01"),
				wn.synset("coconut.n.02"),
				wn.synset("coconut.n.03")],

	# cream
	"U+3a2e":	[wn.synset("cream.n.01"),
				wn.synset("cream.n.03")],

	# nutcracker
	"U+3a32":	[wn.synset("nutcracker.n.01")],

	# kitchen tool, utensils
	"U+3a33":	[wn.synset("utensil.n.01")],

	# nut
	"U+3a34":	[wn.synset("addict.n.01"),
				wn.synset("crackpot.n.01"),
				wn.synset("en.n.01"),
				wn.synset("nut.n.01"),
				wn.synset("nut.n.02"),
				wn.synset("nut.n.03"),
				wn.synset("testis.n.01")],

	# dense, thick, compact, tight, jammed
	"U+3a36":	[wn.synset("compact.a.01"),
				wn.synset("thick.a.01"),
				wn.synset("thick.a.03")],

	# density, denseness, concentration, compactness, tightness
	"U+3a37":	[wn.synset("concentration.n.01"),
				wn.synset("concentration.n.05")],

	# puppy
	"U+3a38":	[wn.synset("puppy.n.02")],

	# bruised, dented
	"U+3a3a":	[wn.synset("bent.s.03"),
				wn.synset("bruise.v.01"),
				wn.synset("bruise.v.03"),
				wn.synset("bruise.v.04"),
				wn.synset("hurt.v.05")],

	# bruise, contusion, haematoma, dent
	"U+3a3b":	[wn.synset("bruise.n.01"),
				wn.synset("dent.n.01"),
				wn.synset("dent.n.03"),
				wn.synset("incision.n.01")],

	# fresh
	"U+3a3d":	[wn.synset("fresh.a.01")],

	# dwarf planet
	"U+3a3e":	[wn.synset("planet.n.01")],

	# planet
	"U+3a3f":	[wn.synset("planet.n.01")],

	# slang
	"U+3a40":	[wn.synset("slang.n.01"),
				wn.synset("slang.n.02")],

	# groom
	"U+3a41":	[wn.synset("dress.v.15"),
				wn.synset("groom.v.03"),
				wn.synset("prepare.v.05")],

	# horse brush, body brush
	"U+3a43":	[wn.synset("currycomb.n.01")],

	# mask, false face face
	"U+3a44":	[wn.synset("mask.n.01")],

	# mash, crush, squeeze, squash, mush, pulp, pumpkin
	"U+3a46":	[wn.synset("crush.v.04"),
				wn.synset("jam.v.03"),
				wn.synset("squash.v.01")],

	# mast
	"U+3a48":	[wn.synset("mast.n.01")],

	# Canada
	"U+3a4b":	[wn.synset("canada.n.01")],

	# flu, influenza
	"U+3a4c":	[wn.synset("influenza.n.01")],

	# motorcycling, motocross
	"U+3a4d":	[wn.synset("motorcycling.n.01")],

	# reflect, consider
	"U+3a4e":	[wn.synset("chew_over.v.01"),
				wn.synset("consider.v.03"),
				wn.synset("consider.v.04"),
				wn.synset("consider.v.05"),
				wn.synset("see.v.05"),
				wn.synset("study.v.03")],

	# reflection, consideration
	"U+3a4f":	[wn.synset("contemplation.n.02")],

	# neigh, whinny
	"U+3a50":	[wn.synset("neigh.v.01")],

	# stop, arrive, end, platform
	"U+3a52":	[wn.synset("discontinue.v.01"),
				wn.synset("stop.v.01")],

	# wart, papilloma
	"U+3a53":	[wn.synset("papilloma.n.01")],

	# stoma, medical hole hole
	"U+3a54":	[wn.synset("fistula.n.02"),
				wn.synset("ostomy.n.01"),
				wn.synset("stoma.n.01"),
				wn.synset("stoma.n.02")],

	# hunt, hunting
	"U+3a55":	[wn.synset("hunt.n.08")],

	# spirit
	"U+3a56":	[wn.synset("heart.n.06"),
				wn.synset("spirit.n.01"),
				wn.synset("spirit.n.02"),
				wn.synset("spirit.n.03"),
				wn.synset("spirit.n.04")],

	# lottery, game of chance of chance
	"U+3a58":	[wn.synset("lottery.n.02")],

	# smile, grin
	"U+3a5a":	[wn.synset("smile.v.01")],

	# appointment
	"U+3a5b":	[wn.synset("date.n.03")],

	# Capricorn
	"U+3a5d":	[wn.synset("capricorn.n.01"),
				wn.synset("capricorn.n.03"),
				wn.synset("capricornus.n.01")],

	# salesperson, shop owner owner
	"U+3a5f":	[wn.synset("salesman.n.01"),
				wn.synset("salesperson.n.01"),
				wn.synset("seller.n.01")],

	# MP3 player, iPod
	"U+3a61":	[wn.synset("ipod.n.01")],

	# electric wire, electric cord, cord, cable, lead
	"U+3a63":	[wn.synset("cable.n.01"),
				wn.synset("cable.n.02"),
				wn.synset("cable.n.03"),
				wn.synset("cable.n.04"),
				wn.synset("cable.n.06"),
				wn.synset("cable_television.n.01"),
				wn.synset("conductor.n.04"),
				wn.synset("cord.n.01"),
				wn.synset("cord.n.02"),
				wn.synset("cord.n.03"),
				wn.synset("cord.n.04"),
				wn.synset("duct.n.01"),
				wn.synset("jumper_cable.n.01"),
				wn.synset("lead.n.01"),
				wn.synset("lead.n.02"),
				wn.synset("lead.n.03"),
				wn.synset("lead.n.04"),
				wn.synset("lead.n.05"),
				wn.synset("lead.n.06"),
				wn.synset("lead.n.07"),
				wn.synset("lead.n.09"),
				wn.synset("lead.n.11"),
				wn.synset("lead.n.14"),
				wn.synset("lead.n.15"),
				wn.synset("lead.n.17"),
				wn.synset("leash.n.01"),
				wn.synset("spark_advance.n.01"),
				wn.synset("star.n.04"),
				wn.synset("tip.n.03")],

	# wire, cable
	"U+3a64":	[wn.synset("cable.n.02"),
				wn.synset("cable.n.04")],

	# underwear, underclothes
	"U+3a65":	[wn.synset("underwear.n.01")],

	# bigness, largeness
	"U+3a66":	[wn.synset("breadth.n.01"),
				wn.synset("largeness.n.02"),
				wn.synset("largeness.n.03"),
				wn.synset("pretentiousness.n.02")],

	# swimsuit, swimwear, bathing suit suit
	"U+3a69":	[wn.synset("swimsuit.n.01")],

	# twin brother
	"U+3a6b":	[wn.synset("counterpart.n.02"),
				wn.synset("twin.n.01")],

	# brother
	"U+3a6c":	[wn.synset("brother.n.01")],

	# beyond, past
	"U+3a6e":	[wn.synset("beyond.r.01"),
				wn.synset("beyond.r.02"),
				wn.synset("beyond.r.03"),
				wn.synset("past.a.01"),
				wn.synset("past.s.02")],

	# ticket, pass
	"U+3a6f":	[wn.synset("ticket.n.01")],

	# vanilla sauce
	"U+3a71":	[wn.synset("vanilla.n.01"),
				wn.synset("vanilla.n.02")],

	# vanilla
	"U+3a72":	[wn.synset("vanilla.n.01"),
				wn.synset("vanilla.n.02"),
				wn.synset("vanilla.n.03")],

	# clock, timepiece
	"U+3a73":	[wn.synset("clock.n.01")],

	# nurse
	"U+3a74":	[wn.synset("nurse.n.01")],

	# contrast
	"U+3a77":	[wn.synset("contrast.v.01"),
				wn.synset("contrast.v.02")],

	# full, satisfied
	"U+3a78":	[wn.synset("broad.s.05"),
				wn.synset("entire.s.01"),
				wn.synset("full.a.01"),
				wn.synset("full.a.05"),
				wn.synset("full.s.03"),
				wn.synset("full.s.04"),
				wn.synset("full.s.06"),
				wn.synset("quenched.s.01"),
				wn.synset("satisfied.s.01"),
				wn.synset("wide.s.06")],

	# empower
	"U+3a79":	[wn.synset("accredit.v.02"),
				wn.synset("authorize.v.01"),
				wn.synset("empower.v.01"),
				wn.synset("endow.v.01"),
				wn.synset("entitle.v.02"),
				wn.synset("mandate.v.03")],

	# empowerment
	"U+3a7a":	[wn.synset("authorization.n.04"),
				wn.synset("mandate.n.01")],

	# Finland
	"U+3a7b":	[wn.synset("finland.n.01")],

	# sauna
	"U+3a7c":	[wn.synset("sauna.n.01")],

	# vomiting, vomit, puking, throw up, puke
	"U+3a7d":	[wn.synset("vomit.n.03")],

	# Latvian
	"U+3a7e":	[wn.synset("latvian.n.02")],

	# Latvia
	"U+3a7f":	[wn.synset("latvia.n.01")],

	# folk tale, legend
	"U+3a81":	[wn.synset("caption.n.03"),
				wn.synset("legend.n.01")],

	# story, historic story, report, tale
	"U+3a82":	[wn.synset("fib.n.01"),
				wn.synset("history.n.02"),
				wn.synset("story.n.02")],

	# criminality, crime
	"U+3a84":	[wn.synset("crime.n.01"),
				wn.synset("crime.n.02")],

	# illegal, criminal
	"U+3a85":	[wn.synset("illegal.a.01")],

	# criminal
	"U+3a86":	[wn.synset("criminal.n.01")],

	# experience
	"U+3a87":	[wn.synset("experience.n.01")],

	# gerbil, guinea pig, hamster
	"U+3a88":	[wn.synset("gerbil.n.01"),
				wn.synset("hamster.n.01")],

	# social
	"U+3a89":	[wn.synset("social.a.01"),
				wn.synset("social.a.02"),
				wn.synset("social.a.03"),
				wn.synset("social.s.04"),
				wn.synset("social.s.05"),
				wn.synset("social.s.06")],

	# society
	"U+3a8a":	[wn.synset("society.n.01")],

	# scepticism, skepticism
	"U+3a8b":	[wn.synset("agnosticism.n.02")],

	# sweetness, sweet
	"U+3a8c":	[wn.synset("dessert.n.01")],

	# spray bottle, vaporizer, spray can
	"U+3a8d":	[wn.synset("atomizer.n.01"),
				wn.synset("vaporizer.n.01")],

	# spray, vaporization, vaporize
	"U+3a8e":	[wn.synset("vaporization.n.01"),
				wn.synset("vaporization.n.02")],

	# period, point, full stop, decimal point
	"U+3a90":	[wn.synset("time_period.n.01")],

	# Scorpio
	"U+3a92":	[wn.synset("scorpio.n.01"),
				wn.synset("scorpio.n.03"),
				wn.synset("scorpion.n.03"),
				wn.synset("scorpius.n.01")],

	# scorpion
	"U+3a93":	[wn.synset("scorpion.n.03")],

	# potty, chamber pot, bedpan
	"U+3a95":	[wn.synset("chamberpot.n.01")],

	# choose, pick, select
	"U+3a97":	[wn.synset("choose.v.01")],

	# pole vaulting
	"U+3a98":	[wn.synset("pole_vault.n.01")],

	# stander
	"U+3a99":	[wn.synset("stander.n.01")],

	# standing
	"U+3a9b":	[wn.synset("person.n.01"),
				wn.synset("person.n.02"),
				wn.synset("person.n.03"),
				wn.synset("standing.n.01"),
				wn.synset("standing.n.02"),
				wn.synset("standing.n.03")],

	# odometer
	"U+3a9c":	[wn.synset("odometer.n.01")],

	# perfume, fragrance, aroma, scent
	"U+3a9e":	[wn.synset("aroma.n.02"),
				wn.synset("olfactory_property.n.01"),
				wn.synset("perfume.n.02")],

	# Russian
	"U+3aa0":	[wn.synset("russian.n.02")],

	# Russia
	"U+3aa1":	[wn.synset("russia.n.03"),
				wn.synset("russia.n.04"),
				wn.synset("soviet_russia.n.01"),
				wn.synset("soviet_union.n.01")],

	# homework, home studying studying
	"U+3aa2":	[wn.synset("homework.n.01")],

	# right triangle
	"U+3aa3":	[wn.synset("triangle.n.01")],

	# triangle
	"U+3aa4":	[wn.synset("triangle.n.01")],

	# curiosity, curiousness, inquisitiveness
	"U+3aa5":	[wn.synset("curio.n.01"),
				wn.synset("curiosity.n.01"),
				wn.synset("curiousness.n.01"),
				wn.synset("foreignness.n.01")],

	# discount store
	"U+3aa6":	[wn.synset("discount_chain.n.01"),
				wn.synset("discount_house.n.01")],

	# discount
	"U+3aa7":	[wn.synset("deduction.n.02"),
				wn.synset("discount.n.01"),
				wn.synset("discount_rate.n.02"),
				wn.synset("rebate.n.01")],

	# woodwind instrument
	"U+3aa8":	[wn.synset("woodwind.n.01")],

	# causality
	"U+3aa9":	[wn.synset("causality.n.01")],

	# shopping centre, mall, plaza
	"U+3aaa":	[wn.synset("hypermarket.n.01"),
				wn.synset("plaza.n.01"),
				wn.synset("plaza.n.02"),
				wn.synset("promenade.n.02")],

	# roe deer
	"U+3aab":	[wn.synset("roe_deer.n.01")],

	# deer, cervine, cervid
	"U+3aac":	[wn.synset("cervine.a.01"),
				wn.synset("deer.n.01")],

	# learn
	"U+3aad":	[wn.synset("determine.v.08"),
				wn.synset("learn.v.01"),
				wn.synset("learn.v.02"),
				wn.synset("learn.v.04"),
				wn.synset("memorize.v.01"),
				wn.synset("teach.v.01")],

	# desk, worktable, work table table
	"U+3aae":	[wn.synset("desk.n.01")],

	# gull, seagull, sea gull gull
	"U+3aaf":	[wn.synset("gull.n.02")],

	# speech therapy
	"U+3ab2":	[wn.synset("speech_therapy.n.01")],

	# gallop
	"U+3ab3":	[wn.synset("gallop.n.01")],

	# canter
	"U+3ab4":	[wn.synset("canter.v.01"),
				wn.synset("canter.v.02"),
				wn.synset("canter.v.03")],

	# autumn, fall
	"U+3ab5":	[wn.synset("fall.n.01")],

	# salty
	"U+3ab6":	[wn.synset("piquant.s.02"),
				wn.synset("salty.a.02"),
				wn.synset("salty.s.03")],

	# hearing, audition, auditory sense sense
	"U+3ab7":	[wn.synset("audition.n.02"),
				wn.synset("earshot.n.01"),
				wn.synset("hearing.n.01"),
				wn.synset("hearing.n.02"),
				wn.synset("hearing.n.05"),
				wn.synset("hearing.n.06"),
				wn.synset("listening.n.01")],

	# sentence, condemn, clause, phrase
	"U+3ab8":	[wn.synset("sentence.v.01")],

	# guilty
	"U+3ab9":	[wn.synset("guilty.a.01")],

	# increase, enlarge
	"U+3aba":	[wn.synset("increase.v.01")],

	# sacked, dismissed
	"U+3abb":	[wn.synset("discharged.s.01")],

	# factory, plant
	"U+3abe":	[wn.synset("factory.n.01")],

	# Israel
	"U+3abf":	[wn.synset("israel.n.01")],

	# soft cheese
	"U+3ac0":	[wn.synset("cheese.n.01")],

	# rowdy
	"U+3ac1":	[wn.synset("raucous.s.02")],

	# niece or nephew
	"U+3ac3":	[wn.synset("grandchild.n.01"),
				wn.synset("grandson.n.01"),
				wn.synset("nephew.n.01")],

	# sibling
	"U+3ac4":	[wn.synset("sibling.n.01")],

	# volleyball
	"U+3ac5":	[wn.synset("volleyball.n.01")],

	# duck, bird, waterbird, waterfowl, seabird, seafowl
	"U+3ac7":	[wn.synset("duck.n.01")],

	# Hebrew
	"U+3ac8":	[wn.synset("hebrew.n.01"),
				wn.synset("jew.n.01")],

	# asparagus
	"U+3ac9":	[wn.synset("asparagus.n.01"),
				wn.synset("asparagus.n.02")],

	# root, rootage, root system
	"U+3aca":	[wn.synset("root.n.01"),
				wn.synset("root.n.08")],

	# foam, mousse
	"U+3acb":	[wn.synset("foam.n.01")],

	# its
	"U+3acc":	[wn.synset("hog.n.03"),
				wn.synset("information_technology.n.01"),
				wn.synset("sus.n.01")],

	# astrology
	"U+3acd":	[wn.synset("astrology.n.01")],

	# quick, fast, quickly, rapid, rapidly
	"U+3ace":	[wn.synset("fast.a.01"),
				wn.synset("quick.s.01"),
				wn.synset("rapid.s.01")],

	# civil engineer
	"U+3ad0":	[wn.synset("engineer.n.01")],

	# colleague
	"U+3ad1":	[wn.synset("colleague.n.01")],

	# equal, same
	"U+3ad2":	[wn.synset("equal.v.01"),
				wn.synset("equal.v.02"),
				wn.synset("equal.v.03")],

	# hysterectomy
	"U+3ad3":	[wn.synset("hysterectomy.n.01")],

	# fire place, campfire site
	"U+3ad4":	[wn.synset("fire.n.04")],

	# stove, furnace, heater, oven
	"U+3ad5":	[wn.synset("fastball.n.01"),
				wn.synset("furnace.n.01"),
				wn.synset("heater.n.01"),
				wn.synset("oven.n.01"),
				wn.synset("stove.n.01"),
				wn.synset("stove.n.02")],

	# suggest, propose
	"U+3ad6":	[wn.synset("propose.v.01")],

	# suggestion, proposal
	"U+3ad7":	[wn.synset("hypnotism.n.01"),
				wn.synset("marriage_proposal.n.01"),
				wn.synset("proposal.n.01"),
				wn.synset("proposal.n.03"),
				wn.synset("suggestion.n.01"),
				wn.synset("suggestion.n.02"),
				wn.synset("suggestion.n.04"),
				wn.synset("suggestion.n.05"),
				wn.synset("trace.n.01")],

	# hot spring
	"U+3ad8":	[wn.synset("geyser.n.01")],

	# snowball
	"U+3ada":	[wn.synset("snowball.n.01"),
				wn.synset("snowball.n.02"),
				wn.synset("snowball.n.03"),
				wn.synset("snowball.n.04")],

	# sea captain, skipper
	"U+3adb":	[wn.synset("captain.n.02"),
				wn.synset("master.n.07")],

	# misuse
	"U+3adc":	[wn.synset("misapply.v.01"),
				wn.synset("pervert.v.03")],

	# always, ever, forever, whenever
	"U+3ade":	[wn.synset("always.r.01"),
				wn.synset("always.r.05"),
				wn.synset("constantly.r.02"),
				wn.synset("ever.r.01"),
				wn.synset("everlastingly.r.01")],

	# knight
	"U+3adf":	[wn.synset("knight.n.01"),
				wn.synset("knight.n.02")],

	# Bliss, Bliss language, Blissymbolics
	"U+3ae0":	[wn.synset("bliss.n.01")],

	# flashlight, lantern
	"U+3ae2":	[wn.synset("flashlight.n.01"),
				wn.synset("lantern.n.01"),
				wn.synset("torch.n.01")],

	# burned out, burnt out
	"U+3ae3":	[wn.synset("burned-out.s.01")],

	# decrease, reduce
	"U+3ae4":	[wn.synset("decrease.v.01"),
				wn.synset("decrease.v.02"),
				wn.synset("reduce.v.01")],

	# Sabbath, day of rest of rest
	"U+3ae5":	[wn.synset("sabbath.n.01")],

	# shortness, length)
	"U+3ae6":	[wn.synset("abruptness.n.01"),
				wn.synset("shortness.n.01"),
				wn.synset("shortness.n.02"),
				wn.synset("shortness.n.03"),
				wn.synset("shortness.n.04"),
				wn.synset("shortness.n.05")],

	# lowness, shortness
	"U+3ae7":	[wn.synset("abruptness.n.01"),
				wn.synset("downheartedness.n.01"),
				wn.synset("low_status.n.01"),
				wn.synset("lowness.n.03"),
				wn.synset("lowness.n.04"),
				wn.synset("shortness.n.01"),
				wn.synset("shortness.n.02"),
				wn.synset("shortness.n.03"),
				wn.synset("shortness.n.04"),
				wn.synset("shortness.n.05")],

	# real, really
	"U+3ae8":	[wn.synset("real.a.01"),
				wn.synset("real.a.02"),
				wn.synset("real.a.06")],

	# try, attempt
	"U+3ae9":	[wn.synset("try.v.01")],

	# psychology
	"U+3aea":	[wn.synset("psychology.n.01")],

	# research
	"U+3aec":	[wn.synset("inquiry.n.01"),
				wn.synset("research.n.01")],

	# belief
	"U+3aed":	[wn.synset("belief.n.01"),
				wn.synset("confidence.n.02"),
				wn.synset("faith.n.02"),
				wn.synset("fidelity.n.02"),
				wn.synset("impression.n.01"),
				wn.synset("religion.n.01"),
				wn.synset("religion.n.02"),
				wn.synset("wedding_ring.n.01")],

	# hypothesis, theory
	"U+3aee":	[wn.synset("guess.n.01"),
				wn.synset("hypothesis.n.02")],

	# table tennis, ping pong
	"U+3af0":	[wn.synset("table_tennis.n.01")],

	# flight deck, cockpit
	"U+3af1":	[wn.synset("cockpit.n.01"),
				wn.synset("cockpit.n.02"),
				wn.synset("cockpit.n.03")],

	# pilot
	"U+3af2":	[wn.synset("pilot.n.01")],

	# old age pension, old-age pension
	"U+3af3":	[wn.synset("boarding_house.n.01"),
				wn.synset("pension.n.01")],

	# suntan
	"U+3af4":	[wn.synset("tan.n.01")],

	# definition
	"U+3af5":	[wn.synset("definition.n.01"),
				wn.synset("definition.n.02")],

	# explanation, reason
	"U+3af6":	[wn.synset("explanation.n.03"),
				wn.synset("rationality.n.01")],

	# dead person
	"U+3af7":	[wn.synset("body.n.03"),
				wn.synset("cadaver.n.01")],

	# repair shop
	"U+3afa":	[wn.synset("repair_shop.n.01"),
				wn.synset("workroom.n.01"),
				wn.synset("workshop.n.01")],

	# suit of armour
	"U+3afd":	[wn.synset("armor.n.01")],

	# slipper
	"U+3aff":	[wn.synset("slipper.n.01")],

	# shoe
	"U+3b00":	[wn.synset("shoe.n.01")],

	# florist
	"U+3b01":	[wn.synset("florist.n.02")],

	# glitter
	"U+3b02":	[wn.synset("glitter.n.01"),
				wn.synset("glitter.n.02")],

	# lump
	"U+3b03":	[wn.synset("swelling.n.01")],

	# visitor, guest
	"U+3b04":	[wn.synset("visitor.n.01")],

	# jet, jet plane plane
	"U+3b05":	[wn.synset("jet.n.01")],

	# saint
	"U+3b07":	[wn.synset("saint.n.01")],

	# lawn mower, mower
	"U+3b08":	[wn.synset("lawn_mower.n.01")],

	# fossil fuel, coal
	"U+3b09":	[wn.synset("coal.n.01")],

	# afraid, frightened, scared
	"U+3b0b":	[wn.synset("afraid.a.01"),
				wn.synset("afraid.s.03")],

	# interviewer
	"U+3b0c":	[wn.synset("interviewer.n.01")],

	# interview
	"U+3b0d":	[wn.synset("interview.v.01")],

	# grace
	"U+3b0e":	[wn.synset("grace.n.01")],

	# Cancer
	"U+3b0f":	[wn.synset("cancer.n.01"),
				wn.synset("cancer.n.02"),
				wn.synset("cancer.n.03"),
				wn.synset("cancer.n.04"),
				wn.synset("cancer.n.05")],

	# knee pad
	"U+3b10":	[wn.synset("knee_pad.n.01"),
				wn.synset("knee_piece.n.01")],

	# sell
	"U+3b12":	[wn.synset("sell.v.01")],

	# heterosexual
	"U+3b13":	[wn.synset("heterosexual.a.01")],

	# heterosexuality
	"U+3b14":	[wn.synset("heterosexuality.n.01")],

	# mood
	"U+3b15":	[wn.synset("temper.n.02")],

	# blackboard, chalkboard, whiteboard, writing board board
	"U+3b18":	[wn.synset("blackboard.n.01")],

	# yawn
	"U+3b19":	[wn.synset("yawn.v.01")],

	# program, programme, presentation
	"U+3b1b":	[wn.synset("broadcast.n.02"),
				wn.synset("course_of_study.n.01"),
				wn.synset("plan.n.01"),
				wn.synset("platform.n.02"),
				wn.synset("program.n.02"),
				wn.synset("program.n.05"),
				wn.synset("program.n.07"),
				wn.synset("program.n.08")],

	# darts
	"U+3b1f":	[wn.synset("darts.n.01")],

	# capture, catch, seize, grab
	"U+3b20":	[wn.synset("capture.v.02"),
				wn.synset("capture.v.06"),
				wn.synset("catch.v.01"),
				wn.synset("catch.v.02"),
				wn.synset("catch.v.04"),
				wn.synset("catch.v.07"),
				wn.synset("catch.v.09"),
				wn.synset("catch.v.10"),
				wn.synset("catch.v.12"),
				wn.synset("catch.v.13"),
				wn.synset("catch.v.14"),
				wn.synset("catch.v.16"),
				wn.synset("catch.v.18"),
				wn.synset("catch.v.19"),
				wn.synset("catch.v.20"),
				wn.synset("catch.v.21"),
				wn.synset("catch.v.22"),
				wn.synset("catch.v.24"),
				wn.synset("catch.v.25"),
				wn.synset("catch.v.26"),
				wn.synset("catch.v.27"),
				wn.synset("catch.v.28"),
				wn.synset("catch.v.29"),
				wn.synset("get.v.11"),
				wn.synset("get.v.19"),
				wn.synset("grab.v.03"),
				wn.synset("grab.v.04"),
				wn.synset("grab.v.05"),
				wn.synset("grab.v.06"),
				wn.synset("hitch.v.01"),
				wn.synset("overtake.v.01"),
				wn.synset("snap_up.v.01"),
				wn.synset("trip_up.v.01"),
				wn.synset("watch.v.03")],

	# protect, cover, shelter, take care of care of
	"U+3b22":	[wn.synset("protect.v.01")],

	# ugh, yuk
	"U+3b25":	[wn.synset("phi.n.01")],

	# golf
	"U+3b26":	[wn.synset("golf.n.01")],

	# gold
	"U+3b27":	[wn.synset("amber.n.01"),
				wn.synset("gold.n.01"),
				wn.synset("gold.n.03"),
				wn.synset("gold.n.04")],

	# mixer, blender
	"U+3b28":	[wn.synset("mixer.n.03")],

	# mixture
	"U+3b29":	[wn.synset("concoction.n.01"),
				wn.synset("mix.n.02"),
				wn.synset("mixture.n.01")],

	# impact
	"U+3b2a":	[wn.synset("impact.n.02")],

	# indicator
	"U+3b2c":	[wn.synset("indicator.n.02"),
				wn.synset("indicator.n.03")],

	# circle
	"U+3b3a":	[wn.synset("circle.n.01")],

	# cassette, audiocassette, videocassette
	"U+3b3e":	[wn.synset("cassette.n.01")],

	# condom
	"U+3b3f":	[wn.synset("condom.n.01")],

	# molasses, dark syrup, black treacle
	"U+3b40":	[wn.synset("molasses.n.01")],

	# syrup
	"U+3b41":	[wn.synset("syrup.n.01")],

	# free of charge, gratis, for free
	"U+3b42":	[wn.synset("complimentary.s.02")],

	# cost, price
	"U+3b43":	[wn.synset("price.n.02")],

	# distance
	"U+3b44":	[wn.synset("distance.n.01"),
				wn.synset("distance.n.03"),
				wn.synset("distance.n.04"),
				wn.synset("distance.n.05"),
				wn.synset("distance.n.06")],

	# dependent
	"U+3b45":	[wn.synset("dependent.a.01"),
				wn.synset("dependent.a.03"),
				wn.synset("dependent.s.02"),
				wn.synset("dependent.s.06"),
				wn.synset("pendent.s.01"),
				wn.synset("subject.s.02")],

	# sunny
	"U+3b46":	[wn.synset("cheery.s.01")],

	# resent
	"U+3b47":	[wn.synset("begrudge.v.02")],

	# compass
	"U+3b48":	[wn.synset("compass.n.01")],

	# cry, weep
	"U+3b49":	[wn.synset("cry.v.02")],

	# proclaim, announce
	"U+3b4a":	[wn.synset("announce.v.02"),
				wn.synset("proclaim.v.02")],

	# proclamation, announcement
	"U+3b4b":	[wn.synset("announcement.n.01")],

	# ocean, sea
	"U+3b4d":	[wn.synset("ocean.n.02"),
				wn.synset("sea.n.01")],

	# movie, film
	"U+3b4e":	[wn.synset("movie.n.01")],

	# cylinder, can
	"U+3b4f":	[wn.synset("can.n.01")],

	# nuclear energy
	"U+3b50":	[wn.synset("no.r.03"),
				wn.synset("not.r.01")],

	# kneel
	"U+3b51":	[wn.synset("kneel.v.01")],

	# adversity, hardship, setback
	"U+3b52":	[wn.synset("reverse.n.03")],

	# half, one half-half
	"U+3b53":	[wn.synset("one-half.n.01")],

	# fish bone
	"U+3b54":	[wn.synset("skeletal_structure.n.01"),
				wn.synset("skeletal_system.n.01")],

	# last, final, etc)
	"U+3b55":	[wn.synset("last.a.02"),
				wn.synset("last.s.01")],

	# South Pole
	"U+3b57":	[wn.synset("south_pole.n.01")],

	# let, allow, permit
	"U+3b5a":	[wn.synset("permit.v.01")],

	# similar, like, alike
	"U+3b5c":	[wn.synset("alike.a.01"),
				wn.synset("alike.r.01"),
				wn.synset("alike.r.02"),
				wn.synset("exchangeable.s.03"),
				wn.synset("like.a.01"),
				wn.synset("like.n.01"),
				wn.synset("like.n.02"),
				wn.synset("similar.a.01"),
				wn.synset("similar.s.04")],

	# approve
	"U+3b5d":	[wn.synset("approve.v.01")],

	# load
	"U+3b5e":	[wn.synset("burden.n.01"),
				wn.synset("cargo.n.01"),
				wn.synset("load.n.01"),
				wn.synset("load.n.02")],

	# bell, chime bar bar
	"U+3b60":	[wn.synset("bell.n.01"),
				wn.synset("bell.n.03"),
				wn.synset("bell.n.04"),
				wn.synset("bell.n.05"),
				wn.synset("bell.n.06"),
				wn.synset("bell.n.07"),
				wn.synset("bell.n.08"),
				wn.synset("bell.n.10"),
				wn.synset("chime.n.01"),
				wn.synset("doorbell.n.01")],

	# lend, loan
	"U+3b61":	[wn.synset("lend.v.02")],

	# indefinite
	"U+3b62":	[wn.synset("general.a.01"),
				wn.synset("general.s.02"),
				wn.synset("indefinite.a.01"),
				wn.synset("indefinite.s.02"),
				wn.synset("overall.s.01")],

	# belt, sash
	"U+3b63":	[wn.synset("belt.n.02")],

	# devil
	"U+3b64":	[wn.synset("devil.n.02"),
				wn.synset("satan.n.01")],

	# electro magnet
	"U+3b66":	[wn.synset("electromagnet.n.01")],

	# hard, firm
	"U+3b67":	[wn.synset("hard.a.03")],

	# sweetheart, lover
	"U+3b68":	[wn.synset("fan.n.03"),
				wn.synset("lover.n.01"),
				wn.synset("lover.n.03"),
				wn.synset("smasher.n.02"),
				wn.synset("sweetheart.n.01"),
				wn.synset("sweetheart.n.02")],

	# board and lodging, room and board
	"U+3b6a":	[wn.synset("billet.n.02"),
				wn.synset("boarding_house.n.01"),
				wn.synset("diggings.n.02"),
				wn.synset("housing.n.01"),
				wn.synset("living_quarters.n.01"),
				wn.synset("pension.n.01"),
				wn.synset("suite.n.02")],

	# infect
	"U+3b6d":	[wn.synset("infect.v.01"),
				wn.synset("infect.v.02"),
				wn.synset("infect.v.03"),
				wn.synset("infect.v.04")],

	# infection
	"U+3b6e":	[wn.synset("infection.n.01")],

	# wakefulness, alertness
	"U+3b70":	[wn.synset("alertness.n.02"),
				wn.synset("alertness.n.03"),
				wn.synset("wakefulness.n.01"),
				wn.synset("wakefulness.n.02"),
				wn.synset("watchfulness.n.01")],

	# cell
	"U+3b73":	[wn.synset("cell.n.02")],

	# shooting sports
	"U+3b74":	[wn.synset("discharge.n.09"),
				wn.synset("fire.n.02"),
				wn.synset("fusillade.n.01"),
				wn.synset("gunfire.n.01"),
				wn.synset("shooting.n.01")],

	# protective mask
	"U+3b75":	[wn.synset("face_guard.n.01"),
				wn.synset("face_mask.n.01")],

	# uncertain, unsure
	"U+3b76":	[wn.synset("changeable.s.03"),
				wn.synset("diffident.a.02"),
				wn.synset("uncertain.a.01"),
				wn.synset("uncertain.a.02"),
				wn.synset("uncertain.a.04"),
				wn.synset("uncertain.s.06"),
				wn.synset("uncertain.s.07"),
				wn.synset("unsealed.a.01")],

	# linear, straight
	"U+3b77":	[wn.synset("analogue.a.01"),
				wn.synset("linear.a.01"),
				wn.synset("linear.a.02"),
				wn.synset("linear.s.04"),
				wn.synset("linear.s.05"),
				wn.synset("neat.s.06"),
				wn.synset("square.s.05"),
				wn.synset("square.s.06"),
				wn.synset("straight.a.02"),
				wn.synset("straight.a.03"),
				wn.synset("straight.a.06"),
				wn.synset("straight.a.08"),
				wn.synset("straight.s.01"),
				wn.synset("straight.s.04"),
				wn.synset("straight.s.05"),
				wn.synset("straight.s.09"),
				wn.synset("straight.s.10"),
				wn.synset("straight.s.14"),
				wn.synset("true.s.12"),
				wn.synset("uncoiled.a.01")],

	# budget, business plan plan
	"U+3b78":	[wn.synset("budget.n.02")],

	# wave
	"U+3b7a":	[wn.synset("wave.n.01")],

	# mistake, error, fault, mishap
	"U+3b7b":	[wn.synset("erroneousness.n.01"),
				wn.synset("error.n.03"),
				wn.synset("error.n.04"),
				wn.synset("error.n.05"),
				wn.synset("error.n.07"),
				wn.synset("mistake.n.01")],

	# quills, spines
	"U+3b7d":	[wn.synset("flight_feather.n.01"),
				wn.synset("quill.n.01"),
				wn.synset("quill.n.02"),
				wn.synset("quill.n.04"),
				wn.synset("spinal_column.n.01"),
				wn.synset("spine.n.03"),
				wn.synset("spine.n.04"),
				wn.synset("spine.n.05"),
				wn.synset("spur.n.02")],

	# swim
	"U+3b7f":	[wn.synset("swim.v.01")],

	# upset, disturbance, agitation
	"U+3b80":	[wn.synset("affray.n.02"),
				wn.synset("agitation.n.01"),
				wn.synset("agitation.n.02"),
				wn.synset("agitation.n.03"),
				wn.synset("agitation.n.04"),
				wn.synset("agitation.n.05"),
				wn.synset("disorder.n.01"),
				wn.synset("disturbance.n.02"),
				wn.synset("disturbance.n.03"),
				wn.synset("disturbance.n.05"),
				wn.synset("mental_disorder.n.01"),
				wn.synset("noise.n.03"),
				wn.synset("overturn.n.02"),
				wn.synset("perturbation.n.03"),
				wn.synset("troubled.a.01"),
				wn.synset("upset.n.02"),
				wn.synset("upset.n.04"),
				wn.synset("upset.n.05")],

	# calculator
	"U+3b81":	[wn.synset("calculator.n.02")],

	# chase
	"U+3b83":	[wn.synset("chase.n.02"),
				wn.synset("chase.n.03"),
				wn.synset("pursuit.n.01")],

	# funny, humorous
	"U+3b84":	[wn.synset("amusing.s.02")],

	# laugh, laughter
	"U+3b85":	[wn.synset("laugh.n.01")],

	# guest room
	"U+3b87":	[wn.synset("guestroom.n.01")],

	# forgiveness, pardon, what did you say did you say
	"U+3b88":	[wn.synset("amnesty.n.03"),
				wn.synset("forgiveness.n.02"),
				wn.synset("pardon.n.02")],

	# watchful, alert
	"U+3b89":	[wn.synset("alert.a.01"),
				wn.synset("alert.s.02"),
				wn.synset("alert.s.03"),
				wn.synset("insomniac.s.01")],

	# cucumber
	"U+3b8a":	[wn.synset("cucumber.n.02")],

	# tobacco
	"U+3b8b":	[wn.synset("tobacco.n.01")],

	# recent, recently
	"U+3b8d":	[wn.synset("recent.s.01")],

	# greenhouse, glasshouse, hothouse
	"U+3b8f":	[wn.synset("greenhouse.n.01")],

	# crayfish
	"U+3b92":	[wn.synset("crayfish.n.02"),
				wn.synset("crayfish.n.03"),
				wn.synset("spiny_lobster.n.01"),
				wn.synset("spiny_lobster.n.02")],

	# horse cloth
	"U+3b94":	[wn.synset("bard.n.02"),
				wn.synset("caparison.n.01"),
				wn.synset("manta.n.01"),
				wn.synset("warp.n.04")],

	# javelin throw
	"U+3b97":	[wn.synset("javelin.n.01")],

	# javelin, spear
	"U+3b98":	[wn.synset("javelin.n.01"),
				wn.synset("javelin.n.02"),
				wn.synset("spear.n.01"),
				wn.synset("spear.n.02")],

	# barge, river boat boat
	"U+3b99":	[wn.synset("barge.n.01")],

	# freighter
	"U+3b9a":	[wn.synset("bottom.n.07")],

	# abstention
	"U+3b9b":	[wn.synset("abstinence.n.01")],

	# sandal
	"U+3b9c":	[wn.synset("sandal.n.01")],

	# goblet, wineglass
	"U+3b9d":	[wn.synset("chalice.n.01"),
				wn.synset("goblet.n.01"),
				wn.synset("wineglass.n.01")],

	# eager, keen, willing
	"U+3b9e":	[wn.synset("willing.a.01")],

	# grapefruit
	"U+3b9f":	[wn.synset("grapefruit.n.02")],

	# surprised
	"U+3ba0":	[wn.synset("surprised.a.01")],

	# surprise
	"U+3ba1":	[wn.synset("storm.v.05"),
				wn.synset("surprise.v.01"),
				wn.synset("surprise.v.02")],

	# niece
	"U+3ba2":	[wn.synset("niece.n.01")],

	# emergency
	"U+3ba3":	[wn.synset("ad_hoc.s.01"),
				wn.synset("emergency.n.01"),
				wn.synset("emergency.n.02"),
				wn.synset("hand_brake.n.01"),
				wn.synset("rapid.s.01")],

	# family, couple
	"U+3ba5":	[wn.synset("class.n.01"),
				wn.synset("couple.n.01"),
				wn.synset("couple.n.02"),
				wn.synset("couple.n.03"),
				wn.synset("couple.n.04"),
				wn.synset("couple.n.05"),
				wn.synset("family.n.01"),
				wn.synset("family.n.02"),
				wn.synset("family.n.04"),
				wn.synset("family.n.06"),
				wn.synset("family.n.08"),
				wn.synset("kin.n.01"),
				wn.synset("pair.n.03"),
				wn.synset("syndicate.n.01")],

	# sick, ill
	"U+3ba6":	[wn.synset("ill.a.01")],

	# washcloth, washrag, flannel
	"U+3ba8":	[wn.synset("flannel.n.01"),
				wn.synset("flannel.n.03"),
				wn.synset("gauntlet.n.02"),
				wn.synset("handle.n.01"),
				wn.synset("knob.n.02"),
				wn.synset("mitten.n.01"),
				wn.synset("strap.n.02"),
				wn.synset("washcloth.n.01")],

	# jackfruit
	"U+3ba9":	[wn.synset("jackfruit.n.02")],

	# heavy
	"U+3baa":	[wn.synset("heavy.a.01")],

	# maple syrup
	"U+3bab":	[wn.synset("maple_syrup.n.01")],

	# OK, alright
	"U+3bac":	[wn.synset("all_right.s.01")],

	# enough
	"U+3bad":	[wn.synset("adequate.s.02"),
				wn.synset("enough.r.01"),
				wn.synset("entire.s.01"),
				wn.synset("filled.s.01"),
				wn.synset("full.a.01"),
				wn.synset("quite.r.01"),
				wn.synset("quite.r.02"),
				wn.synset("reasonably.r.01"),
				wn.synset("sufficiently.r.01")],

	# mouse, pointing device device
	"U+3bae":	[wn.synset("mouse.n.04")],

	# choir, chorus
	"U+3baf":	[wn.synset("choir.n.01"),
				wn.synset("choir.n.02"),
				wn.synset("choir.n.03"),
				wn.synset("chorus.n.01"),
				wn.synset("chorus.n.02"),
				wn.synset("chorus.n.04"),
				wn.synset("chorus.n.05"),
				wn.synset("refrain.n.01")],

	# spring
	"U+3bb1":	[wn.synset("spring.n.01")],

	# palm
	"U+3bb2":	[wn.synset("palm.n.03")],

	# curious, inquisitive
	"U+3bb3":	[wn.synset("curious.a.02"),
				wn.synset("curious.s.01")],

	# twinkle, shine, sparkle
	"U+3bb5":	[wn.synset("fall.v.08"),
				wn.synset("flash.v.01"),
				wn.synset("foam.v.01"),
				wn.synset("glitter.v.01"),
				wn.synset("glow.v.02"),
				wn.synset("glow.v.05"),
				wn.synset("polish.v.01"),
				wn.synset("reflect.v.04"),
				wn.synset("shine.v.02"),
				wn.synset("shine.v.04"),
				wn.synset("shine.v.05"),
				wn.synset("shine.v.07"),
				wn.synset("spark.v.02"),
				wn.synset("sparkle.v.01"),
				wn.synset("sparkle.v.02"),
				wn.synset("twinkle.v.02")],

	# broadband
	"U+3bb6":	[wn.synset("broadband.a.01"),
				wn.synset("broadband.a.02")],

	# band, orchestra
	"U+3bb7":	[wn.synset("band.n.02"),
				wn.synset("band.n.03"),
				wn.synset("band.n.04"),
				wn.synset("band.n.06"),
				wn.synset("band.n.07"),
				wn.synset("band.n.10"),
				wn.synset("band.n.11"),
				wn.synset("band.n.12"),
				wn.synset("band.n.13"),
				wn.synset("dance_band.n.01"),
				wn.synset("isthmus.n.02"),
				wn.synset("orchestra.n.01"),
				wn.synset("orchestra.n.02"),
				wn.synset("ring.n.08"),
				wn.synset("set.n.05")],

	# newness, novelty
	"U+3bb8":	[wn.synset("bangle.n.02"),
				wn.synset("freshness.n.02"),
				wn.synset("knickknack.n.01"),
				wn.synset("newness.n.01"),
				wn.synset("news.n.01"),
				wn.synset("news.n.04"),
				wn.synset("news_program.n.01"),
				wn.synset("novelty.n.02")],

	# protest, object, oppose, objection, opposition, resist, resistance
	"U+3bb9":	[wn.synset("confrontation.n.04"),
				wn.synset("enemy.n.02"),
				wn.synset("expostulation.n.01"),
				wn.synset("objection.n.02"),
				wn.synset("objection.n.04"),
				wn.synset("opposition.n.02"),
				wn.synset("opposition.n.04"),
				wn.synset("opposition.n.05"),
				wn.synset("opposition.n.06"),
				wn.synset("opposition.n.08"),
				wn.synset("protest.n.01"),
				wn.synset("protest.n.02"),
				wn.synset("protest.n.03"),
				wn.synset("resistance.n.01")],

	# school
	"U+3bbd":	[wn.synset("school.n.02")],

	# Christmas song, carol
	"U+3bbe":	[wn.synset("carol.n.01"),
				wn.synset("carol.n.02")],

	# Christmas
	"U+3bbf":	[wn.synset("christmas.n.02")],

	# by, by means of
	"U+3bc0":	[wn.synset("by.r.01")],

	# anything, something
	"U+3bc3":	[wn.synset("some.a.01")],

	# movie theatre, cinema
	"U+3bc4":	[wn.synset("cinema.n.02")],

	# candy, sweets
	"U+3bc7":	[wn.synset("candy.n.01")],

	# tour, sightseeing
	"U+3bc8":	[wn.synset("tour.n.01")],

	# habit, custom
	"U+3bc9":	[wn.synset("habit.n.01"),
				wn.synset("habit.n.02")],

	# usually, usual
	"U+3bca":	[wn.synset("common.s.04"),
				wn.synset("normally.r.01"),
				wn.synset("usual.a.01")],

	# suit
	"U+3bcc":	[wn.synset("courtship.n.01"),
				wn.synset("lawsuit.n.01"),
				wn.synset("suit.n.01"),
				wn.synset("suit.n.03"),
				wn.synset("suit.n.05"),
				wn.synset("suit.n.06")],

	# minister, pastor, preacher, priest, rabbi
	"U+3bcd":	[wn.synset("minister.n.02")],

	# combine, connect, link
	"U+3bcf":	[wn.synset("compound.v.02")],

	# army, regular army, ground forces
	"U+3bd2":	[wn.synset("army.n.01")],

	# Africa
	"U+3bd3":	[wn.synset("africa.n.01")],

	# curry sauce
	"U+3bd4":	[wn.synset("curry.n.01")],

	# harness
	"U+3bd7":	[wn.synset("harness.v.01")],

	# aerial, antenna
	"U+3bd8":	[wn.synset("antenna.n.01"),
				wn.synset("antenna.n.03")],

	# skullcap, kipa, yarmulke
	"U+3bd9":	[wn.synset("calvaria.n.01"),
				wn.synset("skullcap.n.01"),
				wn.synset("skullcap.n.02"),
				wn.synset("yarmulke.n.01")],

	# burnable, combustible, ignitable
	"U+3bda":	[wn.synset("burnable.s.01"),
				wn.synset("combustible.a.01")],

	# influence, affect
	"U+3bdb":	[wn.synset("affect.v.01")],

	# country music
	"U+3bdd":	[wn.synset("country_music.n.01")],

	# parakeet, budgie
	"U+3bde":	[wn.synset("parakeet.n.01")],

	# parrot, myna, talking bird bird
	"U+3bdf":	[wn.synset("parrot.n.01")],

	# pie, tart
	"U+3be0":	[wn.synset("pie.n.01"),
				wn.synset("prostitute.n.01"),
				wn.synset("proto-indo_european.n.01"),
				wn.synset("tart.n.02"),
				wn.synset("tart.n.03")],

	# rabies
	"U+3be1":	[wn.synset("rabies.n.01")],

	# humerus, upper arm bone arm bone
	"U+3be4":	[wn.synset("humerus.n.01")],

	# upper arm
	"U+3be5":	[wn.synset("brachium.n.01")],

	# accusation, charge, prosecution
	"U+3be6":	[wn.synset("accusation.n.01"),
				wn.synset("accusation.n.02"),
				wn.synset("bang.n.04"),
				wn.synset("care.n.05"),
				wn.synset("cathexis.n.01"),
				wn.synset("charge.n.01"),
				wn.synset("charge.n.02"),
				wn.synset("charge.n.03"),
				wn.synset("charge.n.04"),
				wn.synset("charge.n.07"),
				wn.synset("charge.n.08"),
				wn.synset("charge.n.11"),
				wn.synset("charge.n.14"),
				wn.synset("charge.n.15"),
				wn.synset("commission.n.06"),
				wn.synset("mission.n.03"),
				wn.synset("prosecution.n.01"),
				wn.synset("prosecution.n.02"),
				wn.synset("pursuance.n.02")],

	# landing, airplane landing landing
	"U+3be9":	[wn.synset("landing.n.03")],

	# Host, wafer
	"U+3bea":	[wn.synset("horde.n.01"),
				wn.synset("host.n.01"),
				wn.synset("host.n.03"),
				wn.synset("host.n.05"),
				wn.synset("host.n.06"),
				wn.synset("host.n.07"),
				wn.synset("host.n.08"),
				wn.synset("host.n.09"),
				wn.synset("master_of_ceremonies.n.01"),
				wn.synset("server.n.03"),
				wn.synset("wafer.n.01"),
				wn.synset("wafer.n.02"),
				wn.synset("wafer.n.03")],

	# age
	"U+3beb":	[wn.synset("age.n.01")],

	# satellite
	"U+3bec":	[wn.synset("satellite.n.01")],

	# Aegir
	"U+3bed":	[wn.synset("tidal_bore.n.01")],

	# walker
	"U+3bee":	[wn.synset("walker.n.06")],

	# away, at a distance, off
	"U+3bef":	[wn.synset("aside.r.02"),
				wn.synset("aside.r.06"),
				wn.synset("away.a.02"),
				wn.synset("away.r.01"),
				wn.synset("away.r.02"),
				wn.synset("away.r.04"),
				wn.synset("away.r.06"),
				wn.synset("away.r.07"),
				wn.synset("away.r.08"),
				wn.synset("away.r.09"),
				wn.synset("away.r.10"),
				wn.synset("away.s.01"),
				wn.synset("away.s.03"),
				wn.synset("come_away.v.02"),
				wn.synset("murder.v.01"),
				wn.synset("off.a.01"),
				wn.synset("off.a.03"),
				wn.synset("off.r.02"),
				wn.synset("off.r.03"),
				wn.synset("off.s.02"),
				wn.synset("off.s.04"),
				wn.synset("off.s.05"),
				wn.synset("path.n.02"),
				wn.synset("road.n.01"),
				wn.synset("road.n.02"),
				wn.synset("starting_signal.n.01"),
				wn.synset("street.n.01")],

	# Mercury
	"U+3bf1":	[wn.synset("mercury.n.03")],

	# rock planet, terrestrial planet
	"U+3bf2":	[wn.synset("chasuble.n.01"),
				wn.synset("planet.n.01")],

	# code, password
	"U+3bf3":	[wn.synset("code.n.03")],

	# scratch
	"U+3bf4":	[wn.synset("rub.v.02"),
				wn.synset("rub.v.03"),
				wn.synset("scratch.v.02")],

	# illustrated, illustrating
	"U+3bf5":	[wn.synset("exemplify.v.02"),
				wn.synset("illustrate.v.02"),
				wn.synset("illustrate.v.03"),
				wn.synset("pictorial.a.01")],

	# hammer throw
	"U+3bf7":	[wn.synset("hammer_throw.n.01")],

	# leisure time
	"U+3bf8":	[wn.synset("leisure.n.02")],

	# free, freely
	"U+3bf9":	[wn.synset("free.a.01")],

	# send
	"U+3bfa":	[wn.synset("send.v.02"),
				wn.synset("send.v.06"),
				wn.synset("transport.v.04")],

	# artificial insemination
	"U+3bfd":	[wn.synset("artificial_insemination.n.01")],

	# dislike
	"U+3bfe":	[wn.synset("abhor.v.01"),
				wn.synset("dislike.v.01"),
				wn.synset("hate.v.01")],

	# Netherlands, Holland
	"U+3bff":	[wn.synset("netherlands.n.01")],

	# Chanukah, Hanukkah
	"U+3c00":	[wn.synset("hanukkah.n.01")],

	# wipe, dust, polish
	"U+3c03":	[wn.synset("blot.v.01"),
				wn.synset("clean.v.01"),
				wn.synset("clean.v.02"),
				wn.synset("clear.v.05"),
				wn.synset("dry.v.01"),
				wn.synset("dry.v.02"),
				wn.synset("dust.v.01"),
				wn.synset("dust.v.02"),
				wn.synset("dust.v.03"),
				wn.synset("polish.v.01"),
				wn.synset("polish.v.02"),
				wn.synset("polish.v.03"),
				wn.synset("scatter.v.03"),
				wn.synset("wipe.v.01")],

	# magic
	"U+3c04":	[wn.synset("magic.n.01"),
				wn.synset("magic_trick.n.01")],

	# mystery, unknown
	"U+3c05":	[wn.synset("mystery.n.01")],

	# marry
	"U+3c06":	[wn.synset("marry.v.01")],

	# fewer, less
	"U+3c07":	[wn.synset("fewer.a.01"),
				wn.synset("less.a.01")],

	# anxious, anxiously
	"U+3c08":	[wn.synset("anxious.s.01"),
				wn.synset("anxious.s.02"),
				wn.synset("anxiously.r.01"),
				wn.synset("apprehensive.s.02"),
				wn.synset("disquieted.s.01"),
				wn.synset("troubled.a.01")],

	# anxiety
	"U+3c09":	[wn.synset("anxiety.n.02")],

	# compete, race
	"U+3c0a":	[wn.synset("compete.v.01")],

	# rack, single foot-foot
	"U+3c0b":	[wn.synset("extort.v.02"),
				wn.synset("rack.v.02"),
				wn.synset("rack.v.03"),
				wn.synset("rack.v.06"),
				wn.synset("rack.v.07"),
				wn.synset("rack.v.09"),
				wn.synset("rack.v.10"),
				wn.synset("rack.v.11"),
				wn.synset("scud.v.02"),
				wn.synset("single-foot.v.01"),
				wn.synset("torment.v.01")],

	# Iceland
	"U+3c0c":	[wn.synset("iceland.n.02")],

	# promise, pledge
	"U+3c0d":	[wn.synset("promise.v.01"),
				wn.synset("promise.v.02")],

	# sweet shop, candy store
	"U+3c0e":	[wn.synset("confectionery.n.02"),
				wn.synset("tuck_shop.n.01")],

	# touch, sense of touch, tactile sense, feel, touching
	"U+3c0f":	[wn.synset("touch.n.10")],

	# skin
	"U+3c10":	[wn.synset("hide.n.02"),
				wn.synset("peel.n.02"),
				wn.synset("skin.n.01")],

	# biomass, biofuel
	"U+3c11":	[wn.synset("biomass.n.01"),
				wn.synset("biomass.n.02")],

	# trackball
	"U+3c12":	[wn.synset("trackball.n.01")],

	# wheat
	"U+3c13":	[wn.synset("wheat.n.01")],

	# spaghetti
	"U+3c14":	[wn.synset("spaghetti.n.02")],

	# pasta
	"U+3c15":	[wn.synset("pasta.n.01"),
				wn.synset("pasta.n.02")],

	# Durga
	"U+3c16":	[wn.synset("durga.n.01")],

	# index, list of contents
	"U+3c19":	[wn.synset("exponent.n.03"),
				wn.synset("index.n.02"),
				wn.synset("index.n.04"),
				wn.synset("index.n.05")],

	# sauerkraut
	"U+3c1a":	[wn.synset("sauerkraut.n.01")],

	# twins
	"U+3c1c":	[wn.synset("gemini.n.01"),
				wn.synset("gemini.n.03")],

	# switch off, turn off
	"U+3c1d":	[wn.synset("switch_off.v.01")],

	# switch
	"U+3c1e":	[wn.synset("pedal.n.02"),
				wn.synset("substitution.n.01"),
				wn.synset("switch.n.01"),
				wn.synset("switch.n.03"),
				wn.synset("switch.n.04"),
				wn.synset("switch.n.05"),
				wn.synset("switch.n.06"),
				wn.synset("switch.n.07")],

	# scenery, landscape
	"U+3c20":	[wn.synset("landscape.n.01")],

	# lee, shelter
	"U+3c21":	[wn.synset("shelter.n.05")],

	# poverty
	"U+3c22":	[wn.synset("poverty.n.01")],

	# vinegar
	"U+3c23":	[wn.synset("vinegar.n.01"),
				wn.synset("vinegar.n.02")],

	# wow, super, great, neat, cool, wonderful, fantastic, chilly
	"U+3c25":	[wn.synset("chilly.s.01"),
				wn.synset("chilly.s.02"),
				wn.synset("chilly.s.03"),
				wn.synset("cool.a.01"),
				wn.synset("cool.a.03"),
				wn.synset("cool.a.04"),
				wn.synset("cool.s.02"),
				wn.synset("cool.s.05"),
				wn.synset("cool.s.06")],

	# well, water well well
	"U+3c26":	[wn.synset("well.n.01")],

	# fine
	"U+3c27":	[wn.synset("fine.n.01")],

	# case, casing
	"U+3c2b":	[wn.synset("case.n.01"),
				wn.synset("case.n.04"),
				wn.synset("case.n.05"),
				wn.synset("case.n.06"),
				wn.synset("case.n.08"),
				wn.synset("case.n.09"),
				wn.synset("case.n.10"),
				wn.synset("case.n.11"),
				wn.synset("case.n.12"),
				wn.synset("case.n.18"),
				wn.synset("case.n.19"),
				wn.synset("case.n.20"),
				wn.synset("casing.n.02"),
				wn.synset("casing.n.03"),
				wn.synset("character.n.05"),
				wn.synset("event.n.02"),
				wn.synset("font.n.01"),
				wn.synset("lawsuit.n.01"),
				wn.synset("sheath.n.02"),
				wn.synset("shell.n.08"),
				wn.synset("subject.n.06")],

	# coffin
	"U+3c2c":	[wn.synset("coffin.n.01")],

	# reclining, lying
	"U+3c2d":	[wn.synset("cipher.n.04"),
				wn.synset("lying.n.01"),
				wn.synset("no.n.01"),
				wn.synset("none.n.01"),
				wn.synset("none.n.02"),
				wn.synset("person.n.01"),
				wn.synset("person.n.02"),
				wn.synset("person.n.03"),
				wn.synset("reclining.n.01")],

	# grandchild
	"U+3c2f":	[wn.synset("grandchild.n.01")],

	# popcorn
	"U+3c31":	[wn.synset("popcorn.n.02")],

	# castle, palace
	"U+3c32":	[wn.synset("castle.n.02")],

	# maker, manufacturer, producer
	"U+3c33":	[wn.synset("manufacturer.n.01")],

	# sun lounger, deck chair
	"U+3c34":	[wn.synset("deck_chair.n.01")],

	# self control, self-control
	"U+3c36":	[wn.synset("self-denial.n.02")],

	# dormouse
	"U+3c38":	[wn.synset("dormouse.n.01")],

	# samosa, pirogue
	"U+3c39":	[wn.synset("dugout_canoe.n.01"),
				wn.synset("samosa.n.01")],

	# trust, confidence
	"U+3c3a":	[wn.synset("confidence.n.02"),
				wn.synset("confidence.n.03"),
				wn.synset("faith.n.02"),
				wn.synset("trust.n.03")],

	# exciting, excitingly, excited, excitedly
	"U+3c3b":	[wn.synset("excited.a.02")],

	# excitement
	"U+3c3c":	[wn.synset("excitation.n.03"),
				wn.synset("excitement.n.02")],

	# next
	"U+3c3d":	[wn.synset("following.s.02")],

	# repeat, copy, duplicate, reproduce
	"U+3c3f":	[wn.synset("repeat.v.01"),
				wn.synset("repeat.v.04")],

	# fish finger
	"U+3c43":	[wn.synset("fish_stick.n.01")],

	# bar, pub, cake
	"U+3c48":	[wn.synset("bar.n.02"),
				wn.synset("bar.n.03"),
				wn.synset("bar.n.05"),
				wn.synset("bar.n.07"),
				wn.synset("bar.n.08"),
				wn.synset("bar.n.13"),
				wn.synset("bar.n.14"),
				wn.synset("bar.n.15"),
				wn.synset("barroom.n.01"),
				wn.synset("browning_automatic_rifle.n.01"),
				wn.synset("cake.n.01"),
				wn.synset("cake.n.03"),
				wn.synset("legal_profession.n.01"),
				wn.synset("measure.n.07"),
				wn.synset("patty.n.01"),
				wn.synset("prevention.n.01"),
				wn.synset("stripe.n.05"),
				wn.synset("sweet.n.03")],

	# casserole
	"U+3c49":	[wn.synset("casserole.n.01"),
				wn.synset("casserole.n.02")],

	# charity
	"U+3c4a":	[wn.synset("charity.n.02"),
				wn.synset("charity.n.03")],

	# client, customer
	"U+3c4c":	[wn.synset("customer.n.01")],

	# pop music
	"U+3c4d":	[wn.synset("pop_music.n.01")],

	# challenge
	"U+3c4e":	[wn.synset("challenge.n.01")],

	# thinness, narrowness
	"U+3c4f":	[wn.synset("fineness.n.02"),
				wn.synset("leanness.n.02"),
				wn.synset("narrow-mindedness.n.01"),
				wn.synset("narrow_margin.n.01"),
				wn.synset("narrowness.n.01"),
				wn.synset("narrowness.n.03"),
				wn.synset("sparseness.n.01"),
				wn.synset("thinness.n.01"),
				wn.synset("thinness.n.05")],

	# worksheet
	"U+3c51":	[wn.synset("worksheet.n.01"),
				wn.synset("worksheet.n.02")],

	# bend
	"U+3c52":	[wn.synset("bend.v.01"),
				wn.synset("bend.v.02"),
				wn.synset("crouch.v.01"),
				wn.synset("deflect.v.02"),
				wn.synset("flex.v.04"),
				wn.synset("flex.v.05"),
				wn.synset("fold.v.01")],

	# lock
	"U+3c53":	[wn.synset("lock.v.01")],

	# ginger sauce
	"U+3c54":	[wn.synset("ginger.n.01"),
				wn.synset("ginger.n.03")],

	# ginger
	"U+3c55":	[wn.synset("ginger.n.03")],

	# slide, skid, slip
	"U+3c56":	[wn.synset("slither.v.01")],

	# birthday
	"U+3c57":	[wn.synset("birthday.n.01")],

	# frying pan
	"U+3c59":	[wn.synset("frying_pan.n.01"),
				wn.synset("pan.n.01")],

	# comedy
	"U+3c5b":	[wn.synset("comedy.n.01")],

	# notebook, writing book book
	"U+3c5c":	[wn.synset("notebook.n.01"),
				wn.synset("notebook.n.02")],

	# beach, bank, coast, shore
	"U+3c5e":	[wn.synset("beach.n.01")],

	# tomato
	"U+3c5f":	[wn.synset("tomato.n.01")],

	# red
	"U+3c60":	[wn.synset("red.n.01")],

	# dependency
	"U+3c61":	[wn.synset("addiction.n.01"),
				wn.synset("colony.n.05"),
				wn.synset("dependence.n.01")],

	# robot
	"U+3c62":	[wn.synset("automaton.n.02")],

	# Greece
	"U+3c64":	[wn.synset("greece.n.01")],

	# prison officer
	"U+3c65":	[wn.synset("prison_guard.n.01"),
				wn.synset("warder.n.01")],

	# thigh, upper leg leg
	"U+3c66":	[wn.synset("thigh.n.01")],

	# insight
	"U+3c67":	[wn.synset("insight.n.02"),
				wn.synset("insight.n.03"),
				wn.synset("insight.n.04"),
				wn.synset("intuition.n.01"),
				wn.synset("penetration.n.02")],

	# motorcycle, scooter
	"U+3c68":	[wn.synset("iceboat.n.02"),
				wn.synset("motor_scooter.n.01"),
				wn.synset("motorcycle.n.01"),
				wn.synset("scooter.n.02"),
				wn.synset("scoter.n.01"),
				wn.synset("water_scooter.n.01")],

	# volte
	"U+3c69":	[wn.synset("about-face.n.01"),
				wn.synset("about-face.n.02"),
				wn.synset("volta.n.01"),
				wn.synset("volta.n.02")],

	# perfect
	"U+3c6a":	[wn.synset("perfect.a.01")],

	# perfection
	"U+3c6b":	[wn.synset("perfection.n.01")],

	# cease fire, armistice
	"U+3c6c":	[wn.synset("armistice.n.01")],

	# dump, dispose
	"U+3c6d":	[wn.synset("deck.v.03"),
				wn.synset("discard.v.01"),
				wn.synset("dispose.v.01"),
				wn.synset("dispose.v.03"),
				wn.synset("dispose.v.04"),
				wn.synset("dump.v.01"),
				wn.synset("dump.v.02"),
				wn.synset("dump.v.03"),
				wn.synset("dump.v.04"),
				wn.synset("plunge.v.06"),
				wn.synset("qualify.v.04"),
				wn.synset("shed.v.01"),
				wn.synset("throw.v.01"),
				wn.synset("waste.v.01")],

	# horse sled, horse drawn sleigh
	"U+3c6f":	[wn.synset("sled.n.01")],

	# hobby, pastime
	"U+3c72":	[wn.synset("avocation.n.01")],

	# interesting, interested
	"U+3c73":	[wn.synset("interesting.a.01")],

	# burp, belch
	"U+3c74":	[wn.synset("burp.v.01")],

	# earn
	"U+3c76":	[wn.synset("earn.v.02"),
				wn.synset("gain.v.08")],

	# sugar, sweetener
	"U+3c77":	[wn.synset("sugar.n.01")],

	# cage
	"U+3c79":	[wn.synset("batting_cage.n.01"),
				wn.synset("cage.n.01"),
				wn.synset("cage.n.02"),
				wn.synset("cage.n.03"),
				wn.synset("cage.n.04")],

	# bridle, headstall
	"U+3c7b":	[wn.synset("bridle.n.01")],

	# muzzle
	"U+3c7c":	[wn.synset("gag.n.02"),
				wn.synset("gun_muzzle.n.01"),
				wn.synset("muzzle.n.02"),
				wn.synset("muzzle.n.03")],

	# day centre
	"U+3c7d":	[wn.synset("common_room.n.01"),
				wn.synset("community_center.n.01")],

	# glasses, eyeglasses
	"U+3c7f":	[wn.synset("spectacles.n.01")],

	# bump, press, pressing
	"U+3c81":	[wn.synset("blow.n.02"),
				wn.synset("bulge.n.01"),
				wn.synset("bump.n.01"),
				wn.synset("crush.n.02"),
				wn.synset("imperativeness.n.01"),
				wn.synset("press.n.02"),
				wn.synset("press.n.03"),
				wn.synset("press.n.06"),
				wn.synset("press.n.07"),
				wn.synset("press.n.08"),
				wn.synset("press.n.09"),
				wn.synset("pressing.n.02"),
				wn.synset("wardrobe.n.01")],

	# skin disease, eczema, skin disease,eczema
	"U+3c82":	[wn.synset("eczema.n.01")],

	# jigsaw puzzle
	"U+3c83":	[wn.synset("jigsaw_puzzle.n.01")],

	# frequency
	"U+3c84":	[wn.synset("frequency.n.01")],

	# watchdog
	"U+3c85":	[wn.synset("watchdog.n.01"),
				wn.synset("watchdog.n.02")],

	# witness
	"U+3c86":	[wn.synset("spectator.n.01"),
				wn.synset("witness.n.01"),
				wn.synset("witness.n.03"),
				wn.synset("witness.n.04"),
				wn.synset("witness.n.05")],

	# henhouse, chicken coop coop
	"U+3c87":	[wn.synset("chicken_coop.n.01")],

	# grid, matrix
	"U+3c88":	[wn.synset("matrix.n.01")],

	# sacking, dismissal
	"U+3c89":	[wn.synset("dismissal.n.02"),
				wn.synset("dismissal.n.03"),
				wn.synset("dismissal.n.04"),
				wn.synset("judgment_of_dismissal.n.01"),
				wn.synset("sacking.n.01")],

	# resignation
	"U+3c8a":	[wn.synset("resignation.n.01")],

	# microscope
	"U+3c8c":	[wn.synset("microscope.n.01")],

	# rectangular, oblong
	"U+3c8f":	[wn.synset("rectangular.s.01")],

	# songbird, finch, thrush
	"U+3c90":	[wn.synset("finch.n.01"),
				wn.synset("songbird.n.01"),
				wn.synset("thrush.n.01"),
				wn.synset("thrush.n.02"),
				wn.synset("thrush.n.03")],

	# graze
	"U+3c92":	[wn.synset("crop.v.04")],

	# eat
	"U+3c93":	[wn.synset("eat.v.01")],

	# thrilling, scary
	"U+3c95":	[wn.synset("chilling.s.01")],

	# fruit cream, compote, fruit cream,compote
	"U+3c96":	[wn.synset("compote.n.01")],

	# digital memory, digital storage, digital memory,digital storage, RAM, digital memory,RAM
	"U+3c97":	[wn.synset("aries.n.01"),
				wn.synset("aries.n.03"),
				wn.synset("memory.n.03"),
				wn.synset("memory.n.04"),
				wn.synset("ram.n.04"),
				wn.synset("ram.n.05"),
				wn.synset("random-access_memory.n.01")],

	# memory
	"U+3c98":	[wn.synset("memory.n.01"),
				wn.synset("memory.n.02"),
				wn.synset("memory.n.03"),
				wn.synset("memory.n.04")],

	# warm
	"U+3c99":	[wn.synset("warm.a.01")],

	# scarf
	"U+3c9b":	[wn.synset("scarf.n.01")],

	# neck
	"U+3c9c":	[wn.synset("neck.n.01")],

	# advocate, speaking), spokesperson
	"U+3c9d":	[wn.synset("champion.v.01"),
				wn.synset("defend.v.01"),
				wn.synset("defend.v.02"),
				wn.synset("defend.v.03"),
				wn.synset("defend.v.06"),
				wn.synset("fight.v.02"),
				wn.synset("preach.v.02"),
				wn.synset("recommend.v.01")],

	# spider web, cobweb, orb web, spider web,cobweb,orb web
	"U+3ca0":	[wn.synset("cobweb.n.01"),
				wn.synset("cobweb.n.02"),
				wn.synset("cobweb.n.03")],

	# parsnip
	"U+3ca1":	[wn.synset("parsnip.n.01"),
				wn.synset("parsnip.n.02"),
				wn.synset("parsnip.n.03")],

	# Iran
	"U+3ca2":	[wn.synset("iran.n.01")],

	# party, festival
	"U+3ca3":	[wn.synset("party.n.02")],

	# traveller
	"U+3ca4":	[wn.synset("traveler.n.01")],

	# Iraq
	"U+3ca5":	[wn.synset("iraq.n.01")],

	# projectile, rocket, spacecraft
	"U+3ca6":	[wn.synset("projectile.n.01"),
				wn.synset("rocket.n.01")],

	# painful, painfully, sore
	"U+3ca7":	[wn.synset("painful.a.01")],

	# shorts
	"U+3ca9":	[wn.synset("short_pants.n.01")],

	# water snake
	"U+3cab":	[wn.synset("colubrid_snake.n.01"),
				wn.synset("garter_snake.n.01"),
				wn.synset("grass_snake.n.01"),
				wn.synset("hoop_snake.n.01"),
				wn.synset("whip-snake.n.01")],

	# boring, dull, depressing
	"U+3cac":	[wn.synset("boring.s.01")],

	# monotheism
	"U+3cad":	[wn.synset("monotheism.n.01")],

	# steel
	"U+3cae":	[wn.synset("steel.n.01")],

	# hymn, psalm, gospel song song
	"U+3caf":	[wn.synset("hymn.n.01"),
				wn.synset("psalm.n.01")],

	# reproduction
	"U+3cb0":	[wn.synset("reproduction.n.01")],

	# devotion
	"U+3cb1":	[wn.synset("devotion.n.01"),
				wn.synset("devotion.n.02"),
				wn.synset("devotion.n.04"),
				wn.synset("idolatry.n.01")],

	# important, significant
	"U+3cb2":	[wn.synset("important.a.01"),
				wn.synset("significant.a.01")],

	# beggar
	"U+3cb3":	[wn.synset("beggar.n.01")],

	# ask, inquire, question
	"U+3cb4":	[wn.synset("ask.v.01")],

	# deodorant
	"U+3cb9":	[wn.synset("deodorant.n.01")],

	# connector, interface box box
	"U+3cba":	[wn.synset("connection.n.03")],

	# tonight
	"U+3cbb":	[wn.synset("tonight.n.01")],

	# football, soccer
	"U+3cbd":	[wn.synset("soccer.n.01")],

	# bacterium
	"U+3cbf":	[wn.synset("bacteria.n.01")],

	# bassoon
	"U+3cc0":	[wn.synset("bassoon.n.01")],

	# oboe
	"U+3cc1":	[wn.synset("oboe.n.01")],

	# tenor
	"U+3cc2":	[wn.synset("tenor.n.01"),
				wn.synset("tenor.n.03")],

	# cry out, call, cry telephone, ring
	"U+3cc3":	[wn.synset("call.v.03")],

	# ashore
	"U+3cc4":	[wn.synset("ashore.r.01")],

	# wideness, broadness
	"U+3cc5":	[wn.synset("enormousness.n.01"),
				wn.synset("wideness.n.01"),
				wn.synset("width.n.01")],

	# soap, detergent
	"U+3cc6":	[wn.synset("soap.n.01")],

	# raindrop
	"U+3cc8":	[wn.synset("raindrop.n.01")],

	# cipher
	"U+3cc9":	[wn.synset("cipher.n.01"),
				wn.synset("cipher.n.04"),
				wn.synset("cipher.n.05"),
				wn.synset("code.n.02"),
				wn.synset("nothing.n.01"),
				wn.synset("zero.n.02")],

	# thanksgiving
	"U+3cca":	[wn.synset("grace.n.06"),
				wn.synset("grace.n.07"),
				wn.synset("thanksgiving.n.01")],

	# thanks, thank you you
	"U+3ccb":	[wn.synset("thanks.n.01"),
				wn.synset("thanks.n.02")],

	# measuring cup
	"U+3ccc":	[wn.synset("measuring_stick.n.01")],

	# economist
	"U+3cce":	[wn.synset("economist.n.01")],

	# economics
	"U+3ccf":	[wn.synset("economic.a.01"),
				wn.synset("economics.n.01")],

	# principal, headteacher
	"U+3cd0":	[wn.synset("principal.n.01"),
				wn.synset("principal.n.02"),
				wn.synset("principal.n.04"),
				wn.synset("principal.n.05"),
				wn.synset("principal.n.06"),
				wn.synset("star.n.04")],

	# police officer, policeman, policewoman, police officer,policeman,policewoman
	"U+3cd1":	[wn.synset("policeman.n.01")],

	# should, would
	"U+3cd2":	[wn.synset("have.v.10"),
				wn.synset("need.v.03"),
				wn.synset("owe.v.03")],

	# jam, jelly, marmalade, preserves
	"U+3cd3":	[wn.synset("jam.n.01")],

	# ribbon, tape
	"U+3cd4":	[wn.synset("decoration.n.02"),
				wn.synset("magnetic_tape.n.01"),
				wn.synset("ribbon.n.01"),
				wn.synset("ribbon.n.03"),
				wn.synset("ribbon.n.04"),
				wn.synset("tape.n.01"),
				wn.synset("tape.n.02"),
				wn.synset("tape.n.03"),
				wn.synset("tape.n.04")],

	# hope
	"U+3cd5":	[wn.synset("hope.v.01"),
				wn.synset("hope.v.02"),
				wn.synset("hope.v.03")],

	# movement, motion
	"U+3cd7":	[wn.synset("gesture.n.02"),
				wn.synset("motion.n.03"),
				wn.synset("motion.n.06"),
				wn.synset("movement.n.04"),
				wn.synset("movement.n.05"),
				wn.synset("movement.n.10")],

	# handle
	"U+3cd9":	[wn.synset("handle.n.01")],

	# lucky, fortunate
	"U+3cda":	[wn.synset("fortunate.a.01"),
				wn.synset("fortunate.s.02"),
				wn.synset("fortunate.s.03"),
				wn.synset("golden.s.06"),
				wn.synset("lucky.a.02"),
				wn.synset("lucky.s.01")],

	# wiggle, squirm
	"U+3cdb":	[wn.synset("jiggle.v.01"),
				wn.synset("rock.v.01"),
				wn.synset("swing.v.02"),
				wn.synset("vibrate.v.01"),
				wn.synset("writhe.v.01")],

	# string bean, green bean, runner bean, wax bean, string bean,green bean,runner bean,wax bean
	"U+3cdc":	[wn.synset("cowpea.n.02")],

	# exchanger
	"U+3cdd":	[wn.synset("exchanger.n.01")],

	# dance music
	"U+3cde":	[wn.synset("dance_music.n.01"),
				wn.synset("dance_music.n.02")],

	# rein
	"U+3cdf":	[wn.synset("rein.n.01"),
				wn.synset("rein.n.02")],

	# season
	"U+3ce1":	[wn.synset("season.n.01"),
				wn.synset("season.n.02")],

	# darkness
	"U+3ce2":	[wn.synset("dark.n.01")],

	# oven tray
	"U+3ce3":	[wn.synset("phonograph_record.n.01"),
				wn.synset("platinum.n.01"),
				wn.synset("platter.n.01")],

	# pail, bucket
	"U+3ce4":	[wn.synset("bucket.n.01")],

	# sexual arousal, sexual excitement
	"U+3ce5":	[wn.synset("craving.n.01"),
				wn.synset("sexual_desire.n.01")],

	# finger spelling, finger alphabet
	"U+3ce6":	[wn.synset("finger_spelling.n.01"),
				wn.synset("manual_alphabet.n.01")],

	# pencil case, pencil box
	"U+3ce7":	[wn.synset("pencil_box.n.01")],

	# handgun, pistol
	"U+3ce8":	[wn.synset("pistol.n.01")],

	# e mail, email, e-mail,email
	"U+3ce9":	[wn.synset("electronic_mail.n.01")],

	# drum
	"U+3ced":	[wn.synset("drum.n.01")],

	# ramp
	"U+3cee":	[wn.synset("ramp.n.01")],

	# doorway, gate
	"U+3cef":	[wn.synset("gate.n.01")],

	# Jesus, Jesus Christ, Christ
	"U+3cf0":	[wn.synset("jesus.n.01"),
				wn.synset("messiah.n.01")],

	# semi detached house, semi-detached house
	"U+3cf1":	[wn.synset("business.n.01"),
				wn.synset("diggings.n.02"),
				wn.synset("dwelling.n.01"),
				wn.synset("dynasty.n.01"),
				wn.synset("family.n.01"),
				wn.synset("home.n.03"),
				wn.synset("house.n.01"),
				wn.synset("mansion.n.02"),
				wn.synset("residence.n.01"),
				wn.synset("sign_of_the_zodiac.n.01"),
				wn.synset("square.n.07")],

	# letter carrier, postman, mailman, letter carrier,postman,mailman
	"U+3cf2":	[wn.synset("mailman.n.01")],

	# feather
	"U+3cf3":	[wn.synset("feather.n.01")],

	# homosexual, lesbian, gay
	"U+3cf4":	[wn.synset("brave.s.03"),
				wn.synset("cheery.s.01"),
				wn.synset("gay.s.02"),
				wn.synset("gay.s.03"),
				wn.synset("gay.s.05"),
				wn.synset("gay.s.06"),
				wn.synset("homosexual.a.01"),
				wn.synset("homosexuality.n.01")],

	# neighbour
	"U+3cf6":	[wn.synset("neighbor.n.01")],

	# Epiphany
	"U+3cf7":	[wn.synset("epiphany.n.02")],

	# runway
	"U+3cf8":	[wn.synset("runway.n.04")],

	# intranet
	"U+3cfa":	[wn.synset("intranet.n.01")],

	# bathtub, bath, tub
	"U+3cfc":	[wn.synset("bathtub.n.01")],

	# sink, basin
	"U+3cfd":	[wn.synset("sink.n.01")],

	# lust
	"U+3cfe":	[wn.synset("lecherousness.n.01"),
				wn.synset("lust.n.02")],

	# sex drive, sexual urge, libido, sex drive,sexual urge,libido
	"U+3cff":	[wn.synset("craving.n.01"),
				wn.synset("libido.n.01"),
				wn.synset("sex_drive.n.01"),
				wn.synset("sexual_desire.n.01")],

	# birth control
	"U+3d02":	[wn.synset("contraception.n.01")],

	# mountain bike
	"U+3d04":	[wn.synset("mountain_bike.n.01"),
				wn.synset("trail_bike.n.01")],

	# overspend, buy over budget over budget
	"U+3d05":	[wn.synset("overspend.v.01"),
				wn.synset("overspend.v.02"),
				wn.synset("spend.v.02")],

	# often, frequent, frequently
	"U+3d07":	[wn.synset("frequently.r.01")],

	# cremation
	"U+3d08":	[wn.synset("cremation.n.01")],

	# terrorist
	"U+3d09":	[wn.synset("terrorist.n.01")],

	# terrorism
	"U+3d0a":	[wn.synset("terrorism.n.01")],

	# woman doll
	"U+3d0b":	[wn.synset("doll.n.01")],

	# terror, panic
	"U+3d0c":	[wn.synset("panic.n.01")],

	# nervous system
	"U+3d0e":	[wn.synset("nervous_system.n.01")],

	# neuron
	"U+3d0f":	[wn.synset("nerve_cell.n.01")],

	# eternity, infinity
	"U+3d10":	[wn.synset("eternity.n.01"),
				wn.synset("eternity.n.02"),
				wn.synset("eternity.n.03")],

	# swordfish
	"U+3d11":	[wn.synset("swordfish.n.02")],

	# broccoli
	"U+3d13":	[wn.synset("broccoli.n.02")],

	# green
	"U+3d14":	[wn.synset("green.n.01")],

	# rifle, shotgun
	"U+3d17":	[wn.synset("rifle.n.01")],

	# glue, adhesive, paste, stick, log
	"U+3d18":	[wn.synset("glue.n.01")],

	# noisemaker, musical toy toy
	"U+3d1a":	[wn.synset("noisemaker.n.01")],

	# arrest
	"U+3d1b":	[wn.synset("collar.v.01")],

	# cookie jar, biscuit tin
	"U+3d1c":	[wn.synset("cookie.n.01")],

	# scoundrel, villain
	"U+3d1e":	[wn.synset("rogue.n.01"),
				wn.synset("villain.n.01"),
				wn.synset("villain.n.02")],

	# pill, tablet
	"U+3d20":	[wn.synset("pill.n.01"),
				wn.synset("pill.n.02")],

	# government
	"U+3d22":	[wn.synset("government.n.01"),
				wn.synset("government.n.02")],

	# hiding place, cache, hiding place,cache
	"U+3d25":	[wn.synset("bolt-hole.n.01"),
				wn.synset("cache.n.01"),
				wn.synset("cache.n.03"),
				wn.synset("cubby.n.01"),
				wn.synset("hideout.n.01"),
				wn.synset("hiding_place.n.01"),
				wn.synset("hoard.n.01"),
				wn.synset("lurking_place.n.01"),
				wn.synset("retreat.n.02"),
				wn.synset("screen.n.04")],

	# placenta
	"U+3d29":	[wn.synset("placenta.n.02")],

	# you are welcome, you're welcome, you are welcome,you're welcome
	"U+3d2a":	[wn.synset("welcome.n.01"),
				wn.synset("welcome.n.02")],

	# potato chip, chip, crisp
	"U+3d2c":	[wn.synset("chip.n.04")],

	# dove
	"U+3d2d":	[wn.synset("columba.n.01"),
				wn.synset("dove.n.01"),
				wn.synset("dove.n.02"),
				wn.synset("dove.n.05"),
				wn.synset("pigeon.n.01"),
				wn.synset("squab.n.01")],

	# become
	"U+3d2e":	[wn.synset("become.v.01"),
				wn.synset("become.v.02")],

	# thief
	"U+3d2f":	[wn.synset("thief.n.01")],

	# electric current
	"U+3d30":	[wn.synset("current.n.01")],

	# gymnastics
	"U+3d31":	[wn.synset("gymnastics.n.01")],

	# ballot, voting slip slip
	"U+3d32":	[wn.synset("ballot.n.01"),
				wn.synset("vote.n.01")],

	# blue
	"U+3d34":	[wn.synset("amobarbital_sodium.n.01"),
				wn.synset("blue.n.01"),
				wn.synset("blue.n.02"),
				wn.synset("blue.n.03"),
				wn.synset("blue.n.07"),
				wn.synset("blue_sky.n.01"),
				wn.synset("bluing.n.01")],

	# public transport
	"U+3d35":	[wn.synset("public_transport.n.01")],

	# history
	"U+3d36":	[wn.synset("history.n.01"),
				wn.synset("history.n.02"),
				wn.synset("history.n.03"),
				wn.synset("history.n.04"),
				wn.synset("history.n.05")],

	# saucepan
	"U+3d37":	[wn.synset("pot.n.01"),
				wn.synset("pot.n.03"),
				wn.synset("saucepan.n.01")],

	# forgiven
	"U+3d38":	[wn.synset("forgive.v.01")],

	# biology
	"U+3d39":	[wn.synset("biology.n.01")],

	# schedule, timetable
	"U+3d3b":	[wn.synset("agenda.n.01"),
				wn.synset("agenda.n.02"),
				wn.synset("broadcast.n.02"),
				wn.synset("notebook.n.01"),
				wn.synset("plan.n.01"),
				wn.synset("platform.n.02"),
				wn.synset("playbill.n.01"),
				wn.synset("program.n.02"),
				wn.synset("program.n.07"),
				wn.synset("schedule.n.02"),
				wn.synset("timetable.n.01"),
				wn.synset("timetable.n.02")],

	# pressure
	"U+3d3c":	[wn.synset("pressure.n.01")],

	# Yahrzeit
	"U+3d3d":	[wn.synset("yahweh.n.01")],

	# anniversary
	"U+3d3e":	[wn.synset("anniversary.n.01")],

	# iris
	"U+3d3f":	[wn.synset("iris.n.01"),
				wn.synset("iris.n.02"),
				wn.synset("iris.n.03")],

	# sister
	"U+3d40":	[wn.synset("sister.n.01")],

	# conductor, therapist)
	"U+3d41":	[wn.synset("conductor.n.02")],

	# software, computer program, application, app program,application,app
	"U+3d43":	[wn.synset("software.n.01")],

	# Virgo
	"U+3d44":	[wn.synset("virgo.n.01"),
				wn.synset("virgo.n.02"),
				wn.synset("virgo.n.03")],

	# lung
	"U+3d45":	[wn.synset("lung.n.01")],

	# frustration
	"U+3d46":	[wn.synset("frustration.n.01")],

	# catamaran, pontoon boat boat
	"U+3d47":	[wn.synset("catamaran.n.01")],

	# hull, body
	"U+3d48":	[wn.synset("hull.n.06")],

	# circulatory system
	"U+3d49":	[wn.synset("circulatory_system.n.01")],

	# function
	"U+3d4a":	[wn.synset("function.v.01")],

	# funnel
	"U+3d4b":	[wn.synset("funnel.n.02")],

	# rectum
	"U+3d4e":	[wn.synset("rectum.n.01")],

	# count
	"U+3d4f":	[wn.synset("count.v.01")],

	# community centre, town hall, village hall, community centre,town hall,village hall
	"U+3d50":	[wn.synset("town_hall.n.01")],

	# smooth
	"U+3d51":	[wn.synset("fluent.s.01"),
				wn.synset("legato.a.01"),
				wn.synset("placid.s.01"),
				wn.synset("politic.s.02"),
				wn.synset("smooth.a.01"),
				wn.synset("smooth.a.03"),
				wn.synset("smooth.a.06"),
				wn.synset("smooth.s.07")],

	# persuade, convince
	"U+3d52":	[wn.synset("convert.v.09")],

	# persuasion
	"U+3d53":	[wn.synset("conviction.n.01"),
				wn.synset("opinion.n.01"),
				wn.synset("persuasion.n.01")],

	# monument, commemorative work work
	"U+3d54":	[wn.synset("memorial.n.03")],

	# problem
	"U+3d55":	[wn.synset("problem.n.02")],

	# make believe woman, make-believe woman
	"U+3d56":	[wn.synset("imaginary_being.n.01")],

	# menstruation, menstrual period, period period,period
	"U+3d57":	[wn.synset("menstruation.n.01")],

	# spiritual awareness
	"U+3d58":	[wn.synset("spirituality.n.02"),
				wn.synset("spiritualty.n.01")],

	# speech impaired
	"U+3d59":	[wn.synset("gruffness.n.01")],

	# speech impairment, dysarthria, speech impairment,dysarthria
	"U+3d5a":	[wn.synset("dysarthria.n.01")],

	# February
	"U+3d5d":	[wn.synset("february.n.01")],

	# chance, risk
	"U+3d5e":	[wn.synset("risk.n.02")],

	# maracas, calabash
	"U+3d5f":	[wn.synset("calabash.n.01")],

	# veil
	"U+3d61":	[wn.synset("head_covering.n.01")],

	# inspiration
	"U+3d62":	[wn.synset("inspiration.n.03")],

	# fruit salad
	"U+3d63":	[wn.synset("fruit_cocktail.n.01"),
				wn.synset("fruit_salad.n.01")],

	# govern, rule
	"U+3d64":	[wn.synset("govern.v.03")],

	# post office
	"U+3d66":	[wn.synset("post_office.n.01")],

	# write
	"U+3d67":	[wn.synset("spell.v.03"),
				wn.synset("write.v.01"),
				wn.synset("write.v.02"),
				wn.synset("write.v.07")],

	# front, front of a thing of a thing
	"U+3d6a":	[wn.synset("battlefront.n.01"),
				wn.synset("front.n.01"),
				wn.synset("front.n.03"),
				wn.synset("front.n.04"),
				wn.synset("front.n.06"),
				wn.synset("front.n.07"),
				wn.synset("front.n.09"),
				wn.synset("front_man.n.01"),
				wn.synset("movement.n.04"),
				wn.synset("presence.n.02")],

	# desirable
	"U+3d6b":	[wn.synset("desirable.a.01")],

	# kindergarten, preschool, nursery, play group group
	"U+3d6d":	[wn.synset("greenhouse.n.01"),
				wn.synset("kindergarten.n.01"),
				wn.synset("nursery.n.01"),
				wn.synset("preschool.n.01")],

	# protected, saved, sheltered
	"U+3d6e":	[wn.synset("protected.a.01")],

	# voter, elector
	"U+3d6f":	[wn.synset("voter.n.01")],

	# firecraft
	"U+3d71":	[wn.synset("campfire.n.01")],

	# alternating
	"U+3d72":	[wn.synset("alternate.s.03"),
				wn.synset("alternating.a.01"),
				wn.synset("varied.a.01")],

	# alternation
	"U+3d73":	[wn.synset("alternation.n.01")],

	# geology
	"U+3d74":	[wn.synset("geology.n.01")],

	# venereal papilloma
	"U+3d76":	[wn.synset("papilloma.n.01")],

	# whisk, beater
	"U+3d77":	[wn.synset("beater.n.01"),
				wn.synset("beater.n.02"),
				wn.synset("whisk.n.01"),
				wn.synset("whisk.n.02")],

	# detective, investigator
	"U+3d79":	[wn.synset("detective.n.01")],

	# humidity
	"U+3d7a":	[wn.synset("humidity.n.01")],

	# subject
	"U+3d7b":	[wn.synset("subject.n.01"),
				wn.synset("subject.n.02"),
				wn.synset("subject.n.05"),
				wn.synset("topic.n.02")],

	# chew
	"U+3d7c":	[wn.synset("chew.v.01")],

	# midsummer
	"U+3d7e":	[wn.synset("summer_solstice.n.01")],

	# cook, chef
	"U+3d7f":	[wn.synset("cook.n.01")],

	# lizard, reptile
	"U+3d81":	[wn.synset("lizard.n.01")],

	# plug in, connect, plug in,connect
	"U+3d83":	[wn.synset("associate.v.01"),
				wn.synset("connect.v.01"),
				wn.synset("connect.v.03"),
				wn.synset("connect.v.04"),
				wn.synset("connect.v.06"),
				wn.synset("get_in_touch.v.01"),
				wn.synset("plug_in.v.01")],

	# plug
	"U+3d84":	[wn.synset("ballyhoo.n.01"),
				wn.synset("bunghole.n.02"),
				wn.synset("chew.n.01"),
				wn.synset("fireplug.n.01"),
				wn.synset("fishbone.n.01"),
				wn.synset("hack.n.06"),
				wn.synset("plug.n.01"),
				wn.synset("plug.n.05"),
				wn.synset("spark_plug.n.01"),
				wn.synset("spine.n.03")],

	# celebration
	"U+3d87":	[wn.synset("celebration.n.01")],

	# Tuesday
	"U+3d88":	[wn.synset("tuesday.n.01")],

	# Simchat Torah
	"U+3d89":	[wn.synset("succoth.n.01")],

	# Torah
	"U+3d8a":	[wn.synset("torah.n.03")],

	# double bass, bass fiddle, contrabass, double bass,bass fiddle,contrabass
	"U+3d8b":	[wn.synset("bass_fiddle.n.01")],

	# stressed
	"U+3d8d":	[wn.synset("stressed.a.02"),
				wn.synset("stressed.s.01"),
				wn.synset("taut.s.01")],

	# lonely, lonesome
	"U+3d8e":	[wn.synset("alone.s.02"),
				wn.synset("lone.s.02"),
				wn.synset("lone.s.03"),
				wn.synset("lonely.s.02"),
				wn.synset("lonely.s.04")],

	# envious
	"U+3d8f":	[wn.synset("covetous.s.01")],

	# Jew
	"U+3d91":	[wn.synset("jew.n.01")],

	# stomach flu
	"U+3d92":	[wn.synset("vomit.n.03")],

	# bra, brassiere
	"U+3d93":	[wn.synset("brassiere.n.01")],

	# motivate
	"U+3d94":	[wn.synset("motivate.v.01")],

	# motivation
	"U+3d95":	[wn.synset("motivation.n.01"),
				wn.synset("motivation.n.02"),
				wn.synset("motivation.n.03")],

	# blueberry
	"U+3d97":	[wn.synset("bilberry.n.03"),
				wn.synset("blueberry.n.01"),
				wn.synset("blueberry.n.02")],

	# stickball
	"U+3d98":	[wn.synset("stickball.n.01")],

	# geographer
	"U+3d99":	[wn.synset("geographer.n.01")],

	# hug, cuddle, embrace, squeeze
	"U+3d9a":	[wn.synset("credit_crunch.n.01"),
				wn.synset("embrace.n.01"),
				wn.synset("embrace.n.02"),
				wn.synset("embrace.n.03"),
				wn.synset("hug.n.01"),
				wn.synset("power_play.n.01"),
				wn.synset("squeeze.n.01"),
				wn.synset("squeeze.n.03"),
				wn.synset("squeeze.n.04"),
				wn.synset("squeeze.n.05"),
				wn.synset("squeeze.n.08")],

	# mechanic, technician
	"U+3d9b":	[wn.synset("automobile_mechanic.n.01"),
				wn.synset("machinist.n.01"),
				wn.synset("technician.n.01"),
				wn.synset("technician.n.02")],

	# document, written record record, digital document
	"U+3d9c":	[wn.synset("document.n.01")],

	# violin
	"U+3d9d":	[wn.synset("violin.n.01")],

	# CD player, record player, stereo, CD player,record player,stereo
	"U+3d9f":	[wn.synset("record_player.n.01"),
				wn.synset("stereo.n.01"),
				wn.synset("stereo.n.02")],

	# tattoo, picture on skin on skin
	"U+3da2":	[wn.synset("tattoo.n.02")],

	# gamble
	"U+3da3":	[wn.synset("bet.v.01"),
				wn.synset("bet.v.02"),
				wn.synset("gamble.n.01"),
				wn.synset("gamble.n.02"),
				wn.synset("play.v.10")],

	# pizza slice, sector, circle sector
	"U+3da4":	[wn.synset("sector.n.03")],

	# sugar lump, cube, sugar lump,cube
	"U+3da7":	[wn.synset("block.n.03"),
				wn.synset("cube.n.01"),
				wn.synset("cube.n.03"),
				wn.synset("cube.n.04"),
				wn.synset("cube.n.05")],

	# fever, temperature
	"U+3da8":	[wn.synset("fever.n.01")],

	# body temperature
	"U+3da9":	[wn.synset("body_temperature.n.01")],

	# day care centre
	"U+3daa":	[wn.synset("day_nursery.n.01")],

	# birth control pill, pill, birth control pill,pill
	"U+3dac":	[wn.synset("pill.n.01"),
				wn.synset("pill.n.02"),
				wn.synset("pill.n.03"),
				wn.synset("pill.n.04"),
				wn.synset("pill.n.05")],

	# astronaut, cosmonaut
	"U+3dae":	[wn.synset("astronaut.n.01")],

	# appreciate, value, treasure
	"U+3daf":	[wn.synset("appreciate.v.01"),
				wn.synset("appreciate.v.02"),
				wn.synset("appreciate.v.04"),
				wn.synset("appreciate.v.05"),
				wn.synset("care_for.v.02"),
				wn.synset("measure.v.04"),
				wn.synset("prize.v.01"),
				wn.synset("rate.v.03"),
				wn.synset("respect.v.01"),
				wn.synset("value.v.01")],

	# waiter, waitress
	"U+3db1":	[wn.synset("waiter.n.01")],

	# ambulance
	"U+3db2":	[wn.synset("ambulance.n.01")],

	# popsicle
	"U+3db3":	[wn.synset("ice_lolly.n.01")],

	# office
	"U+3db4":	[wn.synset("agency.n.01"),
				wn.synset("office.n.01")],

	# muffin, bun, roll, scone, brioche
	"U+3db5":	[wn.synset("bun.n.01")],

	# lower body
	"U+3db6":	[wn.synset("underbelly.n.02")],

	# adolescence
	"U+3db8":	[wn.synset("adolescence.n.01"),
				wn.synset("adolescence.n.02")],

	# anywhere, anyplace, someplace, somewhere
	"U+3dba":	[wn.synset("anywhere.r.01"),
				wn.synset("somewhere.n.01"),
				wn.synset("somewhere.r.01")],

	# male friend
	"U+3dbb":	[wn.synset("acquaintance.n.03")],

	# friend
	"U+3dbc":	[wn.synset("friend.n.01")],

	# owl, night bird bird
	"U+3dbd":	[wn.synset("owl.n.01")],

	# coffee
	"U+3dbf":	[wn.synset("coffee.n.01")],

	# ashes
	"U+3dc2":	[wn.synset("ash.n.01")],

	# influenced, affected
	"U+3dc3":	[wn.synset("affected.a.01"),
				wn.synset("affected.a.02"),
				wn.synset("charm.v.04"),
				wn.synset("determine.v.02"),
				wn.synset("influence.v.01"),
				wn.synset("moved.a.01")],

	# safe, safely, secure, securely
	"U+3dc4":	[wn.synset("dependable.s.04"),
				wn.synset("impregnable.s.01"),
				wn.synset("safe.a.01"),
				wn.synset("safe.a.03"),
				wn.synset("safe.s.02"),
				wn.synset("safely.r.01"),
				wn.synset("secure.a.01"),
				wn.synset("secure.a.02"),
				wn.synset("secure.a.03"),
				wn.synset("securely.r.01"),
				wn.synset("securely.r.02"),
				wn.synset("securely.r.03"),
				wn.synset("securely.r.04")],

	# safety, security
	"U+3dc5":	[wn.synset("safety.n.01")],

	# rest period, break, rest period,break
	"U+3dc6":	[wn.synset("pause.n.01")],

	# port
	"U+3dca":	[wn.synset("interface.n.04"),
				wn.synset("larboard.n.01"),
				wn.synset("pass.n.04"),
				wn.synset("port.n.01"),
				wn.synset("port.n.02"),
				wn.synset("port.n.03"),
				wn.synset("seaport.n.01")],

	# cartography
	"U+3dcd":	[wn.synset("mapmaking.n.01")],

	# map
	"U+3dce":	[wn.synset("map.n.01")],

	# prawn
	"U+3dcf":	[wn.synset("prawn.n.01"),
				wn.synset("prawn.n.02"),
				wn.synset("shrimp.n.03")],

	# residential institution, group home, hostel, residential home, residential institution,group home,hostel,residential home
	"U+3dd1":	[wn.synset("boarding_school.n.01"),
				wn.synset("hostel.n.01"),
				wn.synset("hostel.n.02"),
				wn.synset("internship.n.01")],

	# fanatic
	"U+3dd3":	[wn.synset("fanatic.s.01")],

	# barrier
	"U+3dd6":	[wn.synset("barrier.n.03")],

	# venereal disease
	"U+3dd7":	[wn.synset("venereal_disease.n.01")],

	# large intestine
	"U+3dd8":	[wn.synset("colon.n.01")],

	# female friend
	"U+3dd9":	[wn.synset("acquaintance.n.03")],

	# September
	"U+3dda":	[wn.synset("september.n.01")],

	# organize, arrange
	"U+3ddd":	[wn.synset("arrange.v.01"),
				wn.synset("arrange.v.02"),
				wn.synset("arrange.v.06"),
				wn.synset("arrange.v.07"),
				wn.synset("dress.v.16"),
				wn.synset("form.v.01"),
				wn.synset("format.v.01"),
				wn.synset("mastermind.v.01"),
				wn.synset("organize.v.02"),
				wn.synset("organize.v.04"),
				wn.synset("organize.v.05"),
				wn.synset("stage.v.02"),
				wn.synset("unionize.v.02")],

	# disembark
	"U+3de0":	[wn.synset("disembark.v.01")],

	# fat, thick
	"U+3de2":	[wn.synset("thick.a.01")],

	# fatness, thickness
	"U+3de3":	[wn.synset("fatness.n.01"),
				wn.synset("thickness.n.01"),
				wn.synset("thickness.n.02"),
				wn.synset("thickness.n.03"),
				wn.synset("thickness.n.04")],

	# illustrate
	"U+3de5":	[wn.synset("illustrate.v.03")],

	# inflate
	"U+3de7":	[wn.synset("balloon.v.02"),
				wn.synset("inflate.v.01"),
				wn.synset("inflate.v.02"),
				wn.synset("inflate.v.03"),
				wn.synset("inflate.v.04")],

	# van, minibus
	"U+3de8":	[wn.synset("avant-garde.n.01"),
				wn.synset("minibus.n.01"),
				wn.synset("van.n.03"),
				wn.synset("van.n.04"),
				wn.synset("van.n.05"),
				wn.synset("vanguard.n.01")],

	# hike
	"U+3de9":	[wn.synset("call_at.v.01"),
				wn.synset("hike.v.01"),
				wn.synset("hike.v.02"),
				wn.synset("layer.v.01"),
				wn.synset("scale.v.04"),
				wn.synset("subtract.v.01")],

	# hiking
	"U+3dea":	[wn.synset("hike.n.01")],

	# Allah
	"U+3deb":	[wn.synset("allah.n.01")],

	# guilt
	"U+3ded":	[wn.synset("guilt.n.01"),
				wn.synset("guilt.n.02")],

	# soda pop, pop, soft drink, soda pop,pop,soft drink
	"U+3dee":	[wn.synset("dad.n.01"),
				wn.synset("pop.n.02"),
				wn.synset("pop.n.03"),
				wn.synset("pop_music.n.01")],

	# house work, housekeeping, housework, house work,housekeeping,housework
	"U+3df0":	[wn.synset("housework.n.01")],

	# Shavuot
	"U+3df4":	[wn.synset("shavous.n.01")],

	# Christianity
	"U+3df5":	[wn.synset("christendom.n.01"),
				wn.synset("christianity.n.01")],

	# silversmith
	"U+3df6":	[wn.synset("silversmith.n.01")],

	# alcoholism, alcohol addiction addiction
	"U+3df7":	[wn.synset("alcoholism.n.01")],

	# alcohol abuse, alcohol addiction
	"U+3df8":	[wn.synset("alcoholism.n.01")],

	# podiatrist, chiropodist
	"U+3df9":	[wn.synset("chiropodist.n.01")],

	# broadcast, transmit
	"U+3dfa":	[wn.synset("air.v.03"),
				wn.synset("broadcast.v.02"),
				wn.synset("circulate.v.02"),
				wn.synset("convey.v.03"),
				wn.synset("impart.v.03"),
				wn.synset("transmit.v.04")],

	# cordless phone
	"U+3dfb":	[wn.synset("telephone.n.01")],

	# drying room, drying chamber
	"U+3dfc":	[wn.synset("dryer.n.01")],

	# landing gear
	"U+3dfe":	[wn.synset("landing_gear.n.01"),
				wn.synset("landing_skid.n.01")],

	# glove, mitt, mitten
	"U+3dff":	[wn.synset("glove.n.02")],

	# cane, stick, walking stick stick
	"U+3e00":	[wn.synset("cane.n.01"),
				wn.synset("cane.n.02"),
				wn.synset("cane.n.03"),
				wn.synset("joint.n.06"),
				wn.synset("pin.n.05"),
				wn.synset("stick.n.01"),
				wn.synset("stick.n.02"),
				wn.synset("stick.n.03"),
				wn.synset("stick.n.04"),
				wn.synset("stick.n.06"),
				wn.synset("stick.n.07"),
				wn.synset("stick.n.09")],

	# nephew
	"U+3e01":	[wn.synset("nephew.n.01")],

	# village
	"U+3e03":	[wn.synset("village.n.01")],

	# geyser
	"U+3e04":	[wn.synset("geyser.n.01")],

	# synthetic fabric
	"U+3e06":	[wn.synset("synthetic.n.01")],

	# geologist
	"U+3e07":	[wn.synset("geologist.n.01")],

	# Elul
	"U+3e08":	[wn.synset("elul.n.01")],

	# personality
	"U+3e09":	[wn.synset("personality.n.01")],

	# steak
	"U+3e0c":	[wn.synset("steak.n.01")],

	# steal
	"U+3e0d":	[wn.synset("steal.v.01")],

	# manager, secretary
	"U+3e0f":	[wn.synset("coach.n.01"),
				wn.synset("director.n.01"),
				wn.synset("repository.n.02"),
				wn.synset("secretary.n.01"),
				wn.synset("secretary.n.02"),
				wn.synset("secretary.n.04")],

	# uninhabited
	"U+3e10":	[wn.synset("uninhabited.a.01")],

	# lemonade
	"U+3e11":	[wn.synset("lemonade.n.01")],

	# termite
	"U+3e12":	[wn.synset("termite.n.01")],

	# Christian hope
	"U+3e14":	[wn.synset("jump.n.01")],

	# unfold
	"U+3e15":	[wn.synset("unfold.v.04")],

	# unfolding
	"U+3e16":	[wn.synset("unfolding.n.01")],

	# horsehair
	"U+3e17":	[wn.synset("horsehair.n.01"),
				wn.synset("horsehair.n.02")],

	# kitchen
	"U+3e18":	[wn.synset("kitchen.n.01")],

	# climate
	"U+3e19":	[wn.synset("climate.n.01")],

	# speech therapist
	"U+3e1a":	[wn.synset("speech_therapist.n.01")],

	# hummus
	"U+3e1b":	[wn.synset("hummus.n.01")],

	# cod
	"U+3e1c":	[wn.synset("cod.n.03")],

	# receiver, dish
	"U+3e1e":	[wn.synset("cup_of_tea.n.01"),
				wn.synset("dish.n.01"),
				wn.synset("dish.n.02"),
				wn.synset("dish.n.03"),
				wn.synset("dish.n.05"),
				wn.synset("liquidator.n.02"),
				wn.synset("receiver.n.01"),
				wn.synset("receiver.n.05"),
				wn.synset("receiver.n.06"),
				wn.synset("recipient.n.01"),
				wn.synset("smasher.n.02"),
				wn.synset("telephone_receiver.n.01")],

	# selfish, self centred, self centered, egoistic, egoistical, egocentric-centred,self-centered,egoistic,egoistical,egocentric
	"U+3e1f":	[wn.synset("egoistic.a.01")],

	# sweet drink
	"U+3e20":	[wn.synset("beverage.n.01")],

	# Ireland
	"U+3e21":	[wn.synset("ireland.n.01"),
				wn.synset("ireland.n.02")],

	# in love
	"U+3e22":	[wn.synset("fall_in_love.v.01")],

	# one storey home
	"U+3e24":	[wn.synset("dwelling.n.01"),
				wn.synset("family.n.01"),
				wn.synset("house.n.01")],

	# easy, easily
	"U+3e25":	[wn.synset("easily.r.01"),
				wn.synset("easy.a.01")],

	# general practitioner
	"U+3e26":	[wn.synset("general_practitioner.n.01")],

	# suddenly, abrupt, sudden
	"U+3e28":	[wn.synset("abruptly.r.01"),
				wn.synset("suddenly.r.01")],

	# voice
	"U+3e2a":	[wn.synset("articulation.n.03"),
				wn.synset("part.n.11"),
				wn.synset("spokesperson.n.01"),
				wn.synset("voice.n.01"),
				wn.synset("voice.n.02"),
				wn.synset("voice.n.03"),
				wn.synset("voice.n.05"),
				wn.synset("voice.n.06"),
				wn.synset("voice.n.07"),
				wn.synset("voice.n.09"),
				wn.synset("voice.n.10")],

	# usually do, habitually do
	"U+3e2b":	[wn.synset("domesticate.v.01")],

	# dizzy
	"U+3e2c":	[wn.synset("airheaded.s.01"),
				wn.synset("dizzy.s.01")],

	# brake
	"U+3e2d":	[wn.synset("brake.n.01")],

	# dump truck, dumper, tipper lorry, tipper, dump truck,dumper,tipper lorry,tipper
	"U+3e2f":	[wn.synset("dump_truck.n.01")],

	# perform
	"U+3e30":	[wn.synset("perform.v.03")],

	# performance, show, demonstrate
	"U+3e31":	[wn.synset("indicate.v.02")],

	# water ice lollipop
	"U+3e32":	[wn.synset("ice_lolly.n.01"),
				wn.synset("icicle.n.01")],

	# independent
	"U+3e34":	[wn.synset("independent.a.01")],

	# hang, hook
	"U+3e35":	[wn.synset("hang.v.02")],

	# fuse
	"U+3e36":	[wn.synset("fuse.n.01")],

	# humble, meek
	"U+3e37":	[wn.synset("base.s.02"),
				wn.synset("humble.a.02"),
				wn.synset("humble.s.01")],

	# talcum powder
	"U+3e39":	[wn.synset("talc.n.01")],

	# musical
	"U+3e3b":	[wn.synset("musical.n.01"),
				wn.synset("song_and_dance.n.01")],

	# indigo
	"U+3e3c":	[wn.synset("anil.n.01"),
				wn.synset("indigo.n.02"),
				wn.synset("indigo.n.03")],

	# photograph, photo, pic
	"U+3e3d":	[wn.synset("photograph.n.01")],

	# stepdaughter
	"U+3e3e":	[wn.synset("stepdaughter.n.01")],

	# cervix
	"U+3e40":	[wn.synset("cervix.n.02"),
				wn.synset("nape.n.01"),
				wn.synset("neck.n.01")],

	# starboard
	"U+3e41":	[wn.synset("starboard.n.01")],

	# passive
	"U+3e42":	[wn.synset("passive.a.01")],

	# passivity
	"U+3e43":	[wn.synset("passivity.n.01")],

	# shout
	"U+3e44":	[wn.synset("exclaim.v.01"),
				wn.synset("shout.v.01"),
				wn.synset("shout.v.02")],

	# double bassoon
	"U+3e4a":	[wn.synset("contrabassoon.n.01")],

	# fingerspell
	"U+3e4b":	[wn.synset("bless.v.03"),
				wn.synset("fingerspell.v.01"),
				wn.synset("sign.v.01"),
				wn.synset("sign.v.02"),
				wn.synset("sign.v.03"),
				wn.synset("sign.v.04"),
				wn.synset("sign.v.05"),
				wn.synset("sign.v.06"),
				wn.synset("sign.v.07")],

	# thermos, cooler, flask
	"U+3e4c":	[wn.synset("thermos.n.01")],

	# starvation
	"U+3e4d":	[wn.synset("dearth.n.01"),
				wn.synset("famine.n.02"),
				wn.synset("starvation.n.01"),
				wn.synset("starvation.n.02")],

	# Bangladesh
	"U+3e4e":	[wn.synset("bangladesh.n.01")],

	# tiger
	"U+3e4f":	[wn.synset("tiger.n.02")],

	# collarbone, clavicle
	"U+3e50":	[wn.synset("clavicle.n.01")],

	# congratulate
	"U+3e51":	[wn.synset("congratulate.v.02")],

	# purple, violet
	"U+3e52":	[wn.synset("violet.n.02")],

	# Leo
	"U+3e54":	[wn.synset("leo.n.01"),
				wn.synset("leo.n.02"),
				wn.synset("leo.n.03")],

	# lion
	"U+3e55":	[wn.synset("lion.n.01")],

	# Shevat, Shvat
	"U+3e56":	[wn.synset("shebat.n.01")],

	# peel
	"U+3e59":	[wn.synset("peel.n.02")],

	# deflation
	"U+3e5a":	[wn.synset("deflation.n.02")],

	# illustration
	"U+3e5b":	[wn.synset("exemplification.n.01"),
				wn.synset("illustration.n.01"),
				wn.synset("illustration.n.04")],

	# filled vegetable, stuffed vegetable
	"U+3e5c":	[wn.synset("greens.n.01")],

	# coral
	"U+3e5d":	[wn.synset("coral.n.02"),
				wn.synset("coral.n.04")],

	# visa
	"U+3e5e":	[wn.synset("visa.n.01")],

	# leprechaun
	"U+3e60":	[wn.synset("elf.n.01"),
				wn.synset("imp.n.02"),
				wn.synset("leprechaun.n.01"),
				wn.synset("puck.n.01")],

	# little person
	"U+3e61":	[wn.synset("gnome.n.01")],

	# octopus
	"U+3e62":	[wn.synset("octopus.n.01"),
				wn.synset("octopus.n.02")],

	# croak
	"U+3e63":	[wn.synset("croak.v.02"),
				wn.synset("die.v.01"),
				wn.synset("murmur.v.02")],

	# frog, toad
	"U+3e64":	[wn.synset("frog.n.01")],

	# glass material
	"U+3e65":	[wn.synset("glass.n.01")],

	# Icelandic
	"U+3e66":	[wn.synset("icelandic.n.01")],

	# dilemma
	"U+3e67":	[wn.synset("dilemma.n.01")],

	# green onion, scallion, spring onion, green onion,scallion,spring onion
	"U+3e68":	[wn.synset("green_onion.n.01")],

	# intellectual impairment, cognitive impairment, mental impairment, intellectual impairment,cognitive impairment,mental impairment
	"U+3e6a":	[wn.synset("retarded.a.01")],

	# compression, compressing, squeezing
	"U+3e6b":	[wn.synset("compaction.n.01"),
				wn.synset("compression.n.02"),
				wn.synset("compression.n.03"),
				wn.synset("compression.n.04"),
				wn.synset("pressure.n.01"),
				wn.synset("pressure.n.05"),
				wn.synset("print.n.02"),
				wn.synset("squeeze.n.01")],

	# way
	"U+3e6c":	[wn.synset("means.n.01"),
				wn.synset("way.n.05")],

	# discuss, converse, debate
	"U+3e6f":	[wn.synset("argue.v.02"),
				wn.synset("debate.v.01"),
				wn.synset("debate.v.03"),
				wn.synset("hash_out.v.01")],

	# throw
	"U+3e70":	[wn.synset("throw.v.01")],

	# road sign
	"U+3e71":	[wn.synset("fingerpost.n.01"),
				wn.synset("signpost.n.01"),
				wn.synset("traffic_light.n.01")],

	# absorbent material, sponge, absorbent material,sponge
	"U+3e72":	[wn.synset("sponge.n.01"),
				wn.synset("sponge.n.04")],

	# veterinarian
	"U+3e74":	[wn.synset("veterinarian.n.01")],

	# evidence
	"U+3e75":	[wn.synset("evidence.n.01"),
				wn.synset("evidence.n.02"),
				wn.synset("evidence.n.03")],

	# manure, fertilizer
	"U+3e76":	[wn.synset("fertilizer.n.01"),
				wn.synset("manure.n.01")],

	# Ascension Day
	"U+3e77":	[wn.synset("ascension.n.01")],

	# Ascension
	"U+3e78":	[wn.synset("ascension.n.01"),
				wn.synset("ascension.n.03")],

	# baguette
	"U+3e79":	[wn.synset("baguet.n.01")],

	# Pterosaur, Pterodactyl
	"U+3e7b":	[wn.synset("pterodactyl.n.01")],

	# flute, recorder, transverse flute flute
	"U+3e7c":	[wn.synset("flute.n.01")],

	# recorder
	"U+3e7d":	[wn.synset("fipple_flute.n.01"),
				wn.synset("recorder.n.01"),
				wn.synset("recorder.n.03"),
				wn.synset("registrar.n.03")],

	# reed, bamboo
	"U+3e7e":	[wn.synset("bamboo.n.01"),
				wn.synset("bamboo.n.02"),
				wn.synset("beating-reed_instrument.n.01"),
				wn.synset("reed.n.01"),
				wn.synset("reed.n.02"),
				wn.synset("reed.n.03"),
				wn.synset("reed.n.04"),
				wn.synset("sharp.a.09")],

	# reality
	"U+3e7f":	[wn.synset("reality.n.02")],

	# holding
	"U+3e80":	[wn.synset("possession.n.01"),
				wn.synset("property.n.01"),
				wn.synset("retention.n.01")],

	# test, assessment, exam
	"U+3e81":	[wn.synset("examination.n.02")],

	# welcome
	"U+3e85":	[wn.synset("welcome.n.01"),
				wn.synset("welcome.n.02")],

	# Koran
	"U+3e86":	[wn.synset("koran.n.01")],

	# reception
	"U+3e87":	[wn.synset("reception.n.01"),
				wn.synset("reception.n.02"),
				wn.synset("reception.n.03"),
				wn.synset("reception.n.04"),
				wn.synset("reception.n.05")],

	# dance, dancing
	"U+3e88":	[wn.synset("dance.n.01"),
				wn.synset("dancing.n.01")],

	# devoted
	"U+3e89":	[wn.synset("attached.a.03"),
				wn.synset("attached.s.04"),
				wn.synset("devoted.s.01"),
				wn.synset("devoted.s.02")],

	# devotee, fan
	"U+3e8a":	[wn.synset("fan.n.03")],

	# splurge
	"U+3e8b":	[wn.synset("splurge.v.01"),
				wn.synset("splurge.v.02")],

	# brown
	"U+3e8d":	[wn.synset("brown.n.01"),
				wn.synset("brown.n.02"),
				wn.synset("brown.n.03"),
				wn.synset("brown_university.n.01")],

	# Formula One, NASCAR Kart
	"U+3e90":	[wn.synset("rally.n.01")],

	# brownie, house elf elf
	"U+3e91":	[wn.synset("brownie.n.01"),
				wn.synset("brownie.n.03"),
				wn.synset("elf.n.01")],

	# sunbathe
	"U+3e92":	[wn.synset("sun.v.01")],

	# kitten
	"U+3e94":	[wn.synset("kitten.n.01")],

	# cat, feline, felid
	"U+3e95":	[wn.synset("cat.n.01")],

	# fresh cheese
	"U+3e98":	[wn.synset("quark_cheese.n.01")],

	# inflammable, flammable
	"U+3e99":	[wn.synset("flammable.s.01")],

	# breakable, fragile
	"U+3e9b":	[wn.synset("delicate.s.03")],

	# electric field
	"U+3e9d":	[wn.synset("electric_field.n.01")],

	# diarrhea, diarrhoea
	"U+3e9e":	[wn.synset("diarrhea.n.01")],

	# courage
	"U+3e9f":	[wn.synset("courage.n.01")],

	# sorry
	"U+3ea0":	[wn.synset("apology.n.01"),
				wn.synset("blue.s.08"),
				wn.synset("deplorable.s.01"),
				wn.synset("excuse.n.01"),
				wn.synset("good-for-nothing.s.01"),
				wn.synset("regretful.a.01")],

	# bedroom
	"U+3ea1":	[wn.synset("bedroom.n.01")],

	# continent
	"U+3ea6":	[wn.synset("continent.n.01")],

	# appear
	"U+3ea7":	[wn.synset("appear.v.02")],

	# appearance, manifestation
	"U+3ea8":	[wn.synset("appearance.n.02"),
				wn.synset("appearance.n.05"),
				wn.synset("demonstration.n.03"),
				wn.synset("expression.n.02"),
				wn.synset("manifestation.n.01")],

	# club
	"U+3eaa":	[wn.synset("club.n.02"),
				wn.synset("clubhouse.n.01")],

	# uniform
	"U+3eab":	[wn.synset("uniform.n.01")],

	# crew, staff
	"U+3eac":	[wn.synset("crew.n.01"),
				wn.synset("crew.n.04"),
				wn.synset("crowd.n.02"),
				wn.synset("gang.n.03"),
				wn.synset("staff.n.01"),
				wn.synset("staff.n.02"),
				wn.synset("staff.n.03"),
				wn.synset("staff.n.04"),
				wn.synset("staff.n.05"),
				wn.synset("staff.n.06")],

	# staff
	"U+3ead":	[wn.synset("staff.n.01")],

	# decade
	"U+3eae":	[wn.synset("decade.n.01")],

	# common, mutual, shared
	"U+3eaf":	[wn.synset("common.s.03")],

	# English
	"U+3eb0":	[wn.synset("english.n.01"),
				wn.synset("english.n.02"),
				wn.synset("english.n.03"),
				wn.synset("english.n.04")],

	# England
	"U+3eb1":	[wn.synset("england.n.01")],

	# teacher, instructor, pedagogue, educator
	"U+3eb2":	[wn.synset("educator.n.01"),
				wn.synset("teacher.n.01")],

	# prayer book, Siddur, prayer book,Siddur
	"U+3eb3":	[wn.synset("catechism.n.02"),
				wn.synset("fundamentals.n.01"),
				wn.synset("prayer_book.n.01")],

	# Portugal
	"U+3eb4":	[wn.synset("portugal.n.01")],

	# drain, sift, strain
	"U+3eb5":	[wn.synset("drain.v.03")],

	# explode, blow up, detonate, burst up,detonate,burst
	"U+3eb6":	[wn.synset("explode.v.02")],

	# trial
	"U+3eb7":	[wn.synset("test.n.04"),
				wn.synset("test.n.05"),
				wn.synset("trial.n.02"),
				wn.synset("trial.n.04"),
				wn.synset("trial.n.05"),
				wn.synset("trial.n.06")],

	# sky sports
	"U+3eb9":	[wn.synset("parasailing.n.01")],

	# retired
	"U+3eba":	[wn.synset("retired.s.01")],

	# retirement
	"U+3ebb":	[wn.synset("pension.n.01"),
				wn.synset("retirement.n.01"),
				wn.synset("retirement.n.02"),
				wn.synset("retirement.n.03")],

	# berth, bunk
	"U+3ebc":	[wn.synset("bunk.n.03")],

	# snowboard
	"U+3ebd":	[wn.synset("snowboard.n.01")],

	# living room, lounge, sitting room, front room, parlor, parlour, waiting room, living room,lounge,sitting room,front room,parlor,parlour,waiting room
	"U+3ebe":	[wn.synset("living_room.n.01")],

	# crayon, coloured pencil, marker pencil,marker
	"U+3ebf":	[wn.synset("marker.n.03")],

	# market
	"U+3ec0":	[wn.synset("market.n.01"),
				wn.synset("market.n.02"),
				wn.synset("marketplace.n.02")],

	# clue
	"U+3ec1":	[wn.synset("clue.n.02"),
				wn.synset("hint.n.02")],

	# impermeable material, insulation, impermeable material,insulation
	"U+3ec3":	[wn.synset("insulating_material.n.01"),
				wn.synset("insulation.n.01"),
				wn.synset("insulation.n.03"),
				wn.synset("insulator.n.01")],

	# MMS
	"U+3ec6":	[wn.synset("millimeter.n.01")],

	# mew, meow
	"U+3ec8":	[wn.synset("meow.v.01"),
				wn.synset("mew.v.02")],

	# heart
	"U+3ec9":	[wn.synset("affection.n.01"),
				wn.synset("center.n.01"),
				wn.synset("heart.n.01"),
				wn.synset("heart.n.02"),
				wn.synset("heart.n.03"),
				wn.synset("heart.n.06"),
				wn.synset("heart.n.07"),
				wn.synset("heart.n.08"),
				wn.synset("heart.n.10"),
				wn.synset("kernel.n.03")],

	# exclude
	"U+3eca":	[wn.synset("bar.v.01"),
				wn.synset("exclude.v.01"),
				wn.synset("exclude.v.02")],

	# bird nest, birdnest, bird nest,birdnest
	"U+3ecb":	[wn.synset("bird's_nest.n.01")],

	# visually impaired
	"U+3ecc":	[wn.synset("dim-sighted.s.01")],

	# Austria
	"U+3ece":	[wn.synset("austria.n.01")],

	# freezer
	"U+3ecf":	[wn.synset("deep-freeze.n.01")],

	# deep fry, deep-fry
	"U+3ed0":	[wn.synset("french-fry.v.01"),
				wn.synset("fry.v.02")],

	# gift, offering, present
	"U+3ed1":	[wn.synset("gift.n.01")],

	# southern
	"U+3ed2":	[wn.synset("southerly.s.01"),
				wn.synset("southern.a.01")],

	# wiggly
	"U+3ed3":	[wn.synset("crinkled.s.01"),
				wn.synset("sinuate.s.01"),
				wn.synset("wavy.s.01"),
				wn.synset("wiggly.s.02")],

	# toilet paper
	"U+3ed4":	[wn.synset("toilet_tissue.n.01")],

	# remember, recall
	"U+3ed6":	[wn.synset("remember.v.01")],

	# anytime, sometime
	"U+3ed7":	[wn.synset("erstwhile.s.01"),
				wn.synset("sometime.r.01")],

	# lid
	"U+3ed9":	[wn.synset("lid.n.02")],

	# counsellor, adviser
	"U+3eda":	[wn.synset("adviser.n.01")],

	# brain
	"U+3edb":	[wn.synset("brain.n.01")],

	# braid, plait, pigtail
	"U+3edd":	[wn.synset("braid.v.01"),
				wn.synset("braid.v.02"),
				wn.synset("plait.v.02")],

	# camper van, RV, camper van,RV
	"U+3ede":	[wn.synset("recreational_vehicle.n.01")],

	# eternal life, immortality, eternal life,immortality
	"U+3ee1":	[wn.synset("immortality.n.01")],

	# sacrament of absolution
	"U+3ee2":	[wn.synset("absolution.n.01"),
				wn.synset("absolution.n.02")],

	# rake
	"U+3ee5":	[wn.synset("rake.n.03")],

	# introduce, present
	"U+3ee6":	[wn.synset("introduce.v.01")],

	# type, kind, sort
	"U+3ee8":	[wn.synset("character.n.05"),
				wn.synset("kind.n.01"),
				wn.synset("sort.n.03"),
				wn.synset("type.n.01"),
				wn.synset("type.n.03")],

	# corridor, hall
	"U+3ee9":	[wn.synset("anteroom.n.01"),
				wn.synset("corridor.n.01"),
				wn.synset("dormitory.n.01"),
				wn.synset("hall.n.03"),
				wn.synset("hall.n.06"),
				wn.synset("hall.n.07"),
				wn.synset("hall.n.08"),
				wn.synset("hall.n.09"),
				wn.synset("hall.n.10"),
				wn.synset("hall.n.12"),
				wn.synset("hall.n.13"),
				wn.synset("hallway.n.01"),
				wn.synset("manor_hall.n.01"),
				wn.synset("mansion.n.02")],

	# barrow, grave mound mound
	"U+3eeb":	[wn.synset("barrow.n.01"),
				wn.synset("barrow.n.03"),
				wn.synset("burial_mound.n.01")],

	# let fall, drop, let fall,drop
	"U+3eec":	[wn.synset("blurt_out.v.01"),
				wn.synset("chicken_out.v.01"),
				wn.synset("dangle.v.01"),
				wn.synset("devolve.v.03"),
				wn.synset("dismiss.v.03"),
				wn.synset("dribble.v.02"),
				wn.synset("drop.v.01"),
				wn.synset("drop.v.02"),
				wn.synset("drop.v.03"),
				wn.synset("drop.v.05"),
				wn.synset("drop.v.06"),
				wn.synset("drop.v.07"),
				wn.synset("drop.v.08"),
				wn.synset("drop.v.10"),
				wn.synset("drop.v.17"),
				wn.synset("drop.v.18"),
				wn.synset("drop.v.20"),
				wn.synset("drop.v.21"),
				wn.synset("drop.v.23"),
				wn.synset("fell.v.01"),
				wn.synset("flatten.v.03"),
				wn.synset("neglect.v.01"),
				wn.synset("shed.v.01"),
				wn.synset("sink.v.01"),
				wn.synset("spend.v.02")],

	# goose
	"U+3eee":	[wn.synset("goose.n.01")],

	# prone board, scooter board, prone board,scooter-board
	"U+3eef":	[wn.synset("skateboard.n.01")],

	# happen, occur
	"U+3ef2":	[wn.synset("happen.v.01")],

	# Norwegian
	"U+3ef4":	[wn.synset("norwegian.n.02")],

	# fjord
	"U+3ef5":	[wn.synset("fjord.n.01")],

	# mental, intellectual, rational, thinking
	"U+3ef7":	[wn.synset("cerebral.a.01"),
				wn.synset("genial.a.02"),
				wn.synset("intellectual.a.02"),
				wn.synset("intellectual.s.01"),
				wn.synset("intelligent.s.04"),
				wn.synset("mental.a.01"),
				wn.synset("mental.a.02"),
				wn.synset("mental.a.03"),
				wn.synset("mental.s.05"),
				wn.synset("rational.a.01"),
				wn.synset("rational.a.03"),
				wn.synset("rational.s.04")],

	# high jump
	"U+3ef8":	[wn.synset("high_jump.n.01"),
				wn.synset("high_jump.n.02")],

	# milkmaid, dairymaid
	"U+3ef9":	[wn.synset("dairymaid.n.01")],

	# parking lot
	"U+3efb":	[wn.synset("parking_lot.n.01")],

	# Eris
	"U+3efc":	[wn.synset("eris.n.01")],

	# invitation
	"U+3efd":	[wn.synset("invitation.n.01")],

	# Hungary
	"U+3efe":	[wn.synset("hungary.n.01")],

	# promotion
	"U+3f00":	[wn.synset("promotion.n.01"),
				wn.synset("promotion.n.02"),
				wn.synset("promotion.n.03")],

	# adventure
	"U+3f01":	[wn.synset("adventure.n.01")],

	# blindness
	"U+3f02":	[wn.synset("blindness.n.01")],

	# Afghanistan
	"U+3f03":	[wn.synset("afghanistan.n.01")],

	# small pancake, blini, small pancake,blini
	"U+3f04":	[wn.synset("blini.n.01"),
				wn.synset("crape.n.01"),
				wn.synset("pancake.n.01")],

	# Asia
	"U+3f06":	[wn.synset("asia.n.01")],

	# sanctify, consecrate
	"U+3f07":	[wn.synset("consecrate.v.04")],

	# tomorrow
	"U+3f08":	[wn.synset("tomorrow.n.02")],

	# size
	"U+3f09":	[wn.synset("size.n.01")],

	# disabled, impaired, handicapped, mentally)
	"U+3f0a":	[wn.synset("afflicted.s.02"),
				wn.synset("disabled.s.01"),
				wn.synset("impaired.a.01")],

	# checked
	"U+3f0b":	[wn.synset("checked.s.01"),
				wn.synset("row.n.05")],

	# silent
	"U+3f0c":	[wn.synset("dumb.s.04"),
				wn.synset("mum.s.01"),
				wn.synset("silent.s.01"),
				wn.synset("silent.s.03"),
				wn.synset("silent.s.04"),
				wn.synset("silent.s.05")],

	# silence, quiet, quietly
	"U+3f0d":	[wn.synset("silence.n.02")],

	# merry go round, carousel, merry-go-round,carousel
	"U+3f0e":	[wn.synset("carousel.n.02")],

	# national
	"U+3f10":	[wn.synset("home.s.03"),
				wn.synset("national.a.01"),
				wn.synset("national.a.02"),
				wn.synset("national.a.03"),
				wn.synset("national.a.06"),
				wn.synset("national.a.07"),
				wn.synset("national.s.04")],

	# child abuse
	"U+3f13":	[wn.synset("exploitation.n.02"),
				wn.synset("maltreatment.n.01"),
				wn.synset("manipulation.n.01")],

	# television
	"U+3f16":	[wn.synset("television_receiver.n.01")],

	# clarinet, reed instrument instrument
	"U+3f17":	[wn.synset("clarinet.n.01")],

	# physiotherapist
	"U+3f19":	[wn.synset("physical_therapist.n.01")],

	# troublesome
	"U+3f1a":	[wn.synset("troublesome.s.01")],

	# trouble
	"U+3f1b":	[wn.synset("trouble.n.01"),
				wn.synset("trouble.n.04")],

	# breakfast
	"U+3f1c":	[wn.synset("breakfast.n.01")],

	# lumpy
	"U+3f1d":	[wn.synset("chunky.s.01")],

	# equipment, gear
	"U+3f1e":	[wn.synset("equipment.n.01")],

	# space travel, space voyage, space flight, space travel,space voyage,space flight
	"U+3f1f":	[wn.synset("spaceflight.n.01")],

	# galaxy
	"U+3f20":	[wn.synset("galaxy.n.03")],

	# disability, handicap, impairment
	"U+3f21":	[wn.synset("disability.n.01")],

	# begin, start
	"U+3f22":	[wn.synset("begin.v.03")],

	# puncture, prick
	"U+3f23":	[wn.synset("sting.v.02")],

	# downhill skiing
	"U+3f24":	[wn.synset("downhill.n.02")],

	# dream
	"U+3f26":	[wn.synset("dream.v.01"),
				wn.synset("dream.v.02")],

	# sunset
	"U+3f27":	[wn.synset("sunset.n.01"),
				wn.synset("sunset.n.03")],

	# step, stair
	"U+3f29":	[wn.synset("step.n.04")],

	# scalene triangle
	"U+3f2b":	[wn.synset("triangle.n.01")],

	# exhibitionism, immodesty, indecent exposure exposure
	"U+3f2e":	[wn.synset("exhibitionism.n.01"),
				wn.synset("exhibitionism.n.02"),
				wn.synset("immodesty.n.01")],

	# leather
	"U+3f2f":	[wn.synset("leather.n.01")],

	# animal skin, hide, pelt, animal skin,hide,pelt
	"U+3f30":	[wn.synset("function.n.03"),
				wn.synset("fur.n.01"),
				wn.synset("hide.n.01"),
				wn.synset("hide.n.02"),
				wn.synset("leather.n.01"),
				wn.synset("peel.n.02"),
				wn.synset("skin.n.04")],

	# concert
	"U+3f32":	[wn.synset("concert.n.01")],

	# active, actively
	"U+3f33":	[wn.synset("active.a.03"),
				wn.synset("active.a.05"),
				wn.synset("active.s.02")],

	# jump rope, skipping rope
	"U+3f34":	[wn.synset("jump_rope.n.01")],

	# loudspeaker
	"U+3f35":	[wn.synset("loudspeaker.n.01")],

	# out, exterior, external, outside
	"U+3f36":	[wn.synset("outside.n.01"),
				wn.synset("outside.n.02")],

	# dressage
	"U+3f37":	[wn.synset("craft.n.04"),
				wn.synset("dexterity.n.01"),
				wn.synset("dressage.n.01"),
				wn.synset("skill.n.01"),
				wn.synset("skill.n.02"),
				wn.synset("skillfulness.n.01")],

	# skyscraper
	"U+3f3a":	[wn.synset("skyscraper.n.01")],

	# tangerine, clementine, mandarin
	"U+3f3c":	[wn.synset("mandarin.n.01"),
				wn.synset("tangerine.n.01")],

	# import
	"U+3f3d":	[wn.synset("import.v.01")],

	# artificial respiration
	"U+3f3e":	[wn.synset("artificial_respiration.n.01"),
				wn.synset("cardiopulmonary_resuscitation.n.01")],

	# health goods shop
	"U+3f40":	[wn.synset("ecological.a.01"),
				wn.synset("ecological.a.02")],

	# broil, barbecue, grill
	"U+3f41":	[wn.synset("bake.v.04"),
				wn.synset("barbeque.v.01"),
				wn.synset("broil.v.01"),
				wn.synset("broil.v.02"),
				wn.synset("grill.v.01"),
				wn.synset("grill.v.02")],

	# base camp
	"U+3f42":	[wn.synset("base.n.14")],

	# first aid
	"U+3f44":	[wn.synset("emergency_room.n.01"),
				wn.synset("first_aid.n.01")],

	# sulky
	"U+3f45":	[wn.synset("sulky.n.01")],

	# skull, cranium
	"U+3f46":	[wn.synset("skull.n.01")],

	# cycling
	"U+3f47":	[wn.synset("bicycling.n.01"),
				wn.synset("cycling.n.01")],

	# dictator
	"U+3f49":	[wn.synset("authoritarian.n.01"),
				wn.synset("dictator.n.01"),
				wn.synset("dictator.n.02")],

	# dictatorship
	"U+3f4a":	[wn.synset("dictatorship.n.01")],

	# stovetop
	"U+3f4b":	[wn.synset("firebox.n.01"),
				wn.synset("hot_plate.n.01"),
				wn.synset("stove.n.01")],

	# navigate airplane
	"U+3f4d":	[wn.synset("voyage.v.01")],

	# worry
	"U+3f51":	[wn.synset("concern.n.04"),
				wn.synset("worry.n.02")],

	# northward
	"U+3f52":	[wn.synset("northbound.s.01")],

	# develop
	"U+3f53":	[wn.synset("develop.v.01")],

	# magnifier, magnifying glass glass
	"U+3f54":	[wn.synset("hand_glass.n.02"),
				wn.synset("magnifier.n.01")],

	# too bad, I'm sorry, I'm so sorry, too bad,I'm sorry,I'm so sorry
	"U+3f55":	[wn.synset("damage.n.01"),
				wn.synset("damage.n.02"),
				wn.synset("damage.n.03"),
				wn.synset("pity.n.02"),
				wn.synset("price.n.02"),
				wn.synset("wrong.n.02")],

	# ruler, measuring stick, tapeline, tape measure stick,tapeline,tape measure
	"U+3f56":	[wn.synset("rule.n.12")],

	# foal
	"U+3f57":	[wn.synset("foal.n.01")],

	# cymbal
	"U+3f58":	[wn.synset("cymbal.n.01")],

	# robot doll
	"U+3f5b":	[wn.synset("automaton.n.02")],

	# breeze
	"U+3f5e":	[wn.synset("breeze.n.01")],

	# foremother
	"U+3f5f":	[wn.synset("foremother.n.01")],

	# joystick
	"U+3f60":	[wn.synset("joystick.n.02")],

	# scabies
	"U+3f62":	[wn.synset("scabies.n.01")],

	# ammeter
	"U+3f63":	[wn.synset("ammeter.n.01")],

	# speed
	"U+3f65":	[wn.synset("speed.n.01")],

	# improvement
	"U+3f67":	[wn.synset("improvement.n.01"),
				wn.synset("improvement.n.02"),
				wn.synset("improvement.n.03")],

	# treatment
	"U+3f69":	[wn.synset("discussion.n.01"),
				wn.synset("treatment.n.01"),
				wn.synset("treatment.n.02"),
				wn.synset("treatment.n.03")],

	# read
	"U+3f6a":	[wn.synset("read.v.01")],

	# early
	"U+3f6b":	[wn.synset("early.a.01")],

	# dust storm, duster, sirocco, dust storm,duster,sirocco
	"U+3f6c":	[wn.synset("dust_storm.n.01"),
				wn.synset("dustcloth.n.01"),
				wn.synset("duster.n.02"),
				wn.synset("duster.n.04")],

	# storm
	"U+3f6d":	[wn.synset("storm.n.01")],

	# incest
	"U+3f6e":	[wn.synset("incest.n.01")],

	# miracle
	"U+3f6f":	[wn.synset("miracle.n.02")],

	# malodor, malodour, stench
	"U+3f70":	[wn.synset("malodor.n.01")],

	# blog, web blog blog
	"U+3f71":	[wn.synset("web_log.n.01")],

	# astronomer
	"U+3f72":	[wn.synset("astronomer.n.01")],

	# astronomy
	"U+3f73":	[wn.synset("astronomy.n.01")],

	# Mars
	"U+3f74":	[wn.synset("mars.n.01")],

	# Mary
	"U+3f75":	[wn.synset("mary.n.01")],

	# babysitter
	"U+3f76":	[wn.synset("babysitter.n.01")],

	# alto
	"U+3f77":	[wn.synset("alto.n.01")],

	# cleaning tool
	"U+3f78":	[wn.synset("purifier.n.01")],

	# Frigg
	"U+3f79":	[wn.synset("frigg.n.01")],

	# gather, assemble
	"U+3f7a":	[wn.synset("assemble.v.03")],

	# bazaar
	"U+3f7b":	[wn.synset("bazaar.n.03")],

	# kite flying
	"U+3f7c":	[wn.synset("libration.n.01")],

	# T shirt, tee shirt, jersey, T-shirt,tee shirt,jersey
	"U+3f7d":	[wn.synset("jersey.n.02"),
				wn.synset("jersey.n.03"),
				wn.synset("jersey.n.04"),
				wn.synset("jersey.n.05"),
				wn.synset("new_jersey.n.01")],

	# chop
	"U+3f7f":	[wn.synset("chop.v.01"),
				wn.synset("chop.v.02"),
				wn.synset("chop.v.03"),
				wn.synset("chop.v.04"),
				wn.synset("chop.v.05"),
				wn.synset("chop.v.06")],

	# testimony
	"U+3f80":	[wn.synset("testimony.n.03")],

	# expose oneself indecently
	"U+3f81":	[wn.synset("produce.v.04")],

	# disinfectant, antiseptic
	"U+3f82":	[wn.synset("antiseptic.n.01")],

	# earring
	"U+3f86":	[wn.synset("earring.n.01")],

	# jewelry, jewellery
	"U+3f87":	[wn.synset("jewelry.n.01")],

	# celeriac, celery
	"U+3f88":	[wn.synset("celery.n.01"),
				wn.synset("celery.n.02")],

	# give artificial respiration, resuscitate, revive, give artificial respiration,resuscitate,revive
	"U+3f89":	[wn.synset("come_to.v.04"),
				wn.synset("revive.v.04")],

	# grater, grinder
	"U+3f8c":	[wn.synset("bomber.n.03"),
				wn.synset("grater.n.01"),
				wn.synset("grinder.n.04"),
				wn.synset("mill.n.04"),
				wn.synset("molar.n.01")],

	# fashion designer
	"U+3f8d":	[wn.synset("couturier.n.01")],

	# omelette, omelet
	"U+3f8f":	[wn.synset("omelet.n.01")],

	# cabin, cottage, hut
	"U+3f90":	[wn.synset("bungalow.n.01"),
				wn.synset("cabin.n.01"),
				wn.synset("cabin.n.02"),
				wn.synset("cabin.n.03"),
				wn.synset("hovel.n.01"),
				wn.synset("hut.n.01")],

	# rowing boat
	"U+3f92":	[wn.synset("dinghy.n.01"),
				wn.synset("skiff.n.01")],

	# cornmeal
	"U+3f94":	[wn.synset("cornmeal.n.01")],

	# describe
	"U+3f95":	[wn.synset("describe.v.01")],

	# farfalle
	"U+3f96":	[wn.synset("farfalle.n.01")],

	# sheath
	"U+3f98":	[wn.synset("cocktail_dress.n.01"),
				wn.synset("sheath.n.01"),
				wn.synset("sheath.n.02")],

	# washing machine, washer, washing machine,washer
	"U+3f9b":	[wn.synset("washer.n.03")],

	# housekeep, housework
	"U+3f9c":	[wn.synset("housekeep.v.01"),
				wn.synset("housework.n.01")],

	# paten, holy tray tray
	"U+3f9d":	[wn.synset("patina.n.01")],

	# houseboat
	"U+3f9e":	[wn.synset("houseboat.n.01")],

	# poor
	"U+3f9f":	[wn.synset("hapless.s.01"),
				wn.synset("poor.a.02")],

	# fledgeling
	"U+3fa0":	[wn.synset("fledgling.n.02"),
				wn.synset("nestling.n.01"),
				wn.synset("newcomer.n.01")],

	# ugly, unattractive
	"U+3fa2":	[wn.synset("atrocious.s.03"),
				wn.synset("despicable.s.01"),
				wn.synset("surly.s.01"),
				wn.synset("ugly.a.01"),
				wn.synset("unattractive.a.01"),
				wn.synset("unattractive.s.02"),
				wn.synset("unattractive.s.03")],

	# cupcake, fancy cake, pastry cake,pastry
	"U+3fa3":	[wn.synset("cake.n.03"),
				wn.synset("cupcake.n.01"),
				wn.synset("pastry.n.01"),
				wn.synset("pastry.n.02")],

	# condensation
	"U+3fa4":	[wn.synset("condensation.n.02")],

	# skeleton
	"U+3fa8":	[wn.synset("skeletal_system.n.01")],

	# considerate, thoughtful
	"U+3fa9":	[wn.synset("considerate.a.01"),
				wn.synset("heedful.a.01")],

	# cardiologist
	"U+3fab":	[wn.synset("cardiologist.n.01")],

	# handball
	"U+3fac":	[wn.synset("handball.n.02")],

	# Moses
	"U+3fad":	[wn.synset("moses.n.01")],

	# religious
	"U+3fae":	[wn.synset("religious.a.02")],

	# rug, carpet, mat
	"U+3faf":	[wn.synset("rug.n.01")],

	# dumpling
	"U+3fb0":	[wn.synset("dumpling.n.01"),
				wn.synset("dumpling.n.02")],

	# fountain
	"U+3fb1":	[wn.synset("fountain.n.01"),
				wn.synset("fountain.n.03"),
				wn.synset("fountain.n.04")],

	# bathroom, washroom
	"U+3fb2":	[wn.synset("bathroom.n.01")],

	# screwdriver
	"U+3fb3":	[wn.synset("screwdriver.n.01")],

	# decide
	"U+3fb5":	[wn.synset("decide.v.01")],

	# glass jar
	"U+3fb6":	[wn.synset("can.n.01"),
				wn.synset("canister.n.02"),
				wn.synset("jar.n.01"),
				wn.synset("jar.n.02")],

	# study
	"U+3fb7":	[wn.synset("analyze.v.01"),
				wn.synset("learn.v.04"),
				wn.synset("study.v.02"),
				wn.synset("study.v.03")],

	# orgasm
	"U+3fb9":	[wn.synset("orgasm.n.01")],

	# protractor
	"U+3fbb":	[wn.synset("protractor.n.01")],

	# suicide
	"U+3fbc":	[wn.synset("suicide.n.01"),
				wn.synset("suicide.n.02")],

	# strength
	"U+3fbd":	[wn.synset("strength.n.01")],

	# frustrating
	"U+3fbe":	[wn.synset("frustrating.s.01"),
				wn.synset("frustrating.s.02")],

	# inspired
	"U+3fbf":	[wn.synset("divine.s.06")],

	# soldier, warrior
	"U+3fc0":	[wn.synset("soldier.n.01")],

	# car mechanic
	"U+3fc1":	[wn.synset("automobile_mechanic.n.01")],

	# carriage racing
	"U+3fc2":	[wn.synset("harness_race.n.01")],

	# put, locate, place
	"U+3fc3":	[wn.synset("arrange.v.07"),
				wn.synset("frame.v.04"),
				wn.synset("identify.v.01"),
				wn.synset("invest.v.01"),
				wn.synset("locate.v.01"),
				wn.synset("locate.v.03"),
				wn.synset("place.v.02"),
				wn.synset("place.v.05"),
				wn.synset("place.v.06"),
				wn.synset("place.v.09"),
				wn.synset("place.v.11"),
				wn.synset("place.v.12"),
				wn.synset("place.v.15"),
				wn.synset("place.v.16"),
				wn.synset("put.v.01"),
				wn.synset("put.v.02"),
				wn.synset("put.v.04"),
				wn.synset("put.v.07"),
				wn.synset("put.v.08"),
				wn.synset("rate.v.01"),
				wn.synset("set.v.09"),
				wn.synset("settle.v.04"),
				wn.synset("situate.v.01"),
				wn.synset("station.v.01"),
				wn.synset("target.v.01")],

	# mysterious, unknown
	"U+3fc4":	[wn.synset("cryptic.s.01")],

	# excuse
	"U+3fc5":	[wn.synset("apologize.v.02"),
				wn.synset("excuse.v.06")],

	# each other, one another
	"U+3fca":	[wn.synset("together.r.01")],

	# swash
	"U+3fcd":	[wn.synset("swash.n.01")],

	# walk, go
	"U+3fce":	[wn.synset("walk.v.01"),
				wn.synset("walk.v.02"),
				wn.synset("walk.v.03"),
				wn.synset("walk.v.04"),
				wn.synset("walk.v.05"),
				wn.synset("walk.v.06"),
				wn.synset("walk.v.07"),
				wn.synset("walk.v.08"),
				wn.synset("walk.v.09"),
				wn.synset("walk.v.10")],

	# fundamentalist
	"U+3fcf":	[wn.synset("fundamentalist.n.01")],

	# fundamentalism
	"U+3fd0":	[wn.synset("fundamentalism.n.01")],

	# ballooning
	"U+3fd1":	[wn.synset("balloon.n.02"),
				wn.synset("ballooning.n.01"),
				wn.synset("hot-air_balloon.n.01")],

	# stave, staff
	"U+3fd2":	[wn.synset("staff.n.06")],

	# archipelago
	"U+3fd3":	[wn.synset("archipelago.n.01")],

	# see you again
	"U+3fd4":	[wn.synset("revision.n.02")],

	# revelry
	"U+3fd5":	[wn.synset("disclosure.n.01"),
				wn.synset("revel.n.01"),
				wn.synset("revelation.n.02")],

	# vase, urn, trophy cup cup
	"U+3fd6":	[wn.synset("urn.n.01"),
				wn.synset("urn.n.02"),
				wn.synset("vase.n.01")],

	# less than
	"U+3fd7":	[wn.synset("relationship.n.02")],

	# xylophone, vibraphone
	"U+3fd8":	[wn.synset("marimba.n.01")],

	# horizontal
	"U+3fdc":	[wn.synset("horizontal.a.01"),
				wn.synset("horizontal.n.01")],

	# brother in law, brother-in-law
	"U+3fde":	[wn.synset("brother-in-law.n.01")],

	# hobbit
	"U+3fe1":	[wn.synset("hobbit.n.01")],

	# universal, world wide-wide
	"U+3fe2":	[wn.synset("cosmopolitan.s.03"),
				wn.synset("global.s.01"),
				wn.synset("universal.s.02"),
				wn.synset("universal.s.03"),
				wn.synset("worldwide.s.01")],

	# touchpad, trackpad
	"U+3fe6":	[wn.synset("smooth_plane.n.01")],

	# soon
	"U+3fe7":	[wn.synset("soon.r.01")],

	# hell
	"U+3fe8":	[wn.synset("hell.n.01"),
				wn.synset("hell.n.03")],

	# moshav
	"U+3fe9":	[wn.synset("moshav.n.01")],

	# guitar, string instrument instrument
	"U+3fea":	[wn.synset("guitar.n.01")],

	# hang gliding
	"U+3feb":	[wn.synset("hang_glider.n.02"),
				wn.synset("hang_gliding.n.01")],

	# motivated
	"U+3fec":	[wn.synset("motivated.a.01")],

	# magnetic field
	"U+3fed":	[wn.synset("magnetic_field.n.01")],

	# bless
	"U+3ff0":	[wn.synset("bless.v.01")],

	# electricity meter
	"U+3ff1":	[wn.synset("tensiometer.n.02"),
				wn.synset("tensiometer.n.03")],

	# bass guitar
	"U+3ff2":	[wn.synset("bass_guitar.n.01")],

	# CD, record
	"U+3ff4":	[wn.synset("cadmium.n.01"),
				wn.synset("candle.n.02"),
				wn.synset("certificate_of_deposit.n.01"),
				wn.synset("compact_disk.n.01"),
				wn.synset("criminal_record.n.01"),
				wn.synset("discus.n.02"),
				wn.synset("disk.n.01"),
				wn.synset("magnetic_disk.n.01"),
				wn.synset("phonograph_record.n.01"),
				wn.synset("puck.n.02"),
				wn.synset("record.n.01"),
				wn.synset("record.n.03"),
				wn.synset("record.n.04"),
				wn.synset("record.n.05"),
				wn.synset("record.n.06"),
				wn.synset("record.n.07")],

	# Czech Republic
	"U+3ff5":	[wn.synset("czech.n.01"),
				wn.synset("czech.n.03"),
				wn.synset("czech_republic.n.01")],

	# beer
	"U+3ff6":	[wn.synset("beer.n.01")],

	# Lapps, Lapplander, Sami
	"U+3ff7":	[wn.synset("lapp.n.01"),
				wn.synset("lapp.n.02"),
				wn.synset("patch.n.03")],

	# unharness
	"U+3ff9":	[wn.synset("unharness.v.01")],

	# surrounded, encircled, surrounding
	"U+3ffb":	[wn.synset("encompassing.s.02"),
				wn.synset("surrounded.s.01")],

	# testify
	"U+3ffc":	[wn.synset("testify.v.02")],

	# publish
	"U+3ffd":	[wn.synset("publish.v.02")],

	# publication
	"U+3ffe":	[wn.synset("issue.n.11"),
				wn.synset("publication.n.01")],

	# gathering of scouts, jamboree, gathering of scouts,jamboree
	"U+4000":	[wn.synset("gala.n.01")],

	# scouting
	"U+4001":	[wn.synset("scouting.n.01")],

	# gardener
	"U+4002":	[wn.synset("gardener.n.01"),
				wn.synset("gardener.n.02")],

	# think, reason
	"U+4004":	[wn.synset("think.v.01"),
				wn.synset("think.v.03")],

	# children's room
	"U+4005":	[wn.synset("child's_room.n.01"),
				wn.synset("nursery.n.01")],

	# cheering
	"U+4006":	[wn.synset("cheering.n.01")],

	# fuel gauge
	"U+4007":	[wn.synset("fuel_gauge.n.01")],

	# gasoline
	"U+4008":	[wn.synset("gasoline.n.01")],

	# blush
	"U+4009":	[wn.synset("blush.v.01")],

	# sufganiya
	"U+400b":	[wn.synset("hanukkah.n.01")],

	# water sports
	"U+400c":	[wn.synset("water_sport.n.01")],

	# knocking
	"U+400d":	[wn.synset("knock.n.01")],

	# miss, lose
	"U+400f":	[wn.synset("miss.v.02")],

	# obedience
	"U+4011":	[wn.synset("obedience.n.01"),
				wn.synset("obedience.n.02"),
				wn.synset("obedience.n.03")],

	# diamond, rhombus, rhomb
	"U+4013":	[wn.synset("baseball_diamond.n.01"),
				wn.synset("diamond.n.01"),
				wn.synset("diamond.n.02")],

	# expect, anticipate
	"U+4014":	[wn.synset("expect.v.01")],

	# gray, grey
	"U+4015":	[wn.synset("gray.n.01"),
				wn.synset("gray.n.05"),
				wn.synset("gray.n.06"),
				wn.synset("gray.n.07"),
				wn.synset("gray.n.08"),
				wn.synset("gray.n.09"),
				wn.synset("grey.n.01"),
				wn.synset("grey.n.02"),
				wn.synset("grey.n.03"),
				wn.synset("grey.n.04"),
				wn.synset("grey.n.06"),
				wn.synset("grey.n.07")],

	# go kart, kart, go-kart,kart
	"U+4017":	[wn.synset("go-kart.n.01")],

	# playroom, family room, recreation room room,recreation room, moadan, recreation room,moadan
	"U+4018":	[wn.synset("rumpus_room.n.01")],

	# juicy
	"U+401a":	[wn.synset("juicy.a.01")],

	# department store
	"U+401c":	[wn.synset("department_store.n.01")],

	# koala
	"U+401d":	[wn.synset("koala.n.01")],

	# cave
	"U+401e":	[wn.synset("cave.n.01")],

	# labour
	"U+401f":	[wn.synset("british_labour_party.n.01"),
				wn.synset("labor.n.01"),
				wn.synset("labor.n.02"),
				wn.synset("parturiency.n.01")],

	# pyjama, nightgown, nightie, pajama
	"U+4020":	[wn.synset("pajama.n.02")],

	# snuff, kat, coca
	"U+4022":	[wn.synset("cake.n.03"),
				wn.synset("coca.n.02"),
				wn.synset("coca.n.03"),
				wn.synset("cocaine.n.01"),
				wn.synset("coke.n.03"),
				wn.synset("erythroxylon_coca.n.01"),
				wn.synset("kat.n.01"),
				wn.synset("sniff.n.01"),
				wn.synset("snuff.n.01"),
				wn.synset("snuff.n.02"),
				wn.synset("snuff.n.03")],

	# archery
	"U+4023":	[wn.synset("archery.n.01")],

	# elbow splint
	"U+4025":	[wn.synset("cubitiere.n.01")],

	# clean
	"U+4027":	[wn.synset("clean.v.01"),
				wn.synset("clean.v.02")],

	# drying cupboard, airing cupboard
	"U+4028":	[wn.synset("clothes_dryer.n.01"),
				wn.synset("hand_blower.n.01")],

	# humid, damp, moist
	"U+402a":	[wn.synset("damp.s.01"),
				wn.synset("humid.s.01")],

	# northern
	"U+402b":	[wn.synset("northern.a.04")],

	# justice
	"U+402c":	[wn.synset("justice.n.01")],

	# French
	"U+402d":	[wn.synset("french.n.01")],

	# France
	"U+402e":	[wn.synset("france.n.01")],

	# lunar eclipse
	"U+402f":	[wn.synset("lunar_eclipse.n.01")],

	# porcupine
	"U+4031":	[wn.synset("porcupine.n.01")],

	# small intestine
	"U+4033":	[wn.synset("small_intestine.n.01")],

	# basement, cellar
	"U+4034":	[wn.synset("basement.n.01")],

	# during, while
	"U+4036":	[wn.synset("throughout.r.01"),
				wn.synset("while.n.01")],

	# no one, nobody, no one,nobody
	"U+4037":	[wn.synset("cipher.n.04")],

	# cramp, spasm
	"U+403b":	[wn.synset("spasm.n.01")],

	# champagne
	"U+403c":	[wn.synset("champagne.n.01")],

	# culture
	"U+403d":	[wn.synset("culture.n.01"),
				wn.synset("culture.n.02")],

	# Kislev
	"U+403e":	[wn.synset("kislev.n.01")],

	# nearness, closeness, proximity
	"U+403f":	[wn.synset("closeness.n.01"),
				wn.synset("closeness.n.05"),
				wn.synset("familiarity.n.03"),
				wn.synset("meanness.n.02"),
				wn.synset("nearness.n.01"),
				wn.synset("proximity.n.01"),
				wn.synset("proximity.n.02"),
				wn.synset("proximity.n.03"),
				wn.synset("stuffiness.n.02")],

	# high water
	"U+4040":	[wn.synset("ocean.n.02"),
				wn.synset("ocean_trip.n.01"),
				wn.synset("sea.n.01"),
				wn.synset("sea.n.03")],

	# gravity, gravitation
	"U+4041":	[wn.synset("gravity.n.01")],

	# probable, likely, probably
	"U+4042":	[wn.synset("probable.a.01")],

	# fishball
	"U+4044":	[wn.synset("gefilte_fish.n.01")],

	# wok, wok pan pan
	"U+4045":	[wn.synset("wok.n.01")],

	# cartographer
	"U+4046":	[wn.synset("cartographer.n.01")],

	# synthesizer, synthesiser, keyboard
	"U+4047":	[wn.synset("keyboard.n.01"),
				wn.synset("keyboard.n.02"),
				wn.synset("synthesist.n.01"),
				wn.synset("synthesizer.n.02")],

	# piano
	"U+4048":	[wn.synset("piano.n.01")],

	# main course
	"U+404b":	[wn.synset("piece_de_resistance.n.02")],

	# middle, centre
	"U+404c":	[wn.synset("center.n.01"),
				wn.synset("center.n.04")],

	# both
	"U+404d":	[wn.synset("both.s.01")],

	# barbershop, beauty shop shop
	"U+404e":	[wn.synset("barbershop.n.01")],

	# eggplant
	"U+404f":	[wn.synset("eggplant.n.01"),
				wn.synset("eggplant.n.02")],

	# mausoleum
	"U+4050":	[wn.synset("mausoleum.n.01")],

	# battery
	"U+4051":	[wn.synset("battery.n.01"),
				wn.synset("battery.n.03")],

	# badminton
	"U+4052":	[wn.synset("badminton.n.01")],

	# solar eclipse
	"U+4054":	[wn.synset("solar_eclipse.n.01")],

	# wet, damp, moist, watery
	"U+4055":	[wn.synset("wet.a.01")],

	# add, gain
	"U+4056":	[wn.synset("add.v.01"),
				wn.synset("add.v.02")],

	# chipmunk
	"U+4057":	[wn.synset("chipmunk.n.01")],

	# baby bottle, feeding bottle
	"U+4058":	[wn.synset("bottle.n.02"),
				wn.synset("bottle.n.03")],

	# liver
	"U+4059":	[wn.synset("liver.n.01")],

	# pram straps, safety harness
	"U+405a":	[wn.synset("safety_belt.n.01")],

	# vaginal discharge
	"U+405b":	[wn.synset("leukorrhea.n.01"),
				wn.synset("vaginal_discharge.n.01")],

	# Spanish, Castilian
	"U+405c":	[wn.synset("spanish.n.01")],

	# temporary
	"U+4060":	[wn.synset("impermanent.a.01"),
				wn.synset("irregular.s.07")],

	# lie down, lie, lie down,lie
	"U+4061":	[wn.synset("dwell.v.02"),
				wn.synset("lie.v.01"),
				wn.synset("lie.v.02"),
				wn.synset("lie.v.04"),
				wn.synset("lie.v.05"),
				wn.synset("lie.v.06"),
				wn.synset("lie_down.v.01")],

	# pasta salad
	"U+4062":	[wn.synset("pasta_salad.n.01")],

	# auditor, accountant
	"U+4063":	[wn.synset("accountant.n.01")],

	# empowered
	"U+4065":	[wn.synset("authorized.a.01"),
				wn.synset("empowered.s.01")],

	# fiancee, bride to be-to-be
	"U+4066":	[wn.synset("fiancee.n.01")],

	# cemetery
	"U+4067":	[wn.synset("cemetery.n.01")],

	# lip
	"U+4068":	[wn.synset("lip.n.01")],

	# evaluate
	"U+4069":	[wn.synset("measure.v.04")],

	# optician
	"U+406c":	[wn.synset("optician.n.01")],

	# eel
	"U+406d":	[wn.synset("eel.n.02")],

	# housekeeper
	"U+406e":	[wn.synset("housekeeper.n.01")],

	# kazoo
	"U+406f":	[wn.synset("kazoo.n.01")],

	# draw, sketch
	"U+4070":	[wn.synset("draw.v.06")],

	# woking
	"U+4071":	[wn.synset("wok.n.01")],

	# multi storey home
	"U+4072":	[wn.synset("business.n.01"),
				wn.synset("dwelling.n.01"),
				wn.synset("dynasty.n.01"),
				wn.synset("family.n.01"),
				wn.synset("home.n.03"),
				wn.synset("house.n.01"),
				wn.synset("sign_of_the_zodiac.n.01"),
				wn.synset("square.n.07")],

	# impoverish
	"U+4074":	[wn.synset("deprive.v.03"),
				wn.synset("devolve.v.03"),
				wn.synset("get_worse.v.01"),
				wn.synset("impoverish.v.01"),
				wn.synset("worsen.v.01"),
				wn.synset("worsen.v.02")],

	# simmer, poach
	"U+4075":	[wn.synset("simmer.v.01")],

	# rain gauge
	"U+4076":	[wn.synset("rain_gauge.n.01")],

	# current events
	"U+4077":	[wn.synset("news.n.01"),
				wn.synset("news.n.02"),
				wn.synset("news_program.n.01"),
				wn.synset("newsworthiness.n.01"),
				wn.synset("topicality.n.01")],

	# run
	"U+4078":	[wn.synset("run.v.01")],

	# rub, massage
	"U+4079":	[wn.synset("massage.n.01")],

	# Ganesh
	"U+407a":	[wn.synset("ganesh.n.01")],

	# stew
	"U+407b":	[wn.synset("stew.n.02")],

	# ache
	"U+407c":	[wn.synset("ache.n.01"),
				wn.synset("grief.n.02"),
				wn.synset("pain.n.01"),
				wn.synset("pain.n.02"),
				wn.synset("pain.n.03"),
				wn.synset("sorrow.n.01")],

	# subtract, remove, take away away, take away,remove
	"U+407d":	[wn.synset("absent.v.01"),
				wn.synset("get_rid_of.v.01"),
				wn.synset("murder.v.01"),
				wn.synset("remove.v.01"),
				wn.synset("remove.v.02"),
				wn.synset("remove.v.05"),
				wn.synset("remove.v.08"),
				wn.synset("take_out.v.01")],

	# dwarf, gnome
	"U+407e":	[wn.synset("dwarf.n.01"),
				wn.synset("dwarf.n.03"),
				wn.synset("gnome.n.01"),
				wn.synset("gnome.n.02")],

	# corn syrup
	"U+4082":	[wn.synset("corn_syrup.n.01")],

	# finally, at last last
	"U+4084":	[wn.synset("finally.r.01"),
				wn.synset("ultimately.r.01")],

	# reef
	"U+4085":	[wn.synset("reef.v.01"),
				wn.synset("reef.v.02"),
				wn.synset("reef.v.03")],

	# Switzerland
	"U+4086":	[wn.synset("switzerland.n.01")],

	# Irish
	"U+4088":	[wn.synset("irish.n.02"),
				wn.synset("irish.n.03")],

	# accessibility
	"U+4089":	[wn.synset("handiness.n.02")],

	# kidney
	"U+408a":	[wn.synset("kidney.n.01")],

	# cotton
	"U+408b":	[wn.synset("cotton.n.01"),
				wn.synset("cotton.n.02"),
				wn.synset("cotton.n.03"),
				wn.synset("cotton.n.04")],

	# nag
	"U+408c":	[wn.synset("nag.v.01"),
				wn.synset("nag.v.02"),
				wn.synset("nag.v.03")],

	# electric, electrical
	"U+408d":	[wn.synset("electric.a.01")],

	# autoharp, zither, kantele
	"U+408e":	[wn.synset("zither.n.01")],

	# fewest, least
	"U+408f":	[wn.synset("few.a.01"),
				wn.synset("fewest.a.01"),
				wn.synset("least.a.01")],

	# resign, quit
	"U+4090":	[wn.synset("leave_office.v.01")],

	# physics
	"U+4092":	[wn.synset("physics.n.01")],

	# outing, excursion
	"U+4093":	[wn.synset("excursion.n.01")],

	# depth
	"U+4094":	[wn.synset("astuteness.n.02"),
				wn.synset("deep.a.03"),
				wn.synset("depth.n.01"),
				wn.synset("depth.n.02"),
				wn.synset("depth.n.03"),
				wn.synset("depth.n.04"),
				wn.synset("depth.n.06")],

	# amenorrhea
	"U+4095":	[wn.synset("amenorrhea.n.01")],

	# Av
	"U+4096":	[wn.synset("ab.n.02")],

	# advance, go
	"U+4099":	[wn.synset("progress.v.01")],

	# wizard
	"U+409a":	[wn.synset("ace.n.03"),
				wn.synset("sorcerer.n.01")],

	# jet ski
	"U+409e":	[wn.synset("water_scooter.n.01")],

	# schooner
	"U+409f":	[wn.synset("schooner.n.02")],

	# ukulele
	"U+40a1":	[wn.synset("uke.n.01")],

	# fishnet
	"U+40a2":	[wn.synset("fishnet.n.01")],

	# nuclear fuel
	"U+40a5":	[wn.synset("nuclear_fuel.n.01")],

	# button, gripper, snap
	"U+40a8":	[wn.synset("button.n.01")],

	# Uranus
	"U+40a9":	[wn.synset("uranus.n.02")],

	# electric light, lamp, electric light,lamp
	"U+40ab":	[wn.synset("lamp.n.01")],

	# micro organism, micro-organism
	"U+40ac":	[wn.synset("microorganism.n.01")],

	# purse, pocketbook, wallet
	"U+40ad":	[wn.synset("bag.n.04"),
				wn.synset("pocketbook.n.01"),
				wn.synset("pocketbook.n.03"),
				wn.synset("purse.n.02"),
				wn.synset("purse.n.03"),
				wn.synset("purse.n.04"),
				wn.synset("wallet.n.01")],

	# vampire
	"U+40ae":	[wn.synset("vampire.n.01")],

	# experiment
	"U+40af":	[wn.synset("experiment.v.01")],

	# kidnapper
	"U+40b0":	[wn.synset("kidnapper.n.01")],

	# brooch
	"U+40b1":	[wn.synset("brooch.n.01")],

	# convert
	"U+40b2":	[wn.synset("convert.v.02"),
				wn.synset("convert.v.05")],

	# conversion
	"U+40b3":	[wn.synset("conversion.n.01"),
				wn.synset("conversion.n.04")],

	# toilet chair, commode chair
	"U+40b4":	[wn.synset("toilet.n.02")],

	# Arabic
	"U+40b5":	[wn.synset("arabic.n.01")],

	# salvation
	"U+40b6":	[wn.synset("redemption.n.01")],

	# pitch
	"U+40b7":	[wn.synset("lurch.n.03"),
				wn.synset("pitch.n.01"),
				wn.synset("pitch.n.02"),
				wn.synset("pitch.n.03"),
				wn.synset("pitch.n.05"),
				wn.synset("pitch.n.06"),
				wn.synset("pitch.n.07"),
				wn.synset("pitch.n.08"),
				wn.synset("pitch.n.10"),
				wn.synset("sales_talk.n.01")],

	# satisfaction, contentment
	"U+40b8":	[wn.synset("atonement.n.01"),
				wn.synset("contentment.n.01"),
				wn.synset("gratification.n.01"),
				wn.synset("satisfaction.n.01"),
				wn.synset("satisfaction.n.04"),
				wn.synset("satisfaction.n.05")],

	# Lent
	"U+40b9":	[wn.synset("lent.n.01")],

	# Denmark
	"U+40bb":	[wn.synset("denmark.n.01")],

	# Wednesday
	"U+40bc":	[wn.synset("wednesday.n.01")],

	# senior citizen
	"U+40be":	[wn.synset("old-age_pensioner.n.01"),
				wn.synset("old-timer.n.02"),
				wn.synset("old_man.n.01"),
				wn.synset("old_man.n.03"),
				wn.synset("patriarch.n.04"),
				wn.synset("retiree.n.01")],

	# appetizer, starter, entree
	"U+40bf":	[wn.synset("appetizer.n.01"),
				wn.synset("crank.n.04"),
				wn.synset("entrance.n.01"),
				wn.synset("entree.n.01"),
				wn.synset("entree.n.02"),
				wn.synset("entree.n.04"),
				wn.synset("hors_d'oeuvre.n.01"),
				wn.synset("newcomer.n.01"),
				wn.synset("starter.n.01"),
				wn.synset("starter.n.02"),
				wn.synset("starter.n.03"),
				wn.synset("starter.n.07")],

	# orange, citrus fruit fruit
	"U+40c3":	[wn.synset("orange.n.02")],

	# tailor, dressmaker, seamstress
	"U+40c6":	[wn.synset("tailor.n.01")],

	# any day, someday, any day,someday
	"U+40c7":	[wn.synset("someday.r.01")],

	# skirt
	"U+40c8":	[wn.synset("skirt.n.02")],

	# sweat, perspire, perspiration
	"U+40c9":	[wn.synset("perspiration.n.01")],

	# oval, elliptic, elliptical, ellipse
	"U+40ca":	[wn.synset("ellipse.n.01")],

	# mailbox, letterbox, postbox
	"U+40cb":	[wn.synset("mailbox.n.01"),
				wn.synset("postbox.n.01")],

	# pink
	"U+40cc":	[wn.synset("pink.n.01")],

	# bells, chime bars, tubular bells bars,tubular bells
	"U+40cd":	[wn.synset("bell.n.01"),
				wn.synset("bell.n.03"),
				wn.synset("bell.n.04"),
				wn.synset("bell.n.05"),
				wn.synset("bell.n.06"),
				wn.synset("bell.n.07"),
				wn.synset("bell.n.08"),
				wn.synset("bell.n.10"),
				wn.synset("chime.n.01"),
				wn.synset("doorbell.n.01")],

	# cutlery
	"U+40ce":	[wn.synset("cutlery.n.02"),
				wn.synset("cutter.n.06"),
				wn.synset("flatware.n.02")],

	# bakery
	"U+40d0":	[wn.synset("bakery.n.01")],

	# agenda
	"U+40d1":	[wn.synset("agenda.n.01"),
				wn.synset("agenda.n.02")],

	# make believe person, imaginary person, make-believe person,imaginary person, make-believe person, water nymph
	"U+40d4":	[wn.synset("imaginary_being.n.01")],

	# stone age
	"U+40d5":	[wn.synset("stone_age.n.01")],

	# salivary gland
	"U+40d7":	[wn.synset("salivary_gland.n.01"),
				wn.synset("sublingual_gland.n.01"),
				wn.synset("submaxillary_gland.n.01")],

	# menstrual blood
	"U+40d8":	[wn.synset("menstruation.n.01")],

	# functional
	"U+40d9":	[wn.synset("functional.a.01"),
				wn.synset("functional.a.02"),
				wn.synset("functional.a.03"),
				wn.synset("functional.s.04"),
				wn.synset("functional.s.05"),
				wn.synset("running.s.06")],

	# sport fanatic
	"U+40db":	[wn.synset("athlete.n.01"),
				wn.synset("sports_fan.n.01")],

	# Venus
	"U+40dc":	[wn.synset("venus.n.01")],

	# university
	"U+40df":	[wn.synset("university.n.03")],

	# armoured force, tank force
	"U+40e0":	[wn.synset("cavalry.n.02")],

	# special, particular
	"U+40e2":	[wn.synset("especial.s.01"),
				wn.synset("particular.s.01"),
				wn.synset("special.s.02"),
				wn.synset("special.s.04")],

	# confess
	"U+40e3":	[wn.synset("concede.v.01"),
				wn.synset("confess.v.01"),
				wn.synset("confess.v.03")],

	# foster mother
	"U+40e4":	[wn.synset("foster-mother.n.01")],

	# wading pool, paddling pool
	"U+40e9":	[wn.synset("wading_pool.n.01")],

	# undo
	"U+40eb":	[wn.synset("unmake.v.01")],

	# drowning
	"U+40ed":	[wn.synset("drown.v.02"),
				wn.synset("drown.v.03"),
				wn.synset("drown.v.04"),
				wn.synset("submerge.v.02"),
				wn.synset("swim.v.04")],

	# Kabbalat Shabbat
	"U+40ee":	[wn.synset("kabbalah.n.02")],

	# timer
	"U+40f0":	[wn.synset("stopwatch.n.01"),
				wn.synset("timekeeper.n.01"),
				wn.synset("timer.n.01"),
				wn.synset("timer.n.03")],

	# keel
	"U+40f1":	[wn.synset("keel.n.02"),
				wn.synset("keel.n.03")],

	# date
	"U+40f3":	[wn.synset("date.n.08")],

	# quality
	"U+40f5":	[wn.synset("quality.n.01"),
				wn.synset("quality.n.02"),
				wn.synset("quality.n.03"),
				wn.synset("timbre.n.01")],

	# headscarf
	"U+40f7":	[wn.synset("fichu.n.01"),
				wn.synset("handkerchief.n.01"),
				wn.synset("headscarf.n.01")],

	# fasten, attach, join, append, connect
	"U+40f9":	[wn.synset("add.v.02"),
				wn.synset("append.v.01"),
				wn.synset("append.v.02"),
				wn.synset("associate.v.01"),
				wn.synset("attach.v.01"),
				wn.synset("attach.v.02"),
				wn.synset("attach.v.03"),
				wn.synset("bind.v.02"),
				wn.synset("connect.v.01"),
				wn.synset("connect.v.03"),
				wn.synset("connect.v.04"),
				wn.synset("connect.v.05"),
				wn.synset("connect.v.06"),
				wn.synset("connect.v.07"),
				wn.synset("connect.v.08"),
				wn.synset("connect.v.11"),
				wn.synset("fasten.v.01"),
				wn.synset("fasten.v.02"),
				wn.synset("fasten.v.03"),
				wn.synset("get_in_touch.v.01"),
				wn.synset("impound.v.01"),
				wn.synset("join.v.01"),
				wn.synset("join.v.02"),
				wn.synset("join.v.03"),
				wn.synset("join.v.04"),
				wn.synset("plug_in.v.01"),
				wn.synset("tighten.v.01")],

	# attack
	"U+40fa":	[wn.synset("approach.n.01"),
				wn.synset("attack.n.01"),
				wn.synset("attack.n.02"),
				wn.synset("attack.n.05"),
				wn.synset("attack.n.06"),
				wn.synset("attack.n.07"),
				wn.synset("attack.n.08"),
				wn.synset("attack.n.09"),
				wn.synset("fire.n.09")],

	# facial hair
	"U+40fc":	[wn.synset("beard.n.01"),
				wn.synset("beard.n.04"),
				wn.synset("chin.n.01"),
				wn.synset("facial_hair.n.01"),
				wn.synset("mustache.n.01")],

	# beg, plead
	"U+40fd":	[wn.synset("beg.v.01"),
				wn.synset("beg.v.03"),
				wn.synset("beg.v.04"),
				wn.synset("plead.v.01"),
				wn.synset("plead.v.02"),
				wn.synset("plead.v.03"),
				wn.synset("plead.v.04"),
				wn.synset("solicit.v.01")],

	# please
	"U+40ff":	[wn.synset("please.r.01"),
				wn.synset("please.v.01"),
				wn.synset("please.v.02"),
				wn.synset("please.v.03")],

	# bee
	"U+4100":	[wn.synset("bee.n.01")],

	# saddle
	"U+4102":	[wn.synset("saddle.n.01")],

	# firework
	"U+4103":	[wn.synset("firework.n.01")],

	# bet
	"U+4104":	[wn.synset("stake.n.04")],

	# microphone
	"U+4106":	[wn.synset("microphone.n.01")],

	# carrycot, bassinet
	"U+4107":	[wn.synset("carrycot.n.01")],

	# Batman
	"U+4108":	[wn.synset("batman.n.01")],

	# speaker, lecturer
	"U+410a":	[wn.synset("speaker.n.01")],

	# orthoptist
	"U+410b":	[wn.synset("orthoptist.n.01")],

	# Sniff
	"U+410c":	[wn.synset("sniff.n.01")],

	# art gallery, gallery, art gallery,gallery
	"U+4110":	[wn.synset("gallery.n.03"),
				wn.synset("gallery.n.06")],

	# mobile phone, cellphone, mobile phone,cellphone
	"U+4111":	[wn.synset("cellular_telephone.n.01")],

	# spleen
	"U+4112":	[wn.synset("spleen.n.01")],

	# skunk
	"U+4114":	[wn.synset("skunk.n.04")],

	# mixing spoon
	"U+4116":	[wn.synset("spoon.n.01")],

	# tire, tyre
	"U+4117":	[wn.synset("tire.n.01")],

	# hopeful
	"U+4118":	[wn.synset("bright.s.10")],

	# rash
	"U+4119":	[wn.synset("dermatitis.n.01"),
				wn.synset("rash.n.01"),
				wn.synset("rash.n.02")],

	# achieve
	"U+411a":	[wn.synset("achieve.v.01")],

	# achievement
	"U+411b":	[wn.synset("accomplishment.n.01"),
				wn.synset("operation.n.07")],

	# roast, joint
	"U+411e":	[wn.synset("articulation.n.02"),
				wn.synset("joint.n.01"),
				wn.synset("joint.n.02"),
				wn.synset("joint.n.05"),
				wn.synset("joint.n.06"),
				wn.synset("knock.n.02"),
				wn.synset("roast.n.01")],

	# Italian
	"U+411f":	[wn.synset("italian.n.02")],

	# opera
	"U+4120":	[wn.synset("opera.n.01"),
				wn.synset("opera.n.03")],

	# DVD, movie disc disc
	"U+4124":	[wn.synset("videodisk.n.01")],

	# motorboat
	"U+4126":	[wn.synset("motorboat.n.01")],

	# preach
	"U+4128":	[wn.synset("preach.v.01")],

	# computer
	"U+412b":	[wn.synset("computer.n.01")],

	# overturn, turn over, tip over over,tip over
	"U+412c":	[wn.synset("overrule.v.01"),
				wn.synset("overthrow.v.01"),
				wn.synset("overturn.v.01"),
				wn.synset("overturn.v.02"),
				wn.synset("revoke.v.02"),
				wn.synset("revolutionize.v.01"),
				wn.synset("topple.v.02")],

	# direction, cardinal point point
	"U+412d":	[wn.synset("direction.n.02")],

	# washable
	"U+412e":	[wn.synset("washable.a.01")],

	# freestyle skiing
	"U+412f":	[wn.synset("ski.n.01"),
				wn.synset("skiing.n.01")],

	# southward
	"U+4130":	[wn.synset("southbound.s.01")],

	# province, county, region, state
	"U+4132":	[wn.synset("country.n.02"),
				wn.synset("state.n.01"),
				wn.synset("state.n.02"),
				wn.synset("state.n.03"),
				wn.synset("state.n.04"),
				wn.synset("state_of_matter.n.01")],

	# tent
	"U+4133":	[wn.synset("tent.n.01")],

	# police force, police, police force,police
	"U+4134":	[wn.synset("police.n.01")],

	# thank
	"U+4135":	[wn.synset("thank.v.01")],

	# succeed
	"U+4136":	[wn.synset("succeed.v.01")],

	# peanut butter
	"U+4137":	[wn.synset("peanut_butter.n.01")],

	# hydrotherapy
	"U+4138":	[wn.synset("hydropathy.n.01")],

	# sari
	"U+413b":	[wn.synset("sari.n.01")],

	# cent
	"U+413e":	[wn.synset("cent.n.01")],

	# sweet potato, yam, sweet potato,yam
	"U+4140":	[wn.synset("yam.n.02"),
				wn.synset("yam.n.03"),
				wn.synset("yam.n.04")],

	# treat, care for for
	"U+4142":	[wn.synset("treat.v.03")],

	# circus
	"U+4143":	[wn.synset("circus.n.01"),
				wn.synset("circus.n.02"),
				wn.synset("circus.n.03"),
				wn.synset("circus.n.04"),
				wn.synset("circus.n.05"),
				wn.synset("circus.n.06")],

	# our, ours
	"U+4146":	[wn.synset("spring.n.01")],

	# respiratory illness
	"U+4147":	[wn.synset("asthma.n.01")],

	# breathe
	"U+4148":	[wn.synset("breathe.v.01")],

	# resident
	"U+414b":	[wn.synset("resident.n.01")],

	# transvestite
	"U+414d":	[wn.synset("transvestite.n.01")],

	# Viking
	"U+414f":	[wn.synset("viking.n.01")],

	# firefighter, fireman
	"U+4150":	[wn.synset("fireman.n.04")],

	# extinction, extinguishing
	"U+4151":	[wn.synset("extinction.n.01"),
				wn.synset("extinction.n.02"),
				wn.synset("extinction.n.03"),
				wn.synset("extinction.n.04"),
				wn.synset("extinction.n.05"),
				wn.synset("extinction.n.06")],

	# hitchrack, hitching bar bar
	"U+4153":	[wn.synset("handbarrow.n.01"),
				wn.synset("hitchrack.n.01")],

	# millepede
	"U+4154":	[wn.synset("millipede.n.01")],

	# magician
	"U+4155":	[wn.synset("magician.n.01"),
				wn.synset("sorcerer.n.01")],

	# sea cucumber
	"U+4156":	[wn.synset("sea_cucumber.n.01")],

	# oval shape
	"U+4157":	[wn.synset("ellipse.n.01")],

	# shalom
	"U+4158":	[wn.synset("adieu.n.01"),
				wn.synset("benefit.n.02"),
				wn.synset("bye.n.01"),
				wn.synset("greeting.n.01"),
				wn.synset("hawaii.n.01"),
				wn.synset("hello.n.01"),
				wn.synset("redemption.n.01"),
				wn.synset("salutation.n.03"),
				wn.synset("salute.n.01"),
				wn.synset("salute.n.03"),
				wn.synset("salvation.n.02"),
				wn.synset("salvation.n.03"),
				wn.synset("salvation.n.04")],

	# goodness
	"U+4159":	[wn.synset("good.n.02")],

	# healthy, well
	"U+415a":	[wn.synset("good.s.13"),
				wn.synset("goodly.s.01"),
				wn.synset("healthy.a.01"),
				wn.synset("healthy.s.02"),
				wn.synset("healthy.s.03"),
				wn.synset("healthy.s.04"),
				wn.synset("well.a.01"),
				wn.synset("well.s.03")],

	# coarse slang
	"U+415b":	[wn.synset("ordinary.n.03")],

	# these
	"U+415c":	[wn.synset("tellurium.n.01")],

	# polder
	"U+415d":	[wn.synset("polder.n.01")],

	# disagree, discord, disaccord
	"U+415e":	[wn.synset("disagree.v.01"),
				wn.synset("disagree.v.02")],

	# Sunday
	"U+4160":	[wn.synset("sunday.n.01")],

	# religious gathering
	"U+4162":	[wn.synset("meeting.n.03"),
				wn.synset("service.n.03")],

	# trot
	"U+4163":	[wn.synset("trot.v.01"),
				wn.synset("trot.v.02"),
				wn.synset("trot.v.03")],

	# disappearance
	"U+4164":	[wn.synset("disappearance.n.01")],

	# propeller, rotor
	"U+4166":	[wn.synset("propeller.n.01"),
				wn.synset("rotor.n.03")],

	# clown
	"U+4167":	[wn.synset("clown.n.01"),
				wn.synset("clown.n.02")],

	# protestantism
	"U+4168":	[wn.synset("protestantism.n.01")],

	# barn, stable, shed
	"U+416a":	[wn.synset("stable.n.01")],

	# chirp, twitter
	"U+416b":	[wn.synset("peep.v.03")],

	# library
	"U+416c":	[wn.synset("library.n.01"),
				wn.synset("library.n.02"),
				wn.synset("library.n.05")],

	# overlay
	"U+416e":	[wn.synset("covering.n.02"),
				wn.synset("overlay.n.02"),
				wn.synset("sheathing.n.01")],

	# cockerel
	"U+416f":	[wn.synset("cock.n.04"),
				wn.synset("cockerel.n.01")],

	# tadpole
	"U+4170":	[wn.synset("tadpole.n.01")],

	# fable, allegory, parable
	"U+4171":	[wn.synset("allegory.n.03"),
				wn.synset("emblem.n.02"),
				wn.synset("fable.n.02"),
				wn.synset("fabrication.n.01"),
				wn.synset("legend.n.01"),
				wn.synset("parable.n.02"),
				wn.synset("simile.n.01")],

	# orienteer, read map map
	"U+4172":	[wn.synset("adviser.n.01")],

	# map reading
	"U+4173":	[wn.synset("orientation.n.03")],

	# magazine, journal
	"U+4174":	[wn.synset("diary.n.01"),
				wn.synset("journal.n.02"),
				wn.synset("magazine.n.01")],

	# computer game
	"U+4176":	[wn.synset("computer_game.n.01")],

	# beige
	"U+4177":	[wn.synset("beige.n.01")],

	# cranberry
	"U+4178":	[wn.synset("cranberry.n.02")],

	# tongue
	"U+4179":	[wn.synset("tongue.n.01")],

	# seminal vesicle
	"U+417a":	[wn.synset("scrotum.n.01")],

	# semen
	"U+417b":	[wn.synset("semen.n.01")],

	# electric piano
	"U+417c":	[wn.synset("piano.n.01")],

	# snowplow, snowplough
	"U+417d":	[wn.synset("snowplow.n.01")],

	# museum
	"U+417e":	[wn.synset("museum.n.01")],

	# pepper sauce
	"U+417f":	[wn.synset("pepper_sauce.n.01")],

	# drumstick
	"U+4180":	[wn.synset("drumstick.n.01"),
				wn.synset("drumstick.n.02"),
				wn.synset("mallet.n.02")],

	# showjumping
	"U+4181":	[wn.synset("showjumping.n.01")],

	# cricket
	"U+4182":	[wn.synset("cricket.n.02")],

	# sacrament of communion
	"U+4183":	[wn.synset("holy_eucharist.n.01")],

	# triangular
	"U+4184":	[wn.synset("triangular.s.01")],

	# palmtop, PDA
	"U+4186":	[wn.synset("personal_digital_assistant.n.01")],

	# abseiling, rappelling
	"U+4188":	[wn.synset("decrease.n.01"),
				wn.synset("demotion.n.01"),
				wn.synset("descent.n.01"),
				wn.synset("descent.n.03"),
				wn.synset("descent.n.05"),
				wn.synset("downfall.n.01"),
				wn.synset("downhill.n.02"),
				wn.synset("drop.n.03"),
				wn.synset("rappel.v.01")],

	# cello
	"U+418a":	[wn.synset("cello.n.01")],

	# education, didactics, pedagogy
	"U+418d":	[wn.synset("teaching_method.n.01")],

	# balcony, porch, veranda
	"U+418e":	[wn.synset("balcony.n.02")],

	# mite, tick
	"U+418f":	[wn.synset("check_mark.n.01"),
				wn.synset("mite.n.02"),
				wn.synset("tick.n.01"),
				wn.synset("tick.n.02"),
				wn.synset("tick.n.04"),
				wn.synset("touch.n.06")],

	# slaughterhouse, abattoir
	"U+4190":	[wn.synset("abattoir.n.01")],

	# slaughter
	"U+4191":	[wn.synset("slaughter.n.01"),
				wn.synset("slaughter.n.03"),
				wn.synset("thrashing.n.01")],

	# fencing
	"U+4192":	[wn.synset("fencing.n.03")],

	# water bucket
	"U+4195":	[wn.synset("watering_can.n.01")],

	# chemist
	"U+4196":	[wn.synset("chemist.n.01")],

	# chemistry
	"U+4197":	[wn.synset("chemistry.n.01")],

	# troll
	"U+4198":	[wn.synset("troll.n.01")],

	# channel
	"U+419b":	[wn.synset("channel.n.01"),
				wn.synset("channel.n.02"),
				wn.synset("channel.n.04"),
				wn.synset("channel.n.05"),
				wn.synset("channel.n.07"),
				wn.synset("distribution_channel.n.01"),
				wn.synset("duct.n.01"),
				wn.synset("groove.n.01")],

	# ecstatic
	"U+419c":	[wn.synset("ecstatic.s.01"),
				wn.synset("excited.a.02")],

	# ecstasy
	"U+419d":	[wn.synset("adam.n.03"),
				wn.synset("ecstasy.n.01"),
				wn.synset("ecstasy.n.02"),
				wn.synset("excitation.n.03"),
				wn.synset("excitement.n.02"),
				wn.synset("foreplay.n.01"),
				wn.synset("inflammation.n.03")],

	# stay, remain
	"U+419e":	[wn.synset("stay.v.02")],

	# celebration of life
	"U+419f":	[wn.synset("celebration.n.01"),
				wn.synset("celebration.n.02"),
				wn.synset("celebration.n.03")],

	# atheism
	"U+41a2":	[wn.synset("atheism.n.01"),
				wn.synset("atheism.n.02")],

	# limited, restricted, confined
	"U+41a4":	[wn.synset("limited.a.01"),
				wn.synset("restricted.a.01")],

	# stomach illness
	"U+41a7":	[wn.synset("stomachache.n.01")],

	# teaspoon
	"U+41a8":	[wn.synset("teaspoon.n.01"),
				wn.synset("teaspoon.n.02")],

	# instruction, teaching, direction
	"U+41a9":	[wn.synset("commission.n.06"),
				wn.synset("direction.n.01"),
				wn.synset("direction.n.02"),
				wn.synset("direction.n.03"),
				wn.synset("direction.n.06"),
				wn.synset("education.n.01"),
				wn.synset("focus.n.01"),
				wn.synset("guidance.n.01"),
				wn.synset("instruction.n.04"),
				wn.synset("management.n.01"),
				wn.synset("steering.n.02"),
				wn.synset("teaching.n.01")],

	# rescue
	"U+41aa":	[wn.synset("rescue.v.01")],

	# tandem bicycle
	"U+41ab":	[wn.synset("bicycle-built-for-two.n.01")],

	# raw, uncooked
	"U+41ac":	[wn.synset("raw.a.03")],

	# farmhouse
	"U+41ad":	[wn.synset("farmhouse.n.01")],

	# chocolate drink
	"U+41ae":	[wn.synset("cocoa.n.01")],

	# cactus
	"U+41b0":	[wn.synset("cactus.n.01")],

	# desktop computer
	"U+41b1":	[wn.synset("computer.n.01")],

	# barometer, manometer
	"U+41b6":	[wn.synset("barometer.n.01")],

	# never
	"U+41b7":	[wn.synset("never.r.01")],

	# anthropology
	"U+41b8":	[wn.synset("anthropology.n.01")],

	# remote control
	"U+41b9":	[wn.synset("remote_control.n.01")],

	# cardboard, paperboard
	"U+41ba":	[wn.synset("cardboard.n.01"),
				wn.synset("paperboard.n.01")],

	# piercing
	"U+41bb":	[wn.synset("acute.s.03"),
				wn.synset("cutting.s.03"),
				wn.synset("perforation.n.03"),
				wn.synset("pierce.v.01"),
				wn.synset("pierce.v.02"),
				wn.synset("pierce.v.03"),
				wn.synset("pierce.v.04"),
				wn.synset("pierce.v.05")],

	# male genitals
	"U+41bc":	[wn.synset("man.n.01")],

	# skytrain, monorail
	"U+41be":	[wn.synset("monorail.n.01")],

	# bronze age
	"U+41bf":	[wn.synset("bronze_age.n.01"),
				wn.synset("bronze_age.n.02")],

	# bronze
	"U+41c1":	[wn.synset("bronze.n.01"),
				wn.synset("bronze.n.02")],

	# advise, counsel, recommend
	"U+41c2":	[wn.synset("rede.v.02")],

	# advice, counsel, recommendation
	"U+41c3":	[wn.synset("advice.n.01")],

	# supporters, cheering section section
	"U+41c4":	[wn.synset("assistant.n.01"),
				wn.synset("athletic_supporter.n.01"),
				wn.synset("fandom.n.01"),
				wn.synset("following.n.01"),
				wn.synset("garter.n.01"),
				wn.synset("patron.n.03"),
				wn.synset("supporter.n.01")],

	# warn
	"U+41c5":	[wn.synset("warn.v.01")],

	# warning
	"U+41c6":	[wn.synset("admonition.n.01"),
				wn.synset("warning.n.01"),
				wn.synset("warning.n.03")],

	# dhoti, lungi
	"U+41c9":	[wn.synset("dhoti.n.01")],

	# anchor
	"U+41cc":	[wn.synset("anchor.n.01")],

	# one storey building, bungalow, one storey building,bungalow
	"U+41cd":	[wn.synset("building.n.01"),
				wn.synset("bungalow.n.01")],

	# social worker
	"U+41d0":	[wn.synset("social_worker.n.01")],

	# honey
	"U+41d1":	[wn.synset("honey.n.01")],

	# briefcase
	"U+41d3":	[wn.synset("briefcase.n.01")],

	# twin sister
	"U+41d4":	[wn.synset("binoculars.n.01"),
				wn.synset("counterpart.n.02"),
				wn.synset("gemini.n.01"),
				wn.synset("twin.n.01")],

	# president
	"U+41d5":	[wn.synset("president.n.03")],

	# chairman
	"U+41d6":	[wn.synset("president.n.04")],

	# go to sea
	"U+41d7":	[wn.synset("embark.v.01")],

	# boarding, embarkation
	"U+41d8":	[wn.synset("boarding.n.01"),
				wn.synset("boarding.n.02")],

	# buy, purchase
	"U+41da":	[wn.synset("buy.v.01")],

	# deck
	"U+41db":	[wn.synset("deck.n.01")],

	# hibernation
	"U+41dc":	[wn.synset("hibernation.n.01")],

	# siren of the woods
	"U+41dd":	[wn.synset("dryad.n.01")],

	# better
	"U+41de":	[wn.synset("better.a.01")],

	# missionary
	"U+41df":	[wn.synset("missionary.n.02")],

	# French horn
	"U+41e0":	[wn.synset("french_horn.n.01")],

	# bow and string
	"U+41e1":	[wn.synset("bow.n.02"),
				wn.synset("snare.n.05")],

	# viola
	"U+41e2":	[wn.synset("viola.n.03")],

	# sterilization
	"U+41e3":	[wn.synset("sterilization.n.01"),
				wn.synset("sterilization.n.02")],

	# weakness
	"U+41e4":	[wn.synset("failing.n.01")],

	# unemployed
	"U+41e5":	[wn.synset("unemployed.a.01")],

	# caterpillar
	"U+41e6":	[wn.synset("caterpillar.n.01")],

	# sleepless
	"U+41e7":	[wn.synset("insomniac.s.01")],

	# India
	"U+41e8":	[wn.synset("india.n.01")],

	# bake, cook, roast
	"U+41e9":	[wn.synset("bake.v.01"),
				wn.synset("bake.v.02"),
				wn.synset("bake.v.04"),
				wn.synset("broil.v.02"),
				wn.synset("cook.v.01"),
				wn.synset("cook.v.02"),
				wn.synset("cook.v.03"),
				wn.synset("cook.v.05"),
				wn.synset("fudge.v.01"),
				wn.synset("ridicule.v.01"),
				wn.synset("roast.v.01")],

	# navy
	"U+41ea":	[wn.synset("navy.n.01")],

	# Tammuz
	"U+41eb":	[wn.synset("tammuz.n.01")],

	# kebab, NL)
	"U+41ec":	[wn.synset("kabob.n.01")],

	# body brace, corset, body brace,corset
	"U+41ee":	[wn.synset("corset.n.01")],

	# signature
	"U+41ef":	[wn.synset("signature.n.01")],

	# loud, noisy
	"U+41f1":	[wn.synset("brassy.s.02"),
				wn.synset("forte.a.01"),
				wn.synset("loud.a.01"),
				wn.synset("noisy.a.01"),
				wn.synset("noisy.s.02")],

	# noise
	"U+41f2":	[wn.synset("noise.n.01"),
				wn.synset("noise.n.02"),
				wn.synset("noise.n.03"),
				wn.synset("noise.n.04"),
				wn.synset("noise.n.05"),
				wn.synset("randomness.n.02")],

	# naughty, not nice nice
	"U+41f3":	[wn.synset("blue.s.05"),
				wn.synset("disobedient.a.01"),
				wn.synset("naughty.s.02")],

	# Buddhism
	"U+41f4":	[wn.synset("buddhism.n.02")],

	# computer peripheral
	"U+41f6":	[wn.synset("beltway.n.01"),
				wn.synset("peripheral.n.01"),
				wn.synset("periphery.n.01")],

	# historian
	"U+41f7":	[wn.synset("historian.n.01")],

	# boating
	"U+41f8":	[wn.synset("boating.n.01")],

	# spice box
	"U+41f9":	[wn.synset("pepper_shaker.n.01")],

	# shallowness
	"U+41fa":	[wn.synset("shallowness.n.02"),
				wn.synset("superficiality.n.01")],

	# gym, gymnasium
	"U+41fc":	[wn.synset("gymnasium.n.02")],

	# gambler
	"U+41fd":	[wn.synset("gambler.n.01"),
				wn.synset("gambler.n.02")],

	# solar energy, solar power
	"U+41fe":	[wn.synset("solar_energy.n.01")],

	# rattle
	"U+41ff":	[wn.synset("rattle.n.01"),
				wn.synset("rattle.n.02"),
				wn.synset("rattle.n.03")],

	# my, mine
	"U+4200":	[wn.synset("mine.n.01"),
				wn.synset("mine.n.02")],

	# seem
	"U+4203":	[wn.synset("appear.v.04")],

	# bass clarinet
	"U+4205":	[wn.synset("bass_clarinet.n.01")],

	# cheer
	"U+4206":	[wn.synset("cheer.v.01"),
				wn.synset("cheer.v.05")],

	# chess
	"U+4208":	[wn.synset("check.n.13"),
				wn.synset("chess.n.01"),
				wn.synset("chess.n.02")],

	# royal
	"U+420b":	[wn.synset("royal.a.01")],

	# alarm
	"U+420c":	[wn.synset("alarm.n.01"),
				wn.synset("alarm.n.02"),
				wn.synset("alarm.n.03")],

	# sequin, spangle
	"U+420d":	[wn.synset("sequin.n.01")],

	# retire
	"U+420e":	[wn.synset("adjourn.v.02"),
				wn.synset("go_to_bed.v.01")],

	# poison
	"U+420f":	[wn.synset("poison.n.01"),
				wn.synset("poison.n.02")],

	# explain, give a reason a reason
	"U+4212":	[wn.synset("explain.v.01")],

	# acne
	"U+4213":	[wn.synset("acne.n.01")],

	# adding, additive
	"U+4214":	[wn.synset("add.v.01"),
				wn.synset("add.v.02"),
				wn.synset("add.v.04"),
				wn.synset("add.v.06"),
				wn.synset("additive.n.01"),
				wn.synset("lend.v.01"),
				wn.synset("summation.n.04"),
				wn.synset("total.v.02")],

	# Frey
	"U+4218":	[wn.synset("frey.n.01")],

	# polenta
	"U+4219":	[wn.synset("polenta.n.01")],

	# folder
	"U+421b":	[wn.synset("booklet.n.01"),
				wn.synset("directory.n.02"),
				wn.synset("folder.n.02")],

	# eating disorder
	"U+421d":	[wn.synset("anorexia.n.01")],

	# mental illness
	"U+421e":	[wn.synset("insanity.n.01"),
				wn.synset("lunacy.n.01"),
				wn.synset("mental_illness.n.01")],

	# meditate
	"U+4220":	[wn.synset("chew_over.v.01"),
				wn.synset("study.v.06")],

	# obey, comply
	"U+4222":	[wn.synset("comply.v.01"),
				wn.synset("obey.v.01")],

	# disco
	"U+4223":	[wn.synset("disco.n.02")],

	# bleat, baa
	"U+4225":	[wn.synset("bleat.v.02")],

	# linguist
	"U+4226":	[wn.synset("linguist.n.01")],

	# linguistics
	"U+4227":	[wn.synset("linguistics.n.01")],

	# secret agent, spy, secret agent,spy
	"U+4229":	[wn.synset("spy.n.01"),
				wn.synset("spy.n.02")],

	# prophesy
	"U+422a":	[wn.synset("preach.v.01"),
				wn.synset("profess.v.02"),
				wn.synset("profess.v.06"),
				wn.synset("prophesy.v.01")],

	# prophecy
	"U+422b":	[wn.synset("prophecy.n.02")],

	# Christmas Eve
	"U+422d":	[wn.synset("christmas_eve.n.01")],

	# shaver, razor
	"U+422e":	[wn.synset("razor.n.01")],

	# physicist
	"U+422f":	[wn.synset("physicist.n.01")],

	# mezuzah
	"U+4230":	[wn.synset("mezuzah.n.01")],

	# cousin
	"U+4231":	[wn.synset("cousin.n.01")],

	# theologian, theologist
	"U+4232":	[wn.synset("theologian.n.01")],

	# Gemini
	"U+4233":	[wn.synset("gemini.n.01"),
				wn.synset("gemini.n.02"),
				wn.synset("gemini.n.03")],

	# website
	"U+4236":	[wn.synset("web_site.n.01"),
				wn.synset("world_wide_web.n.01")],

	# paraskiing
	"U+4237":	[wn.synset("parasailing.n.01")],

	# recording disk
	"U+4239":	[wn.synset("disk.n.02"),
				wn.synset("slice.n.05")],

	# Persian
	"U+423c":	[wn.synset("irani.n.01"),
				wn.synset("persian.n.02")],

	# diaphragm, pessary, midriff
	"U+423f":	[wn.synset("diaphragm.n.01"),
				wn.synset("diaphragm.n.02"),
				wn.synset("diaphragm.n.03")],

	# shame
	"U+4241":	[wn.synset("shame.n.01")],

	# astrologer, astrologist
	"U+4242":	[wn.synset("astrologer.n.01")],

	# disappear
	"U+4243":	[wn.synset("disappear.v.01")],

	# growl
	"U+4245":	[wn.synset("grumble.v.03"),
				wn.synset("snap.v.01")],

	# writer, author
	"U+4246":	[wn.synset("writer.n.01")],

	# waterfall
	"U+4248":	[wn.synset("waterfall.n.01")],

	# garlic
	"U+424a":	[wn.synset("garlic.n.02")],

	# unicorn
	"U+424b":	[wn.synset("unicorn.n.01")],

	# jealous
	"U+424d":	[wn.synset("covetous.s.01"),
				wn.synset("jealous.s.02")],

	# butter
	"U+424f":	[wn.synset("butter.n.01")],

	# tombstone
	"U+4250":	[wn.synset("gravestone.n.01")],

	# left turn, left, left turn,left
	"U+4251":	[wn.synset("left.n.01"),
				wn.synset("left.n.02"),
				wn.synset("left.n.03"),
				wn.synset("left.n.05"),
				wn.synset("left_field.n.01")],

	# napkin, serviette
	"U+4252":	[wn.synset("napkin.n.01")],

	# yes
	"U+4254":	[wn.synset("ti.n.03"),
				wn.synset("yes.n.01")],

	# sunflower
	"U+4255":	[wn.synset("sunflower.n.01")],

	# Aquarius
	"U+4256":	[wn.synset("aquarius.n.01"),
				wn.synset("aquarius.n.02"),
				wn.synset("aquarius.n.03")],

	# Freya
	"U+4257":	[wn.synset("freya.n.01")],

	# rock music
	"U+4258":	[wn.synset("rock_'n'_roll.n.01")],

	# signal reception
	"U+425a":	[wn.synset("reception.n.01"),
				wn.synset("reception.n.04"),
				wn.synset("reception_room.n.01")],

	# identity card
	"U+425b":	[wn.synset("card.n.02"),
				wn.synset("identification.n.02")],

	# deaf
	"U+425c":	[wn.synset("deaf.a.01")],

	# dining room
	"U+425d":	[wn.synset("dining_room.n.01")],

	# invoice
	"U+425e":	[wn.synset("bill.n.02")],

	# dear
	"U+425f":	[wn.synset("beloved.n.01"),
				wn.synset("lamb.n.04")],

	# theatre
	"U+4260":	[wn.synset("dramaturgy.n.01"),
				wn.synset("theater.n.01")],

	# microwave
	"U+4262":	[wn.synset("microwave.n.01"),
				wn.synset("microwave.n.02"),
				wn.synset("microwave.v.01")],

	# tracker
	"U+4263":	[wn.synset("tracker.n.01")],

	# burn
	"U+4264":	[wn.synset("burn.v.01"),
				wn.synset("burn.v.15"),
				wn.synset("burn_off.v.01")],

	# North America
	"U+4265":	[wn.synset("north_america.n.01")],

	# Sweden
	"U+4266":	[wn.synset("sweden.n.01")],

	# ice field
	"U+4267":	[wn.synset("ice_rink.n.01")],

	# bolt
	"U+4268":	[wn.synset("abscond.v.01"),
				wn.synset("bolt.v.01"),
				wn.synset("bolt.v.02"),
				wn.synset("bolt.v.03"),
				wn.synset("bolt.v.07"),
				wn.synset("box.v.01"),
				wn.synset("gobble.v.01"),
				wn.synset("pack.v.01"),
				wn.synset("run_off.v.02")],

	# bury
	"U+426a":	[wn.synset("bury.v.02")],

	# hide, conceal
	"U+426b":	[wn.synset("hide.v.01")],

	# sleeping bag
	"U+426c":	[wn.synset("sleeping_bag.n.01")],

	# afternoon
	"U+426d":	[wn.synset("afternoon.n.01")],

	# nerve
	"U+426e":	[wn.synset("nerve.n.01")],

	# castanets
	"U+426f":	[wn.synset("bones.n.01")],

	# jobcentre, job centre-centre
	"U+4270":	[wn.synset("jobcentre.n.01")],

	# flying
	"U+4272":	[wn.synset("fast-flying.s.01"),
				wn.synset("flying.s.02")],

	# educationalist, educationist
	"U+4273":	[wn.synset("educationist.n.01")],

	# January
	"U+4274":	[wn.synset("january.n.01")],

	# diaper, nappy
	"U+4275":	[wn.synset("diaper.n.01")],

	# fort, fortress
	"U+4276":	[wn.synset("fortress.n.01"),
				wn.synset("garrison.n.01")],

	# return, come back, reverse back,reverse
	"U+4277":	[wn.synset("come_back.v.01"),
				wn.synset("return.v.01")],

	# ski jumping
	"U+4278":	[wn.synset("ski_jump.n.01")],

	# lower leg, shank, shin, lower leg,shank,shin
	"U+4279":	[wn.synset("bet.n.02"),
				wn.synset("cannon.n.05"),
				wn.synset("shank.n.01"),
				wn.synset("shank.n.02"),
				wn.synset("shank.n.03"),
				wn.synset("shank.n.04"),
				wn.synset("shank.n.05"),
				wn.synset("shank.n.06"),
				wn.synset("shank.n.08"),
				wn.synset("shin.n.01"),
				wn.synset("shin.n.02"),
				wn.synset("shin.n.03"),
				wn.synset("tibia.n.01")],

	# Romanian
	"U+427a":	[wn.synset("romanian.n.02")],

	# Romania
	"U+427b":	[wn.synset("romania.n.01")],

	# Tibet
	"U+427e":	[wn.synset("tibet.n.01")],

	# cartoon, animated picture picture
	"U+427f":	[wn.synset("animation.n.05"),
				wn.synset("cartoon.n.01"),
				wn.synset("cartoon.n.02")],

	# digital
	"U+4280":	[wn.synset("digital.a.01")],

	# diet
	"U+4281":	[wn.synset("diet.n.01"),
				wn.synset("diet.n.03")],

	# exported
	"U+4282":	[wn.synset("export.v.01"),
				wn.synset("export.v.02"),
				wn.synset("export.v.03")],

	# export
	"U+4283":	[wn.synset("export.n.01")],

	# weekend
	"U+4284":	[wn.synset("weekend.n.01")],

	# week
	"U+4285":	[wn.synset("week.n.01"),
				wn.synset("week.n.03")],

	# potato
	"U+4286":	[wn.synset("potato.n.01")],

	# monkey, ape, gorilla, primate
	"U+4287":	[wn.synset("anthropoid.n.01"),
				wn.synset("ape.n.01"),
				wn.synset("archpriest.n.01"),
				wn.synset("copycat.n.01"),
				wn.synset("gorilla.n.01"),
				wn.synset("imp.n.02"),
				wn.synset("monkey.n.01"),
				wn.synset("primate.n.02")],

	# Megillah
	"U+4289":	[wn.synset("megillah.n.01"),
				wn.synset("megillah.n.02")],

	# invent
	"U+428a":	[wn.synset("fabricate.v.02"),
				wn.synset("invent.v.01")],

	# disgusting
	"U+428b":	[wn.synset("disgusting.s.01")],

	# disgust
	"U+428d":	[wn.synset("disgust.n.01")],

	# Holy Trinity
	"U+428f":	[wn.synset("trinity.n.02")],

	# smartphone, digital phone phone
	"U+4290":	[wn.synset("cellular_telephone.n.01")],

	# yeast
	"U+4292":	[wn.synset("yeast.n.01"),
				wn.synset("yeast.n.02")],

	# rubber boat, dinghy, rubber boat,dinghy
	"U+4293":	[wn.synset("dinghy.n.01")],

	# die
	"U+4294":	[wn.synset("die.v.01")],

	# dice, die
	"U+4295":	[wn.synset("die.n.01"),
				wn.synset("die.n.02"),
				wn.synset("die.n.03")],

	# magnet
	"U+4296":	[wn.synset("magnet.n.01")],

	# excellence
	"U+4297":	[wn.synset("excellence.n.01")],

	# correctness
	"U+4298":	[wn.synset("correctness.n.01"),
				wn.synset("correctness.n.02")],

	# shave
	"U+4299":	[wn.synset("shave.v.01")],

	# international
	"U+429c":	[wn.synset("international.a.01")],

	# makeup
	"U+429e":	[wn.synset("makeup.n.01")],

	# detest, despise
	"U+429f":	[wn.synset("abhor.v.01"),
				wn.synset("contemn.v.01"),
				wn.synset("hate.v.01")],

	# earthquake
	"U+42a0":	[wn.synset("earthquake.n.01")],

	# wait, waiting
	"U+42a2":	[wn.synset("delay.n.01"),
				wn.synset("wait.n.02")],

	# The Groke
	"U+42a4":	[wn.synset("bogey.n.01"),
				wn.synset("bogeyman.n.01"),
				wn.synset("bugbear.n.02")],

	# rocking horse
	"U+42a8":	[wn.synset("cockhorse.n.01"),
				wn.synset("hobby.n.02")],

	# kayak
	"U+42aa":	[wn.synset("kayak.n.01")],

	# Australia
	"U+42ac":	[wn.synset("australia.n.01"),
				wn.synset("australia.n.02")],

	# discus
	"U+42ad":	[wn.synset("disco.n.01"),
				wn.synset("disco.n.02"),
				wn.synset("discus.n.01"),
				wn.synset("discus.n.02"),
				wn.synset("disk.n.01"),
				wn.synset("disk.n.02"),
				wn.synset("magnetic_disk.n.01"),
				wn.synset("phonograph_record.n.01")],

	# bottle opener
	"U+42ae":	[wn.synset("bottle_opener.n.01"),
				wn.synset("cap_opener.n.01")],

	# somersault
	"U+42b0":	[wn.synset("somersault.n.01")],

	# cremate
	"U+42b1":	[wn.synset("cremate.v.01")],

	# labyrinth, maze
	"U+42b2":	[wn.synset("maze.n.01")],

	# GPS, satnav
	"U+42b3":	[wn.synset("global_positioning_system.n.01")],

	# soul
	"U+42b5":	[wn.synset("soul.n.01")],

	# reflector
	"U+42b6":	[wn.synset("reflector.n.01")],

	# predict
	"U+42b7":	[wn.synset("predict.v.01")],

	# rathole
	"U+42b9":	[wn.synset("rathole.n.02")],

	# purr
	"U+42ba":	[wn.synset("whizz.v.01")],

	# psychiatrist
	"U+42bb":	[wn.synset("psychiatrist.n.01")],

	# allergy, hypersensitivity
	"U+42bc":	[wn.synset("allergy.n.01")],

	# reaction
	"U+42bd":	[wn.synset("reaction.n.03"),
				wn.synset("reaction.n.05")],

	# tile
	"U+42be":	[wn.synset("tile.n.01")],

	# fertility counselling
	"U+42bf":	[wn.synset("fertility.n.02")],

	# sacrament of marriage
	"U+42c0":	[wn.synset("marriage.n.01"),
				wn.synset("marriage.n.02"),
				wn.synset("matrimony.n.02")],

	# accessory
	"U+42c1":	[wn.synset("accessory.n.01"),
				wn.synset("accessory.n.02"),
				wn.synset("accessory.n.03"),
				wn.synset("neckerchief.n.01")],

	# open one's mouth, hold one's mouth open, gape, open one's mouth,hold one's mouth open,gape
	"U+42c2":	[wn.synset("gape.v.02"),
				wn.synset("goggle.v.01")],

	# tablecloth
	"U+42c3":	[wn.synset("tablecloth.n.01")],

	# jellyfish
	"U+42c4":	[wn.synset("jellyfish.n.02")],

	# Christian charity
	"U+42c6":	[wn.synset("charity.n.03"),
				wn.synset("charity.n.05")],

	# pillowcase
	"U+42c8":	[wn.synset("case.n.19")],

	# shake, jiggle
	"U+42c9":	[wn.synset("shake.v.01")],

	# quarter of an hour
	"U+42ca":	[wn.synset("quarter.n.04")],

	# killer, murderer
	"U+42cc":	[wn.synset("murderer.n.01")],

	# lunch, dinner
	"U+42ce":	[wn.synset("lunch.n.01")],

	# safari, wildlife expedition expedition
	"U+42cf":	[wn.synset("campaign.n.04")],

	# sea chart
	"U+42d0":	[wn.synset("chart.n.02")],

	# own, possess
	"U+42d1":	[wn.synset("own.v.01"),
				wn.synset("possess.v.03")],

	# man made, man-made
	"U+42d2":	[wn.synset("fat.s.05"),
				wn.synset("man-made.s.01")],

	# bookshop
	"U+42d3":	[wn.synset("bookshop.n.01")],

	# monster
	"U+42d8":	[wn.synset("freak.n.01"),
				wn.synset("monster.n.01"),
				wn.synset("monster.n.04")],

	# ajar
	"U+42d9":	[wn.synset("ajar.s.01")],

	# cough
	"U+42da":	[wn.synset("cough.v.01")],

	# video recorder
	"U+42dc":	[wn.synset("videocassette_recorder.n.01")],

	# blacksmith
	"U+42dd":	[wn.synset("blacksmith.n.01")],

	# few, little
	"U+42e0":	[wn.synset("few.a.01"),
				wn.synset("little.a.02")],

	# mermaid
	"U+42e1":	[wn.synset("mermaid.n.01")],

	# anus
	"U+42e2":	[wn.synset("anus.n.01")],

	# Nisan, Nissan
	"U+42e3":	[wn.synset("nisan.n.01")],

	# memo, reminder note note
	"U+42e5":	[wn.synset("memo.n.01")],

	# exhibition hall, showplace, exhibition hall,showplace
	"U+42e6":	[wn.synset("audience.n.01"),
				wn.synset("dramaturgy.n.01"),
				wn.synset("scene.n.01"),
				wn.synset("showplace.n.01"),
				wn.synset("theater.n.01")],

	# osteopath
	"U+42e7":	[wn.synset("osteopath.n.01")],

	# ceramics, pottery
	"U+42e8":	[wn.synset("ceramic.n.01"),
				wn.synset("ceramics.n.01"),
				wn.synset("pottery.n.01"),
				wn.synset("pottery.n.02"),
				wn.synset("pottery.n.03")],

	# sailing
	"U+42e9":	[wn.synset("cruise.n.01"),
				wn.synset("glide.n.03"),
				wn.synset("sailing.n.02"),
				wn.synset("sailing.n.03"),
				wn.synset("seafaring.n.01")],

	# gigantic
	"U+42ea":	[wn.synset("elephantine.s.01"),
				wn.synset("gigantic.s.01")],

	# lullaby
	"U+42eb":	[wn.synset("lullaby.n.01")],

	# lick
	"U+42ec":	[wn.synset("lick.v.02")],

	# piccolo
	"U+42ed":	[wn.synset("piccolo.n.01")],

	# direct current, DC, direct current,DC
	"U+42ef":	[wn.synset("direct_current.n.01")],

	# silk fabric
	"U+42f0":	[wn.synset("silk.n.01"),
				wn.synset("silk.n.02")],

	# endangered
	"U+42f1":	[wn.synset("endangered.s.01")],

	# Kazakhstan
	"U+42f2":	[wn.synset("kazakhstan.n.01")],

	# chocolate bar
	"U+42f3":	[wn.synset("chocolate_bar.n.01"),
				wn.synset("jimmy.n.01")],

	# zigzag
	"U+42f4":	[wn.synset("zigzag.s.01")],

	# pair
	"U+42f6":	[wn.synset("couple.n.04"),
				wn.synset("pair.n.01"),
				wn.synset("pair.n.03")],

	# cornea
	"U+42f9":	[wn.synset("cornea.n.01")],

	# umbilical cord
	"U+42fb":	[wn.synset("umbilical_cord.n.01")],

	# cards, playing cards cards
	"U+42fc":	[wn.synset("batting_order.n.01"),
				wn.synset("calling_card.n.02"),
				wn.synset("card.n.01"),
				wn.synset("card.n.02"),
				wn.synset("card.n.03"),
				wn.synset("card.n.04"),
				wn.synset("card.n.08"),
				wn.synset("card_game.n.01"),
				wn.synset("circuit_board.n.01"),
				wn.synset("menu.n.01"),
				wn.synset("poster.n.01"),
				wn.synset("wag.n.01")],

	# hostage
	"U+42fd":	[wn.synset("hostage.n.01")],

	# hide and seek
	"U+42fe":	[wn.synset("hide-and-seek.n.01")],

	# family planning
	"U+4300":	[wn.synset("birth_control.n.01")],

	# chiropractor
	"U+4301":	[wn.synset("chiropractor.n.01")],

	# stupid, dumb
	"U+4304":	[wn.synset("stupid.a.01")],

	# fire truck, fire engine
	"U+4305":	[wn.synset("fire_engine.n.01")],

	# seal
	"U+4306":	[wn.synset("seal.n.09")],

	# calendar
	"U+430a":	[wn.synset("calendar.n.01")],

	# decoration, ornament
	"U+430c":	[wn.synset("decoration.n.01"),
				wn.synset("decoration.n.03")],

	# pump
	"U+430d":	[wn.synset("pump.v.03")],

	# killing, murder, slaughter
	"U+4310":	[wn.synset("murder.n.01")],

	# fried
	"U+4311":	[wn.synset("fried.s.01")],

	# rugby, football
	"U+4312":	[wn.synset("rugby.n.01")],

	# cancer
	"U+4315":	[wn.synset("cancer.n.01"),
				wn.synset("cancer.n.02"),
				wn.synset("cancer.n.03"),
				wn.synset("cancer.n.04"),
				wn.synset("cancer.n.05")],

	# light meter
	"U+4316":	[wn.synset("light_meter.n.01")],

	# mare
	"U+4317":	[wn.synset("mare.n.01")],

	# undershirt
	"U+4318":	[wn.synset("singlet.n.01")],

	# Good Friday
	"U+431a":	[wn.synset("good_friday.n.01")],

	# polytheism
	"U+431c":	[wn.synset("polytheism.n.01")],

	# bear's head
	"U+431e":	[wn.synset("bear.n.01")],

	# synagogue
	"U+4320":	[wn.synset("synagogue.n.01")],

	# workplace
	"U+4321":	[wn.synset("workplace.n.01")],

	# caesarean section, C section
	"U+4322":	[wn.synset("cesarean_delivery.n.01")],

	# running
	"U+4324":	[wn.synset("run.n.07")],

	# cloudberry
	"U+4325":	[wn.synset("cloudberry.n.01")],

	# Heaven, Kingdom of God of God
	"U+4326":	[wn.synset("eden.n.01")],

	# weave
	"U+4327":	[wn.synset("weave.v.02")],

	# school uniform
	"U+4328":	[wn.synset("uniform.n.01")],

	# Ramadan
	"U+4329":	[wn.synset("ramadan.n.01")],

	# solve
	"U+432a":	[wn.synset("solve.v.01")],

	# anemometer
	"U+432c":	[wn.synset("anemometer.n.01")],

	# riding school, manege
	"U+432f":	[wn.synset("carousel.n.01"),
				wn.synset("carousel.n.02"),
				wn.synset("merry-go-round.n.01")],

	# Taurus
	"U+4331":	[wn.synset("sanchez.n.01"),
				wn.synset("taurus.n.02"),
				wn.synset("taurus.n.03"),
				wn.synset("taurus.n.04")],

	# bull
	"U+4332":	[wn.synset("bull.n.01")],

	# copier, photocopier
	"U+4334":	[wn.synset("duplicator.n.01"),
				wn.synset("photocopier.n.01")],

	# filled food, stuffed food
	"U+4335":	[wn.synset("commissariat.n.01"),
				wn.synset("diet.n.01"),
				wn.synset("fare.n.04"),
				wn.synset("mast.n.03"),
				wn.synset("mess.n.03"),
				wn.synset("nutriment.n.01")],

	# terrorize
	"U+4336":	[wn.synset("terrify.v.01"),
				wn.synset("terrorize.v.01")],

	# nosy
	"U+4337":	[wn.synset("nosy.s.01")],

	# doll
	"U+4338":	[wn.synset("doll.n.01")],

	# rise, ascend, go up up
	"U+4339":	[wn.synset("arise.v.03"),
				wn.synset("ascend.v.01"),
				wn.synset("ascend.v.02"),
				wn.synset("ascend.v.03"),
				wn.synset("ascend.v.04"),
				wn.synset("ascend.v.05"),
				wn.synset("ascend.v.06"),
				wn.synset("ascend.v.08"),
				wn.synset("get_up.v.02"),
				wn.synset("heighten.v.01"),
				wn.synset("originate.v.01"),
				wn.synset("rebel.v.01"),
				wn.synset("resurrect.v.03"),
				wn.synset("rise.v.01"),
				wn.synset("rise.v.02"),
				wn.synset("rise.v.04"),
				wn.synset("rise.v.11"),
				wn.synset("rise.v.12"),
				wn.synset("rise.v.13"),
				wn.synset("rise.v.15"),
				wn.synset("rise.v.16"),
				wn.synset("surface.v.01"),
				wn.synset("wax.v.02")],

	# alternating current, AC
	"U+433a":	[wn.synset("alternating_current.n.01")],

	# pasture, enclosed field field, put out to pasture out to pasture
	"U+433b":	[wn.synset("crop.v.04"),
				wn.synset("crop.v.05")],

	# organization, organizing
	"U+433c":	[wn.synset("administration.n.02"),
				wn.synset("arrangement.n.03"),
				wn.synset("constitution.n.02"),
				wn.synset("form.v.01"),
				wn.synset("mastermind.v.01"),
				wn.synset("organization.n.01"),
				wn.synset("organization.n.04"),
				wn.synset("organization.n.05"),
				wn.synset("organization.n.06"),
				wn.synset("organize.v.02"),
				wn.synset("organize.v.04"),
				wn.synset("organize.v.05"),
				wn.synset("unionize.v.02")],

	# too much, too many
	"U+433d":	[wn.synset("excessively.r.01"),
				wn.synset("overmuch.r.01")],

	# lotto, bingo
	"U+433e":	[wn.synset("lotto.n.01")],

	# raincoat
	"U+433f":	[wn.synset("raincoat.n.01")],

	# broken
	"U+4340":	[wn.synset("broken.a.01"),
				wn.synset("broken.s.13")],

	# bird of prey, raptor, bird of prey,raptor
	"U+4341":	[wn.synset("bird_of_prey.n.01")],

	# tease
	"U+4343":	[wn.synset("tease.v.01"),
				wn.synset("tease.v.02"),
				wn.synset("tease.v.03"),
				wn.synset("tease.v.04"),
				wn.synset("tease.v.05"),
				wn.synset("tease.v.06"),
				wn.synset("tease.v.07"),
				wn.synset("tease.v.08"),
				wn.synset("tease.v.09")],

	# roar
	"U+4345":	[wn.synset("bellow.v.02"),
				wn.synset("howl.v.01"),
				wn.synset("roar.v.01"),
				wn.synset("roar.v.04"),
				wn.synset("roar.v.06"),
				wn.synset("thunder.v.02")],

	# toothpaste
	"U+4346":	[wn.synset("toothpaste.n.01")],

	# folk music
	"U+4347":	[wn.synset("folk_music.n.01")],

	# fertile
	"U+4348":	[wn.synset("fertile.a.01")],

	# control oneself
	"U+4349":	[wn.synset("administer.v.01"),
				wn.synset("check.v.08"),
				wn.synset("check.v.19"),
				wn.synset("check.v.22"),
				wn.synset("control.v.01"),
				wn.synset("control.v.02"),
				wn.synset("control.v.05"),
				wn.synset("control.v.06"),
				wn.synset("dominate.v.02"),
				wn.synset("dominate.v.03"),
				wn.synset("dominate.v.05"),
				wn.synset("exceed.v.01"),
				wn.synset("exceed.v.02"),
				wn.synset("excel.v.01"),
				wn.synset("get_the_better_of.v.01"),
				wn.synset("govern.v.03"),
				wn.synset("manipulate.v.05"),
				wn.synset("master.v.04"),
				wn.synset("monitor.v.01"),
				wn.synset("operate.v.03"),
				wn.synset("outclass.v.01"),
				wn.synset("outdo.v.02"),
				wn.synset("outpoint.v.02"),
				wn.synset("outshine.v.02"),
				wn.synset("outwit.v.01"),
				wn.synset("predominate.v.01"),
				wn.synset("prevail.v.03"),
				wn.synset("prevail.v.04"),
				wn.synset("see.v.10"),
				wn.synset("surpass.v.02")],

	# liquor shop
	"U+434a":	[wn.synset("package_store.n.01")],

	# Balder
	"U+434b":	[wn.synset("balder.n.01")],

	# trapeze
	"U+434f":	[wn.synset("trapeze.n.01")],

	# acrobatics
	"U+4350":	[wn.synset("acrobatics.n.01")],

	# baby carriage, buggy, pram, pushchair, stroller, baby carriage,buggy,pram,pushchair,stroller
	"U+4352":	[wn.synset("baby_buggy.n.01")],

	# God the father
	"U+4353":	[wn.synset("deity.n.01")],

	# hiccup
	"U+4354":	[wn.synset("hiccup.n.01")],

	# multi storey building
	"U+4355":	[wn.synset("building.n.01")],

	# walkway, footpath
	"U+4356":	[wn.synset("pathway.n.02"),
				wn.synset("walk.n.05")],

	# blackbird, crow, raven
	"U+4358":	[wn.synset("blackbird.n.02")],

	# USA
	"U+435b":	[wn.synset("united_states.n.01"),
				wn.synset("united_states_army.n.01")],

	# rapids
	"U+435c":	[wn.synset("rapid.n.01")],

	# general
	"U+435d":	[wn.synset("general.a.01")],

	# examine
	"U+435e":	[wn.synset("examine.v.02")],

	# girlfriend
	"U+435f":	[wn.synset("girlfriend.n.02")],

	# court, field, courtroom, courthouse
	"U+4360":	[wn.synset("court.n.10"),
				wn.synset("discipline.n.01"),
				wn.synset("field.n.01"),
				wn.synset("field.n.03"),
				wn.synset("field.n.05"),
				wn.synset("field.n.06"),
				wn.synset("field.n.10"),
				wn.synset("field.n.11"),
				wn.synset("field.n.14"),
				wn.synset("field.n.16"),
				wn.synset("plain.n.01"),
				wn.synset("playing_field.n.02"),
				wn.synset("sphere.n.01")],

	# sneeze
	"U+4363":	[wn.synset("sneeze.v.01")],

	# herring, sardine
	"U+4364":	[wn.synset("herring.n.01"),
				wn.synset("herring.n.02"),
				wn.synset("pilchard.n.02"),
				wn.synset("sardine.n.02")],

	# ovary
	"U+4366":	[wn.synset("ovary.n.02")],

	# tuna fish
	"U+4367":	[wn.synset("tuna.n.03")],

	# dollar
	"U+4368":	[wn.synset("dollar.n.01"),
				wn.synset("dollar.n.02")],

	# those
	"U+436a":	[wn.synset("conviction.n.02"),
				wn.synset("judgment.n.03"),
				wn.synset("verdict.n.01")],

	# scout
	"U+436c":	[wn.synset("browser.n.02"),
				wn.synset("camper.n.01"),
				wn.synset("lookout.n.01"),
				wn.synset("scout.n.02"),
				wn.synset("scout.n.03"),
				wn.synset("scout.n.04")],

	# Sivan
	"U+436e":	[wn.synset("sivan.n.01")],

	# portable
	"U+436f":	[wn.synset("portable.a.01"),
				wn.synset("portable.s.02")],

	# grasshopper
	"U+4370":	[wn.synset("grasshopper.n.01")],

	# lawyer
	"U+4372":	[wn.synset("lawyer.n.01")],

	# cable car
	"U+4373":	[wn.synset("telpherage.n.01")],

	# public
	"U+4375":	[wn.synset("populace.n.01"),
				wn.synset("public.n.02")],

	# donkey, mule
	"U+4377":	[wn.synset("domestic_ass.n.01"),
				wn.synset("donkey.n.01")],

	# publisher
	"U+4378":	[wn.synset("publisher.n.01")],

	# search
	"U+4379":	[wn.synset("research.v.02"),
				wn.synset("search.v.01"),
				wn.synset("search.v.02"),
				wn.synset("search.v.04")],

	# lasagne, lasagna
	"U+437b":	[wn.synset("lasagna.n.01"),
				wn.synset("lasagna.n.02")],

	# airport
	"U+437c":	[wn.synset("airport.n.01")],

	# cowardly
	"U+437e":	[wn.synset("cowardly.a.01")],

	# water meter
	"U+437f":	[wn.synset("water_meter.n.01")],

	# armed
	"U+4380":	[wn.synset("armed.a.01")],

	# weapon
	"U+4381":	[wn.synset("weapon.n.01")],

	# Europe
	"U+4382":	[wn.synset("europe.n.01")],

	# lollipop, sucker
	"U+4383":	[wn.synset("lollipop.n.02")],

	# splash
	"U+4384":	[wn.synset("spatter.v.01")],

	# coral reef
	"U+4385":	[wn.synset("breakwater.n.01"),
				wn.synset("stumbling_block.n.01")],

	# maple syrup flavouring
	"U+4386":	[wn.synset("maple_syrup.n.01")],

	# nothing, none
	"U+4388":	[wn.synset("nothing.n.01")],

	# isosceles triangle
	"U+4389":	[wn.synset("triangle.n.01")],

	# driving license
	"U+438a":	[wn.synset("driver's_license.n.01")],

	# den, lair
	"U+438b":	[wn.synset("bullet.n.01"),
				wn.synset("burrow.n.01"),
				wn.synset("den.n.03"),
				wn.synset("den.n.04"),
				wn.synset("hideout.n.01"),
				wn.synset("lair.n.01")],

	# shark
	"U+438c":	[wn.synset("shark.n.01")],

	# ritual
	"U+438d":	[wn.synset("ritual.n.01"),
				wn.synset("ritual.n.02")],

	# hamburger
	"U+438e":	[wn.synset("hamburger.n.01")],

	# share
	"U+438f":	[wn.synset("share.v.02")],

	# birdhouse, house for bird for bird
	"U+4390":	[wn.synset("birdhouse.n.01")],

	# botanist
	"U+4391":	[wn.synset("botanist.n.01")],

	# botany
	"U+4392":	[wn.synset("botany.n.02")],

	# rye
	"U+4394":	[wn.synset("rye.n.01")],

	# Tyr
	"U+4395":	[wn.synset("tyr.n.01")],

	# punk rock
	"U+4396":	[wn.synset("punk_rock.n.01")],

	# orchard
	"U+4398":	[wn.synset("grove.n.02")],

	# mislead
	"U+4399":	[wn.synset("misinform.v.01")],

	# stepparent, step parent-parent
	"U+439a":	[wn.synset("stepparent.n.01")],

	# Christmas pudding
	"U+439b":	[wn.synset("plum_pudding.n.01")],

	# New Year's Day
	"U+439c":	[wn.synset("new_year's_day.n.01")],

	# dough
	"U+439d":	[wn.synset("dough.n.01")],

	# flour
	"U+439e":	[wn.synset("flour.n.01")],

	# muskrat
	"U+43a0":	[wn.synset("muskrat.n.02")],

	# late
	"U+43a2":	[wn.synset("belated.s.01"),
				wn.synset("former.s.03"),
				wn.synset("late.a.01"),
				wn.synset("late.a.05"),
				wn.synset("late.a.06"),
				wn.synset("late.r.01"),
				wn.synset("late.s.03"),
				wn.synset("late.s.04")],

	# detach, take apart apart
	"U+43a3":	[wn.synset("detach.v.01"),
				wn.synset("detach.v.02"),
				wn.synset("detach.v.03")],

	# chairlift
	"U+43a6":	[wn.synset("chairlift.n.01")],

	# pregnant
	"U+43a7":	[wn.synset("pregnant.a.01")],

	# astarboard
	"U+43a8":	[wn.synset("starboard.n.01")],

	# greengrocer
	"U+43a9":	[wn.synset("greengrocer.n.01")],

	# rabbit, hare
	"U+43ab":	[wn.synset("rabbit.n.01")],

	# difficulty
	"U+43ac":	[wn.synset("difficulty.n.02"),
				wn.synset("difficulty.n.03"),
				wn.synset("difficulty.n.04"),
				wn.synset("trouble.n.04")],

	# schoolmate
	"U+43ae":	[wn.synset("schoolmate.n.01")],

	# harp
	"U+43af":	[wn.synset("harp.n.01")],

	# prepare food, cook
	"U+43b0":	[wn.synset("cook.v.02")],

	# print
	"U+43b1":	[wn.synset("print.v.01"),
				wn.synset("print.v.02"),
				wn.synset("print.v.03"),
				wn.synset("print.v.04")],

	# Ukraine
	"U+43b4":	[wn.synset("ukraine.n.01")],

	# nice, pleasant
	"U+43b5":	[wn.synset("pleasant.a.01")],

	# prophet
	"U+43b7":	[wn.synset("prophet.n.01"),
				wn.synset("prophet.n.02")],

	# corkscrew
	"U+43b8":	[wn.synset("corkscrew.n.01")],

	# copper
	"U+43ba":	[wn.synset("copper.n.01")],

	# shoal, school
	"U+43bb":	[wn.synset("school.n.07")],

	# divorce
	"U+43bc":	[wn.synset("disassociate.v.01"),
				wn.synset("divorce.v.02")],

	# hidden treasure, treasure trove
	"U+43bd":	[wn.synset("tax.n.01"),
				wn.synset("treasure.n.04")],

	# jewel
	"U+43be":	[wn.synset("jewel.n.02")],

	# build, construct
	"U+43bf":	[wn.synset("construct.v.01"),
				wn.synset("construct.v.03"),
				wn.synset("manufacture.v.01")],

	# paint, dye
	"U+43c0":	[wn.synset("paint.n.01")],

	# statement
	"U+43c1":	[wn.synset("affirmation.n.02"),
				wn.synset("argument.n.01"),
				wn.synset("instruction.n.04"),
				wn.synset("statement.n.01"),
				wn.synset("statement.n.03"),
				wn.synset("statement.n.04"),
				wn.synset("statement.n.07")],

	# Belgium
	"U+43c2":	[wn.synset("belgium.n.01")],

	# compartment
	"U+43c3":	[wn.synset("compartment.n.01"),
				wn.synset("compartment.n.02")],

	# voyeurism
	"U+43c4":	[wn.synset("voyeurism.n.01")],

	# breathing aid
	"U+43c6":	[wn.synset("breathing_device.n.01"),
				wn.synset("respirator.n.01")],

	# dentist
	"U+43c7":	[wn.synset("dentist.n.01")],

	# believe
	"U+43c9":	[wn.synset("believe.v.01")],

	# wind power, wind energy, wind farm, wind power,wind energy,wind farm
	"U+43ca":	[wn.synset("wind_generation.n.01")],

	# salmon
	"U+43cb":	[wn.synset("salmon.n.01"),
				wn.synset("salmon.n.02"),
				wn.synset("salmon.n.03"),
				wn.synset("salmon.n.04")],

	# Christmas tree
	"U+43cd":	[wn.synset("christmas_tree.n.05")],

	# charm
	"U+43ce":	[wn.synset("appeal.n.02")],

	# refrigerator, fridge
	"U+43cf":	[wn.synset("electric_refrigerator.n.01"),
				wn.synset("refrigerator.n.01")],

	# Egypt
	"U+43d0":	[wn.synset("egypt.n.01")],

	# train station
	"U+43d1":	[wn.synset("railway_station.n.01")],

	# Pisces
	"U+43d2":	[wn.synset("pisces.n.01")],

	# organism
	"U+43d3":	[wn.synset("organism.n.01"),
				wn.synset("organism.n.02")],

	# outdoor, outdoors
	"U+43d7":	[wn.synset("outdoor.a.01")],

	# find
	"U+43d8":	[wn.synset("find.v.01"),
				wn.synset("find.v.03")],

	# giant
	"U+43d9":	[wn.synset("colossus.n.02"),
				wn.synset("giant.n.01"),
				wn.synset("giant.n.03"),
				wn.synset("giant.n.04"),
				wn.synset("giant.n.05"),
				wn.synset("giant.n.06"),
				wn.synset("giant_star.n.01")],

	# bandit, armed robber robber
	"U+43da":	[wn.synset("bandit.n.01")],

	# batter
	"U+43dd":	[wn.synset("batter.n.02")],

	# smell bad, stink
	"U+43de":	[wn.synset("reek.v.02"),
				wn.synset("stink.v.01")],

	# silk
	"U+43e0":	[wn.synset("silk.n.01")],

	# TV programme, TV show, radio programme, TV programme,TV show,radio programme
	"U+43e1":	[wn.synset("show.n.01")],

	# infectious, contagious
	"U+43e2":	[wn.synset("infectious.a.02")],

	# Triceratops
	"U+43e4":	[wn.synset("triceratops.n.01")],

	# snorkeling, scuba diving, deep sea diving diving,deep sea diving
	"U+43e5":	[wn.synset("dip.n.08"),
				wn.synset("dive.n.02"),
				wn.synset("dive.n.03"),
				wn.synset("snorkeling.n.01")],

	# gospel
	"U+43e6":	[wn.synset("gospel.n.01")],

	# lower arm bone
	"U+43e7":	[wn.synset("radio.n.01"),
				wn.synset("radio.n.03"),
				wn.synset("radio_receiver.n.01"),
				wn.synset("radium.n.01"),
				wn.synset("radius.n.01"),
				wn.synset("radius.n.02"),
				wn.synset("radius.n.03"),
				wn.synset("radius.n.04"),
				wn.synset("spoke.n.01")],

	# lower arm
	"U+43e8":	[wn.synset("forearm.n.01")],

	# burned, burnt
	"U+43e9":	[wn.synset("burned.s.01")],

	# sparkling wine
	"U+43ea":	[wn.synset("champagne.n.01")],

	# restaurant, cafeteria
	"U+43eb":	[wn.synset("restaurant.n.01")],

	# foreign
	"U+43ed":	[wn.synset("foreign.a.01"),
				wn.synset("foreign.a.02")],

	# hard cheese
	"U+43ee":	[wn.synset("cheese.n.01")],

	# misericordia
	"U+43ef":	[wn.synset("commiseration.n.01"),
				wn.synset("compassion.n.02"),
				wn.synset("mercifulness.n.01"),
				wn.synset("mercifulness.n.02")],

	# expensive
	"U+43f1":	[wn.synset("expensive.a.01")],

	# apostle
	"U+43f2":	[wn.synset("apostle.n.03")],

	# create
	"U+43f3":	[wn.synset("create.v.02"),
				wn.synset("make.v.03")],

	# Passover
	"U+43f4":	[wn.synset("passover.n.01")],

	# choke, gag
	"U+43f6":	[wn.synset("choke.v.01"),
				wn.synset("choke.v.02"),
				wn.synset("choke.v.03"),
				wn.synset("choke.v.04"),
				wn.synset("choke.v.06"),
				wn.synset("choke.v.07"),
				wn.synset("choke.v.13"),
				wn.synset("clog.v.01"),
				wn.synset("die.v.01"),
				wn.synset("gag.v.01"),
				wn.synset("gag.v.03"),
				wn.synset("gag.v.04"),
				wn.synset("gag.v.05"),
				wn.synset("gag.v.06"),
				wn.synset("gag.v.07"),
				wn.synset("suffocate.v.02"),
				wn.synset("suffocate.v.03"),
				wn.synset("suffocate.v.04")],

	# pierce
	"U+43f8":	[wn.synset("pierce.v.04"),
				wn.synset("pierce.v.05")],

	# politician
	"U+43f9":	[wn.synset("politician.n.02")],

	# politics
	"U+43fa":	[wn.synset("politics.n.03")],

	# genocide, holocaust
	"U+43fb":	[wn.synset("genocide.n.01")],

	# horseshoe
	"U+43fd":	[wn.synset("horseshoe.n.01"),
				wn.synset("horseshoe.n.02")],

	# remembrance day
	"U+43fe":	[wn.synset("commemoration.n.01")],

	# sexuality
	"U+4400":	[wn.synset("sex.n.04")],

	# radio
	"U+4401":	[wn.synset("radio_receiver.n.01")],

	# century
	"U+4402":	[wn.synset("century.n.01")],

	# breastbone, sternum
	"U+4404":	[wn.synset("sternum.n.01")],

	# urethra
	"U+4405":	[wn.synset("urethra.n.01")],

	# sociologist
	"U+4406":	[wn.synset("sociologist.n.01")],

	# medical insurance
	"U+4407":	[wn.synset("health_care.n.01"),
				wn.synset("health_insurance.n.01")],

	# ewe
	"U+4408":	[wn.synset("ewe.n.01"),
				wn.synset("ewe.n.02"),
				wn.synset("ewe.n.03"),
				wn.synset("thank.v.01")],

	# itch
	"U+4409":	[wn.synset("itch.n.03"),
				wn.synset("scabies.n.01"),
				wn.synset("tinea.n.01"),
				wn.synset("urge.n.02")],

	# uncomfortable
	"U+440a":	[wn.synset("uncomfortable.a.01"),
				wn.synset("uncomfortable.a.02")],

	# leopard
	"U+440b":	[wn.synset("leopard.n.02")],

	# yesterday
	"U+440c":	[wn.synset("yesterday.n.01")],

	# lacrosse
	"U+440e":	[wn.synset("lacrosse.n.01")],

	# iron age
	"U+4410":	[wn.synset("iron_age.n.01")],

	# cut
	"U+4412":	[wn.synset("cut.v.01")],

	# wound, cut, sore
	"U+4413":	[wn.synset("wound.n.01")],

	# stand in, substitute, alternate, stand-in,substitute,alternate
	"U+4415":	[wn.synset("deputy.n.02"),
				wn.synset("stand-in.n.01"),
				wn.synset("substitute.n.01"),
				wn.synset("substitute.n.02"),
				wn.synset("surrogate.n.01")],

	# North Pole
	"U+4416":	[wn.synset("north_pole.n.01")],

	# easter
	"U+4417":	[wn.synset("easter.n.01")],

	# bib
	"U+4419":	[wn.synset("bib.n.02")],

	# littleness, smallness
	"U+441a":	[wn.synset("pettiness.n.03"),
				wn.synset("smallness.n.01"),
				wn.synset("smallness.n.02"),
				wn.synset("smallness.n.03")],

	# knock, tap
	"U+441c":	[wn.synset("faucet.n.01"),
				wn.synset("pat.n.01"),
				wn.synset("rap.n.02"),
				wn.synset("tap.n.04"),
				wn.synset("tap.n.05"),
				wn.synset("tap.n.06"),
				wn.synset("tap.n.08"),
				wn.synset("water_faucet.n.01"),
				wn.synset("wiretap.n.01")],

	# sports glove, glove, mitt, sports glove,glove,mitt
	"U+441d":	[wn.synset("baseball_glove.n.01"),
				wn.synset("boxing_glove.n.01"),
				wn.synset("glove.n.02"),
				wn.synset("hand.n.01")],

	# walrus
	"U+441f":	[wn.synset("walrus.n.01")],

	# cheerleader
	"U+4420":	[wn.synset("cheerleader.n.01"),
				wn.synset("cheerleader.n.02")],

	# falafel
	"U+4421":	[wn.synset("falafel.n.01")],

	# candle
	"U+4422":	[wn.synset("candle.n.01")],

	# pet
	"U+4423":	[wn.synset("pet.n.01")],

	# bench, pew
	"U+4425":	[wn.synset("bench.n.01"),
				wn.synset("bench.n.05"),
				wn.synset("bench.n.06"),
				wn.synset("bench.n.07"),
				wn.synset("judiciary.n.01"),
				wn.synset("pew.n.01"),
				wn.synset("terrace.n.02"),
				wn.synset("workbench.n.01")],

	# cut and paste
	"U+4426":	[wn.synset("break.v.43"),
				wn.synset("carve.v.02"),
				wn.synset("cut.v.01"),
				wn.synset("cut_off.v.03"),
				wn.synset("dilute.v.01"),
				wn.synset("divide.v.01"),
				wn.synset("edit.v.03"),
				wn.synset("interrupt.v.01"),
				wn.synset("mow.v.01"),
				wn.synset("reduce.v.01"),
				wn.synset("slash.v.01"),
				wn.synset("slash.v.03"),
				wn.synset("slash.v.04"),
				wn.synset("slice.v.04"),
				wn.synset("slit.v.01"),
				wn.synset("snip.v.02"),
				wn.synset("traverse.v.01")],

	# patient, enduring
	"U+4428":	[wn.synset("patient.a.01")],

	# patience
	"U+4429":	[wn.synset("patience.n.01")],

	# drama
	"U+442d":	[wn.synset("drama.n.02"),
				wn.synset("drama.n.03"),
				wn.synset("drama.n.04"),
				wn.synset("play.n.01")],

	# pollution
	"U+442e":	[wn.synset("pollution.n.01")],

	# seat belt
	"U+442f":	[wn.synset("seat_belt.n.01")],

	# water skiing
	"U+4430":	[wn.synset("water-skiing.n.01")],

	# water ski
	"U+4431":	[wn.synset("water_ski.n.01")],

	# jockey
	"U+4433":	[wn.synset("jockey.n.01")],

	# horse rider, equestrian
	"U+4434":	[wn.synset("horseman.n.01")],

	# infected
	"U+4435":	[wn.synset("infection.n.01"),
				wn.synset("septic.a.01")],

	# translate
	"U+4437":	[wn.synset("translate.v.01")],

	# Cheshvan
	"U+4439":	[wn.synset("heshvan.n.01")],

	# garden centre
	"U+443a":	[wn.synset("hatchery.n.01")],

	# cure
	"U+443b":	[wn.synset("bring_around.v.02")],

	# percent, percentage, %,%
	"U+443c":	[wn.synset("percentage.n.01")],

	# May
	"U+443d":	[wn.synset("may.n.01")],

	# tax, regional)
	"U+443e":	[wn.synset("tax.n.01")],

	# favourite
	"U+443f":	[wn.synset("favored.s.01"),
				wn.synset("favorite.s.01")],

	# tablespoon
	"U+4440":	[wn.synset("tablespoon.n.01"),
				wn.synset("tablespoon.n.02")],

	# charming
	"U+4441":	[wn.synset("charming.s.01"),
				wn.synset("charming.s.02")],

	# desert
	"U+4442":	[wn.synset("desert.n.01")],

	# day and night
	"U+4443":	[wn.synset("day.n.01")],

	# give birth
	"U+4445":	[wn.synset("food.n.01")],

	# reindeer, caribou
	"U+4446":	[wn.synset("caribou.n.01")],

	# amplifier
	"U+4448":	[wn.synset("amplifier.n.01")],

	# snowmobile
	"U+444a":	[wn.synset("snowmobile.n.01")],

	# rudder
	"U+444b":	[wn.synset("rudder.n.01"),
				wn.synset("rudder.n.02")],

	# ingredient
	"U+444c":	[wn.synset("ingredient.n.01")],

	# dessert
	"U+444d":	[wn.synset("dessert.n.01")],

	# rhyme
	"U+444e":	[wn.synset("rhyme.n.01")],

	# accuse, charge, prosecute
	"U+444f":	[wn.synset("accuse.v.01"),
				wn.synset("agitate.v.02"),
				wn.synset("appoint.v.02"),
				wn.synset("blame.v.03"),
				wn.synset("charge.v.01"),
				wn.synset("charge.v.02"),
				wn.synset("charge.v.03"),
				wn.synset("charge.v.06"),
				wn.synset("charge.v.07"),
				wn.synset("charge.v.08"),
				wn.synset("charge.v.09"),
				wn.synset("charge.v.12"),
				wn.synset("charge.v.13"),
				wn.synset("charge.v.15"),
				wn.synset("charge.v.17"),
				wn.synset("charge.v.18"),
				wn.synset("charge.v.19"),
				wn.synset("charge.v.20"),
				wn.synset("charge.v.22"),
				wn.synset("charge.v.23"),
				wn.synset("charge.v.24"),
				wn.synset("charge.v.25"),
				wn.synset("commit.v.03"),
				wn.synset("consign.v.02"),
				wn.synset("indict.v.01"),
				wn.synset("load.v.02"),
				wn.synset("prosecute.v.01"),
				wn.synset("prosecute.v.02"),
				wn.synset("prosecute.v.03"),
				wn.synset("tear.v.03")],

	# surgeon
	"U+4450":	[wn.synset("surgeon.n.01")],

	# challah
	"U+4451":	[wn.synset("challah.n.01")],

	# Turkey
	"U+4454":	[wn.synset("turkey.n.02")],

	# Norway
	"U+4458":	[wn.synset("norway.n.01")],

	# intrauterine device, IUD
	"U+445a":	[wn.synset("coil.n.02"),
				wn.synset("coil.n.04"),
				wn.synset("intrauterine_device.n.01"),
				wn.synset("spiral.n.01"),
				wn.synset("spiral.n.04")],

	# access
	"U+445b":	[wn.synset("access.v.01"),
				wn.synset("access.v.02")],

	# climb
	"U+445f":	[wn.synset("climb.v.01"),
				wn.synset("rise.v.02")],

	# ejaculation
	"U+4461":	[wn.synset("ejaculation.n.02")],

	# Valhalla
	"U+4462":	[wn.synset("valhalla.n.01")],

	# manna
	"U+4463":	[wn.synset("miraculous_food.n.01")],

	# trachea, wind pipe pipe
	"U+4464":	[wn.synset("trachea.n.01")],

	# private
	"U+4465":	[wn.synset("private.a.01")],

	# composer
	"U+4467":	[wn.synset("composer.n.01")],

	# lime
	"U+4468":	[wn.synset("lime.n.04"),
				wn.synset("lime.n.06")],

	# thirsty
	"U+446a":	[wn.synset("athirst.s.01"),
				wn.synset("thirsty.a.02"),
				wn.synset("thirsty.s.01"),
				wn.synset("thirsty.s.04")],

	# orthopaedist
	"U+446b":	[wn.synset("orthopedist.n.01")],

	# asteroid
	"U+446c":	[wn.synset("asteroid.n.01")],

	# handcraft, craft
	"U+446d":	[wn.synset("craft.v.01"),
				wn.synset("handcraft.v.01")],

	# harvest
	"U+446e":	[wn.synset("crop.n.01")],

	# Estonia
	"U+446f":	[wn.synset("estonia.n.01")],

	# hymnal, hymn book book
	"U+4470":	[wn.synset("hymnal.n.01")],

	# hangar
	"U+4473":	[wn.synset("airdock.n.01")],

	# democracy
	"U+4474":	[wn.synset("democracy.n.01"),
				wn.synset("democracy.n.02"),
				wn.synset("majority_rule.n.01")],

	# boxing
	"U+4476":	[wn.synset("boxing.n.01")],

	# philosophy
	"U+4478":	[wn.synset("doctrine.n.01"),
				wn.synset("philosophy.n.02"),
				wn.synset("philosophy.n.03")],

	# curtain, drape
	"U+4479":	[wn.synset("curtain.n.01"),
				wn.synset("curtain.n.02"),
				wn.synset("drape.n.02"),
				wn.synset("drape.n.03")],

	# linen, flax fabric fabric
	"U+447a":	[wn.synset("linen.n.03")],

	# Buddha
	"U+447b":	[wn.synset("buddha.n.01"),
				wn.synset("buddha.n.02")],

	# spell
	"U+447d":	[wn.synset("spell.v.01"),
				wn.synset("spell.v.02"),
				wn.synset("spell.v.03"),
				wn.synset("spell.v.04"),
				wn.synset("spell.v.05"),
				wn.synset("spell.v.06")],

	# prime minister
	"U+447e":	[wn.synset("chancellor.n.02")],

	# cider
	"U+447f":	[wn.synset("cider.n.01")],

	# musical group
	"U+4480":	[wn.synset("musical_organization.n.01")],

	# be patient
	"U+4481":	[wn.synset("patient.a.01"),
				wn.synset("patient.n.01")],

	# China
	"U+4482":	[wn.synset("china.n.01")],

	# barley
	"U+4483":	[wn.synset("barley.n.01"),
				wn.synset("barley.n.02")],

	# straw, drinking straw straw
	"U+4484":	[wn.synset("chaff.n.01"),
				wn.synset("pale_yellow.n.01"),
				wn.synset("straw.n.01"),
				wn.synset("straw.n.04")],

	# amuse, entertain, please
	"U+4485":	[wn.synset("amuse.v.01"),
				wn.synset("amuse.v.02")],

	# bleed
	"U+4486":	[wn.synset("shed_blood.v.02")],

	# eyebrow pencil
	"U+4488":	[wn.synset("eyebrow_pencil.n.01")],

	# mortal
	"U+4489":	[wn.synset("mortal.a.01"),
				wn.synset("mortal.s.03")],

	# workbook
	"U+448a":	[wn.synset("fascicle.n.01"),
				wn.synset("workbook.n.01")],

	# embarrassed
	"U+448b":	[wn.synset("abashed.s.01"),
				wn.synset("coy.s.03"),
				wn.synset("embarrassed.s.02")],

	# embarrassment
	"U+448c":	[wn.synset("embarrassment.n.01")],

	# puppet
	"U+448d":	[wn.synset("creature.n.03"),
				wn.synset("puppet.n.01"),
				wn.synset("puppet.n.03")],

	# oesophagus, gullet
	"U+448f":	[wn.synset("esophagus.n.01")],

	# unending
	"U+4490":	[wn.synset("ageless.s.01")],

	# prune
	"U+4491":	[wn.synset("prune.n.01")],

	# shampoo
	"U+4492":	[wn.synset("shampoo.n.01")],

	# amplitude
	"U+4493":	[wn.synset("amplitude.n.01"),
				wn.synset("amplitude.n.03")],

	# anthropologist
	"U+4494":	[wn.synset("anthropologist.n.01")],

	# bisexual
	"U+4496":	[wn.synset("bisexual.a.01")],

	# bisexuality
	"U+4497":	[wn.synset("bisexuality.n.02")],

	# comfortable, restful
	"U+4498":	[wn.synset("comfortable.a.01"),
				wn.synset("comfortable.a.02"),
				wn.synset("comfortable.s.03"),
				wn.synset("comfortable.s.04"),
				wn.synset("comfortable.s.05"),
				wn.synset("pleasant.a.01"),
				wn.synset("restful.a.01")],

	# have
	"U+449a":	[wn.synset("experience.v.03"),
				wn.synset("give_birth.v.01"),
				wn.synset("have.v.01"),
				wn.synset("have.v.02"),
				wn.synset("have.v.09"),
				wn.synset("have.v.10"),
				wn.synset("have.v.11"),
				wn.synset("have.v.12"),
				wn.synset("own.v.01")],

	# sidecar
	"U+449b":	[wn.synset("sidecar.n.01"),
				wn.synset("sidecar.n.02")],

	# billiards
	"U+449d":	[wn.synset("billiards.n.01")],

	# great experience
	"U+449f":	[wn.synset("excellence.n.01"),
				wn.synset("excellency.n.01")],

	# prisoner
	"U+44a1":	[wn.synset("prisoner.n.01")],

	# request
	"U+44a3":	[wn.synset("request.v.01")],

	# switch on, turn on
	"U+44a4":	[wn.synset("ignite.v.01"),
				wn.synset("open.v.02"),
				wn.synset("switch_on.v.01")],

	# Saturday
	"U+44a5":	[wn.synset("saturday.n.01")],

	# birdfeeder, bird table table
	"U+44a6":	[wn.synset("bird_feeder.n.01")],

	# reaching aid, grabber
	"U+44ab":	[wn.synset("clasp.n.02"),
				wn.synset("grabber.n.01"),
				wn.synset("grasping.n.02"),
				wn.synset("handle.n.01")],

	# hearing aid
	"U+44ad":	[wn.synset("acoustic.n.01"),
				wn.synset("hearing_aid.n.01"),
				wn.synset("hearing_aid.n.02")],

	# spermicide
	"U+44ae":	[wn.synset("spermicide.n.01")],

	# Finnish
	"U+44b0":	[wn.synset("finnish.n.01")],

	# striped
	"U+44b3":	[wn.synset("striped.s.01")],

	# ashtray
	"U+44b4":	[wn.synset("ashtray.n.01")],

	# shot put
	"U+44b6":	[wn.synset("shot_put.n.01")],

	# binoculars, field glass glass
	"U+44b7":	[wn.synset("binoculars.n.01")],

	# water polo
	"U+44b8":	[wn.synset("water_polo.n.01")],

	# Pluto
	"U+44b9":	[wn.synset("pluto.n.03")],

	# hammock
	"U+44bb":	[wn.synset("hammock.n.02")],

	# July
	"U+44bc":	[wn.synset("july.n.01")],

	# respect, admiration
	"U+44bd":	[wn.synset("respect.n.03")],

	# cauliflower
	"U+44be":	[wn.synset("cauliflower.n.02")],

	# monarchy
	"U+44bf":	[wn.synset("monarchy.n.01")],

	# empathy
	"U+44c1":	[wn.synset("empathy.n.01")],

	# joke
	"U+44c2":	[wn.synset("joke.v.01"),
				wn.synset("joke.v.02")],

	# swallow
	"U+44c3":	[wn.synset("swallow.v.01")],

	# memory game, Kim's game, memory game,Kim's game
	"U+44c4":	[wn.synset("memory.n.01"),
				wn.synset("memory.n.02"),
				wn.synset("memory.n.03"),
				wn.synset("memory.n.04"),
				wn.synset("memory.n.05"),
				wn.synset("mind.n.02"),
				wn.synset("recall.n.04"),
				wn.synset("recollection.n.03"),
				wn.synset("remembrance.n.01")],

	# teamwork
	"U+44c5":	[wn.synset("teamwork.n.01")],

	# volunteer
	"U+44c6":	[wn.synset("volunteer.n.02")],

	# next week
	"U+44c7":	[wn.synset("margarine.n.01"),
				wn.synset("oil.n.01"),
				wn.synset("petroleum.n.01"),
				wn.synset("vegetable_oil.n.01")],

	# handwriting, penmanship
	"U+44ca":	[wn.synset("calligraphy.n.01")],

	# Haggadah
	"U+44cb":	[wn.synset("haggadah.n.01")],

	# father in law, father-in-law
	"U+44cc":	[wn.synset("father-in-law.n.01")],

	# sunburn
	"U+44d0":	[wn.synset("tan.n.01")],

	# domestic
	"U+44d3":	[wn.synset("domestic.a.01"),
				wn.synset("domestic.a.02"),
				wn.synset("domestic.a.03"),
				wn.synset("domestic.s.04"),
				wn.synset("domestic.s.05")],

	# clinic
	"U+44d4":	[wn.synset("clinic.n.01")],

	# hospital, clinic
	"U+44d5":	[wn.synset("hospital.n.01")],

	# toothbrush
	"U+44d7":	[wn.synset("toothbrush.n.01")],

	# Friday
	"U+44d8":	[wn.synset("friday.n.01")],

	# lake, pond
	"U+44d9":	[wn.synset("lake.n.01")],

	# bobsleigh
	"U+44da":	[wn.synset("bobsled.n.01"),
				wn.synset("bobsled.n.02")],

	# match
	"U+44db":	[wn.synset("match.n.01")],

	# thread, string, cord
	"U+44dd":	[wn.synset("cord.n.04"),
				wn.synset("string.n.01"),
				wn.synset("thread.n.01")],

	# enter, absorb, insert, penetrate, go through through
	"U+44de":	[wn.synset("enter.v.01")],

	# journalist
	"U+44df":	[wn.synset("journalist.n.01")],

	# chick
	"U+44e0":	[wn.synset("chick.n.01"),
				wn.synset("chicken.n.02"),
				wn.synset("dame.n.01")],

	# care centre
	"U+44e1":	[wn.synset("hospice.n.02")],

	# accessible
	"U+44e2":	[wn.synset("accessible.a.01"),
				wn.synset("accessible.s.02"),
				wn.synset("accessible.s.03"),
				wn.synset("accessible.s.04"),
				wn.synset("approachable.a.02")],

	# paddock
	"U+44e3":	[wn.synset("paddock.n.01")],

	# corpse, cadaver
	"U+44e4":	[wn.synset("cadaver.n.01")],

	# hurricane
	"U+44e6":	[wn.synset("hurricane.n.01")],

	# December
	"U+44e9":	[wn.synset("december.n.01")],

	# South America
	"U+44ea":	[wn.synset("south_america.n.01")],

	# Japan
	"U+44eb":	[wn.synset("japan.n.01")],

	# sunrise
	"U+44ec":	[wn.synset("dawn.n.01"),
				wn.synset("sunrise.n.02")],

	# tomb
	"U+44ed":	[wn.synset("grave.n.02")],

	# blood vessel
	"U+44ee":	[wn.synset("blood_vessel.n.01")],

	# hitch, tie up, fix up up,fix up
	"U+44ef":	[wn.synset("adhere.v.06"),
				wn.synset("buck.v.04"),
				wn.synset("hitch.v.01"),
				wn.synset("hitch.v.05"),
				wn.synset("hitchhike.v.01"),
				wn.synset("limp.v.01"),
				wn.synset("tie.v.01"),
				wn.synset("tie_down.v.01")],

	# condense
	"U+44f0":	[wn.synset("condense.v.01"),
				wn.synset("condense.v.03"),
				wn.synset("condense.v.04"),
				wn.synset("condense.v.05"),
				wn.synset("condense.v.06"),
				wn.synset("condense.v.07"),
				wn.synset("digest.v.07")],

	# November
	"U+44f2":	[wn.synset("november.n.01")],

	# dangerous
	"U+44f5":	[wn.synset("dangerous.a.01")],

	# minutes
	"U+44f6":	[wn.synset("hour.n.04"),
				wn.synset("minute.n.01"),
				wn.synset("minute.n.04"),
				wn.synset("minute.n.05"),
				wn.synset("minutes.n.01"),
				wn.synset("moment.n.01"),
				wn.synset("moment.n.02")],

	# skating
	"U+44f7":	[wn.synset("skating.n.01")],

	# Tevet
	"U+44f8":	[wn.synset("tebet.n.01")],

	# whisper
	"U+44f9":	[wn.synset("whisper.v.01")],

	# domino
	"U+44fa":	[wn.synset("domino.n.01"),
				wn.synset("domino.n.02"),
				wn.synset("domino.n.03"),
				wn.synset("domino.n.04"),
				wn.synset("dominoes.n.01")],

	# tabletop
	"U+44fc":	[wn.synset("tabletop.n.01")],

	# April
	"U+44ff":	[wn.synset("april.n.01")],

	# baker
	"U+4500":	[wn.synset("baker.n.01"),
				wn.synset("baker.n.02")],

	# student, pupil
	"U+4501":	[wn.synset("pupil.n.02"),
				wn.synset("scholar.n.01"),
				wn.synset("schoolchild.n.01"),
				wn.synset("student.n.01")],

	# bagpipe
	"U+4502":	[wn.synset("bagpipe.n.01")],

	# ladybird
	"U+4503":	[wn.synset("ladybug.n.01")],

	# hate, hatred
	"U+4506":	[wn.synset("hate.n.01")],

	# playground
	"U+4509":	[wn.synset("playground.n.02")],

	# dreidel top
	"U+450a":	[wn.synset("top.n.08")],

	# each, every
	"U+450b":	[wn.synset("each.s.01"),
				wn.synset("every.s.01")],

	# enjoy
	"U+450d":	[wn.synset("amuse.v.01"),
				wn.synset("amuse.v.02"),
				wn.synset("delight.v.02"),
				wn.synset("enjoy.v.01"),
				wn.synset("enjoy.v.02"),
				wn.synset("enjoy.v.04"),
				wn.synset("love.v.02")],

	# butcher shop
	"U+450f":	[wn.synset("butcher.n.01"),
				wn.synset("butcher.n.03")],

	# French fries, chips
	"U+4510":	[wn.synset("french_fries.n.01")],

	# go by airplane
	"U+4514":	[wn.synset("fly.v.01")],

	# slaughterer
	"U+4516":	[wn.synset("butcher.n.03")],

	# June
	"U+4517":	[wn.synset("june.n.01")],

	# Messiah
	"U+4518":	[wn.synset("messiah.n.01"),
				wn.synset("messiah.n.02")],

	# excellent
	"U+4519":	[wn.synset("excellent.s.01")],

	# kangaroo, marsupial, pouched mammal
	"U+451a":	[wn.synset("kangaroo.n.01")],

	# advocacy, representation
	"U+451b":	[wn.synset("advocacy.n.01"),
				wn.synset("apology.n.02"),
				wn.synset("representation.n.01"),
				wn.synset("representation.n.02"),
				wn.synset("representation.n.03"),
				wn.synset("representation.n.04"),
				wn.synset("representation.n.05"),
				wn.synset("representation.n.06"),
				wn.synset("representation.n.08"),
				wn.synset("representation.n.09"),
				wn.synset("representation.n.10"),
				wn.synset("theatrical_performance.n.01")],

	# Muhammad, Mohammed, Muhammed
	"U+451c":	[wn.synset("mohammed.n.01")],

	# tissue
	"U+451d":	[wn.synset("tissue.n.01"),
				wn.synset("tissue.n.02")],

	# Brahma
	"U+451e":	[wn.synset("brahma.n.01")],

	# woodpecker
	"U+4520":	[wn.synset("woodpecker.n.01")],

	# slalom
	"U+4521":	[wn.synset("slalom.n.01")],

	# ancestor
	"U+4524":	[wn.synset("ancestor.n.01")],

	# altar
	"U+4528":	[wn.synset("altar.n.02")],

	# prince
	"U+452c":	[wn.synset("prince.n.01")],

	# digest
	"U+452d":	[wn.synset("digest.v.01"),
				wn.synset("digest.v.02"),
				wn.synset("digest.v.03")],

	# digestion
	"U+452e":	[wn.synset("digestion.n.02")],

	# uterine contraction
	"U+452f":	[wn.synset("contraction.n.04"),
				wn.synset("cutback.n.01")],

	# writing
	"U+4530":	[wn.synset("script.n.03"),
				wn.synset("writing.n.01"),
				wn.synset("writing.n.02"),
				wn.synset("writing.n.03"),
				wn.synset("writing.n.04"),
				wn.synset("writing.n.05")],

	# croquet
	"U+4532":	[wn.synset("croquet.n.01")],

	# Spain
	"U+4533":	[wn.synset("spain.n.01")],

	# Judaism
	"U+4535":	[wn.synset("judaism.n.01"),
				wn.synset("judaism.n.02")],

	# tourist
	"U+4536":	[wn.synset("tourist.n.01")],

	# Noah
	"U+4538":	[wn.synset("noah.n.01")],

	# constipation
	"U+4539":	[wn.synset("constipation.n.01")],

	# waffle
	"U+453a":	[wn.synset("wafer.n.02"),
				wn.synset("waffle.n.01")],

	# hotel, motel
	"U+453d":	[wn.synset("hotel.n.01")],

	# eternal
	"U+453e":	[wn.synset("ageless.s.01")],

	# acrobat
	"U+453f":	[wn.synset("acrobat.n.01")],

	# cheap, inexpensive
	"U+4540":	[wn.synset("cheap.a.01")],

	# Antarctic
	"U+4541":	[wn.synset("antarctic.n.01")],

	# lovable
	"U+4542":	[wn.synset("lovable.a.01"),
				wn.synset("pleasant.a.01")],

	# mercury
	"U+4543":	[wn.synset("mercury.n.01")],

	# thermometer
	"U+4544":	[wn.synset("thermometer.n.01")],

	# table game
	"U+4546":	[wn.synset("contest.n.01"),
				wn.synset("game.n.01"),
				wn.synset("game.n.02"),
				wn.synset("pastime.n.01"),
				wn.synset("play.n.05"),
				wn.synset("play.n.08"),
				wn.synset("set.n.01"),
				wn.synset("turn.n.03"),
				wn.synset("turn.n.09")],

	# paediatrician
	"U+4547":	[wn.synset("baby_doctor.n.01")],

	# kill, murder
	"U+4548":	[wn.synset("murder.v.01")],

	# western
	"U+454b":	[wn.synset("westerly.s.01"),
				wn.synset("western.a.01"),
				wn.synset("western.a.02"),
				wn.synset("western.s.03")],

	# sanitary napkin, sanitary towel, tampon, sanitary napkin,sanitary towel,tampon
	"U+454c":	[wn.synset("tampon.n.01")],

	# tie whipping knot
	"U+454d":	[wn.synset("barrel.v.01")],

	# rag
	"U+454f":	[wn.synset("rag.n.01")],

	# handkerchief
	"U+4550":	[wn.synset("handkerchief.n.01")],

	# ram
	"U+4551":	[wn.synset("aries.n.01"),
				wn.synset("aries.n.03"),
				wn.synset("ram.n.04"),
				wn.synset("ram.n.05"),
				wn.synset("random-access_memory.n.01")],

	# rap
	"U+4552":	[wn.synset("blame.n.02"),
				wn.synset("knock.n.05"),
				wn.synset("pat.n.01"),
				wn.synset("rap.n.02"),
				wn.synset("rap.n.04"),
				wn.synset("rap.n.05")],

	# food processor, kitchen machine
	"U+4554":	[wn.synset("mixer.n.04")],

	# milkman
	"U+4556":	[wn.synset("milkman.n.01")],

	# evangelise
	"U+4557":	[wn.synset("evangelize.v.01"),
				wn.synset("evangelize.v.02")],

	# Brontosaurus
	"U+4558":	[wn.synset("apatosaur.n.01")],

	# coin
	"U+4559":	[wn.synset("coin.n.01")],

	# unforgivable, inexcusable
	"U+455a":	[wn.synset("inexcusable.a.01"),
				wn.synset("inexcusable.s.02"),
				wn.synset("unpardonable.a.01")],

	# glow
	"U+455b":	[wn.synset("freshness.n.03"),
				wn.synset("gleam.n.01"),
				wn.synset("glow.n.04"),
				wn.synset("glow.n.05"),
				wn.synset("hot_weather.n.01"),
				wn.synset("incandescence.n.01"),
				wn.synset("luminescence.n.02"),
				wn.synset("passion.n.01"),
				wn.synset("radiance.n.01"),
				wn.synset("reflection.n.02")],

	# raisins, currants
	"U+455e":	[wn.synset("raisin.n.01")],

	# inspire
	"U+455f":	[wn.synset("inspire.v.02")],

	# queen
	"U+4560":	[wn.synset("queen.n.02")],

	# aid store room
	"U+4561":	[wn.synset("deposit.n.09"),
				wn.synset("sediment.n.01"),
				wn.synset("storehouse.n.01")],

	# head louse
	"U+4563":	[wn.synset("head_louse.n.01")],

	# bus stop, bus bay
	"U+4564":	[wn.synset("bus_stop.n.01")],

	# sunglasses
	"U+4566":	[wn.synset("sunglasses.n.01")],

	# rowing
	"U+4569":	[wn.synset("rowing.n.01")],

	# erupt
	"U+456a":	[wn.synset("erupt.v.05")],

	# eruption
	"U+456b":	[wn.synset("volcanic_eruption.n.01")],

	# Jupiter
	"U+456c":	[wn.synset("jupiter.n.01")],

	# approach
	"U+456e":	[wn.synset("access.n.03"),
				wn.synset("approach.n.01"),
				wn.synset("approach.n.02"),
				wn.synset("approach.n.05"),
				wn.synset("approach.n.07"),
				wn.synset("approach.n.08"),
				wn.synset("approach.n.09"),
				wn.synset("approach_path.n.01"),
				wn.synset("overture.n.03")],

	# come, approach
	"U+456f":	[wn.synset("come.v.01"),
				wn.synset("come.v.03")],

	# weak
	"U+4570":	[wn.synset("weak.a.01")],

	# improve
	"U+4571":	[wn.synset("better.v.02")],

	# betting
	"U+4573":	[wn.synset("bet.v.01"),
				wn.synset("bet.v.02"),
				wn.synset("count.v.08"),
				wn.synset("dissipated.s.02")],

	# tallith
	"U+4574":	[wn.synset("prayer_shawl.n.01")],

	# beef
	"U+4576":	[wn.synset("beef.n.02")],

	# Sandman
	"U+4577":	[wn.synset("sandman.n.01")],

	# fairy tale
	"U+4578":	[wn.synset("saga.n.01")],

	# beet
	"U+4579":	[wn.synset("beet.n.01"),
				wn.synset("beet.n.02")],

	# bladder
	"U+457b":	[wn.synset("bladder.n.01"),
				wn.synset("bladder.n.02")],

	# glider
	"U+457d":	[wn.synset("glider.n.01")],

	# decorated cake
	"U+457e":	[wn.synset("cake.n.03")],

	# list, inventory
	"U+457f":	[wn.synset("list.n.01")],

	# shoulder blade, scapula
	"U+4580":	[wn.synset("scapula.n.01")],

	# several
	"U+4581":	[wn.synset("respective.s.01"),
				wn.synset("several.s.01"),
				wn.synset("several.s.03")],

	# moose, elk
	"U+4582":	[wn.synset("elk.n.01")],

	# cycle, ride a bike a bike
	"U+4584":	[wn.synset("bicycle.v.01")],

	# snowman
	"U+4585":	[wn.synset("snowman.n.01")],

	# Estonian
	"U+4586":	[wn.synset("estonian.n.01")],

	# laptop
	"U+4587":	[wn.synset("laptop.n.01"),
				wn.synset("notebook.n.02")],

	# Christian faith
	"U+4588":	[wn.synset("belief.n.01"),
				wn.synset("creed.n.01"),
				wn.synset("impression.n.01"),
				wn.synset("religion.n.01")],

	# elf
	"U+4589":	[wn.synset("elf.n.01")],

	# turquoise
	"U+458a":	[wn.synset("greenish_blue.n.01")],

	# bandy
	"U+458b":	[wn.synset("bandy.s.01"),
				wn.synset("bandy.v.01"),
				wn.synset("bandy.v.02"),
				wn.synset("bandy.v.03")],

	# vulture
	"U+458c":	[wn.synset("vulture.n.01")],

	# paratrooper
	"U+458d":	[wn.synset("paratrooper.n.01")],

	# celibacy, chastity, abstinence
	"U+458f":	[wn.synset("abstinence.n.02")],

	# specific
	"U+4591":	[wn.synset("specific.a.01"),
				wn.synset("specific.s.02")],

	# mosquito
	"U+4592":	[wn.synset("mosquito.n.01")],

	# escape
	"U+4594":	[wn.synset("escape.n.01"),
				wn.synset("escape.n.02"),
				wn.synset("escape.n.04"),
				wn.synset("escape.n.05"),
				wn.synset("escape.n.06"),
				wn.synset("escape.n.07"),
				wn.synset("evasion.n.03"),
				wn.synset("safety_valve.n.01")],

	# icy, frozen
	"U+4595":	[wn.synset("arctic.s.02"),
				wn.synset("frigid.s.03")],

	# backspace
	"U+4596":	[wn.synset("backspace.v.01"),
				wn.synset("erase.v.03")],

	# espionage, spying
	"U+4597":	[wn.synset("detection.n.02"),
				wn.synset("espionage.n.01"),
				wn.synset("spying.n.01"),
				wn.synset("spying.n.02")],

	# menopause
	"U+4598":	[wn.synset("menopause.n.01")],

	# chapter
	"U+459a":	[wn.synset("chapter.n.01"),
				wn.synset("chapter.n.02")],

	# curry
	"U+459b":	[wn.synset("curry.n.01")],

	# speed skating
	"U+459c":	[wn.synset("speed_skate.n.01"),
				wn.synset("speed_skating.n.01")],

	# rolling pin
	"U+459d":	[wn.synset("rolling_pin.n.01")],

	# fuselage
	"U+459e":	[wn.synset("fuselage.n.01")],

	# electorate
	"U+459f":	[wn.synset("electorate.n.01")],

	# Chumash, Pentateuch
	"U+45a1":	[wn.synset("torah.n.02")],

	# why
	"U+45a2":	[wn.synset("why.n.01")],

	# wildflower
	"U+45a3":	[wn.synset("plant.n.02"),
				wn.synset("wildflower.n.01")],

	# heal
	"U+45a4":	[wn.synset("bring_around.v.02"),
				wn.synset("mend.v.02")],

	# dollhouse, doll house house
	"U+45a6":	[wn.synset("dollhouse.n.01"),
				wn.synset("dollhouse.n.02")],

	# rich, wealthy
	"U+45a7":	[wn.synset("abundance.n.01"),
				wn.synset("affluence.n.01"),
				wn.synset("affluent.s.01"),
				wn.synset("ample.s.02"),
				wn.synset("deep.s.07"),
				wn.synset("fat.s.05"),
				wn.synset("full-bodied.s.01"),
				wn.synset("money.n.02"),
				wn.synset("profusion.n.01"),
				wn.synset("prosperity.n.01"),
				wn.synset("rich.a.01"),
				wn.synset("rich.a.02"),
				wn.synset("rich.a.07"),
				wn.synset("rich.a.08"),
				wn.synset("rich.s.03"),
				wn.synset("rich.s.06"),
				wn.synset("rich.s.09"),
				wn.synset("rich.s.11"),
				wn.synset("wealth.n.01"),
				wn.synset("wealth.n.03")],

	# amphibian
	"U+45aa":	[wn.synset("amphibian.n.03")],

	# longer
	"U+45ab":	[wn.synset("farseeing.s.02"),
				wn.synset("long.a.01"),
				wn.synset("long.a.02"),
				wn.synset("long.a.05"),
				wn.synset("long.a.06"),
				wn.synset("long.s.03"),
				wn.synset("long.s.07"),
				wn.synset("long.s.09"),
				wn.synset("retentive.a.01")],

	# navel
	"U+45ac":	[wn.synset("navel.n.01")],

	# rob
	"U+45ad":	[wn.synset("overcharge.v.01"),
				wn.synset("pilfer.v.01"),
				wn.synset("rob.v.01"),
				wn.synset("steal.v.01")],

	# long time
	"U+45af":	[wn.synset("long.r.01")],

	# sing
	"U+45b0":	[wn.synset("sing.v.02")],

	# navigational sign
	"U+45b2":	[wn.synset("beacon.n.03")],

	# tablet computer, tablet, tablet PC
	"U+45b3":	[wn.synset("pad.n.01"),
				wn.synset("pill.n.02"),
				wn.synset("tablet.n.01"),
				wn.synset("tablet.n.03")],

	# layer, level
	"U+45b4":	[wn.synset("layer.n.02")],

	# cloudy
	"U+45b5":	[wn.synset("cloudy.a.02")],

	# dried
	"U+45b6":	[wn.synset("dried.s.01"),
				wn.synset("dried.s.02")],

	# agnosticism
	"U+45b8":	[wn.synset("agnosticism.n.01")],

	# baseball
	"U+45ba":	[wn.synset("baseball.n.01")],

	# proud
	"U+45bb":	[wn.synset("proud.a.01")],

	# cinnamon
	"U+45bc":	[wn.synset("cinnamon.n.01"),
				wn.synset("cinnamon.n.02"),
				wn.synset("cinnamon.n.03")],

	# bark
	"U+45bd":	[wn.synset("bark.v.04")],

	# weight lifting
	"U+45be":	[wn.synset("weightlift.n.01")],

	# compare
	"U+45bf":	[wn.synset("compare.v.01")],

	# Aries
	"U+45c0":	[wn.synset("aries.n.01"),
				wn.synset("aries.n.02"),
				wn.synset("aries.n.03")],

	# runes
	"U+45c1":	[wn.synset("alphabet.n.01"),
				wn.synset("rune.n.01")],

	# today
	"U+45c2":	[wn.synset("today.n.01")],

	# October
	"U+45c3":	[wn.synset("october.n.01")],

	# Eve
	"U+45c4":	[wn.synset("eve.n.01")],

	# employee
	"U+45c5":	[wn.synset("employee.n.01")],

	# drown
	"U+45c6":	[wn.synset("drown.v.04")],

	# judo
	"U+45c7":	[wn.synset("judo.n.01")],

	# German
	"U+45c8":	[wn.synset("german.n.02")],

	# Germany
	"U+45c9":	[wn.synset("germany.n.01")],

	# sandstorm
	"U+45ca":	[wn.synset("dust_storm.n.01")],

	# ferry
	"U+45cb":	[wn.synset("ferry.n.01")],

	# stroke
	"U+45cd":	[wn.synset("caress.v.01"),
				wn.synset("stroke.v.01"),
				wn.synset("stroke.v.02"),
				wn.synset("stroke.v.03"),
				wn.synset("stroke.v.04")],

	# Advent
	"U+45cf":	[wn.synset("advent.n.01"),
				wn.synset("advent.n.02"),
				wn.synset("second_coming.n.01")],

	# classroom
	"U+45d0":	[wn.synset("classroom.n.01")],

	# Ceres
	"U+45d1":	[wn.synset("cere.n.01"),
				wn.synset("ceres.n.01"),
				wn.synset("ceres.n.02")],

	# disability benefit
	"U+45d2":	[wn.synset("pension.n.01")],

	# midnight
	"U+45d4":	[wn.synset("midnight.n.01")],

	# chalice
	"U+45d5":	[wn.synset("chalice.n.01")],

	# married
	"U+45d9":	[wn.synset("marital.a.01"),
				wn.synset("married.a.01")],

	# zebra
	"U+45dc":	[wn.synset("zebra.n.01")],

	# oral sex
	"U+45de":	[wn.synset("oral_sex.n.01")],

	# light year
	"U+45df":	[wn.synset("light_year.n.01")],

	# hawk, eagle
	"U+45e0":	[wn.synset("hawk.n.01")],

	# flyer
	"U+45e1":	[wn.synset("aviator.n.01"),
				wn.synset("circular.n.01"),
				wn.synset("flier.n.01")],

	# notary
	"U+45e2":	[wn.synset("notary.n.01")],

	# sceptical, skeptical, questioning
	"U+45e3":	[wn.synset("disbelieving.s.01"),
				wn.synset("doubting.s.01"),
				wn.synset("inquisitive.s.01"),
				wn.synset("questioning.s.01")],

	# fallopian tube
	"U+45e4":	[wn.synset("fallopian_tube.n.01")],

	# pelican
	"U+45e7":	[wn.synset("pelican.n.01")],

	# plastic
	"U+45e9":	[wn.synset("plastic.n.01")],

	# mustard
	"U+45eb":	[wn.synset("mustard.n.01"),
				wn.synset("mustard.n.02"),
				wn.synset("mustard.n.03"),
				wn.synset("powdered_mustard.n.01")],

	# oats
	"U+45ec":	[wn.synset("oat.n.02")],

	# Shiva
	"U+45ee":	[wn.synset("siva.n.01")],

	# ant
	"U+45ef":	[wn.synset("ant.n.01")],

	# tambourine
	"U+45f1":	[wn.synset("tambourine.n.01")],

	# kibbutz
	"U+45f2":	[wn.synset("kibbutz.n.01")],

	# multiply
	"U+45f3":	[wn.synset("multiply.v.01")],

	# librarian
	"U+45f4":	[wn.synset("librarian.n.01")],

	# bluebird
	"U+45f5":	[wn.synset("bluebird.n.02"),
				wn.synset("buffalo_clover.n.02"),
				wn.synset("fairy_bluebird.n.01")],

	# tendon
	"U+45f6":	[wn.synset("tendon.n.01")],

	# hungry
	"U+45f7":	[wn.synset("athirst.s.01"),
				wn.synset("hungry.a.01")],

	# masturbation
	"U+45f8":	[wn.synset("masturbation.n.01")],

	# perch
	"U+45fa":	[wn.synset("perch.n.06")],

	# cheat
	"U+45fb":	[wn.synset("cheat.v.02")],

	# witch
	"U+45fc":	[wn.synset("enchantress.n.02"),
				wn.synset("witch.n.02")],

	# Pegasus
	"U+45fd":	[wn.synset("pegasus.n.01")],

	# wool
	"U+45fe":	[wn.synset("wool.n.01")],

	# control tower
	"U+45ff":	[wn.synset("control_tower.n.01")],

	# neither
	"U+4600":	[wn.synset("neither.s.01")],

	# Resurrection of Christ
	"U+4601":	[wn.synset("resurrection.n.01"),
				wn.synset("resurrection.n.02")],

	# resurrection
	"U+4602":	[wn.synset("resurrection.n.02")],

	# buffalo, bison
	"U+4603":	[wn.synset("american_bison.n.01")],

	# picnic
	"U+4605":	[wn.synset("picnic.n.03")],

	# stepson
	"U+4606":	[wn.synset("stepson.n.01")],

	# voluntary
	"U+4607":	[wn.synset("voluntary.a.01"),
				wn.synset("voluntary.a.02")],

	# volunteering
	"U+4608":	[wn.synset("volunteer.v.01"),
				wn.synset("volunteer.v.02"),
				wn.synset("volunteer.v.03")],

	# amen
	"U+4609":	[wn.synset("amen.n.01")],

	# shiva
	"U+460a":	[wn.synset("siva.n.01")],

	# hiss
	"U+460c":	[wn.synset("boo.v.01"),
				wn.synset("hiss.v.01"),
				wn.synset("hiss.v.02"),
				wn.synset("hiss.v.03")],

	# when, what time time
	"U+460d":	[wn.synset("equally.r.01"),
				wn.synset("once.r.02")],

	# oil tanker
	"U+4610":	[wn.synset("oil_tanker.n.01")],

	# polo
	"U+4611":	[wn.synset("polo.n.02")],

	# brussels sprout
	"U+4612":	[wn.synset("brussels_sprout.n.01"),
				wn.synset("brussels_sprouts.n.01")],

	# pod
	"U+4613":	[wn.synset("pod.n.01")],

	# turkey
	"U+4615":	[wn.synset("turkey.n.01")],

	# ravioli
	"U+4616":	[wn.synset("ravioli.n.01")],

	# tasteless
	"U+4618":	[wn.synset("bland.s.01"),
				wn.synset("tasteless.a.01"),
				wn.synset("tasteless.a.02")],

	# careful
	"U+4619":	[wn.synset("careful.a.01")],

	# dribble
	"U+461a":	[wn.synset("drivel.v.01")],

	# robber
	"U+461b":	[wn.synset("robber.n.01"),
				wn.synset("thief.n.01")],

	# cast
	"U+461d":	[wn.synset("cast.n.05")],

	# participant
	"U+4620":	[wn.synset("participant.n.01")],

	# macaroni
	"U+4621":	[wn.synset("macaroni.n.02")],

	# driver, chauffeur
	"U+4622":	[wn.synset("driver.n.01")],

	# footprint
	"U+4623":	[wn.synset("footprint.n.01")],

	# magical
	"U+4624":	[wn.synset("charming.s.02")],

	# sinner
	"U+4625":	[wn.synset("sinner.n.01")],

	# sin
	"U+4626":	[wn.synset("sin.n.02")],

	# blow
	"U+4628":	[wn.synset("blow.v.01")],

	# blot
	"U+4629":	[wn.synset("blot.n.02"),
				wn.synset("smudge.n.02")],

	# rose
	"U+462b":	[wn.synset("rose.n.01")],

	# inflation
	"U+4630":	[wn.synset("inflation.n.01")],

	# furniture
	"U+4631":	[wn.synset("furniture.n.01")],

	# towel
	"U+4632":	[wn.synset("towel.n.01")],

	# bracelet
	"U+4633":	[wn.synset("bracelet.n.02")],

	# trolleybus
	"U+4634":	[wn.synset("trolleybus.n.01")],

	# Danish
	"U+4635":	[wn.synset("danish.n.01")],

	# poem
	"U+4638":	[wn.synset("poem.n.01")],

	# communicate
	"U+4639":	[wn.synset("communicate.v.01"),
				wn.synset("communicate.v.02"),
				wn.synset("communicate.v.04")],

	# terrified
	"U+463a":	[wn.synset("awful.s.02"),
				wn.synset("fearful.s.04"),
				wn.synset("panicky.s.01"),
				wn.synset("tragic.s.01")],

	# shrimp
	"U+463c":	[wn.synset("prawn.n.01")],

	# stand
	"U+463d":	[wn.synset("bide.v.01"),
				wn.synset("digest.v.03"),
				wn.synset("persist.v.03"),
				wn.synset("resist.v.04"),
				wn.synset("stand.v.01"),
				wn.synset("stand.v.02"),
				wn.synset("stand.v.03"),
				wn.synset("stand.v.04"),
				wn.synset("stand.v.06"),
				wn.synset("stand.v.07"),
				wn.synset("stand.v.08"),
				wn.synset("stand.v.09"),
				wn.synset("stand.v.10"),
				wn.synset("stand.v.12"),
				wn.synset("stay.v.02"),
				wn.synset("stay.v.04"),
				wn.synset("stay.v.05"),
				wn.synset("stick.v.05"),
				wn.synset("wait.v.01")],

	# ox
	"U+463e":	[wn.synset("ox.n.01")],

	# chive
	"U+463f":	[wn.synset("chives.n.01")],

	# syringe
	"U+4640":	[wn.synset("syringe.n.01")],

	# fishing
	"U+4641":	[wn.synset("fishing.n.01")],

	# sacrament of confirmation
	"U+4642":	[wn.synset("confirmation.n.05")],

	# promote
	"U+4643":	[wn.synset("promote.v.01")],

	# tiptoe
	"U+4644":	[wn.synset("tiptoe.v.01")],

	# bishop
	"U+4647":	[wn.synset("bishop.n.01")],

	# biochemistry
	"U+4648":	[wn.synset("biochemistry.n.01")],

	# signature stamp
	"U+4649":	[wn.synset("autograph.n.01"),
				wn.synset("autograph.n.02"),
				wn.synset("buffer.n.01"),
				wn.synset("key_signature.n.01"),
				wn.synset("navy_seal.n.01"),
				wn.synset("polarity.n.02"),
				wn.synset("seal.n.02"),
				wn.synset("signature.n.01"),
				wn.synset("signature.n.03"),
				wn.synset("signature.n.05"),
				wn.synset("stamp.n.02"),
				wn.synset("stamp.n.03"),
				wn.synset("tampon.n.01"),
				wn.synset("touch.n.04")],

	# classmate
	"U+464a":	[wn.synset("schoolmate.n.01")],

	# lipstick
	"U+464c":	[wn.synset("lipstick.n.01")],

	# mother in law, mother-in-law
	"U+464e":	[wn.synset("mother-in-law.n.01")],

	# follow
	"U+4651":	[wn.synset("follow.v.01")],

	# pasta wheel
	"U+4652":	[wn.synset("pasta.n.02"),
				wn.synset("pastry.n.01")],

	# dairy
	"U+4653":	[wn.synset("dairy.n.01")],

	# painter
	"U+4654":	[wn.synset("painter.n.01")],

	# fax
	"U+4655":	[wn.synset("facsimile.n.02")],

	# chameleon
	"U+4656":	[wn.synset("chameleon.n.03")],

	# psychologist
	"U+4659":	[wn.synset("psychologist.n.01")],

	# awful
	"U+465a":	[wn.synset("amazing.s.02"),
				wn.synset("atrocious.s.02"),
				wn.synset("awed.s.01"),
				wn.synset("awful.s.02"),
				wn.synset("frightful.s.02"),
				wn.synset("nasty.a.01")],

	# saxophone
	"U+465b":	[wn.synset("sax.n.02")],

	# tea
	"U+465c":	[wn.synset("tea.n.01")],

	# imported
	"U+465d":	[wn.synset("imported.s.01")],

	# christian
	"U+465f":	[wn.synset("christian.a.01")],

	# summer day camp
	"U+4660":	[wn.synset("camp.n.08")],

	# behaviour
	"U+4661":	[wn.synset("behavior.n.01"),
				wn.synset("behavior.n.02"),
				wn.synset("demeanor.n.01")],

	# tragedy
	"U+4662":	[wn.synset("tragedy.n.02")],

	# milkshake
	"U+4663":	[wn.synset("milkshake.n.01")],

	# bus lane
	"U+4664":	[wn.synset("bus_lane.n.01")],

	# plant louse, plant-louse
	"U+4669":	[wn.synset("ant_cow.n.01"),
				wn.synset("aphid.n.01"),
				wn.synset("greenfly.n.01"),
				wn.synset("pale_chrysanthemum_aphid.n.01"),
				wn.synset("plant_louse.n.01")],

	# flax
	"U+466a":	[wn.synset("flax.n.01"),
				wn.synset("flax.n.02"),
				wn.synset("linen.n.01")],

	# short time home
	"U+466b":	[wn.synset("dwelling.n.01"),
				wn.synset("living_quarters.n.01"),
				wn.synset("tenement.n.01")],

	# embarrassing
	"U+466d":	[wn.synset("awkward.s.05")],

	# religious service
	"U+466e":	[wn.synset("service.n.03")],

	# solar system
	"U+466f":	[wn.synset("solar_system.n.01")],

	# stone material
	"U+4670":	[wn.synset("rock.n.01")],

	# goat
	"U+4671":	[wn.synset("goat.n.01")],

	# sandwich
	"U+4672":	[wn.synset("sandwich.n.01")],

	# repair room
	"U+4674":	[wn.synset("workshop.n.02")],

	# March
	"U+4675":	[wn.synset("march.n.01")],

	# pray
	"U+4676":	[wn.synset("pray.v.01")],

	# power plant, power station
	"U+4677":	[wn.synset("power_station.n.01")],

	# hunter
	"U+4678":	[wn.synset("hunter.n.01")],

	# adventurous
	"U+4679":	[wn.synset("adventurous.a.01")],

	# mathematician
	"U+467a":	[wn.synset("mathematician.n.01")],

	# athletics
	"U+467b":	[wn.synset("athletic_contest.n.01")],

	# Vishnu
	"U+467c":	[wn.synset("vishnu.n.01")],

	# hill
	"U+467d":	[wn.synset("hill.n.01")],

	# cookie, biscuit
	"U+467e":	[wn.synset("cookie.n.03")],

	# Iyar
	"U+467f":	[wn.synset("iyar.n.01")],

	# snowboarding
	"U+4682":	[wn.synset("snowboarding.n.01")],

	# feed
	"U+4683":	[wn.synset("feed.v.02")],

	# lunch box
	"U+4684":	[wn.synset("bagpipe.n.01"),
				wn.synset("musette.n.01")],

	# speedometer
	"U+4685":	[wn.synset("speedometer.n.01")],

	# pensioner
	"U+4686":	[wn.synset("pensioner.n.01")],

	# exploded
	"U+4687":	[wn.synset("exploded.s.01")],

	# surfboard
	"U+4689":	[wn.synset("surfboard.n.01")],

	# king
	"U+468a":	[wn.synset("king.n.01"),
				wn.synset("king.n.10")],

	# architect
	"U+468b":	[wn.synset("architect.n.01")],

	# sister in law, sister-in-law
	"U+468e":	[wn.synset("sister-in-law.n.01")],

	# banjo
	"U+4692":	[wn.synset("banjo.n.01")],

	# react
	"U+4693":	[wn.synset("react.v.01"),
				wn.synset("react.v.02"),
				wn.synset("react.v.03")],

	# daughter in law, daughter-in-law
	"U+4694":	[wn.synset("daughter-in-law.n.01")],

	# constitution
	"U+4695":	[wn.synset("fundamental_law.n.01")],

	# make believe man, make-believe man
	"U+4696":	[wn.synset("imaginary_being.n.01")],

	# shepherd
	"U+4697":	[wn.synset("shepherd.n.01")],

	# hit
	"U+4698":	[wn.synset("attack.n.01"),
				wn.synset("blow.n.01"),
				wn.synset("calamity.n.01"),
				wn.synset("hit.v.01"),
				wn.synset("hit.v.02"),
				wn.synset("hit.v.03"),
				wn.synset("hit.v.05"),
				wn.synset("hit.v.09"),
				wn.synset("hit.v.12"),
				wn.synset("hit.v.15"),
				wn.synset("hit.v.16"),
				wn.synset("hit.v.17"),
				wn.synset("murder.v.01"),
				wn.synset("reach.v.01"),
				wn.synset("reach.v.02"),
				wn.synset("score.v.01"),
				wn.synset("shoot.v.01"),
				wn.synset("strike.v.04"),
				wn.synset("strike.v.10"),
				wn.synset("stroke.n.01"),
				wn.synset("stumble.v.03"),
				wn.synset("tusk.n.02")],

	# whistle
	"U+4699":	[wn.synset("whistle.v.05")],

	# longest
	"U+469a":	[wn.synset("farseeing.s.02"),
				wn.synset("long.a.01"),
				wn.synset("long.a.02"),
				wn.synset("long.a.05"),
				wn.synset("long.a.06"),
				wn.synset("long.s.03"),
				wn.synset("long.s.07"),
				wn.synset("long.s.09"),
				wn.synset("retentive.a.01")],

	# foster parent
	"U+469b":	[wn.synset("caregiver.n.02"),
				wn.synset("probation_officer.n.01")],

	# snowstorm
	"U+469d":	[wn.synset("blizzard.n.01")],

	# vulva
	"U+469e":	[wn.synset("vulva.n.01")],

	# farrier
	"U+469f":	[wn.synset("farrier.n.01")],

	# equilateral triangle
	"U+46a0":	[wn.synset("triangle.n.01")],

	# corruption
	"U+46a1":	[wn.synset("bribery.n.01"),
				wn.synset("corruption.n.03"),
				wn.synset("corruption.n.04"),
				wn.synset("corruption.n.05"),
				wn.synset("corruption.n.06"),
				wn.synset("corruptness.n.02"),
				wn.synset("putrescence.n.01")],

	# religious fanatic
	"U+46a2":	[wn.synset("fanatic.n.01")],

	# sole
	"U+46a4":	[wn.synset("sole.n.01"),
				wn.synset("sole.n.02"),
				wn.synset("sole.n.03"),
				wn.synset("sole.n.04")],

	# fire extinguisher
	"U+46a5":	[wn.synset("fire_extinguisher.n.01")],

	# ampullae
	"U+46a6":	[wn.synset("ampulla.n.01"),
				wn.synset("ampulla.n.02")],

	# prescription
	"U+46a7":	[wn.synset("prescription.n.01"),
				wn.synset("prescription.n.03"),
				wn.synset("prescription.n.04"),
				wn.synset("prescription_drug.n.01")],

	# interrogate
	"U+46a8":	[wn.synset("interrogate.v.02")],

	# Superman
	"U+46a9":	[wn.synset("acid.n.02"),
				wn.synset("demigod.n.01"),
				wn.synset("hero.n.01"),
				wn.synset("hero.n.02")],

	# strategy
	"U+46ae":	[wn.synset("scheme.n.01"),
				wn.synset("strategy.n.02"),
				wn.synset("tactic.n.01")],

	# demand
	"U+46b0":	[wn.synset("demand.v.01")],

	# price rise
	"U+46b2":	[wn.synset("inflation.n.01"),
				wn.synset("inflation.n.02")],

	# Italy
	"U+46b3":	[wn.synset("italy.n.01")],

	# rib
	"U+46b4":	[wn.synset("rib.n.02")],

	# biochemist
	"U+46b5":	[wn.synset("biochemist.n.01")],

	# birch
	"U+46b6":	[wn.synset("birch.n.01"),
				wn.synset("birch.n.02"),
				wn.synset("birch.n.03")],

	# contact sports
	"U+46b7":	[wn.synset("martial_art.n.01")],

	# lower
	"U+46b8":	[wn.synset("lower.v.01"),
				wn.synset("lower.v.04"),
				wn.synset("turn_down.v.05")],

	# horse racing
	"U+46b9":	[wn.synset("horse_racing.n.01")],

	# homeward
	"U+46ba":	[wn.synset("homeward.s.01")],

	# margarine
	"U+46bb":	[wn.synset("margarine.n.01")],

	# rocking chair
	"U+46bd":	[wn.synset("rocking_chair.n.01"),
				wn.synset("shoofly.n.01"),
				wn.synset("shoofly.n.02")],

	# nipple
	"U+46bf":	[wn.synset("nipple.n.01")],

	# piglet
	"U+46c0":	[wn.synset("piglet.n.01")],

	# vacuum cleaner
	"U+46c2":	[wn.synset("vacuum.n.04")],

	# porridge
	"U+46c3":	[wn.synset("porridge.n.01")],

	# zombie
	"U+46c4":	[wn.synset("automaton.n.01"),
				wn.synset("zombi.n.01"),
				wn.synset("zombie.n.05")],

	# altimeter
	"U+46c5":	[wn.synset("altimeter.n.01")],

	# tefillin
	"U+46c6":	[wn.synset("phylactery.n.01")],

	# hair spray
	"U+46c8":	[wn.synset("enamel.n.04"),
				wn.synset("hair_spray.n.01"),
				wn.synset("lac.n.01"),
				wn.synset("lacquer.n.01"),
				wn.synset("lake.n.01"),
				wn.synset("varnish.n.01")],

	# canal
	"U+46cb":	[wn.synset("duct.n.01")],

	# Belarus
	"U+46cd":	[wn.synset("belarus.n.01")],

	# wave length
	"U+46ce":	[wn.synset("wavelength.n.01")],

	# hydropower, hydro energy energy
	"U+46d0":	[wn.synset("waterpower.n.01")],

	# sled sport
	"U+46d2":	[wn.synset("sledding.n.01"),
				wn.synset("toboggan.n.01")],

	# crane
	"U+46d3":	[wn.synset("crane.n.04")],

	# penguin
	"U+46d4":	[wn.synset("penguin.n.01")],

	# forefather
	"U+46d5":	[wn.synset("ancestor.n.01"),
				wn.synset("forefather.n.01"),
				wn.synset("forefather.n.02")],

	# apricot
	"U+46d6":	[wn.synset("apricot.n.01"),
				wn.synset("apricot.n.02"),
				wn.synset("yellowish_pink.n.01")],

	# summer house, summerhouse
	"U+46d7":	[wn.synset("gazebo.n.01")],

	# sometimes
	"U+46d8":	[wn.synset("sometimes.r.01")],

	# Father's Day
	"U+46d9":	[wn.synset("father's_day.n.01")],

	# Earth, Tellus
	"U+46da":	[wn.synset("earth.n.01"),
				wn.synset("earth.n.04")],

	# rainbow
	"U+46db":	[wn.synset("rainbow.n.01")],

	# rainy
	"U+46dc":	[wn.synset("showery.s.01")],

	# fertilized
	"U+46df":	[wn.synset("fertilize.v.01"),
				wn.synset("fertilize.v.02"),
				wn.synset("inseminate.v.02")],

	# weigh
	"U+46e0":	[wn.synset("weigh.v.01"),
				wn.synset("weigh.v.03")],

	# once
	"U+46e3":	[wn.synset("once.r.01"),
				wn.synset("once.r.02"),
				wn.synset("once.r.03"),
				wn.synset("time.n.01")],

	# Libra
	"U+46e4":	[wn.synset("libra.n.03")],

	# philosopher
	"U+46e5":	[wn.synset("philosopher.n.01")],

	# discordant
	"U+46e6":	[wn.synset("discordant.a.01"),
				wn.synset("discordant.s.02")],

	# include
	"U+46e8":	[wn.synset("include.v.01")],

	# confirmation
	"U+46eb":	[wn.synset("confirmation.n.05")],

	# ladle
	"U+46ec":	[wn.synset("ladle.n.01")],

	# along with
	"U+46ed":	[wn.synset("bunch.n.01"),
				wn.synset("ensemble.n.05"),
				wn.synset("set.n.02"),
				wn.synset("whole.n.01"),
				wn.synset("whole.n.02")],

	# cardiovascular system
	"U+46ee":	[wn.synset("circulatory_system.n.01")],

	# wrestling
	"U+46ef":	[wn.synset("stock.n.02"),
				wn.synset("wrestle.n.01"),
				wn.synset("wrestling.n.02")],

	# meatball
	"U+46f1":	[wn.synset("meatball.n.01")],

	# scales
	"U+46f3":	[wn.synset("scale.n.07")],

	# respirator
	"U+46f5":	[wn.synset("respirator.n.01")],

	# redo
	"U+46f6":	[wn.synset("remake.v.01")],

	# fee
	"U+46f8":	[wn.synset("fee.n.01"),
				wn.synset("fee.n.02")],

	# otolaryngologist
	"U+46f9":	[wn.synset("ent_man.n.01")],

	# musician
	"U+46fb":	[wn.synset("musician.n.01"),
				wn.synset("musician.n.02")],

	# mechanical engineer
	"U+46fc":	[wn.synset("mechanical_engineer.n.01")],

	# rape
	"U+46fd":	[wn.synset("rape.n.01"),
				wn.synset("rape.n.02"),
				wn.synset("rape.n.03")],

	# sit
	"U+46fe":	[wn.synset("seat.v.01"),
				wn.synset("sit.v.01"),
				wn.synset("sit_down.v.01")],

	# goldsmith
	"U+4700":	[wn.synset("goldsmith.n.01"),
				wn.synset("goldsmith.n.02")],

	# long jump
	"U+4701":	[wn.synset("broad_jump.n.02"),
				wn.synset("long_jump.n.01")],

	# hurdles
	"U+4702":	[wn.synset("hurdles.n.01")],

	# daycare
	"U+4703":	[wn.synset("daycare.n.01")],

	# son in law, son-in-law
	"U+4704":	[wn.synset("son-in-law.n.01")],

	# necklace
	"U+4705":	[wn.synset("necklace.n.01")],

	# inlet
	"U+4706":	[wn.synset("inlet.n.01")],

	# swimming pool
	"U+4707":	[wn.synset("swimming_pool.n.01")],

	# eastward
	"U+4708":	[wn.synset("eastbound.s.01")],

	# Adar
	"U+470a":	[wn.synset("adar.n.01")],

	# Adam
	"U+470b":	[wn.synset("adam.n.01")],

	# fingerprint
	"U+470c":	[wn.synset("fingermark.n.01"),
				wn.synset("fingerprint.n.01"),
				wn.synset("fingerprint.n.02")],

	# flea
	"U+470d":	[wn.synset("flea.n.01")],

	# piggery
	"U+470e":	[wn.synset("piggery.n.01")],

	# tram
	"U+470f":	[wn.synset("streetcar.n.01")],

	# trap
	"U+4711":	[wn.synset("trap.n.01")],

	# schoolbag
	"U+4712":	[wn.synset("schoolbag.n.01")],

	# parasailing
	"U+4714":	[wn.synset("parasailing.n.01")],

	# scrambled eggs
	"U+4715":	[wn.synset("scrambled_eggs.n.01")],

	# utensil
	"U+4716":	[wn.synset("tool.n.01"),
				wn.synset("utensil.n.01")],

	# Neptune
	"U+4718":	[wn.synset("neptune.n.01"),
				wn.synset("neptune.n.02")],

	# tanker
	"U+471b":	[wn.synset("oil_tanker.n.01")],

	# zoologist
	"U+471c":	[wn.synset("zoologist.n.01")],

	# zoology
	"U+471d":	[wn.synset("zoology.n.02")],

	# sew
	"U+471e":	[wn.synset("sew.v.01"),
				wn.synset("sew.v.02")],

	# galley
	"U+4720":	[wn.synset("galley.n.04")],

	# act in favour of
	"U+4721":	[wn.synset("represent.v.04")],

	# boil
	"U+4722":	[wn.synset("boil.v.01"),
				wn.synset("boil.v.02"),
				wn.synset("boil.v.03"),
				wn.synset("churn.v.02"),
				wn.synset("seethe.v.02")],

	# goblin
	"U+4723":	[wn.synset("goblin.n.01")],

	# apartment block
	"U+4726":	[wn.synset("apartment.n.01"),
				wn.synset("suite.n.02")],

	# sculpture
	"U+4727":	[wn.synset("sculpture.n.01"),
				wn.synset("sculpture.n.02")],

	# electric pan
	"U+4729":	[wn.synset("saucepan.n.01")],

	# westward
	"U+472a":	[wn.synset("westbound.s.01")],

	# bagel
	"U+472b":	[wn.synset("bagel.n.01")],

	# pharmacist
	"U+472c":	[wn.synset("pharmacist.n.01")],

	# Abraham
	"U+472d":	[wn.synset("abraham.n.01")],

	# seaweed
	"U+472f":	[wn.synset("seaweed.n.01")],

	# sled dog
	"U+4731":	[wn.synset("sled_dog.n.01")],

	# buzzer
	"U+4732":	[wn.synset("doorbell.n.01")],

	# spending spree
	"U+4733":	[wn.synset("thriftlessness.n.01")],

	# sewing machine
	"U+4735":	[wn.synset("sewing_machine.n.01")],

	# kitchen tongs
	"U+4736":	[wn.synset("forceps.n.01"),
				wn.synset("hook.n.04"),
				wn.synset("lion-jaw_forceps.n.01"),
				wn.synset("mouse-tooth_forceps.n.01"),
				wn.synset("pliers.n.01"),
				wn.synset("pump-type_pliers.n.01"),
				wn.synset("rib_joint_pliers.n.01"),
				wn.synset("tongs.n.01")],

	# sheltered workshop
	"U+4738":	[wn.synset("sheltered_workshop.n.01")],

	# closed
	"U+4739":	[wn.synset("closed.a.01"),
				wn.synset("closed.a.04"),
				wn.synset("shut.a.01")],

	# frustrated
	"U+473a":	[wn.synset("defeated.s.02")],

	# dish rack
	"U+473b":	[wn.synset("drainboard.n.01")],

	# lifeboat
	"U+473c":	[wn.synset("lifeboat.n.01")],

	# puberty
	"U+473f":	[wn.synset("puberty.n.01")],

	# farmer
	"U+4740":	[wn.synset("farmer.n.01")],

	# cowshed
	"U+4741":	[wn.synset("cowbarn.n.01")],

	# buddhist
	"U+4742":	[wn.synset("buddhist.n.01")],

	# member
	"U+4743":	[wn.synset("member.n.01")],

	# low water
	"U+4745":	[wn.synset("neap_tide.n.01")],

	# hamentasch
	"U+4746":	[wn.synset("hammer.n.02"),
				wn.synset("malleus.n.01")],

	# whale
	"U+4747":	[wn.synset("whale.n.02")],

	# collar
	"U+4748":	[wn.synset("collar.n.06")],

	# splint
	"U+4749":	[wn.synset("splint.n.01"),
				wn.synset("splint.n.02")],

	# biologist
	"U+474c":	[wn.synset("biologist.n.01")],

	# drunk
	"U+474d":	[wn.synset("intoxicated.a.01")],

	# myth
	"U+474f":	[wn.synset("myth.n.01")],

	# know
	"U+4750":	[wn.synset("know.v.01"),
				wn.synset("know.v.02"),
				wn.synset("know.v.03")],

	# doughnut
	"U+4751":	[wn.synset("doughnut.n.02")],

	# virginity
	"U+4756":	[wn.synset("virginity.n.01")],

	# hovercraft
	"U+4759":	[wn.synset("hovercraft.n.01")],

	# food ball
	"U+475a":	[wn.synset("meat_loaf.n.01"),
				wn.synset("meatball.n.01")],

	# bugle
	"U+475b":	[wn.synset("bugle.n.01"),
				wn.synset("bugle.n.02"),
				wn.synset("bugle.n.03")],

	# wilderness
	"U+475c":	[wn.synset("wilderness.n.03")],

	# polisher
	"U+475e":	[wn.synset("buffer.n.05")],

	# Valentine's Day
	"U+4761":	[wn.synset("valentine_day.n.01")],

	# figure skating
	"U+4762":	[wn.synset("figure_skating.n.01")],

	# domestic animal
	"U+4767":	[wn.synset("animal.n.01"),
				wn.synset("animalia.n.01")],

	# boom
	"U+4768":	[wn.synset("boom.n.01"),
				wn.synset("boom.n.02"),
				wn.synset("boom.n.03"),
				wn.synset("boom.n.04"),
				wn.synset("boom.n.05")],

	# Universe
	"U+4769":	[wn.synset("universe.n.01")],

	# The Nordic countries
	"U+476a":	[wn.synset("scandinavia.n.02")],

	# flatfish
	"U+476c":	[wn.synset("flatfish.n.02")],

	# gynecologist
	"U+476d":	[wn.synset("gynecologist.n.01")],

}
'''
BLISSNET0 = {	
	# squirrel
	"U+3201":   [wn.synset("squirrel.n.01")],

	# fire
	"U+3202":   [wn.synset("fire.n.03")],

	# mango
	"U+3203":   [wn.synset("mango.n.02"),
				wn.synset("mango.n.01")],

	# cloud
	"U+3205":   [wn.synset("cloud.n.02")],

	# water, fluid, liquid
	"U+3206":   [wn.synset("water.v.01")],

	# oil, lubricant
	"U+3207":   [wn.synset("oil.n.01")],

	# steam
	"U+3209":   [wn.synset("steam.v.06"),
				 wn.synset("steam.v.01"),
				 wn.synset("steam.v.02"),
				 wn.synset("steam.v.03")],

	# rain
	"U+320a":   [wn.synset("rain.v.01")],

	# hail
	"U+320b":   [wn.synset("hail.n.01")],

	# ice
	"U+320e":   [wn.synset("ice.n.01")],

	# pool, snooker
	"U+320f":   [wn.synset("snooker.n.01"),
				wn.synset("pool.n.01")],

	# snow
	"U+3210":   [wn.synset("snow.v.01")],

	# snowflake
	"U+3211":   [wn.synset("snowflake.n.01")],

	# freeze, solidify
	"U+3212":   [wn.synset("freeze.v.08")],

	# rice
	"U+3214":   [wn.synset("rice.n.01")],

	# mud, clay
	"U+3215":   [wn.synset("mud.n.01")],

	# swamp, bog, marsh
	"U+3216":   [wn.synset("marsh.n.01"),
				wn.synset("bog.n.01"),
				wn.synset("swamp.n.01")],

	# island
	"U+3217":   [wn.synset("island.n.01")],

	# medicine, medication, medical practice
	"U+3219":   [wn.synset("medication.n.02"),
				wn.synset("medicine.n.03"),
				wn.synset("medicine.n.02"),
				wn.synset("medicine.n.01")],

	# sperm
	"U+321b":   [wn.synset("sperm.n.01")],

	# feeling, emotion, sensation
	"U+321f":   [wn.synset("emotion.n.01")],

	# comfort, console
	"U+3221":   [wn.synset("comfort.v.01")],

	# discomfort
	"U+3222":   [wn.synset("discomfort.n.01")],

	# cloth, fabric, material, textile, net
	"U+3223":   [wn.synset("fabric.n.01")],

	# number
	"U+3224":   [wn.synset("act.n.04"),
				wn.synset("number.n.08"),
				wn.synset("issue.n.02"),
				wn.synset("number.n.02")],

	# garage
	"U+3226":   [wn.synset("garage.n.01")],

	# yard
	"U+3228":   [wn.synset("yard.n.02")],

	# fence, wall
	"U+3229":   [wn.synset("fence.n.01")],

	# chimney
	"U+322a":   [wn.synset("chimney.n.01")],

	# ear, spike, capitulum
	"U+322b":   [wn.synset("capitulum.n.01"),
				wn.synset("capitulum.n.02"),
				wn.synset("capitulum.n.03"),
				wn.synset("spike_heel.n.01"),
				wn.synset("ear.n.05"),
				wn.synset("spike.n.03"),
				wn.synset("spike.n.04")],

	# sound
	"U+322c":   [wn.synset("sound.v.01")],

	# deafness
	"U+322d":   [wn.synset("deafness.n.01")],

	# continue, pass
	"U+322f":   [wn.synset("continue.v.02"),
				wn.synset("continue.v.01"),
				 wn.synset("continue.v.04"),
				 wn.synset("continue.v.05")],

	# gas
	"U+3231":   [wn.synset("gas.n.01")],

	# bubble
	"U+3232":   [wn.synset("bubble.n.01")],

	# give, offer, provide, sacrifice
	"U+3233":   [wn.synset("sacrifice.n.04"),
				wn.synset("forfeit.n.03")],

	# exchange, substitute, trade, substitution
	"U+3234":   [wn.synset("trade.v.04"),
				 wn.synset("substitute.v.01")],

	# forward
	"U+3236":   [wn.synset("forward.n.02"),
				wn.synset("forward.n.01")],

	# meet, encounter, see, look, watch, wristwatch
	"U+3237":   [wn.synset("watch.v.03"),
				wn.synset("watch.v.01")],

	# river, stream, current
	"U+3239":   [wn.synset("river.n.01")],

	# agreement, contract
	"U+323a":   [wn.synset("agreement.n.01"),
				wn.synset("agreement.n.02"),
				wn.synset("agreement.n.04")],

	# back and forth, backward and forward, to and fro
	"U+323b":   [wn.synset("back_and_forth.r.01")],

	# through
	"U+323c":   [wn.synset("through.r.05"),
				wn.synset("through.r.04"),
				wn.synset("through.r.03"),
				wn.synset("through.s.02"),
				wn.synset("through.r.01"),
				wn.synset("through.r.02")],

	# visit
	"U+323d":   [wn.synset("visit.n.02"),
				wn.synset("visit.n.01"),
				wn.synset("sojourn.n.01")],

	# understand, see
	"U+323e":   [wn.synset("understand.v.02")],

	# into
	"U+323f":   [wn.synset("inside.n.01"),
				wn.synset("inside.n.02")],

	# crush, squeeze
	"U+3240":   [wn.synset("jam.v.03")],

	# push, shove, pushing
	"U+3241":   [wn.synset("push.n.05"),
				wn.synset("push.n.01"),
				wn.synset("push.n.02")],

	# end, arrival, stop, arrive, platform
	"U+3243":   [wn.synset("end.n.03"),
				wn.synset("end.n.02"),
				wn.synset("end.n.01"),
				wn.synset("arrival.n.02"),
				wn.synset("arrival.n.01"),
				wn.synset("end.n.05"),
				wn.synset("goal.n.01"),
				wn.synset("end.n.06")],

	# race, competition, contest
	"U+3244":   [wn.synset("competition.n.03"),
				wn.synset("contest.n.01")],

	# get, acquire, receive
	"U+3247":   [wn.synset("pick_up.v.09"),
				wn.synset("receive.v.02"),
				wn.synset("receive.v.01"),
				wn.synset("get.v.25")],

	# crash
	"U+3248":   [wn.synset("crash.v.09"),
				wn.synset("crash.v.07"),
				wn.synset("crash.v.11"),
				wn.synset("crash.v.05"),
				wn.synset("crash.v.04"),
				wn.synset("crash.v.03"),
				wn.synset("crash.v.02"),
				wn.synset("crash.v.01"),
				wn.synset("crash.v.06"),
				wn.synset("crash.v.10"),
				wn.synset("crash.v.12")],

	# mirror
	"U+324b":   [wn.synset("mirror.n.01")],

	# success
	"U+324d":   [wn.synset("success.n.01")],

	# backward, back
	"U+324e":   [wn.synset("back.r.02"),
				wn.synset("back.r.04")],

	# gathering, assembly, meeting, conference, encounter
	"U+3251":   [wn.synset("meeting.n.01")],

	# explosive
	"U+3252":   [wn.synset("explosive.a.01")],

	# year
	"U+3253":   [wn.synset("year.n.01")],

	# atom
	"U+3255":   [wn.synset("atom.n.01")],

	# nucleus
	"U+3256":   [wn.synset("nucleus.n.02")],

	# rotate, circle, circulate, wind up, orbit
	"U+3257":   [wn.synset("wind.v.05"),
				wn.synset("arouse.v.07"),
				wn.synset("wind_up.v.02"),
				wn.synset("rotate.v.02"),
				wn.synset("encircle.v.01"),
				wn.synset("circulate.v.04"),
				wn.synset("circulate.v.02"),
				wn.synset("circulate.v.03"),
				wn.synset("rotate.v.04"),
				wn.synset("finish_up.v.02"),
				wn.synset("mobilize.v.04"),
				wn.synset("circle.v.02"),
				wn.synset("go_around.v.02"),
				wn.synset("turn.v.04"),
				wn.synset("circulate.v.07"),
				wn.synset("circle.v.01"),
				wn.synset("circulate.v.06"),
				wn.synset("revolve.v.01"),
				wn.synset("orb.v.01"),
				wn.synset("turn_out.v.10"),
				wn.synset("rotate.v.06"),
				wn.synset("rotate.v.03")],

	# mix, blend
	"U+3258":   [wn.synset("shuffle.v.03"),
				wn.synset("blend.v.03")],

	# jump
	"U+3259":   [wn.synset("jump.v.13"),
				wn.synset("jump.v.01")],

	# turn, play, turning
	"U+325a":   [wn.synset("turn.v.04"),
				wn.synset("turn.v.10")],

	# swing, sway, rock, swinging
	"U+325c":   [wn.synset("rock.v.01")],

	# tractor
	"U+325f":   [wn.synset("tractor.n.01"),
				wn.synset("tractor.n.02")],

	# wheel
	"U+3260":   [wn.synset("rack.n.04"),
				wn.synset("steering_wheel.n.01"),
				wn.synset("wheel.n.03"),
				wn.synset("wheel.n.01"),
				wn.synset("roulette_wheel.n.01"),
				wn.synset("wheel.n.04")],

	# balloon
	"U+3264":   [wn.synset("balloon.n.01")],

	# sun
	"U+3265":   [wn.synset("sun.n.01")],

	# north
	"U+3266":   [wn.synset("north.n.07"),
				wn.synset("north.n.06"),
				wn.synset("north.n.05"),
				wn.synset("north.n.04"),
				wn.synset("north.n.03"),
				wn.synset("north.n.01")],

	# east
	"U+3267":   [wn.synset("east.n.01")],

	# south
	"U+3268":   [wn.synset("south.n.03")],

	# west
	"U+3269":   [wn.synset("west.n.02")],

	# weather
	"U+326a":   [wn.synset("weather.n.01")],

	# change, alteration, alter
	"U+326b":   [wn.synset("change.v.01"),
				wn.synset("change.v.03"),
				wn.synset("change.v.02"),
				wn.synset("switch.v.03"),
				wn.synset("change.v.10")],

	# development
	"U+326c":   [wn.synset("growth.n.01"),
				wn.synset("development.n.04"),
				wn.synset("development.n.02"),
				wn.synset("development.n.01"),
				wn.synset("development.n.08")],

	# machine, appliance, engine, motor
	"U+326d":   [wn.synset("machine.n.01")],

	# ring
	"U+326e":   [wn.synset("ring.n.08")],

	# melon
	"U+326f":   [wn.synset("melon.n.02"),
				wn.synset("melon.n.01")],

	# light
	"U+3270":   [wn.synset("light.a.01")],

	# egg, ovum, boiled egg, fried egg, poached egg
	"U+3271":   [wn.synset("egg.n.02"),
				wn.synset("egg.n.01"),
				wn.synset("poached_egg.n.01"),
				wn.synset("testis.n.01")],

	# head
	"U+3273":   [wn.synset("head.n.01")],

	# face
	"U+3274":   [wn.synset("face.n.01")],

	# chin
	"U+3275":   [wn.synset("chin.n.01")],

	# cheek
	"U+3276":   [wn.synset("cheek.n.01")],

	# forehead
	"U+3277":   [wn.synset("brow.n.01")],

	# beard
	"U+3278":   [wn.synset("beard.n.01")],

	# pimple, blemish
	"U+3279":   [wn.synset("pimple.n.01")],

	# raccoon
	"U+327b":   [wn.synset("raccoon.n.02")],

	# bear
	"U+327c":   [wn.synset("bear.n.01")],

	# day
	"U+327d":   [wn.synset("day.n.01")],

	# life
	"U+327e":   [wn.synset("life.n.03")],

	# death
	"U+327f":   [wn.synset("death.n.02"),
				wn.synset("death.n.04")],

	# new
	"U+3280":   [wn.synset("new.a.01")],

	# pizza
	"U+3281":   [wn.synset("pizza.n.01")],

	# time
	"U+3283":   [wn.synset("time.n.05"),
				wn.synset("time.n.03")],

	# poetry
	"U+3285":   [wn.synset("poetry.n.01")],

	# metaphor
	"U+3286":   [wn.synset("metaphor.n.01")],

	# pretend, make believe
	"U+3287":   [wn.synset("dissemble.v.03"),
				wn.synset("make.v.42"),
				wn.synset("feign.v.01"),
				wn.synset("pretend.v.03"),
				wn.synset("guess.v.02"),
				wn.synset("profess.v.07")],

	# generalization
	"U+3289":   [wn.synset("abstraction.n.03")],

	# girl
	"U+328a":   [wn.synset("female_child.n.01")],

	# boy, lad
	"U+328b":   [wn.synset("male_child.n.01"),
				wn.synset("boy.n.02"),
				wn.synset("son.n.01")],

	# child, kid, youngster
	"U+328c":   [wn.synset("child.n.02"),
				wn.synset("child.n.03"),
				wn.synset("child.n.01")],

	# money, cash
	"U+328d":   [wn.synset("money.n.01"),
				wn.synset("money.n.02"),
				wn.synset("money.n.03"),
				wn.synset("cash.n.01"),
				wn.synset("cash.n.02"),
				wn.synset("cash.n.03")],

	# flower, bloom, blossom
	"U+328f":   [wn.synset("flower.n.01")],

	# stem, stalk
	"U+3290":   [wn.synset("stalk.n.02")],

	# garden
	"U+3291":   [wn.synset("garden.n.01"),
				wn.synset("garden.n.03")],

	# plant
	"U+3294":   [wn.synset("plant.n.02")],

	# park
	"U+3295":   [wn.synset("park.n.02")],

	# tennis, racket sport, racquet sport
	"U+3296":   [wn.synset("tennis.n.01")],

	# mouth, open mouth, gape
	"U+3297":   [wn.synset("mouth.n.05"),
				wn.synset("mouth.n.04"),
				wn.synset("mouth.n.03"),
				wn.synset("mouth.n.02"),
				wn.synset("mouth.n.01"),
				wn.synset("mouth.n.08"),
				wn.synset("mouthpiece.n.03"),
				wn.synset("gape.n.01"),
				wn.synset("gape.n.02"),
				wn.synset("sass.n.01")],

	# currants
	"U+3299":   [wn.synset("currant.n.03"),
				wn.synset("currant.n.02"),
				wn.synset("currant.n.01")],

	# spider
	"U+329a":   [wn.synset("spider.n.01")],

	# eye
	"U+329b":   [wn.synset("eye.n.01")],

	# eyelid
	"U+329c":   [wn.synset("eyelid.n.01")],

	# colour
	"U+329d":   [wn.synset("color.n.01")],

	# news
	"U+329e":   [wn.synset("news.n.01"),
				wn.synset("news.n.02"),
				wn.synset("news.n.04"),
				wn.synset("news_program.n.01"),
				wn.synset("newsworthiness.n.01")],

	# blind
	"U+32a0":   [wn.synset("blind.a.01")],

	# taste, gustation, sense of taste
	"U+32a1":   [wn.synset("preference.n.01"),
				wn.synset("taste.n.06")],

	# food
	"U+32a2":   [wn.synset("food.n.01")],

	# spread, paste
	"U+32a3":   [wn.synset("spread.v.10")],

	# be, am, are, is, exist
	"U+32a4":   [wn.synset("constitute.v.01"),
				wn.synset("equal.v.01"),
				wn.synset("be.v.01"),
				wn.synset("be.v.02"),
				wn.synset("be.v.03"),
				wn.synset("be.v.11"),
				wn.synset("exist.v.01")],

	# event, happening, occasion
	"U+32a5":   [wn.synset("event.n.01")],

	# nonspeaking
	"U+32a6":   [wn.synset("nonspeaking.a.01")],

	# name, label, term, title
	"U+32a7":   [wn.synset("name.n.01")],

	# language
	"U+32a8":   [wn.synset("language.n.05"),
				wn.synset("terminology.n.01"),
				wn.synset("linguistic_process.n.02"),
				wn.synset("speech.n.02"),
				wn.synset("lyric.n.01"),
				wn.synset("language.n.01")],

	# combination, connection
	"U+32a9":   [wn.synset("connection.n.04"),
				wn.synset("connection.n.07"),
				wn.synset("connection.n.06"),
				wn.synset("connection.n.01"),
				wn.synset("connection.n.03"),
				wn.synset("connection.n.02"),
				wn.synset("combination.n.01"),
				wn.synset("combination.n.03"),
				wn.synset("combination.n.02"),
				wn.synset("combination.n.05"),
				wn.synset("combination.n.04"),
				wn.synset("combination.n.07"),
				wn.synset("combination.n.06"),
				wn.synset("joining.n.01"),
				wn.synset("association.n.04"),
				wn.synset("connection.n.08")],

	# spit
	"U+32aa":   [wn.synset("spit.v.01")],

	# kiss
	"U+32ab":   [wn.synset("kiss.n.01")],

	# grapes
	"U+32ac":   [wn.synset("grape.n.01")],

	# bow, fore, arc
	"U+32ad":   [wn.synset("bow.n.04")],

	# berry
	"U+32ae":   [wn.synset("berry.n.01"),
				wn.synset("berry.n.02"),
				wn.synset("berry.n.03")],

	# strawberry
	"U+32af":   [wn.synset("strawberry.n.01"),
				wn.synset("strawberry.n.02"),
				wn.synset("strawberry.n.03")],

	# ball
	"U+32b2":   [wn.synset("ball.n.03"),
				wn.synset("ball.n.01"),
				wn.synset("testis.n.01")],

	# earphones, headphones
	"U+32b4":   [wn.synset("earphone.n.01"),
				wn.synset("headset.n.01")],

	# fruit
	"U+32b5":   [wn.synset("fruit.n.01")],

	# plum, drupe
	"U+32b7":   [wn.synset("plum.n.02")],

	# cherries
	"U+32b8":   [wn.synset("cherry.n.03")],

	# smoking
	"U+32ba":   [wn.synset("smoke.n.07"),
				wn.synset("smoke.n.02")],

	# cigarette
	"U+32bb":   [wn.synset("cigarette.n.01")],

	# pipe, smoking pipe, hose, tube
	"U+32bc":   [wn.synset("hose.n.02"),
				wn.synset("hose.n.03"),
				wn.synset("organ_pipe.n.01"),
				wn.synset("tube.n.02"),
				wn.synset("tube.n.01"),
				wn.synset("metro.n.01"),
				wn.synset("hosiery.n.01"),
				wn.synset("pipe.n.04"),
				wn.synset("pipe.n.03"),
				wn.synset("pipe.n.02"),
				wn.synset("pipe.n.01"),
				wn.synset("tube.n.04")],

	# baby girl
	"U+32bd":   [wn.synset("baby.n.01")],

	# baby boy
	"U+32be":   [wn.synset("baby.n.01")],

	# scissors
	"U+32bf":   [wn.synset("scissors.n.01")],

	# musical note
	"U+32c0":   [wn.synset("note.n.03")],

	# baby, infant
	"U+32c1":   [wn.synset("baby.n.01")],

	# raspberry, blackberry, compound berry
	"U+32c4":   [wn.synset("raspberry.n.02"),
				wn.synset("raspberry.n.01"),
				wn.synset("blackberry.n.01")],

	# conscience
	"U+32c6":   [wn.synset("conscience.n.01")],

	# forgive, pardon, what did you say
	"U+32c7":   [wn.synset("forgiveness.n.02"),
				wn.synset("amnesty.n.03"),
				wn.synset("excuse.v.02")],

	# moral, good, right
	"U+32c8":   [wn.synset("correct.s.02"),
				wn.synset("good.a.03"),
				wn.synset("good.a.01"),
				wn.synset("full.s.06"),
				wn.synset("estimable.s.02"),
				wn.synset("right.a.05"),
				wn.synset("right.a.04"),
				wn.synset("correct.a.01")],

	# immoral, bad, wrong
	"U+32c9":   [wn.synset("base.s.04"),
				wn.synset("wrong.a.02"),
				wn.synset("immoral.a.01")],

	# mind, intellect, reason
	"U+32ca":   [wn.synset("mind.n.01"),
				wn.synset("mind.n.07")],

	# wish, desire
	"U+32cb":   [wn.synset("wish.n.01"),
				wn.synset("desire.n.03"),
				wn.synset("desire.n.01")],

	# decision
	"U+32cd":   [wn.synset("decision.n.02")],

	# idea, thought
	"U+32ce":   [wn.synset("idea.n.01")],

	# opinion
	"U+32cf":   [wn.synset("opinion.n.01")],

	# observe
	"U+32d0":   [wn.synset("note.v.03"),
				wn.synset("watch.v.02")],

	# nonsense
	"U+32d1":   [wn.synset("nonsense.n.01")],

	# state of mind
	"U+32d2":   [wn.synset("state_of_mind.n.01"),
				wn.synset("cognitive_state.n.01")],

	# fact
	"U+32d3":   [wn.synset("fact.n.04"),
				wn.synset("fact.n.01"),
				wn.synset("fact.n.03"),
				wn.synset("fact.n.02")],

	# meaning, sense, significance
	"U+32d4":   [wn.synset("meaning.n.02")],

	# use
	"U+32d5":   [wn.synset("practice.v.04"),
				wn.synset("use.v.04"),
				wn.synset("use.v.06"),
				wn.synset("use.v.01"),
				wn.synset("use.v.03"),
				wn.synset("use.v.02")],

	# knowledge, class
	"U+32d6":   [wn.synset("cognition.n.01")],

	# forget
	"U+32d7":   [wn.synset("forget.v.02")],

	# kind, kindly
	"U+32d9":   [wn.synset("kind.a.01"),
				wn.synset("kind.s.03"),
				wn.synset("charitable.s.03"),
				wn.synset("kindly.s.02")],

	# fan
	"U+32da":   [wn.synset("ventilator.n.01")],

	# good, well, fine, ok, okay, all right
	"U+32db":   [wn.synset("fine.n.01")],

	# science, body of learning
	"U+32dc":   [wn.synset("science.n.01"),
				 wn.synset("discipline.n.1")],

	# truth
	"U+32dd":   [wn.synset("truth.n.01"),
				wn.synset("truth.n.03")],

	# mathematics, arithmetic, math
	"U+32de":   [wn.synset("mathematics.n.01")],

	# beetle
	"U+32df":   [wn.synset("beetle.n.01")],

	# bad, wrong
	"U+32e1":   [wn.synset("bad.s.07")],

	# judge
	"U+32e2":   [wn.synset("judge.n.01")],

	# selfishness, egoism
	"U+32e3":   [wn.synset("egoism.n.01"),
				wn.synset("egoism.n.02"),
				wn.synset("selfishness.n.01")],

	# consideration, thoughtfulness
	"U+32e4":   [wn.synset("consideration.n.04"),
				wn.synset("consideration.n.06"),
				wn.synset("thoughtfulness.n.03")],

	# doubt, uncertainty
	"U+32e5":   [wn.synset("doubt.n.02")],

	# interest
	"U+32e6":   [wn.synset("interest.n.05"),
				wn.synset("interest.n.04"),
				wn.synset("interest.n.06"),
				wn.synset("interest.n.01"),
				wn.synset("sake.n.01"),
				wn.synset("interest.n.03"),
				wn.synset("pastime.n.01")],

	# importance, significance
	"U+32e7":   [wn.synset("importance.n.02"),
				wn.synset("importance.n.01"),
				wn.synset("meaning.n.01"),
				wn.synset("significance.n.02"),
				wn.synset("significance.n.01")],

	# calculate
	"U+32e8":   [wn.synset("calculate.v.01")],

	# lead, direct, guide
	"U+32e9":   [wn.synset("lead.n.05"),
				wn.synset("lead.n.04"),
				wn.synset("lead.n.07"),
				wn.synset("lead.n.06"),
				wn.synset("lead.n.01"),
				wn.synset("lead.n.03"),
				wn.synset("lead.n.02"),
				wn.synset("lead.n.09"),
				wn.synset("lead.n.14"),
				wn.synset("leash.n.01"),
				wn.synset("lead.n.17"),
				wn.synset("lead.n.15"),
				wn.synset("star.n.04"),
				wn.synset("spark_advance.n.01"),
				wn.synset("lead.n.11"),
				wn.synset("jumper_cable.n.01"),
				wn.synset("tip.n.03")],

	# swan
	"U+32eb":   [wn.synset("swan.n.01")],

	# fish
	"U+32ec":   [wn.synset("fish.n.02")],

	# morning
	"U+32ed":   [wn.synset("morning.n.01")],

	# horizon
	"U+32ee":   [wn.synset("horizon.n.01")],

	# curve, curved line
	"U+32ef":   [wn.synset("curve.n.01"),
				wn.synset("bend.n.03")],

	# container, bowl, holder, pouch, basket
	"U+32f0":   [wn.synset("bowling_ball.n.01"),
				wn.synset("basket.n.04"),
				wn.synset("holder.n.03"),
				wn.synset("holder.n.02"),
				wn.synset("holder.n.01"),
				wn.synset("basket.n.03"),
				wn.synset("bowl.n.02"),
				wn.synset("basket.n.01"),
				wn.synset("bowl.n.07"),
				wn.synset("bowl.n.04"),
				wn.synset("bowl.n.08"),
				wn.synset("pouch.n.03"),
				wn.synset("pouch.n.02"),
				wn.synset("pouch.n.01"),
				wn.synset("stadium.n.01"),
				wn.synset("bowl.n.03"),
				wn.synset("basket.n.02"),
				wn.synset("bowl.n.01"),
				wn.synset("container.n.01"),
				wn.synset("roll.n.15")],

	# float
	"U+32f1":   [wn.synset("float.v.02")],

	# sieve, colander, strainer
	"U+32f2":   [wn.synset("sieve.n.01")],

	# take, bring, carry, move
	"U+32f3":   [wn.synset("lead.v.01"),
				wn.synset("bring.v.04"),
				wn.synset("bring.v.06"),
				wn.synset("bring.v.01"),
				wn.synset("bring.v.03"),
				wn.synset("post.v.07")],

	# apple
	"U+32f7":   [wn.synset("apple.n.01")],

	# peach, nectarine
	"U+32f8":   [wn.synset("peach.n.03")],

	# cabbage
	"U+32f9":   [wn.synset("cabbage.n.01"),
				wn.synset("cabbage.n.03"),
				wn.synset("boodle.n.01")],

	# handbag
	"U+32fc":   [wn.synset("bag.n.04")],

	# dromedary
	"U+32fd":   [wn.synset("arabian_camel.n.01")],

	# camel
	"U+32fe":   [wn.synset("camel.n.01")],

	# mushroom
	"U+3300":   [wn.synset("mushroom.n.03")],

	# snake, viper, boa, grass snake
	"U+3301":   [wn.synset("snake.n.01")],

	# dolphin, porpoise
	"U+3304":   [wn.synset("dolphin.n.02")],

	# pig, boar
	"U+3306":   [wn.synset("hog.n.03")],

	# spiral, curl
	"U+3307":   [wn.synset("spiral.n.04"),
				wn.synset("coil.n.01"),
				wn.synset("spiral.n.06"),
				wn.synset("spiral.n.01"),
				wn.synset("spiral.n.03"),
				wn.synset("helix.n.01")],

	# gun, firearm
	"U+3309":   [wn.synset("gun.n.01")],

	# pliers
	"U+330b":   [wn.synset("pliers.n.01")],

	# dog, canine, canid
	"U+330c":   [wn.synset("dog.n.01")],

	# tail
	"U+330d":   [wn.synset("buttocks.n.01"),
				wn.synset("stern.n.01"),
				wn.synset("tail.n.01"),
				wn.synset("tail.n.03"),
				wn.synset("fag_end.n.01"),
				wn.synset("tail.n.05"),
				wn.synset("tail.n.07"),
				wn.synset("tail.n.06")],

	# pineapple
	"U+330f":   [wn.synset("pineapple.n.02")],

	# airplane, aeroplane, plane
	"U+3312":   [wn.synset("airplane.n.01")],

	# angel
	"U+3315":   [wn.synset("angel.n.01")],

	# fly
	"U+3316":   [wn.synset("fly.v.01")],

	# bird
	"U+3317":   [wn.synset("bird.n.01")],

	# bat
	"U+3319":   [wn.synset("bat.n.05")],

	# tree
	"U+331e":   [wn.synset("tree.n.01")],

	# branch
	"U+331f":   [wn.synset("branch.n.02")],

	# trunk, tree trunk, bole
	"U+3320":   [wn.synset("trunk.n.01")],

	# evergreen tree, spruce, fir, fir tree
	"U+3321":   [wn.synset("spruce.n.02"),
				wn.synset("spruce.n.01"),
				wn.synset("fir.n.02"),
				wn.synset("fir.n.01"),
				wn.synset("evergreen.n.01")],

	# countryside, country
	"U+3322":   [wn.synset("country.n.04"),
				wn.synset("countryside.n.01")],

	# shamrock
	"U+3327":   [wn.synset("clover.n.01"),
				wn.synset("common_wood_sorrel.n.01"),
				wn.synset("white_clover.n.01"),
				wn.synset("hop_clover.n.02")],

	# corn
	"U+332a":   [wn.synset("corn.n.01")],

	# celery
	"U+332b":   [wn.synset("celery.n.02"),
				wn.synset("celery.n.01")],

	# cheese
	"U+332d":   [wn.synset("cheese.n.01")],

	# grass
	"U+332e":   [wn.synset("grass.n.01")],

	# grain, cereal
	"U+332f":   [wn.synset("cereal.n.01"),
				wn.synset("grain.n.07"),
				wn.synset("grain.n.02"),
				wn.synset("grain.n.01")],

	# field
	"U+3330":   [wn.synset("playing_field.n.02"),
				wn.synset("plain.n.01"),
				wn.synset("sphere.n.01"),
				wn.synset("field.n.11"),
				wn.synset("field.n.10"),
				wn.synset("field.n.16"),
				wn.synset("field.n.14"),
				wn.synset("field.n.05"),
				wn.synset("discipline.n.01"),
				wn.synset("field.n.01"),
				wn.synset("field.n.06"),
				wn.synset("field.n.03")],

	# iron, smoothing iron
	"U+3331":   [wn.synset("iron.v.01")],

	# beaver
	"U+3332":   [wn.synset("beaver.n.07")],

	# shellfish
	"U+3334":   [wn.synset("shellfish.n.01"),
				wn.synset("bivalve.n.01"),
				wn.synset("mollusk.n.01"),
				wn.synset("crustacean.n.01")],

	# past
	"U+3335":   [wn.synset("past.n.01")],

	# present
	"U+3336":   [wn.synset("present.n.01")],

	# moon
	"U+3337":   [wn.synset("moon.n.06"),
				wn.synset("lunar_month.n.01"),
				wn.synset("moon.n.05"),
				wn.synset("moon.n.02"),
				wn.synset("moon.n.01"),
				wn.synset("moonlight.n.01")],

	# banana
	"U+3338":   [wn.synset("banana.n.02")],

	# future
	"U+3339":   [wn.synset("future.n.01")],

	# bean, chick pea, kidney bean, pinto bean
	"U+333a":   [wn.synset("bean.n.01")],

	# peas
	"U+333b":   [wn.synset("pea.n.01")],

	# expectation, anticipation
	"U+333c":   [wn.synset("expectation.n.01"),
				wn.synset("anticipation.n.04")],

	# insurance
	"U+333d":   [wn.synset("indemnity.n.01")],

	# snowshoe
	"U+333e":   [wn.synset("snowshoe.n.01")],

	# leaf, flap
	"U+333f":   [wn.synset("dither.n.01"),
				wn.synset("flap.n.04"),
				wn.synset("flap.n.05"),
				wn.synset("flap.n.01"),
				wn.synset("flap.n.03"),
				wn.synset("leaf.n.03"),
				wn.synset("leaf.n.02"),
				wn.synset("leaf.n.01")],

	# turnip, rutabaga, vegetable
	"U+3340":   [wn.synset("turnip.n.01")],

	# lemon
	"U+3341":   [wn.synset("gamboge.n.02"),
				wn.synset("lemon.n.05"),
				wn.synset("lemon.n.04"),
				wn.synset("lemon.n.03"),
				wn.synset("lemon.n.01")],

	# butterfly, moth
	"U+3342":   [wn.synset("butterfly.n.01")],

	# body, trunk
	"U+3343":   [wn.synset("body.n.01")],

	# chest
	"U+3344":   [wn.synset("thorax.n.02"),
				wn.synset("chest.n.02"),
				wn.synset("chest_of_drawers.n.01"),
				wn.synset("breast.n.01")],

	# breasts
	"U+3345":   [wn.synset("breast.n.02")],

	# crotch
	"U+3346":   [wn.synset("fork.n.03"),
				wn.synset("genitalia.n.01"),
				wn.synset("crotch.n.02")],

	# waist
	"U+3348":   [wn.synset("waist.n.01")],

	# shoulder
	"U+3349":   [wn.synset("shoulder.n.01")],

	# stomach, abdomen, belly, tummy, tum
	"U+334b":   [wn.synset("stomach.n.01")],

	# embryo
	"U+334c":   [wn.synset("embryo.n.02")],

	# pubic hair
	"U+334e":   [wn.synset("hair.n.06"),
				wn.synset("pubic_hair.n.01"),
				wn.synset("hair.n.01")],

	# uterus, womb
	"U+334f":   [wn.synset("uterus.n.01")],

	# vagina
	"U+3351":   [wn.synset("vagina.n.01")],

	# ago, then
	"U+3352":   [wn.synset("then.n.01"),
				wn.synset("ago.r.01"),
				wn.synset("ago.s.01"),
				wn.synset("then.r.01")],

	# now
	"U+3353":   [wn.synset("now.n.01")],

	# then, so, later
	"U+3354":   [wn.synset("later.s.01"),
				wn.synset("sol.n.03"),
				wn.synset("late.s.04"),
				wn.synset("belated.s.01"),
				wn.synset("by_and_by.r.01"),
				wn.synset("former.s.03"),
				wn.synset("late.a.01"),
				wn.synset("late.a.06"),
				wn.synset("then.r.01"),
				wn.synset("late.a.05"),
				wn.synset("late.s.03"),
				wn.synset("then.n.01"),
				wn.synset("subsequently.r.01"),
				wn.synset("later.r.03")],

	# olive
	"U+3355":   [wn.synset("olive.n.03"),
				wn.synset("olive.n.02"),
				wn.synset("olive.n.01"),
				wn.synset("olive.n.05"),
				wn.synset("olive.n.04")],

	# pear
	"U+3356":   [wn.synset("pear.n.01")],

	# avocado
	"U+3357":   [wn.synset("avocado.n.02"),
				wn.synset("avocado.n.01")],

	# bread, loaf of bread, loaf, sliced bread
	"U+3358":   [wn.synset("bread.n.01")],

	# toast
	"U+3359":   [wn.synset("toast.n.01")],

	# pita
	"U+335a":   [wn.synset("pita.n.01")],

	# roll, bun, scone, brioche
	"U+335b":   [wn.synset("bun.n.01")],

	# hair
	"U+3360":   [wn.synset("hair.n.01")],

	# fur, coat, hair
	"U+3361":   [wn.synset("fur.n.01")],

	# pit, stone
	"U+3362":   [wn.synset("stone.n.12"),
				wn.synset("pit.n.09"),
				wn.synset("hell.n.03"),
				wn.synset("pit.n.02"),
				wn.synset("pit.n.01"),
				wn.synset("pit.n.07"),
				wn.synset("pit.n.06"),
				wn.synset("pit.n.05"),
				wn.synset("gem.n.02"),
				wn.synset("pit.n.08"),
				wn.synset("orchestra_pit.n.01"),
				wn.synset("stone.n.13"),
				wn.synset("stone.n.10"),
				wn.synset("stone.n.02"),
				wn.synset("stone.n.05"),
				wn.synset("stone.n.07"),
				wn.synset("stone.n.06"),
				wn.synset("stone.n.09"),
				wn.synset("stone.n.08"),
				wn.synset("rock.n.02"),
				wn.synset("rock.n.01"),
				wn.synset("stone.n.11"),
				wn.synset("colliery.n.01")],

	# enclosure
	"U+3363":   [wn.synset("enclosure.n.01"),
				wn.synset("enclosure.n.03")],

	# bottom, base, bottom of a thing
	"U+3364":   [wn.synset("bottom.n.07"),
				wn.synset("bed.n.03"),
				wn.synset("buttocks.n.01"),
				wn.synset("bottom.n.02"),
				wn.synset("bottom.n.01"),
				wn.synset("bottomland.n.01"),
				wn.synset("bottom.n.04")],

	# top, top of a thing
	"U+3366":   [wn.synset("peak.n.04"),
				wn.synset("acme.n.01"),
				wn.synset("top.n.08"),
				wn.synset("circus_tent.n.01"),
				wn.synset("top.n.04"),
				wn.synset("top.n.07"),
				wn.synset("top.n.06"),
				wn.synset("top.n.01"),
				wn.synset("top.n.02"),
				wn.synset("top.n.09"),
				wn.synset("top.n.10")],

	# out of, exit
	"U+336a":   [wn.synset("out_of.r.01"),
				wn.synset("exit.n.03"),
				wn.synset("exit.n.01"),
				wn.synset("passing.n.02")],

	# camera
	"U+336b":   [wn.synset("camera.n.01")],

	# projector
	"U+336c":   [wn.synset("projector.n.02")],

	# secret
	"U+336d":   [wn.synset("secret.n.01")],

	# sleep
	"U+336e":   [wn.synset("sleep.v.01")],

	# window
	"U+3373":   [wn.synset("window.n.01")],

	# all, every, everything, total, whole
	"U+3374":   [wn.synset("all.s.02"),
				wn.synset("sum.n.02"),
				wn.synset("sum.n.05"),
				wn.synset("all.a.01"),
				wn.synset("every.s.01"),
				wn.synset("every.s.02"),
				wn.synset("wholly.r.01"),
				wn.synset("whole.n.02"),
				wn.synset("whole.n.01")],

	# chest of drawers, bureau, dresser
	"U+3376":   [wn.synset("chest_of_drawers.n.01")],

	# drawer
	"U+3377":   [wn.synset("drawer.n.01")],

	# book
	"U+3378":   [wn.synset("book.n.01")],

	# cupboard, closet, wardrobe
	"U+3379":   [wn.synset("cupboard.n.01"),
				wn.synset("cabinet.n.03"),
				wn.synset("water_closet.n.01"),
				wn.synset("wardrobe.n.03"),
				wn.synset("wardrobe.n.02"),
				wn.synset("wardrobe.n.01"),
				wn.synset("closet.n.04")],

	# answer, reply
	"U+337a":   [wn.synset("answer.n.01")],

	# exit
	"U+337b":   [wn.synset("exit.v.01")],

	# postcard
	"U+337c":   [wn.synset("postcard.n.01")],

	# transport, transportation
	"U+337f":   [wn.synset("transportation.n.05")],

	# cart, carriage
	"U+3380":   [wn.synset("diligence.n.01"),
				wn.synset("passenger_car.n.01"),
				wn.synset("carriage.n.03"),
				wn.synset("carriage.n.02"),
				wn.synset("stagecoach.n.01"),
				wn.synset("carriage.n.04"),
				wn.synset("baby_buggy.n.01"),
				wn.synset("assiduity.n.01")],

	# thing, object
	"U+3382":   [wn.synset("object.n.01")],

	# goods, contents
	"U+3383":   [wn.synset("good.n.02"),
				wn.synset("good.n.03"),
				wn.synset("good.n.01"),
				wn.synset("subject.n.02"),
				wn.synset("message.n.02"),
				wn.synset("contents.n.01"),
				wn.synset("content.n.05"),
				wn.synset("content.n.03"),
				wn.synset("content.n.01"),
				wn.synset("capacity.n.03"),
				wn.synset("commodity.n.01"),
				wn.synset("contentedness.n.01")],

	# waste, garbage, rubbish, trash
	"U+3385":   [wn.synset("garbage.n.01"),
				wn.synset("trash.n.02"),
				wn.synset("folderol.n.01"),
				wn.synset("rubbish.n.01")],

	# block, brick, city block
	"U+3388":   [wn.synset("block.n.05"),
				wn.synset("block.n.04"),
				wn.synset("block.n.07"),
				wn.synset("block.n.06"),
				wn.synset("block.n.01"),
				wn.synset("block.n.03"),
				wn.synset("block.n.02"),
				wn.synset("blocking.n.01"),
				wn.synset("pulley.n.01"),
				wn.synset("engine_block.n.01"),
				wn.synset("blockage.n.02"),
				wn.synset("auction_block.n.01")],

	# pull, drag, tow, tug, pulling
	"U+338a":   [wn.synset("pull.v.01")],

	# solid thing
	"U+338c":   [wn.synset("solid.n.01")],

	# kite
	"U+3391":   [wn.synset("kite.n.03")],

	# rectangle, oblong
	"U+3394":   [wn.synset("rectangle.n.01")],

	# parcel, package
	"U+3395":   [wn.synset("package.n.01")],

	# paper, card, page
	"U+3396":   [wn.synset("card.n.08"),
				wn.synset("card.n.04"),
				wn.synset("card.n.01"),
				wn.synset("card.n.03"),
				wn.synset("card.n.02"),
				wn.synset("menu.n.01"),
				wn.synset("calling_card.n.02"),
				wn.synset("wag.n.01"),
				wn.synset("poster.n.01"),
				wn.synset("batting_order.n.01"),
				wn.synset("circuit_board.n.01")],

	# door
	"U+3397":   [wn.synset("door.n.01")],

	# goal
	"U+3398":   [wn.synset("goal.n.04")],

	# shelf
	"U+3399":   [wn.synset("shelf.n.01")],

	# room
	"U+339a":   [wn.synset("room.n.01")],

	# ceiling
	"U+339b":   [wn.synset("ceiling.n.01")],

	# floor, storey, level, etage
	"U+339c":   [wn.synset("floor.n.06"),
				wn.synset("floor.n.07"),
				wn.synset("floor.n.04"),
				wn.synset("floor.n.05"),
				wn.synset("floor.n.02"),
				wn.synset("floor.n.03"),
				wn.synset("floor.n.01"),
				wn.synset("floor.n.08"),
				wn.synset("floor.n.09"),
				wn.synset("floor.n.10")],

	# floor covering, linoleum
	"U+339d":   [wn.synset("floor_cover.n.01"),
				wn.synset("linoleum.n.01")],

	# wall
	"U+339e":   [wn.synset("wall.n.02"),
				wn.synset("wall.n.01")],

	# corner
	"U+339f":   [wn.synset("corner.n.03"),
				wn.synset("corner.n.04")],

	# steam bath
	"U+33a0":   [wn.synset("turkish_bath.n.02"),
				wn.synset("steam_bath.n.01"),
				wn.synset("sauna.n.01")],

	# shower
	"U+33a1":   [wn.synset("shower.n.02"),
				wn.synset("shower.n.01")],

	# opening
	"U+33a2":   [wn.synset("opening.n.05"),
				wn.synset("opening.n.02"),
				wn.synset("opening.n.03"),
				wn.synset("opening.n.01")],

	# fireplace
	"U+33a3":   [wn.synset("fireplace.n.01")],

	# freedom, liberty
	"U+33a4":   [wn.synset("freedom.n.01")],

	# awake
	"U+33a5":   [wn.synset("alert.s.03"),
				wn.synset("awake.a.01")],

	# question, be sceptical, doubt
	"U+33a6":   [wn.synset("interrogate.v.02")],

	# badge, shield
	"U+33a9":   [wn.synset("badge.n.02"),
				wn.synset("badge.n.01")],

	# table
	"U+33aa":   [wn.synset("table.n.03")],

	# board, board of directors, executive
	"U+33ab":   [wn.synset("directorate.n.01")],

	# edge
	"U+33ac":   [wn.synset("edge.n.06")],

	# pier
	"U+33af":   [wn.synset("pier.n.01")],

	# brush
	"U+33b1":   [wn.synset("brush.v.01"),
				wn.synset("brush.v.02"),
				wn.synset("brush.v.03"),
				wn.synset("brush.v.04"),
				wn.synset("brush.v.05"),
				wn.synset("brush.v.06")],

	# box, cube
	"U+33b2":   [wn.synset("box.n.01")],

	# comb
	"U+33b3":   [wn.synset("comb.n.01")],

	# shekel
	"U+33b4":   [wn.synset("shekel.n.01")],

	# pot, pan, kettle, boiler
	"U+33b5":   [wn.synset("pan.n.01"),
				wn.synset("toilet.n.02"),
				wn.synset("potentiometer.n.02"),
				wn.synset("pot.n.09"),
				wn.synset("pan.n.04"),
				wn.synset("pot.n.04"),
				wn.synset("pot.n.07"),
				wn.synset("pot.n.06"),
				wn.synset("pot.n.01"),
				wn.synset("pan.n.03"),
				wn.synset("pot.n.03"),
				wn.synset("batch.n.02"),
				wn.synset("pan.n.02")],

	# glass, drinking glass
	"U+33b6":   [wn.synset("glass.n.02"),
				wn.synset("glass.n.03")],

	# mug, cup
	"U+33b7":   [wn.synset("cup.n.02"),
				wn.synset("cup.n.01")],

	# effect, result
	"U+33b9":   [wn.synset("effect.n.05"),
				wn.synset("effect.n.06"),
				wn.synset("impression.n.02"),
				wn.synset("consequence.n.01"),
				wn.synset("effect.n.03")],

	# make, manufacture, produce
	"U+33ba":   [wn.synset("produce.v.02")],

	# cause
	"U+33bb":   [wn.synset("produce.v.03"),
				wn.synset("induce.v.02"),
				wn.synset("effect.v.01"),
				wn.synset("cause.v.01")],

	# therefore, so, so that
	"U+33bc":   [wn.synset("sol.n.03"),
				wn.synset("therefore.r.01"),
				wn.synset("consequently.r.02")],

	# mountain
	"U+33bd":   [wn.synset("mountain.n.01")],

	# mine
	"U+33be":   [wn.synset("mine.n.01")],

	# stone, rock
	"U+33bf":   [wn.synset("rock.n.01")],

	# valley
	"U+33c1":   [wn.synset("valley.n.01")],

	# bone
	"U+33c5":   [wn.synset("bone.n.01")],

	# structure, construction
	"U+33c6":   [wn.synset("structure.n.01"),
				wn.synset("structure.n.03"),
				wn.synset("structure.n.02")],

	# joint
	"U+33c7":   [wn.synset("joint.n.01")],

	# over, above, superior
	"U+33c9":   [wn.synset("over.n.01"),
				wn.synset("lake_superior.n.01"),
				wn.synset("superscript.n.01"),
				wn.synset("above.r.01"),
				wn.synset("superior.n.01"),
				wn.synset("superior.n.02"),
				wn.synset("above.r.02"),
				wn.synset("above.n.01"),
				wn.synset("superior.n.05"),
				wn.synset("upstairs.r.01"),
				wn.synset("victor.n.01")],

	# division
	"U+33ca":   [wn.synset("division.n.08"),
				wn.synset("division.n.09"),
				wn.synset("class.n.05"),
				wn.synset("division.n.01"),
				wn.synset("division.n.03"),
				wn.synset("division.n.04"),
				wn.synset("division.n.05"),
				wn.synset("division.n.11"),
				wn.synset("division.n.10"),
				wn.synset("division.n.07"),
				wn.synset("division.n.12"),
				wn.synset("part.n.09")],

	# part, bit, piece, portion, part of
	"U+33cb":   [wn.synset("bit.n.05"),
				wn.synset("morsel.n.02")],

	# dot
	"U+33cc":   [wn.synset("acid.n.02"),
				wn.synset("dot.n.03"),
				wn.synset("department_of_transportation.n.01"),
				wn.synset("point.n.09"),
				wn.synset("period.n.07")],

	# again
	"U+33cd":   [wn.synset("again.r.01")],

	# there
	"U+33ce":   [wn.synset("speed_of_light.n.01"),
				wn.synset("there.n.01")],

	# before, in front of, prior to
	"U+33cf":   [wn.synset("ahead.r.01"),
				wn.synset("earlier.r.01")],

	# around
	"U+33d0":   [wn.synset("round.r.01"),
				wn.synset("about.r.02")],

	# either
	"U+33d1":   [wn.synset("either.r.01"),
				wn.synset("o.n.02")],

	# that
	"U+33d3":   [wn.synset("such.s.01")],

	# powder, dust
	"U+33d5":   [wn.synset("powder.n.01")],

	# stamp
	"U+33d7":   [wn.synset("stamp.n.08")],

	# fold, pleat, folding, pleating
	"U+33d9":   [wn.synset("fold.v.01")],

	# space, dimension
	"U+33db":   [wn.synset("space.n.07"),
				wn.synset("space.n.05"),
				wn.synset("space.n.02"),
				wn.synset("space.n.03"),
				wn.synset("space.n.01"),
				wn.synset("outer_space.n.01"),
				wn.synset("distance.n.05"),
				wn.synset("space.n.08"),
				wn.synset("proportion.n.02"),
				wn.synset("quad.n.03"),
				wn.synset("property.n.04"),
				wn.synset("dimension.n.01"),
				wn.synset("dimension.n.03")],

	# arm
	"U+33dc":   [wn.synset("arm.n.01")],

	# wrist
	"U+33dd":   [wn.synset("wrist.n.01")],

	# elbow
	"U+33de":   [wn.synset("elbow.n.01")],

	# muscle
	"U+33df":   [wn.synset("muscle.n.01")],

	# strong, powerful, mighty
	"U+33e0":   [wn.synset("powerful.a.01")],

	# health
	"U+33e2":   [wn.synset("health.n.01")],

	# ride, drive
	"U+33e4":   [wn.synset("ride.v.01")],

	# tray
	"U+33e8":   [wn.synset("tray.n.01")],

	# buttocks, bottom, bum, rear, ass, back of a thing
	"U+33eb":   [wn.synset("buttocks.n.01")],

	# genitals, sex organs
	"U+33ec":   [wn.synset("reproductive_organ.n.01"),
				wn.synset("genitalia.n.01")],

	# erection, erect penis
	"U+33ed":   [wn.synset("erection.n.01")],

	# male, masculine
	"U+33ee":   [wn.synset("male.a.01")],

	# penis
	"U+33ef":   [wn.synset("penis.n.01")],

	# left
	"U+33f0":   [wn.synset("left.a.01"),
				wn.synset("left.s.03"),
				wn.synset("leftover.s.01"),
				wn.synset("left.a.04")],

	# right
	"U+33f1":   [wn.synset("correct.s.03"),
				wn.synset("correct.s.02"),
				wn.synset("right.n.02"),
				wn.synset("right.n.04"),
				wn.synset("right.n.05"),
				wn.synset("right.s.12"),
				wn.synset("veracious.s.02"),
				wn.synset("good.s.12"),
				wn.synset("right.s.09"),
				wn.synset("right.s.08"),
				wn.synset("right.a.01"),
				wn.synset("right.a.07"),
				wn.synset("right.a.05"),
				wn.synset("right.a.04"),
				wn.synset("correct.a.01"),
				wn.synset("proper.s.04"),
				wn.synset("right.s.11")],

	# key, tonality
	"U+33f3":   [wn.synset("key.n.01"),
				wn.synset("key.n.02"),
				wn.synset("key.n.11")],

	# protection, shelter
	"U+33f5":   [wn.synset("protection.n.01"),
				wn.synset("protection.n.04"),
				wn.synset("protective_covering.n.01")],

	# harbour
	"U+33f6":   [wn.synset("seaport.n.01")],

	# clothing, clothes, garment
	"U+33f7":   [wn.synset("clothing.n.01")],

	# marriage, wedding
	"U+33f8":   [wn.synset("marriage.n.03"),
				wn.synset("marriage.n.01"),
				wn.synset("marriage.n.04")],

	# cone, conifer cone, strobilus
	"U+33f9":   [wn.synset("cone.n.04"),
				wn.synset("cone.n.01"),
				wn.synset("cone.n.02"),
				wn.synset("cone.n.03")],

	# farm
	"U+33fa":   [wn.synset("farm.n.01")],

	# parent
	"U+33fb":   [wn.synset("parent.n.01")],

	# birth
	"U+33fc":   [wn.synset("parturition.n.01"),
				wn.synset("parentage.n.02"),
				wn.synset("birth.n.01"),
				wn.synset("birth.n.05"),
				wn.synset("birth.n.02")],

	# daughter
	"U+33fd":   [wn.synset("daughter.n.01")],

	# son
	"U+33fe":   [wn.synset("son.n.01")],

	# offspring, child
	"U+33ff":   [wn.synset("offspring.n.01")],

	# umbrella
	"U+3400":   [wn.synset("umbrella.n.03"),
				wn.synset("umbrella.n.02"),
				wn.synset("umbrella.n.01"),
				wn.synset("gamp.n.01")],

	# mother, mom, mommy, mum
	"U+3401":   [wn.synset("mother.n.01")],

	# father, dad, daddy, papa, pa, pop
	"U+3402":   [wn.synset("forefather.n.01"),
				wn.synset("father.n.06"),
				wn.synset("founder.n.02"),
				wn.synset("father.n.03"),
				wn.synset("father.n.01")],

	# relative, relation
	"U+3403":   [wn.synset("sexual_intercourse.n.01"),
				wn.synset("relative.n.02"),
				wn.synset("relative.n.01"),
				wn.synset("relation.n.04"),
				wn.synset("relation_back.n.01"),
				wn.synset("relation.n.01"),
				wn.synset("relation.n.06")],

	# wife
	"U+3404":   [wn.synset("wife.n.01")],

	# stepmother
	"U+3405":   [wn.synset("stepmother.n.01")],

	# grandparent
	"U+3406":   [wn.synset("grandparent.n.01")],

	# aunt
	"U+3407":   [wn.synset("aunt.n.01")],

	# uncle
	"U+3408":   [wn.synset("uncle.n.01")],

	# grandmother, grandma, granny
	"U+3409":   [wn.synset("grandma.n.01")],

	# grandfather, granddad, grandpa
	"U+340c":   [wn.synset("grandfather.n.01")],

	# illness, disease, sickness
	"U+3410":   [wn.synset("illness.n.01")],

	# purpose
	"U+3412":   [wn.synset("purpose.n.01"),
				wn.synset("function.n.02")],

	# opposition, counter purpose
	"U+3417":   [wn.synset("resistance.n.01"),
				wn.synset("enemy.n.02"),
				wn.synset("opposition.n.02"),
				wn.synset("opposition.n.05"),
				wn.synset("opposition.n.04"),
				wn.synset("opposition.n.06"),
				wn.synset("opposition.n.08"),
				wn.synset("confrontation.n.04")],

	# crystal
	"U+3419":   [wn.synset("crystal.n.05")],

	# pointer
	"U+341b":   [wn.synset("pointer.n.02"),
				wn.synset("cursor.n.01"),
				wn.synset("arrow.n.01"),
				wn.synset("pointer.n.04")],

	# about, concerning, in relation to, of, on
	"U+341c":   [wn.synset("approximately.r.01"),
				wn.synset("about.s.01"),
				wn.synset("refer.v.02"),
				wn.synset("on.r.02"),
				wn.synset("on.a.02"),
				wn.synset("on.r.03"),
				wn.synset("along.r.01"),
				wn.synset("about.r.05"),
				wn.synset("about.r.04"),
				wn.synset("about.r.07"),
				wn.synset("about.r.06"),
				wn.synset("about.r.03"),
				wn.synset("about.r.02"),
				wn.synset("on.a.01"),
				wn.synset("concern.v.02")],

	# at
	"U+341e":   [wn.synset("up.r.01"),
				wn.synset("upstairs.r.01"),
				wn.synset("above.r.01"),
				wn.synset("above.r.02"),
				wn.synset("at.n.02"),
				wn.synset("astatine.n.01")],

	# here
	"U+341f":   [wn.synset("hera.n.01"),
				wn.synset("here.n.01")],

	# heat
	"U+3423":   [wn.synset("heat.v.01")],

	# cold, common cold
	"U+3424":   [wn.synset("cold.n.01")],

	# nuclear radiation, radioactivity
	"U+3425":   [wn.synset("radiation.n.04")],

	# or
	"U+3426":   [wn.synset("oregon.n.01"),
				wn.synset("operating_room.n.01"),
				wn.synset("o.n.02")],

	# against, opposed to
	"U+3427":   [wn.synset("antonym.n.01"),
				wn.synset("inverse.n.01"),
				wn.synset("contrary.n.02"),
				wn.synset("reverse.n.01")],

	# person, human being, individual, human
	"U+3428":   [wn.synset("person.n.01")],

	# spouse, cohabitant, partner, dancing, business)
	"U+342d":   [wn.synset("partner.n.03")],

	# addition, gain
	"U+3431":   [wn.synset("summation.n.04")],

	# and, also, plus, too
	"U+3434":   [wn.synset("asset.n.01"),
				wn.synset("besides.r.02"),
				wn.synset("summation.n.04"),
				wn.synset("excessively.r.01")],

	# belongs to, of
	"U+3437":   [wn.synset("delaware.n.04")],

	# cross, Christianity
	"U+3438":   [wn.synset("christendom.n.01"),
				wn.synset("christianity.n.01")],

	# across
	"U+3439":   [wn.synset("across.r.01"),
				wn.synset("across.r.02"),
				wn.synset("short.r.03"),
				wn.synset("over.r.03")],

	# multiplication
	"U+343a":   [wn.synset("multiplication.n.03")],

	# choice, selection, election
	"U+343c":   [wn.synset("choice.n.02"),
				wn.synset("option.n.02"),
				wn.synset("choice.n.01")],

	# more
	"U+343d":   [wn.synset("more.a.02"),
				wn.synset("more.a.01"),
				wn.synset("quite.r.01"),
				wn.synset("additionally.r.01"),
				wn.synset("again.r.01"),
				wn.synset("more.r.01"),
				wn.synset("no_longer.r.01"),
				wn.synset("more.r.02"),
				wn.synset("no.r.01"),
				wn.synset("plus_sign.n.01"),
				wn.synset("most.r.01"),
				wn.synset("most.r.02")],

	# much, many, very
	"U+343e":   [wn.synset("many.a.01"),
				wn.synset("very.s.01"),
				wn.synset("identical.s.02"),
				wn.synset("much.a.01")],

	# war
	"U+343f":   [wn.synset("war.n.01")],

	# wand
	"U+3442":   [wn.synset("scepter.n.02"),
				wn.synset("baton.n.01"),
				wn.synset("wand.n.01"),
				wn.synset("wand.n.02")],

	# star
	"U+3444":   [wn.synset("star.n.01")],

	# comet
	"U+3447":   [wn.synset("comet.n.01")],

	# knife, sword
	"U+3448":   [wn.synset("knife.n.01")],

	# plough
	"U+344a":   [wn.synset("plow.n.01")],

	# creation, nature
	"U+344b":   [wn.synset("creation.n.01")],

	# danger
	"U+344d":   [wn.synset("danger.n.04"),
				wn.synset("danger.n.03"),
				wn.synset("risk.n.02"),
				wn.synset("danger.n.01")],

	# pyramid
	"U+344e":   [wn.synset("pyramid.n.01")],

	# rocket, spaceship
	"U+3450":   [wn.synset("starship.n.01"),
				wn.synset("rocket.n.01"),
				wn.synset("rocket.n.03"),
				wn.synset("rocket.n.02"),
				wn.synset("rocket.n.04"),
				wn.synset("skyrocket.n.02")],

	# female, feminine
	"U+3451":   [wn.synset("female.n.01"),
				wn.synset("female.n.02")],

	# tooth
	"U+3452":   [wn.synset("tooth.n.05"),
				wn.synset("tooth.n.01")],

	# teeth
	"U+3453":   [wn.synset("dentition.n.02"),
				wn.synset("tooth.n.04"),
				wn.synset("tooth.n.05"),
				wn.synset("tooth.n.02"),
				wn.synset("tooth.n.03"),
				wn.synset("tooth.n.01")],

	# cavity, caries
	"U+3454":   [wn.synset("cavity.n.03")],

	# action, act, deed, demonstrate, demonstration
	"U+3457":   [wn.synset("demonstrate.v.04"),
				wn.synset("work.v.03"),
				wn.synset("act.v.10"),
				wn.synset("show.v.01"),
				wn.synset("prove.v.02"),
				wn.synset("act.v.06"),
				wn.synset("act.v.04"),
				wn.synset("act.v.05"),
				wn.synset("act.v.02"),
				wn.synset("act.v.03"),
				wn.synset("act.v.01"),
				wn.synset("attest.v.01"),
				wn.synset("dissemble.v.03"),
				wn.synset("act.v.08")],

	# hip
	"U+3459":   [wn.synset("pelvis.n.01"),
				wn.synset("hip.n.05"),
				wn.synset("hip.n.04"),
				wn.synset("hip.n.03"),
				wn.synset("hip.n.01")],

	# leg
	"U+345a":   [wn.synset("leg.n.01")],

	# heel
	"U+345b":   [wn.synset("heel.n.02")],

	# foot
	"U+345c":   [wn.synset("foot.n.02")],

	# kick
	"U+345d":   [wn.synset("kick.v.04"),
				wn.synset("kick.v.07"),
				wn.synset("kick.v.06"),
				wn.synset("kick.v.01"),
				wn.synset("complain.v.01"),
				wn.synset("kick.v.03"),
				wn.synset("kick.v.02"),
				wn.synset("kick_back.v.02")],

	# toe
	"U+345e":   [wn.synset("toe.n.01")],

	# roller skates
	"U+345f":   [wn.synset("roller_skate.n.01")],

	# ice skates
	"U+3460":   [wn.synset("ice_skate.n.01")],

	# evaluation, value
	"U+3461":   [wn.synset("value.n.06"),
				wn.synset("value.n.01")],

	# work, employment, job
	"U+3463":   [wn.synset("job.n.05"),
				wn.synset("job.n.04"),
				wn.synset("job.n.07"),
				wn.synset("job.n.06"),
				wn.synset("job.n.03"),
				wn.synset("job.n.02"),
				wn.synset("job.n.12"),
				wn.synset("job.n.09"),
				wn.synset("job.n.10"),
				wn.synset("job.n.11"),
				wn.synset("caper.n.03"),
				wn.synset("work.n.01"),
				wn.synset("problem.n.01"),
				wn.synset("oeuvre.n.01"),
				wn.synset("occupation.n.01"),
				wn.synset("workplace.n.01"),
				wn.synset("use.n.01"),
				wn.synset("work.n.02"),
				wn.synset("study.n.02"),
				wn.synset("employment.n.03"),
				wn.synset("employment.n.02"),
				wn.synset("employment.n.01"),
				wn.synset("work.n.05")],

	# gender, sex
	"U+3465":   [wn.synset("gender.n.01")],

	# insect, bug
	"U+3466":   [wn.synset("insect.n.01")],

	# electricity
	"U+3472":   [wn.synset("electricity.n.02"),
				wn.synset("electricity.n.01")],

	# hand
	"U+3474":   [wn.synset("hand.n.01")],

	# thumb
	"U+3475":   [wn.synset("thumb.n.01")],

	# finger
	"U+3476":   [wn.synset("finger.n.02")],

	# tool, instrument
	"U+3477":   [wn.synset("tool.n.01"),
				wn.synset("instrument.n.01"),
				wn.synset("instrument.n.02"),
				wn.synset("instrument.n.03"),
				wn.synset("instrumental_role.n.01"),
				wn.synset("cock.n.01"),
				wn.synset("musical_instrument.n.01"),
				wn.synset("creature.n.03"),
				wn.synset("legal_document.n.01")],

	# nose
	"U+347a":   [wn.synset("nose.n.01")],

	# road
	"U+347d":   [wn.synset("road.n.01")],

	# bus, coach
	"U+347f":   [wn.synset("bus.n.01")],

	# worm
	"U+3481":   [wn.synset("worm.n.01")],

	# sky
	"U+3482":   [wn.synset("sky.n.01")],

	# fog
	"U+3483":   [wn.synset("fog.n.01")],

	# environment
	"U+3484":   [wn.synset("environment.n.02")],

	# peace, peace of mind, serenity
	"U+3485":   [wn.synset("peace.n.02"),
				wn.synset("peace.n.03"),
				wn.synset("peace.n.01"),
				wn.synset("peace.n.05")],

	# disturbance, unrest
	"U+3486":   [wn.synset("perturbation.n.03"),
				wn.synset("agitation.n.02"),
				wn.synset("worry.n.02"),
				wn.synset("disturbance.n.02"),
				wn.synset("disturbance.n.03"),
				wn.synset("unrest.n.02"),
				wn.synset("disturbance.n.05"),
				wn.synset("mental_disorder.n.01"),
				wn.synset("affray.n.02"),
				wn.synset("noise.n.03")],

	# world
	"U+3487":   [wn.synset("universe.n.01"),
				wn.synset("world.n.06"),
				wn.synset("earth.n.01"),
				wn.synset("world.n.02"),
				wn.synset("world.n.03"),
				wn.synset("worldly_concern.n.01"),
				wn.synset("world.n.08"),
				wn.synset("populace.n.01")],

	# lightning
	"U+3489":   [wn.synset("lightning.n.01")],

	# air, atmosphere
	"U+348a":   [wn.synset("air.n.01")],

	# wind
	"U+348b":   [wn.synset("wind.n.01")],

	# subtraction, loss
	"U+348c":   [wn.synset("personnel_casualty.n.01"),
				wn.synset("passing.n.02"),
				wn.synset("subtraction.n.01"),
				wn.synset("subtraction.n.02"),
				wn.synset("loss.n.01"),
				wn.synset("loss.n.02"),
				wn.synset("loss.n.03"),
				wn.synset("loss.n.04"),
				wn.synset("loss.n.05"),
				wn.synset("loss.n.06")],

	# vehicle, carriage, railway car
	"U+348d":   [wn.synset("vehicle.n.01")],

	# fill
	"U+3490":   [wn.synset("fill.v.01")],

	# sailboat, sailing boat, yacht
	"U+3491":   [wn.synset("sailboat.n.01")],

	# under, below, inferior
	"U+3492":   [wn.synset("downstairs.r.01"),
				wn.synset("below.r.01"),
				wn.synset("below.r.02")],

	# weight
	"U+3493":   [wn.synset("weight.n.01")],

	# animal, beast, bovine, ovine
	"U+3494":   [wn.synset("animal.n.01")],

	# paw
	"U+3495":   [wn.synset("paw.n.01")],

	# hippopotamus
	"U+3497":   [wn.synset("hippopotamus.n.01")],

	# claw
	"U+349c":   [wn.synset("claw.n.01"),
				wn.synset("claw.n.03"),
				wn.synset("claw.n.04"),
				wn.synset("hook.n.04")],

	# giraffe
	"U+349d":   [wn.synset("giraffe.n.01")],

	# horse
	"U+349e":   [wn.synset("horse.n.01"),
				wn.synset("knight.n.02")],

	# rhinoceros
	"U+349f":   [wn.synset("rhinoceros.n.01")],

	# horn, antler
	"U+34a0":   [wn.synset("french_horn.n.01"),
				wn.synset("automobile_horn.n.01"),
				wn.synset("horn.n.06"),
				wn.synset("horn.n.07"),
				wn.synset("horn.n.04"),
				wn.synset("horn.n.02"),
				wn.synset("horn.n.03"),
				wn.synset("horn.n.01"),
				wn.synset("antler.n.01"),
				wn.synset("horn.n.09"),
				wn.synset("horn.n.08"),
				wn.synset("cornet.n.01")],

	# place, area, location, space
	"U+34a3":   [wn.synset("topographic_point.n.01"),
				wn.synset("position.n.01")],

	# bulb
	"U+34a5":   [wn.synset("bulb.n.01"),
				wn.synset("light_bulb.n.01"),
				wn.synset("bulb.n.06")],

	# onion, vegetable
	"U+34a6":   [wn.synset("onion.n.01")],

	# seed
	"U+34a8":   [wn.synset("seed.n.01"),
				wn.synset("semen.n.01")],

	# carrot, vegetable
	"U+34a9":   [wn.synset("vegetable.n.02"),
				wn.synset("vegetable.n.01"),
				wn.synset("carrot.n.02"),
				wn.synset("carrot.n.03"),
				wn.synset("carrot.n.01"),
				wn.synset("carrot.n.04")],

	# grave
	"U+34aa":   [wn.synset("grave.n.02")],

	# snail
	"U+34ab":   [wn.synset("snail.n.01")],

	# lawn, meadow
	"U+34ac":   [wn.synset("lawn.n.01"),
				wn.synset("hayfield.n.01")],

	# night
	"U+34ad":   [wn.synset("night.n.01")],

	# evening
	"U+34ae":   [wn.synset("evening.n.01")],

	# street
	"U+34b0":   [wn.synset("street.n.02"),
				wn.synset("street.n.03"),
				wn.synset("street.n.01"),
				wn.synset("street.n.04"),
				wn.synset("street.n.05")],

	# ski, runner
	"U+34b1":   [wn.synset("ski.n.01")],

	# skateboard
	"U+34b2":   [wn.synset("skateboard.n.01")],

	# adult, grownup, mature
	"U+34b4":   [wn.synset("fledged.a.01"),
				wn.synset("ripe.a.01"),
				wn.synset("adult.n.01"),
				wn.synset("adult.n.02"),
				wn.synset("pornographic.s.01"),
				wn.synset("mature.s.02"),
				wn.synset("adult.s.01"),
				wn.synset("mature.a.01"),
				wn.synset("mature.a.03")],

	# teenager, adolescent, youth
	"U+34b5":   [wn.synset("adolescent.n.01")],

	# eyebrow
	"U+34b6":   [wn.synset("eyebrow.n.01")],

	# temperature
	"U+34b8":   [wn.synset("temperature.n.01")],

	# most, maximum
	"U+34b9":   [wn.synset("maximal.a.01")],

	# high, tall
	"U+34ba":   [wn.synset("high.a.02"),
				wn.synset("tall.a.01"),
				wn.synset("high.a.01"),
				wn.synset("high.a.04")],

	# nail
	"U+34bb":   [wn.synset("nail.n.02")],

	# shovel, spade
	"U+34bc":   [wn.synset("shovel.n.01")],

	# dig
	"U+34bd":   [wn.synset("excavate.v.04"),
				wn.synset("dig.v.01")],

	# same, equal, equality
	"U+34bf":   [wn.synset("lapp.n.01"),
				wn.synset("lapp.n.02"),
				wn.synset("equality.n.01"),
				wn.synset("peer.n.01"),
				wn.synset("equality.n.02")],

	# different, other, difference
	"U+34c0":   [wn.synset("different.a.01")],

	# not, negative, no, don't, doesn't
	"U+34c1":   [wn.synset("not.r.01"),
				wn.synset("negative.n.02"),
				wn.synset("no.n.01")],

	# nowhere, no place
	"U+34c2":   [wn.synset("nowhere.n.01"),
				wn.synset("beak.n.04"),
				wn.synset("nose.n.01")],

	# low, short
	"U+34c3":   [wn.synset("low.a.02")],

	# pin
	"U+34c4":   [wn.synset("peg.n.02"),
				wn.synset("peg.n.06"),
				wn.synset("bowling_pin.n.01"),
				wn.synset("personal_identification_number.n.01"),
				wn.synset("fall.n.10"),
				wn.synset("pin.n.09"),
				wn.synset("pin.n.08"),
				wn.synset("pivot.n.02"),
				wn.synset("pin.n.01"),
				wn.synset("pin.n.05"),
				wn.synset("pin.n.07")],

	# love, affection
	"U+34c6":   [wn.synset("beloved.n.01"),
				wn.synset("love.n.02"),
				wn.synset("love.n.01"),
				wn.synset("affection.n.01"),
				wn.synset("love.n.04")],

	# but, except
	"U+34c7":   [wn.synset("merely.r.01"),
				wn.synset("demur.v.01"),
				wn.synset("exclude.v.01"),
				wn.synset("milliampere.n.01")],

	# break, crack, fracture, tear, gap, cleft, teardrop
	"U+34c8":   [wn.synset("crack.n.01"),
				wn.synset("gap.n.01")],

	# on
	"U+34ca":   [wn.synset("on.a.01"),
				wn.synset("on.a.02"),
				wn.synset("above.r.01"),
				wn.synset("above.r.02"),
				wn.synset("along.r.01"),
				wn.synset("upstairs.r.01"),
				wn.synset("on.r.02"),
				wn.synset("on.r.03")],

	# bridge, overpass
	"U+34cb":   [wn.synset("bridge.n.01")],

	# hole
	"U+34cc":   [wn.synset("hole.n.03"),
				wn.synset("hole.n.05")],

	# maple leaf
	"U+34ce":   [wn.synset("maple-leaf.n.01")],

	# line, stripe, queue
	"U+34cf":   [wn.synset("line.n.05"),
				wn.synset("line.n.04"),
				wn.synset("lineage.n.01")],

	# screw
	"U+34d0":   [wn.synset("screw.n.04"),
				wn.synset("screw.n.03"),
				wn.synset("fuck.n.01"),
				wn.synset("screw.n.02"),
				wn.synset("prison_guard.n.01")],

	# after, behind
	"U+34d1":   [wn.synset("after.s.01"),
				wn.synset("after.r.02"),
				wn.synset("buttocks.n.01"),
				wn.synset("subsequently.r.01")],

	# between
	"U+34d2":   [wn.synset("between.r.02"),
				wn.synset("between.r.01")],

	# attach
	"U+34d3":   [wn.synset("attach.v.01")],

	# parallel
	"U+34d4":   [wn.synset("latitude.n.03")],

	# other, another
	"U+34d5":   [wn.synset("other.a.01"),
				wn.synset("other.s.02"),
				wn.synset("another.s.01")],

	# copy, duplicate
	"U+34d6":   [wn.synset("duplicate.n.02"),
				wn.synset("extra.n.03"),
				wn.synset("copy.n.02"),
				wn.synset("copy.n.03"),
				wn.synset("transcript.n.02"),
				wn.synset("copy.n.04")],

	# thin, slim, narrow
	"U+34d7":   [wn.synset("thin.a.01")],

	# deep
	"U+34d9":   [wn.synset("bass.s.01"),
				wn.synset("deep.s.05"),
				wn.synset("deep.s.02"),
				wn.synset("deep.a.01")],

	# wide, broad
	"U+34db":   [wn.synset("broad.s.03"),
				wn.synset("wide.a.01"),
				wn.synset("across-the-board.s.01")],

	# broom
	"U+34dc":   [wn.synset("broom.n.01")],

	# perpendicular
	"U+34dd":   [wn.synset("perpendicular.n.01"),
				wn.synset("perpendicular.n.02"),
				wn.synset("perpendicular.n.04"),
				wn.synset("plumb_line.n.01")],

	# beginning, start
	"U+34de":   [wn.synset("beginning.n.02")],

	# month
	"U+34e0":   [wn.synset("calendar_month.n.01")],

	# needle
	"U+34e1":   [wn.synset("needle.n.03")],

	# account
	"U+34e3":   [wn.synset("bill.n.02"),
				wn.synset("account.n.03")],

	# commandments
	"U+34e5":   [wn.synset("teaching.n.02"),
				wn.synset("commandment.n.01")],

	# chair, seat
	"U+34e7":   [wn.synset("chair.n.01")],

	# toilet
	"U+34e8":   [wn.synset("toilet.n.01")],

	# wheelchair
	"U+34e9":   [wn.synset("wheelchair.n.01")],

	# armchair
	"U+34ea":   [wn.synset("armchair.n.01")],

	# bed
	"U+34eb":   [wn.synset("bed.n.01")],

	# pillow, cushion
	"U+34ec":   [wn.synset("cushion.n.03"),
				wn.synset("pillow.n.01")],

	# bottle, flask
	"U+34ed":   [wn.synset("bottle.n.01")],

	# woman, female
	"U+34ee":   [wn.synset("woman.n.02"),
				wn.synset("woman.n.01")],

	# man, male
	"U+34f4":   [wn.synset("man.n.01")],

	# citizen
	"U+34f8":   [wn.synset("citizen.n.01")],

	# husband
	"U+34f9":   [wn.synset("husband.n.01")],

	# stepfather
	"U+34fc":   [wn.synset("stepfather.n.01")],

	# boat, ship
	"U+3500":   [wn.synset("ship.n.01")],

	# sack, bag, dismiss
	"U+3501":   [wn.synset("displace.v.03")],

	# crab, shellfish
	"U+3502":   [wn.synset("crab.n.01")],

	# ankle
	"U+3504":   [wn.synset("ankle.n.01")],

	# knee
	"U+3505":   [wn.synset("knee.n.01")],

	# menorah
	"U+3506":   [wn.synset("menorah.n.02"),
				wn.synset("menorah.n.01")],

	# near, almost, close, nearly
	"U+3508":   [wn.synset("near.a.01")],

	# far, distant
	"U+350a":   [wn.synset("far.a.01"),
				wn.synset("distant.a.01")],

	# from
	"U+350b":   [wn.synset("delaware.n.04")],

	# length, longness
	"U+350d":   [wn.synset("length.n.01"),
				wn.synset("length.n.03")],

	# measurement, measure
	"U+350e":   [wn.synset("measure.n.07"),
				wn.synset("measure.n.02"),
				wn.synset("measure.n.01")],

	# injection, inoculation, shot
	"U+350f":   [wn.synset("injection.n.03")],

	# hypodermic needle
	"U+3510":   [wn.synset("hypodermic_needle.n.01")],

	# short
	"U+3511":   [wn.synset("short.a.02")],

	# pepper
	"U+3512":   [wn.synset("capsicum.n.01"),
				wn.synset("pepper.n.01"),
				wn.synset("pepper.n.03"),
				wn.synset("pepper.n.04")],

	# it
	"U+3513":   [wn.synset("information_technology.n.01")],

	# until, till, to
	"U+3514":   [wn.synset("public_treasury.n.01"),
				wn.synset("till.n.01"),
				wn.synset("cashbox.n.01"),
				wn.synset("so_far.r.01")],

	# flag
	"U+3515":   [wn.synset("flag.n.01")],

	# country, state
	"U+3516":   [wn.synset("state_of_matter.n.01"),
				wn.synset("state.n.03"),
				wn.synset("state.n.02"),
				wn.synset("state.n.04"),
				wn.synset("country.n.02")],

	# sail
	"U+3517":   [wn.synset("sail.n.01")],

	# crown
	"U+3518":   [wn.synset("crown.n.04")],

	# shallow
	"U+3519":   [wn.synset("shallow.s.03"),
				wn.synset("shallow.a.01")],

	# fight, combat
	"U+351a":   [wn.synset("contend.v.06"),
				wn.synset("battle.v.01"),
				wn.synset("crusade.v.01"),
				wn.synset("fight.v.03"),
				wn.synset("fight.v.02")],

	# soft
	"U+351b":   [wn.synset("soft.a.01")],

	# etrog
	"U+351d":   [wn.synset("citron.n.02"),
				wn.synset("citronwood.n.01"),
				wn.synset("citron.n.01")],

	# ladder
	"U+3520":   [wn.synset("ladder.n.01")],

	# help, aid, assistance, support, assist, serve
	"U+3524":   [wn.synset("aid.n.02")],

	# sport stick
	"U+3526":   [wn.synset("cane.n.02"),
				wn.synset("cane.n.03"),
				wn.synset("walking_stick.n.02"),
				wn.synset("cane.n.01"),
				wn.synset("walking_stick.n.01"),
				wn.synset("staff.n.06"),
				wn.synset("reed.n.01"),
				wn.synset("stick.n.06"),
				wn.synset("fishing_rod.n.01"),
				wn.synset("pole.n.02"),
				wn.synset("baton.n.01")],

	# helicopter
	"U+352c":   [wn.synset("helicopter.n.01")],

	# seesaw, teeter totter, teeter board
	"U+352d":   [wn.synset("seesaw.n.01")],

	# electromagnetic radiation
	"U+352f":   [wn.synset("electromagnetic_radiation.n.01")],

	# energy
	"U+3530":   [wn.synset("energy.n.02")],

	# fuel
	"U+3531":   [wn.synset("fuel.n.01")],

	# microwave oven
	"U+3532":   [wn.synset("microwave.n.02")],

	# power, powerfulness
	"U+3533":   [wn.synset("world_power.n.01"),
				wn.synset("ability.n.02"),
				wn.synset("important_person.n.01"),
				wn.synset("exponent.n.03"),
				wn.synset("power.n.05"),
				wn.synset("baron.n.03"),
				wn.synset("power.n.01"),
				wn.synset("office.n.04"),
				wn.synset("might.n.01"),
				wn.synset("power.n.02")],

	# saw
	"U+3535":   [wn.synset("saw.n.02")],

	# tank
	"U+3537":   [wn.synset("tank.n.01")],

	# destroy, annul, cancel, cross out, delete
	"U+3538":   [wn.synset("erase.v.03")],

	# angle, right angle
	"U+3539":   [wn.synset("slant.n.01"),
				wn.synset("angle.n.03"),
				wn.synset("right_angle.n.01"),
				wn.synset("angle.n.01")],

	# cannon, gun
	"U+353a":   [wn.synset("cannon.n.01")],

	# fork
	"U+353e":   [wn.synset("fork.n.01")],

	# hammer, gavel, mallet
	"U+353f":   [wn.synset("gavel.n.01"),
				wn.synset("hammer.n.08"),
				wn.synset("hammer.n.07"),
				wn.synset("hammer.n.06"),
				wn.synset("hammer.n.05"),
				wn.synset("hammer.n.02"),
				wn.synset("hammer.n.01"),
				wn.synset("mallet.n.02"),
				wn.synset("mallet.n.03"),
				wn.synset("mallet.n.01"),
				wn.synset("malleus.n.01")],

	# the
	"U+3540":   [wn.synset("la.n.03")],

	# spoon
	"U+3543":   [wn.synset("spoon.n.01")],

	# pen, pencil
	"U+3545":   [wn.synset("pen.n.05"),
				wn.synset("pencil.n.01"),
				wn.synset("pencil.n.02"),
				wn.synset("pencil.n.03"),
				wn.synset("pen.n.01"),
				wn.synset("playpen.n.01"),
				wn.synset("pen.n.02"),
				wn.synset("pencil.n.04"),
				wn.synset("penitentiary.n.01")],

	# couch, chesterfield, sofa
	"U+3547":   [wn.synset("sofa.n.01")],

	# pitcher, jug, kettle, pot
	"U+3548":   [wn.synset("jug.n.01"),
				wn.synset("jug.n.02"),
				wn.synset("pitcher.n.02")],

	# wagon, cart, truck
	"U+3549":   [wn.synset("police_van.n.01"),
				wn.synset("tow.n.01"),
				wn.synset("beach_wagon.n.01"),
				wn.synset("truck.n.01"),
				wn.synset("wagon.n.04"),
				wn.synset("wagon.n.01"),
				wn.synset("handcart.n.01"),
				wn.synset("big_dipper.n.01"),
				wn.synset("hand_truck.n.01"),
				wn.synset("cart.n.01")],

	# hedgehog
	"U+354a":   [wn.synset("hedgehog.n.02")],

	# soup, broth
	"U+354f":   [wn.synset("soup.n.01")],

	# salad
	"U+3550":   [wn.synset("salad.n.01")],

	# dish, plate, platter
	"U+3551":   [wn.synset("plate.n.04")],

	# cereal
	"U+3552":   [wn.synset("cereal.n.01"),
				wn.synset("cereal.n.03"),
				wn.synset("grain.n.02")],

	# what, question mark
	"U+3555":   [wn.synset("central_heating.n.01"),
				wn.synset("cobalt.n.01")],

	# command, order
	"U+3557":   [wn.synset("command.v.03"),
				wn.synset("command.v.02"),
				wn.synset("command.v.01"),
				wn.synset("ordain.v.02"),
				wn.synset("regulate.v.02"),
				wn.synset("dominate.v.05"),
				wn.synset("rate.v.01"),
				wn.synset("order.v.06"),
				wn.synset("arrange.v.07"),
				wn.synset("order.v.01"),
				wn.synset("order.v.02"),
				wn.synset("order.v.03"),
				wn.synset("order.v.05"),
				wn.synset("control.v.01")],

	# comma
	"U+3559":   [wn.synset("comma.n.01")],

	# colon
	"U+355a":   [wn.synset("colon.n.05")],

	# question mark
	"U+355c":   [wn.synset("question_mark.n.01")],

	# exclamation mark
	"U+355d":   [wn.synset("exclamation_mark.n.01")],

	# zero, 0
	"U+355f":   [wn.synset("zero.n.03"),
				wn.synset("zero.n.02"),
				wn.synset("zero.n.04"),
				wn.synset("nothing.n.01")],

	# one, 1
	"U+3560":   [wn.synset("one.n.01")],

	# self, oneself, ego
	"U+3561":   [wn.synset("self.n.01")],

	# two, 2
	"U+3562":   [wn.synset("two.n.01"),
				wn.synset("deuce.n.04")],

	# three, 3
	"U+3563":   [wn.synset("three.n.01")],

	# four, 4
	"U+3564":   [wn.synset("four-spot.n.01"),
				wn.synset("four.n.01")],

	# five, 5
	"U+3565":   [wn.synset("five.n.01")],

	# six, 6
	"U+3566":   [wn.synset("six.n.01")],

	# seven, 7
	"U+3567":   [wn.synset("seven.n.01")],

	# eight, 8
	"U+3568":   [wn.synset("eight.n.01")],

	# nine, 9
	"U+3569":   [wn.synset("nine.n.01")],

	# difficult, hard, firm
	"U+3576":   [wn.synset("difficult.a.01")],

	# percent, percentage, %
	"U+3577":   [wn.synset("percentage.n.01")],

	# period, point, full stop, decimal point, tip, peak, indicate
	"U+3578":   [wn.synset("indicate.v.02")],

	# indicator
	"U+3579":   [wn.synset("indicator.n.03"),
				wn.synset("indicator.n.02")],

	# a, an, any
	"U+3583":   [wn.synset("vitamin_a.n.01"),
				wn.synset("angstrom.n.01"),
				wn.synset("associate_in_nursing.n.01"),
				wn.synset("one.n.01"),
				wn.synset("any.r.01"),
				wn.synset("any.s.01"),
				wn.synset("deoxyadenosine_monophosphate.n.01"),
				wn.synset("ampere.n.02"),
				wn.synset("a.n.07"),
				wn.synset("a.n.06"),
				wn.synset("adenine.n.01")],

	# ability, capability, capacity, potential
	"U+3584":   [wn.synset("ability.n.01")],

	# abortion
	"U+3585":   [wn.synset("abortion.n.01")],

	# miscarriage, abortion
	"U+3587":   [wn.synset("abortion.n.01"),
				wn.synset("spontaneous_abortion.n.01"),
				wn.synset("miscarriage.n.01")],

	# absorbent material, sponge
	"U+3588":   [wn.synset("sponge.n.01"),
				wn.synset("sponge.n.04")],

	# material, raw material, stuff
	"U+3589":   [wn.synset("material.n.02"),
				wn.synset("material.n.01")],

	# celibacy, chastity, abstinence
	"U+358b":   [wn.synset("celibacy.n.01")],

	# abuse, assault, violence
	"U+358f":   [wn.synset("ferocity.n.01"),
				wn.synset("assault.n.01"),
				wn.synset("assault.n.03"),
				wn.synset("assault.n.02"),
				wn.synset("maltreatment.n.01"),
				wn.synset("misuse.n.01"),
				wn.synset("rape.n.03"),
				wn.synset("abuse.n.02"),
				wn.synset("violence.n.03"),
				wn.synset("violence.n.01")],

	# accessory
	"U+3592":   [wn.synset("neckerchief.n.01"),
				wn.synset("accessory.n.02"),
				wn.synset("accessory.n.03"),
				wn.synset("accessory.n.01")],

	# accident, chance event
	"U+3594":   [wn.synset("accident.n.01")],

	# ache
	"U+3596":   [wn.synset("pain.n.03"),
				wn.synset("ache.n.01"),
				wn.synset("pain.n.02")],

	# pain, suffering
	"U+3597":   [wn.synset("pain.n.03"),
				wn.synset("pain.n.02"),
				wn.synset("pain.n.01"),
				wn.synset("suffering.n.04"),
				wn.synset("distress.n.01")],

	# acne
	"U+3599":   [wn.synset("acne.n.01")],

	# activity, male gender
	"U+359c":   [wn.synset("action.n.02"),
				wn.synset("activeness.n.02")],

	# active, actively
	"U+359d":   [wn.synset("active.a.03"),
				wn.synset("active.s.02"),
				wn.synset("active.a.05")],

	# Adar
	"U+359f":   [wn.synset("adar.n.01")],

	# add, gain
	"U+35a0":   [wn.synset("add.v.01"),
				wn.synset("add.v.02")],

	# adolescence
	"U+35a2":   [wn.synset("adolescence.n.02"),
				wn.synset("adolescence.n.01")],

	# limited time, interval, period, awhile, for a while
	"U+35a3":   [wn.synset("time_period.n.01")],

	# advance, go, depart, leave
	"U+35a5":   [wn.synset("leave.v.01"),
				wn.synset("depart.v.04"),
				wn.synset("depart.v.03"),
				wn.synset("exit.v.01"),
				wn.synset("go.v.28"),
				wn.synset("sidetrack.v.01")],

	# advertisement
	"U+35a7":   [wn.synset("ad.n.01")],

	# attention
	"U+35a9":   [wn.synset("attention.n.03"),
				wn.synset("attention.n.01"),
				wn.synset("attention.n.05")],

	# advice, counsel, recommendation
	"U+35aa":   [wn.synset("advice.n.01")],

	# suggestion, proposal
	"U+35ab":   [wn.synset("proposal.n.01"),
				wn.synset("hypnotism.n.01"),
				wn.synset("suggestion.n.01"),
				wn.synset("proposal.n.03"),
				wn.synset("suggestion.n.02"),
				wn.synset("suggestion.n.05"),
				wn.synset("suggestion.n.04"),
				wn.synset("marriage_proposal.n.01"),
				wn.synset("trace.n.01")],

	# advise, counsel, recommend
	"U+35ad":   [wn.synset("rede.v.02")],

	# afraid, frightened, scared
	"U+35ae":   [wn.synset("afraid.s.04"),
				wn.synset("afraid.a.01"),
				wn.synset("afraid.s.03"),
				wn.synset("panicky.s.01"),
				wn.synset("afraid.s.02"),
				wn.synset("frightened.s.01")],

	# fear, be afraid, dread, fright, concern
	"U+35af":   [wn.synset("fear.v.01"),
				wn.synset("fear.v.03"),
				wn.synset("fear.v.02"),
				wn.synset("reverence.v.01"),
				wn.synset("fear.v.04")],

	# afternoon
	"U+35b2":   [wn.synset("afternoon.n.01")],

	# agree
	"U+35b5":   [wn.synset("agree.v.01"),
				wn.synset("harmonize.v.01"),
				wn.synset("agree.v.07"),
				wn.synset("match.v.01"),
				wn.synset("agree.v.02"),
				wn.synset("agree.v.06"),
				wn.synset("agree.v.05")],

	# aid, device, support
	"U+35b6":   [wn.synset("documentation.n.03"),
				wn.synset("accompaniment.n.02"),
				wn.synset("support.n.02"),
				wn.synset("support.n.08"),
				wn.synset("care.n.01"),
				wn.synset("aid.n.01"),
				wn.synset("aid.n.02"),
				wn.synset("aid.n.03"),
				wn.synset("device.n.03"),
				wn.synset("support.n.04"),
				wn.synset("device.n.01"),
				wn.synset("support.n.06"),
				wn.synset("device.n.02"),
				wn.synset("device.n.05"),
				wn.synset("device.n.04"),
				wn.synset("support.n.01"),
				wn.synset("support.n.10"),
				wn.synset("support.n.11"),
				wn.synset("support.n.03"),
				wn.synset("support.n.07")],

	# airport
	"U+35b7":   [wn.synset("airport.n.01")],

	# alcoholic drink, alcoholic beverage, liquor
	"U+35b9":   [wn.synset("liquor.n.01")],

	# alligator, crocodile
	"U+35bc":   [wn.synset("crocodile.n.01")],

	# alone, just, only, solitary, fair
	"U+35bd":   [wn.synset("lonely.s.04"),
				wn.synset("just.a.01"),
				wn.synset("good.s.07"),
				wn.synset("lonely.s.02"),
				wn.synset("nongregarious.s.01"),
				wn.synset("lone.s.02"),
				wn.synset("lone.s.03"),
				wn.synset("equitable.a.01"),
				wn.synset("fair.a.01"),
				wn.synset("alone.s.04"),
				wn.synset("alone.s.01"),
				wn.synset("alone.s.02"),
				wn.synset("alone.s.03")],

	# along with
	"U+35bf":   [wn.synset("set.n.02"),
				wn.synset("ensemble.n.05"),
				wn.synset("whole.n.02"),
				wn.synset("whole.n.01"),
				wn.synset("bunch.n.01")],

	# always, ever, forever, whenever
	"U+35c2":   [wn.synset("everlastingly.r.01"),
				wn.synset("always.r.05"),
				wn.synset("constantly.r.02"),
				wn.synset("always.r.01"),
				wn.synset("ever.r.01")],

	# ambulance
	"U+35c3":   [wn.synset("ambulance.n.01")],

	# car, automobile, motor vehicle
	"U+35c4":   [wn.synset("car.n.01")],

	# amenorrhea
	"U+35c6":   [wn.synset("amenorrhea.n.01")],

	# amphibian
	"U+35c8":   [wn.synset("amphibian.n.03")],

	# earth, globe, world, ground, land
	"U+35c9":   [wn.synset("bring.v.05"),
				wn.synset("down.v.04"),
				wn.synset("land.v.02"),
				wn.synset("land.v.01"),
				wn.synset("land.v.06"),
				wn.synset("land.v.04"),
				wn.synset("land.v.05")],

	# amuse, entertain, please
	"U+35ca":   [wn.synset("please.r.01"),
				wn.synset("please.v.03"),
				wn.synset("please.v.02"),
				wn.synset("please.v.01")],

	# happiness, fun, joy, pleasure
	"U+35cc":   [wn.synset("pleasure.n.01"),
				wn.synset("pleasure.n.03"),
				wn.synset("fun.n.03"),
				wn.synset("fun.n.02"),
				wn.synset("fun.n.01"),
				wn.synset("happiness.n.01"),
				wn.synset("happiness.n.02"),
				wn.synset("pleasure.n.04"),
				wn.synset("playfulness.n.02"),
				wn.synset("joy.n.01"),
				wn.synset("joy.n.02"),
				wn.synset("pleasure.n.05")],

	# anal intercourse
	"U+35cd":   [wn.synset("sodomy.n.01")],

	# anus
	"U+35d0":   [wn.synset("anus.n.01")],

	# angry, angrily, mad
	"U+35d1":   [wn.synset("angry.a.01")],

	# deer, cervine, cervid
	"U+35d2":   [wn.synset("deer.n.01"),
				wn.synset("cervine.a.01")],

	# domestic animal
	"U+35d3":   [wn.synset("animal.n.01"),
				wn.synset("animalia.n.01"),
				wn.synset("domestic_animal.n.01")],

	# cat, feline, felid
	"U+35d4":   [wn.synset("cat.n.01")],

	# kangaroo, marsupial, pouched mammal
	"U+35d5":   [wn.synset("kangaroo.n.01")],

	# rat, rodent, gnawer, gnawing animal
	"U+35d8":   [wn.synset("rat.n.05"),
				wn.synset("informer.n.01"),
				wn.synset("rat.n.01"),
				wn.synset("rodent.n.01"),
				wn.synset("scab.n.01"),
				wn.synset("rotter.n.01")],

	# animal skin, hide, pelt, conceal
	"U+35d9":   [wn.synset("hide.v.02"),
				wn.synset("hide.v.01"),
				wn.synset("conceal.v.02")],

	# lizard, reptile
	"U+35da":   [wn.synset("lizard.n.01")],

	# open
	"U+35dc":   [wn.synset("open.s.04"),
				wn.synset("overt.a.01"),
				wn.synset("open.a.02"),
				wn.synset("open.a.01")],

	# anniversary
	"U+35de":   [wn.synset("anniversary.n.01")],

	# ant
	"U+35df":   [wn.synset("ant.n.01")],

	# intensity
	"U+35e0":   [wn.synset("intensity.n.02")],

	# anxiety
	"U+35e2":   [wn.synset("anxiety.n.02")],

	# upset, disturbance, agitation
	"U+35e3":   [wn.synset("upset.s.03"),
				wn.synset("upset.s.04"),
				wn.synset("broken.s.08"),
				wn.synset("disquieted.s.01"),
				wn.synset("overturned.s.01")],

	# anxious, anxiously
	"U+35e4":   [wn.synset("apprehensive.s.02"),
				wn.synset("anxious.s.01"),
				wn.synset("anxious.s.02"),
				wn.synset("disquieted.s.01"),
				wn.synset("troubled.a.01"),
				wn.synset("anxiously.r.01")],

	# anyone, anybody, somebody, someone
	"U+35e5":   [wn.synset("person.n.01")],

	# anything, something
	"U+35e7":   [wn.synset("some.a.01")],

	# anytime, sometime
	"U+35e9":   [wn.synset("sometime.r.01"),
				wn.synset("erstwhile.s.01")],

	# anywhere, anyplace, someplace, somewhere
	"U+35eb":   [wn.synset("somewhere.n.01"),
				wn.synset("somewhere.r.01"),
				wn.synset("anywhere.r.01")],

	# apartment, flat, unit, example, sample
	"U+35ec":   [wn.synset("flat.s.01")],

	# house, building, dwelling, residence
	"U+35ed":   [wn.synset("house.n.01")],

	# apologize, apologise, regret
	"U+35ee":   [wn.synset("sorrow.n.02"),
				wn.synset("mind.v.01"),
				wn.synset("repent.v.02"),
				wn.synset("attrition.n.03"),
				wn.synset("regret.v.04"),
				wn.synset("repentance.n.01"),
				wn.synset("regret.v.02"),
				wn.synset("regret.v.03"),
				wn.synset("dissatisfy.v.01")],

	# appointment
	"U+35f1":   [wn.synset("date.n.03")],

	# approach
	"U+35f3":   [wn.synset("approach_path.n.01"),
				wn.synset("overture.n.03"),
				wn.synset("approach.n.09"),
				wn.synset("approach.n.08"),
				wn.synset("access.n.03"),
				wn.synset("approach.n.02"),
				wn.synset("approach.n.01"),
				wn.synset("approach.n.07"),
				wn.synset("approach.n.05")],

	# approve
	"U+35f5":   [wn.synset("approve.v.01")],

	# correct, accurate, good, right
	"U+35f6":   [wn.synset("correct.a.01")],

	# apricot
	"U+35f7":   [wn.synset("yellowish_pink.n.01"),
				wn.synset("apricot.n.01"),
				wn.synset("apricot.n.02")],

	# April
	"U+35f9":   [wn.synset("april.n.01")],

	# apron, coverall, smock, overall
	"U+35fa":   [wn.synset("apron.n.01")],

	# architect
	"U+35fb":   [wn.synset("architect.n.01")],

	# argue, dispute, quarrel, row
	"U+35fe":   [wn.synset("quarrel.n.02"),
				wn.synset("quarrel.n.01"),
				wn.synset("row.n.06"),
				wn.synset("row.n.05"),
				wn.synset("row.n.03"),
				wn.synset("row.n.01"),
				wn.synset("course.n.08"),
				wn.synset("rowing.n.01")],

	# argument, dispute, quarrel
	"U+35ff":   [wn.synset("dispute.n.01"),
				wn.synset("quarrel.n.01")],

	# discussion, conversation, debate, chat
	"U+3600":   [wn.synset("discussion.n.02"),
				wn.synset("debate.n.02"),
				wn.synset("argument.n.03")],

	# military, armed forces, armed services
	"U+3601":   [wn.synset("military.n.01")],

	# group
	"U+3602":   [wn.synset("group.n.03")],

	# art
	"U+3603":   [wn.synset("art.n.02")],

	# art gallery, gallery
	"U+3605":   [wn.synset("gallery.n.03"),
				wn.synset("gallery.n.06")],

	# work of art, art object
	"U+3606":   [wn.synset("work_of_art.n.01"),
				wn.synset("objet_d'art.n.01")],

	# artificial insemination
	"U+3607":   [wn.synset("artificial_insemination.n.01")],

	# medical, medically
	"U+3608":   [wn.synset("medical.a.01")],

	# artificial respiration
	"U+360a":   [wn.synset("artificial_respiration.n.01")],

	# give artificial respiration, resuscitate, revive
	"U+360c":   [wn.synset("revive.v.04"),
				wn.synset("come_to.v.04")],

	# ashes
	"U+360d":   [wn.synset("ash.n.01")],

	# ashtray
	"U+360f":   [wn.synset("ashtray.n.01")],

	# ask, inquire, question
	"U+3611":   [wn.synset("ask.v.01")],

	# asleep
	"U+3612":   [wn.synset("asleep.s.03"),
				wn.synset("sleepy.s.01"),
				wn.synset("asleep.s.02"),
				wn.synset("asleep.a.01")],

	# astronaut, cosmonaut
	"U+3613":   [wn.synset("astronaut.n.01")],

	# attack
	"U+3614":   [wn.synset("fire.n.09"),
				wn.synset("attack.n.09"),
				wn.synset("attack.n.08"),
				wn.synset("attack.n.05"),
				wn.synset("approach.n.01"),
				wn.synset("attack.n.06"),
				wn.synset("attack.n.01"),
				wn.synset("attack.n.07"),
				wn.synset("attack.n.02")],

	# August
	"U+3617":   [wn.synset("august.n.01")],

	# autumn, fall, drop, spill, tumble, slop
	"U+3618":   [wn.synset("fall.v.01")],

	# down, downward
	"U+3619":   [wn.synset("down.r.01")],

	# Av
	"U+361a":   [wn.synset("ab.n.02")],

	# church ruin, temple ruin, wreck, wreckage, temple, mosque)
	"U+361b":   [wn.synset("wreck.n.04"),
				wn.synset("shipwreck.n.03"),
				wn.synset("temple.n.01"),
				wn.synset("temple.n.02"),
				wn.synset("wreck.n.01"),
				wn.synset("wreckage.n.01"),
				wn.synset("crash.n.02"),
				wn.synset("synagogue.n.01"),
				wn.synset("temple.n.03")],

	# wreck, wreckage
	"U+361d":   [wn.synset("crash.n.02"),
				wn.synset("wreck.n.04"),
				wn.synset("wreckage.n.01"),
				wn.synset("shipwreck.n.03"),
				wn.synset("wreck.n.01")],

	# wakefulness, alertness
	"U+3621":   [wn.synset("alertness.n.02"),
				wn.synset("watchfulness.n.01"),
				wn.synset("wakefulness.n.02"),
				wn.synset("alertness.n.03"),
				wn.synset("wakefulness.n.01")],

	# baby carriage, buggy, pram, pushchair, stroller
	"U+3623":   [wn.synset("baby_buggy.n.01")],

	# clinic
	"U+3625":   [wn.synset("clinic.n.01")],

	# babysitter
	"U+3627":   [wn.synset("babysitter.n.01")],

	# back
	"U+3629":   [wn.synset("back.n.08"),
				wn.synset("back.n.09"),
				wn.synset("rear.n.05"),
				wn.synset("back.n.07"),
				wn.synset("back.n.01"),
				wn.synset("back.n.03"),
				wn.synset("back.n.04"),
				wn.synset("binding.n.05"),
				wn.synset("spinal_column.n.01")],

	# backpack, rucksack
	"U+362b":   [wn.synset("backpack.n.01")],

	# back up
	"U+362d":   [wn.synset("back_up.v.04"),
				wn.synset("back_up.v.02"),
				wn.synset("clog.v.01"),
				wn.synset("support.v.01"),
				wn.synset("rescue.n.01"),
				wn.synset("back.v.09")],

	# bacon
	"U+362e":   [wn.synset("bacon.n.01")],

	# pork, ham
	"U+362f":   [wn.synset("pork.n.01"),
				wn.synset("pork_barrel.n.01"),
				wn.synset("ham.n.01"),
				wn.synset("ham.n.02"),
				wn.synset("ham.n.03"),
				wn.synset("ham.n.04")],

	# linear thing, pole, bar
	"U+3630":   [wn.synset("bar.n.07"),
				wn.synset("barroom.n.01")],

	# badminton
	"U+3632":   [wn.synset("badminton.n.01")],

	# shuttlecock, birdie
	"U+3633":   [wn.synset("shuttlecock.n.01"),
				wn.synset("birdie.n.01")],

	# baggage, bag, luggage, suitcase
	"U+3634":   [wn.synset("bag.n.06"),
				wn.synset("baggage.n.01")],

	# bake, cook, roast, chef, joint
	"U+3635":   [wn.synset("crematory.n.02"),
				wn.synset("roast.v.01"),
				wn.synset("fudge.v.01"),
				wn.synset("bake.v.02"),
				wn.synset("bake.v.01"),
				wn.synset("broil.v.02"),
				wn.synset("bake.v.04"),
				wn.synset("ridicule.v.01"),
				wn.synset("furnace.n.01"),
				wn.synset("cook.v.05"),
				wn.synset("stove.n.02"),
				wn.synset("cook.v.03"),
				wn.synset("cook.v.02"),
				wn.synset("cook.v.01")],

	# balcony, porch, veranda
	"U+3637":   [wn.synset("balcony.n.02")],

	# bandage, dressing
	"U+3639":   [wn.synset("bandage.n.01")],

	# bank
	"U+363b":   [wn.synset("depository_financial_institution.n.01")],

	# bar, pub, cake
	"U+363d":   [wn.synset("measure.n.07"),
				wn.synset("browning_automatic_rifle.n.01"),
				wn.synset("prevention.n.01"),
				wn.synset("bar.n.07"),
				wn.synset("barroom.n.01"),
				wn.synset("bar.n.03"),
				wn.synset("bar.n.02"),
				wn.synset("bar.n.13"),
				wn.synset("bar.n.14"),
				wn.synset("bar.n.15"),
				wn.synset("legal_profession.n.01"),
				wn.synset("sweet.n.03"),
				wn.synset("bar.n.05"),
				wn.synset("bar.n.08"),
				wn.synset("patty.n.01"),
				wn.synset("cake.n.03"),
				wn.synset("cake.n.01"),
				wn.synset("stripe.n.05")],

	# barber, hairdresser
	"U+363f":   [wn.synset("barber.n.02")],

	# barbershop, beauty shop
	"U+3641":   [wn.synset("barbershop.n.01")],

	# barn, stable, shed
	"U+3642":   [wn.synset("stable.n.01")],

	# barrier
	"U+3643":   [wn.synset("barrier.n.03")],

	# baseball
	"U+3645":   [wn.synset("baseball.n.01")],

	# base camp
	"U+3646":   [wn.synset("base.n.14")],

	# basketball
	"U+3648":   [wn.synset("basketball.n.01")],

	# bathroom, washroom
	"U+3649":   [wn.synset("bathroom.n.01")],

	# battery
	"U+364b":   [wn.synset("battery.n.01")],

	# beach, bank, coast, shore
	"U+364d":   [wn.synset("beach.n.01")],

	# bear's head
	"U+364e":   [wn.synset("bear.n.01")],

	# beautiful, attractive, good looking, handsome, pretty
	"U+364f":   [wn.synset("beautiful.a.01")],

	# beauty
	"U+3650":   [wn.synset("beauty.n.01")],

	# become
	"U+3652":   [wn.synset("become.v.01"),
				wn.synset("become.v.02")],

	# bedroom
	"U+3654":   [wn.synset("bedroom.n.01")],

	# bee
	"U+3657":   [wn.synset("bee.n.01")],

	# beef
	"U+3658":   [wn.synset("beef.n.02")],

	# beer
	"U+3659":   [wn.synset("beer.n.01")],

	# beet
	"U+365a":   [wn.synset("beet.n.02"),
				wn.synset("beet.n.01")],

	# vegetable
	"U+365b":   [wn.synset("vegetable.n.02"),
				wn.synset("vegetable.n.01"),
				wn.synset("salad.n.01")],

	# red
	"U+365c":   [wn.synset("red.n.01")],

	# begin, start
	"U+365d":   [wn.synset("begin.v.03")],

	# behaviour
	"U+365e":   [wn.synset("demeanor.n.01"),
				wn.synset("behavior.n.01"),
				wn.synset("behavior.n.02")],

	# creature, being
	"U+365f":   [wn.synset("animal.n.01"),
				wn.synset("being.n.01"),
				wn.synset("creature.n.02")],

	# belief
	"U+3660":   [wn.synset("faith.n.02"),
				wn.synset("belief.n.01"),
				wn.synset("impression.n.01"),
				wn.synset("fidelity.n.02"),
				wn.synset("confidence.n.02"),
				wn.synset("religion.n.01"),
				wn.synset("religion.n.02"),
				wn.synset("wedding_ring.n.01")],

	# hypothesis, theory
	"U+3661":   [wn.synset("guess.n.01"),
				wn.synset("hypothesis.n.02")],

	# believe
	"U+3663":   [wn.synset("think.v.01"),
				wn.synset("believe.v.01"),
				wn.synset("believe.v.05")],

	# bell, chime bar
	"U+3664":   [wn.synset("doorbell.n.01")],

	# belt, sash
	"U+3665":   [wn.synset("belt.n.02")],

	# bench, pew
	"U+3666":   [wn.synset("judiciary.n.01"),
				wn.synset("workbench.n.01"),
				wn.synset("terrace.n.02"),
				wn.synset("pew.n.01"),
				wn.synset("bench.n.06"),
				wn.synset("bench.n.07"),
				wn.synset("bench.n.05"),
				wn.synset("bench.n.01")],

	# seat, sitting
	"U+3667":   [wn.synset("seat.n.03")],

	# best
	"U+3669":   [wn.synset("adept.s.01"),
				wn.synset("estimable.s.02"),
				wn.synset("good.a.03"),
				wn.synset("good.a.01"),
				wn.synset("effective.s.04"),
				wn.synset("beneficial.s.01"),
				wn.synset("good.s.06"),
				wn.synset("dependable.s.04"),
				wn.synset("good.s.15"),
				wn.synset("best.a.01"),
				wn.synset("good.s.12"),
				wn.synset("good.s.13"),
				wn.synset("good.s.16"),
				wn.synset("good.s.17"),
				wn.synset("good.s.21"),
				wn.synset("full.s.06"),
				wn.synset("good.s.09"),
				wn.synset("good.s.18"),
				wn.synset("good.s.19"),
				wn.synset("good.s.07"),
				wn.synset("good.s.20"),
				wn.synset("better.s.03"),
				wn.synset("dear.s.02")],

	# better
	"U+366a":   [wn.synset("better.a.01")],

	# bib
	"U+366b":   [wn.synset("bib.n.02")],

	# bicycle
	"U+366c":   [wn.synset("bicycle.n.01")],

	# big, large
	"U+366d":   [wn.synset("large.a.01")],

	# bigness, largeness
	"U+366e":   [wn.synset("pretentiousness.n.02"),
				wn.synset("breadth.n.01"),
				wn.synset("largeness.n.02"),
				wn.synset("largeness.n.03")],

	# bindi, tika
	"U+3670":   [wn.synset("bandage.n.01"),
				wn.synset("tie.n.07")],

	# duck, bird, waterbird, waterfowl, seabird, seafowl
	"U+3671":   [wn.synset("duck.n.01")],

	# fetus
	"U+3673":   [wn.synset("fetus.n.01")],

	# birth control
	"U+3675":   [wn.synset("birth_control.n.01"),
				wn.synset("contraception.n.01")],

	# birth control pill, pill, tablet
	"U+3677":   [wn.synset("pill.n.01"),
				wn.synset("pill.n.02")],

	# birthday
	"U+3678":   [wn.synset("birthday.n.01")],

	# bite
	"U+3679":   [wn.synset("bite.v.01")],

	# bitter
	"U+367a":   [wn.synset("bitter.s.04"),
				wn.synset("bitter.s.05"),
				wn.synset("bitter.s.06"),
				wn.synset("acrimonious.s.01"),
				wn.synset("bitter.s.02"),
				wn.synset("acerb.s.02"),
				wn.synset("biting.s.02")],

	# black
	"U+367b":   [wn.synset("black.n.01")],

	# blackbird, crow, raven
	"U+367d":   [wn.synset("blackbird.n.02")],

	# blackboard, chalkboard, whiteboard, writing board
	"U+3680":   [wn.synset("blackboard.n.01")],

	# bladder
	"U+3682":   [wn.synset("bladder.n.01"),
				wn.synset("bladder.n.02")],

	# blanket, duvet, quilt
	"U+3684":   [wn.synset("blanket.n.01")],

	# bleed
	"U+3686":   [wn.synset("shed_blood.v.02")],

	# blindness
	"U+3688":   [wn.synset("blindness.n.01")],

	# blood
	"U+368d":   [wn.synset("blood.n.01")],

	# liquid
	"U+368e":   [wn.synset("liquid.n.01"),
				wn.synset("liquid.n.03")],

	# blow
	"U+368f":   [wn.synset("blow.v.01")],

	# blue
	"U+3690":   [wn.synset("blue.n.07"),
				wn.synset("amobarbital_sodium.n.01"),
				wn.synset("blue.n.03"),
				wn.synset("bluing.n.01"),
				wn.synset("blue_sky.n.01"),
				wn.synset("blue.n.02"),
				wn.synset("blue.n.01")],

	# blueberry
	"U+3693":   [wn.synset("blueberry.n.01"),
				wn.synset("blueberry.n.02"),
				wn.synset("bilberry.n.03")],

	# bluebird
	"U+3695":   [wn.synset("buffalo_clover.n.02"),
				wn.synset("fairy_bluebird.n.01"),
				wn.synset("bluebird.n.02")],

	# boil
	"U+3696":   [wn.synset("churn.v.02"),
				wn.synset("boil.v.01"),
				wn.synset("seethe.v.02"),
				wn.synset("boil.v.03"),
				wn.synset("boil.v.02")],

	# bonfire, barbeque, campfire
	"U+3697":   [wn.synset("bonfire.n.01"),
				wn.synset("barbecue.n.01"),
				wn.synset("barbecue.n.02"),
				wn.synset("barbecue.n.03"),
				wn.synset("campfire.n.01")],

	# boot, trunk, roof box, luggage compartment
	"U+3698":   [wn.synset("luggage_compartment.n.01")],

	# borrow
	"U+369a":   [wn.synset("adopt.v.02"),
				wn.synset("lend.v.02"),
				wn.synset("borrow.v.01")],

	# both
	"U+369c":   [wn.synset("both.s.01")],

	# bowel movement, defecation, shitting, feces, shit, poop
	"U+369d":   [wn.synset("defecation.n.01")],

	# bowling
	"U+369e":   [wn.synset("bowling.n.02"),
				wn.synset("bowling.n.03"),
				wn.synset("bowling.n.01")],

	# ball field
	"U+369f":   [wn.synset("ball_field.n.01")],

	# boxing
	"U+36a0":   [wn.synset("boxing.n.01")],

	# bra, brassiere
	"U+36a2":   [wn.synset("brassiere.n.01")],

	# medical aid
	"U+36a4":   [wn.synset("medical_care.n.01")],

	# bracha, berakah, prayer
	"U+36a6":   [wn.synset("entreaty.n.01"),
				wn.synset("prayer.n.05"),
				wn.synset("prayer.n.02"),
				wn.synset("prayer.n.04"),
				wn.synset("prayer.n.01")],

	# little, small
	"U+36a7":   [wn.synset("little.s.03"),
				wn.synset("small.a.01"),
				wn.synset("minor.s.10")],

	# Brahma
	"U+36a8":   [wn.synset("brahma.n.01")],

	# brain
	"U+36a9":   [wn.synset("brain.n.01")],

	# breakable, fragile
	"U+36ab":   [wn.synset("delicate.s.03")],

	# breakfast
	"U+36ad":   [wn.synset("breakfast.n.01")],

	# meal
	"U+36ae":   [wn.synset("meal.n.01")],

	# breath
	"U+36af":   [wn.synset("breath.n.02"),
				wn.synset("breath.n.01")],

	# breathe
	"U+36b0":   [wn.synset("breathe.v.01")],

	# bright
	"U+36b2":   [wn.synset("bright.s.02"),
				wn.synset("bright.s.03"),
				wn.synset("bright.s.06"),
				wn.synset("bright.s.04"),
				wn.synset("bright.s.05"),
				wn.synset("bright.a.01"),
				wn.synset("bright.s.08"),
				wn.synset("bright.s.09"),
				wn.synset("bright.s.10"),
				wn.synset("undimmed.a.01")],

	# bring
	"U+36b3":   [wn.synset("bring.v.01")],

	# broccoli
	"U+36b5":   [wn.synset("broccoli.n.02")],

	# green
	"U+36b6":   [wn.synset("green.n.01")],

	# broil, barbecue, grill
	"U+36b7":   [wn.synset("grill.v.01"),
				wn.synset("grill.v.02"),
				wn.synset("bake.v.04"),
				wn.synset("broil.v.01"),
				wn.synset("broil.v.02"),
				wn.synset("barbeque.v.01")],

	# broken
	"U+36b8":   [wn.synset("broken.a.01")],

	# brother
	"U+36bb":   [wn.synset("brother.n.01")],

	# brown
	"U+36bc":   [wn.synset("brown.s.01")],

	# toothbrush
	"U+36c0":   [wn.synset("toothbrush.n.01")],

	# brussels sprout
	"U+36c1":   [wn.synset("brussels_sprout.n.01")],

	# buffalo, bison
	"U+36c3":   [wn.synset("american_bison.n.01")],

	# bull
	"U+36c4":   [wn.synset("bull.n.06"),
				wn.synset("bull.n.01")],

	# burn
	"U+36c7":   [wn.synset("burn_off.v.01"),
				wn.synset("burn.v.01"),
				wn.synset("burn.v.15")],

	# burned, burnt
	"U+36c8":   [wn.synset("burned.s.01")],

	# burning
	"U+36c9":   [wn.synset("burning.s.01")],

	# burp, belch
	"U+36ca":   [wn.synset("burp.v.01")],

	# bury
	"U+36cc":   [wn.synset("bury.v.02")],

	# bus driver
	"U+36cd":   [wn.synset("busman.n.01")],

	# bush, shrub
	"U+36cf":   [wn.synset("shrub.n.01")],

	# business, economy, commerce, trade
	"U+36d0":   [wn.synset("commerce.n.03"),
				wn.synset("trade.n.02"),
				wn.synset("trade.n.01")],

	# butter
	"U+36d1":   [wn.synset("butter.n.01")],

	# cream
	"U+36d2":   [wn.synset("cream.n.03"),
				wn.synset("cream.n.01")],

	# button, gripper, snap
	"U+36d3":   [wn.synset("button.n.01")],

	# disc, disk
	"U+36d4":   [wn.synset("disk.n.01")],

	# buy, purchase
	"U+36d6":   [wn.synset("buy.v.01")],

	# by, by means of, of
	"U+36d7":   [wn.synset("by.r.01")],

	# cabin, cottage, hut
	"U+36d8":   [wn.synset("hovel.n.01"),
				wn.synset("bungalow.n.01"),
				wn.synset("cabin.n.01"),
				wn.synset("cabin.n.03"),
				wn.synset("cabin.n.02"),
				wn.synset("hut.n.01")],

	# caesarean section, C section
	"U+36d9":   [wn.synset("cesarean_delivery.n.01")],

	# cafe, coffee house, snack bar
	"U+36dc":   [wn.synset("cafe.n.01")],

	# cage
	"U+36de":   [wn.synset("cage.n.03"),
				wn.synset("cage.n.02"),
				wn.synset("cage.n.01"),
				wn.synset("batting_cage.n.01"),
				wn.synset("cage.n.04")],

	# cake, bread with sugar
	"U+36e0":   [wn.synset("cake.n.03")],

	# digits
	"U+36e3":   [wn.synset("digit.n.01"),
				wn.synset("digit.n.03")],

	# calculator
	"U+36e4":   [wn.synset("calculator.n.02")],

	# calendar
	"U+36e6":   [wn.synset("calendar.n.01")],

	# camp
	"U+36e8":   [wn.synset("camp.n.08"),
				wn.synset("camp.n.02"),
				wn.synset("camp.n.03"),
				wn.synset("camp.n.01"),
				wn.synset("camp.n.06"),
				wn.synset("camp.n.07"),
				wn.synset("camp.n.05")],

	# camper, caravan, mobile home
	"U+36e9":   [wn.synset("van.n.04")],

	# can, be able, tin, jar
	"U+36ea":   [wn.synset("can.n.01")],

	# cylinder, can
	"U+36eb":   [wn.synset("can.n.01")],

	# Canada
	"U+36ec":   [wn.synset("canada.n.01")],

	# candle
	"U+36ee":   [wn.synset("candle.n.01")],

	# cane, stick, walking stick, log
	"U+36ef":   [wn.synset("stick.n.07")],

	# cards, playing cards
	"U+36f1":   [wn.synset("card_game.n.01"),
				wn.synset("playing_card.n.01")],

	# careful
	"U+36f4":   [wn.synset("careful.s.05"),
				wn.synset("careful.s.04"),
				wn.synset("careful.s.03"),
				wn.synset("careful.a.01"),
				wn.synset("careful.s.02")],

	# observation
	"U+36f5":   [wn.synset("observation.n.02")],

	# carry, move, transport, movement
	"U+36f6":   [wn.synset("transport.v.02")],

	# carrycot, bassinet
	"U+36f8":   [wn.synset("carrycot.n.01")],

	# cassette, audiocassette, videocassette
	"U+36f9":   [wn.synset("cassette.n.01")],

	# cast
	"U+36fa":   [wn.synset("cast.n.05")],

	# catch, grab
	"U+36fb":   [wn.synset("get.v.11"),
				wn.synset("catch.v.04")],

	# caterpillar
	"U+36fc":   [wn.synset("caterpillar.n.01")],

	# cauliflower
	"U+36fd":   [wn.synset("cauliflower.n.02")],

	# be caused by
	"U+36fe":   [wn.synset("be_due.v.01"),
				wn.synset("derive.v.03"),
				wn.synset("derive.v.04"),
				wn.synset("derive.v.05")],

	# cave
	"U+3700":   [wn.synset("cave.n.01")],

	# cemetery
	"U+3701":   [wn.synset("cemetery.n.01")],

	# cent
	"U+3703":   [wn.synset("cent.n.01")],

	# century
	"U+3704":   [wn.synset("century.n.01")],

	# cervix
	"U+3706":   [wn.synset("cervix.n.02")],

	# challah
	"U+3709":   [wn.synset("challah.n.01")],

	# Sabbath, day of rest
	"U+370a":   [wn.synset("sabbath.n.01")],

	# chameleon
	"U+370b":   [wn.synset("chameleon.n.03")],

	# Chanukah, Hanukkah
	"U+370d":   [wn.synset("hanukkah.n.01")],

	# holiday, festival
	"U+370e":   [wn.synset("holiday.n.02"),
				wn.synset("vacation.n.01"),
				wn.synset("festival.n.01"),
				wn.synset("festival.n.02")],

	# charity
	"U+370f":   [wn.synset("charity.n.02"),
				wn.synset("charity.n.03")],

	# Cheshvan
	"U+3713":   [wn.synset("heshvan.n.01")],

	# chew
	"U+3715":   [wn.synset("chew.v.01")],

	# chicken, poultry
	"U+3717":   [wn.synset("chicken.n.04"),
				wn.synset("chicken.n.01"),
				wn.synset("chicken.n.02")],

	# child abuse
	"U+3719":   [wn.synset("child_abuse.n.01"),
				wn.synset("maltreatment.n.01"),
				wn.synset("exploitation.n.02"),
				wn.synset("manipulation.n.01")],

	# chipmunk
	"U+371c":   [wn.synset("chipmunk.n.01")],

	# choir, chorus
	"U+371f":   [wn.synset("choir.n.03"),
				wn.synset("choir.n.02"),
				wn.synset("choir.n.01"),
				wn.synset("chorus.n.02"),
				wn.synset("chorus.n.01"),
				wn.synset("chorus.n.05"),
				wn.synset("chorus.n.04")],

	# choke, gag
	"U+3721":   [wn.synset("suffocate.v.02"),
				wn.synset("suffocate.v.03"),
				wn.synset("suffocate.v.04"),
				wn.synset("choke.v.01"),
				wn.synset("choke.v.02"),
				wn.synset("choke.v.03"),
				wn.synset("choke.v.04"),
				wn.synset("choke.v.06"),
				wn.synset("choke.v.07"),
				wn.synset("gag.v.07"),
				wn.synset("gag.v.06"),
				wn.synset("gag.v.05"),
				wn.synset("gag.v.04"),
				wn.synset("gag.v.03"),
				wn.synset("gag.v.01"),
				wn.synset("choke.v.13")],

	# choose, pick, select
	"U+3723":   [wn.synset("choose.v.01")],

	# chop
	"U+3724":   [wn.synset("chop.v.06"),
				wn.synset("chop.v.05"),
				wn.synset("chop.v.04"),
				wn.synset("chop.v.03"),
				wn.synset("chop.v.02"),
				wn.synset("chop.v.01")],

	# christian
	"U+3726":   [wn.synset("christian.a.01")],

	# Christmas
	"U+3727":   [wn.synset("christmas.n.02")],

	# Chumash, Pentateuch
	"U+3729":   [wn.synset("torah.n.02")],

	# Torah
	"U+372a":   [wn.synset("torah.n.03")],

	# church, mosque, temple
	"U+372b":   [wn.synset("church.n.02")],

	# God
	"U+372c":   [wn.synset("deity.n.01")],

	# circle
	"U+372e":   [wn.synset("circle.n.01")],

	# shape, form
	"U+372f":   [wn.synset("shape.n.01"),
				wn.synset("form.n.03")],

	# circumcision
	"U+3731":   [wn.synset("circumcision.n.03"),
				wn.synset("circumcision.n.02")],

	# town, city, metropolis
	"U+3733":   [wn.synset("city.n.01")],

	# class
	"U+3734":   [wn.synset("class.n.08"),
				wn.synset("class.n.01"),
				wn.synset("class.n.02"),
				wn.synset("class.n.03"),
				wn.synset("class.n.07")],

	# classroom
	"U+3736":   [wn.synset("classroom.n.01")],

	# clean
	"U+3739":   [wn.synset("clean.v.01"),
				wn.synset("clean.v.02")],

	# dirty, soiled
	"U+373a":   [wn.synset("dirty.a.01")],

	# clear, transparent
	"U+373b":   [wn.synset("clean.s.03")],

	# clearness, clarity, transparency, transparence
	"U+373c":   [wn.synset("clarity.n.01"),
				wn.synset("clearness.n.02")],

	# clerk, legal aid
	"U+3740":   [wn.synset("clerk.n.01"),
				wn.synset("salesclerk.n.01")],

	# helper, aide, assistant, personal assistant
	"U+3741":   [wn.synset("assistant.n.01")],

	# climb
	"U+3742":   [wn.synset("rise.v.02"),
				wn.synset("climb.v.01")],

	# up, upward
	"U+3743":   [wn.synset("up.r.01")],

	# clitoris
	"U+3744":   [wn.synset("clitoris.n.01")],

	# clock, timepiece
	"U+3746":   [wn.synset("clock.n.01")],

	# close, enclose, shut
	"U+3747":   [wn.synset("close.v.01")],

	# cloudy
	"U+3748":   [wn.synset("cloudy.a.02")],

	# club
	"U+3749":   [wn.synset("clubhouse.n.01"),
				wn.synset("club.n.02")],

	# biomass, biofuel
	"U+374a":   [wn.synset("biomass.n.01"),
				wn.synset("biomass.n.02")],

	# coat, jacket, jumper, sweater
	"U+374b":   [wn.synset("coat.n.01"),
				wn.synset("jacket.n.01")],

	# coconut
	"U+374c":   [wn.synset("coconut.n.01"),
				wn.synset("coconut.n.03"),
				wn.synset("coconut.n.02")],

	# coffee
	"U+374e":   [wn.synset("coffee.n.01")],

	# drink, beverage
	"U+374f":   [wn.synset("beverage.n.01")],

	# coin
	"U+3750":   [wn.synset("coin.n.01")],

	# coldness, cold
	"U+3751":   [wn.synset("coldness.n.03")],

	# opposite meaning, opposite of, opposite
	"U+3753":   [wn.synset("inverse.n.01")],

	# hot, spicy, peppery
	"U+3754":   [wn.synset("hot.s.20"),
				wn.synset("hot.s.21"),
				wn.synset("piquant.s.01"),
				wn.synset("hot.s.13"),
				wn.synset("hot.s.15"),
				wn.synset("blue.s.05"),
				wn.synset("blistering.s.03"),
				wn.synset("peppery.s.01"),
				wn.synset("hot.a.01"),
				wn.synset("hot.a.03"),
				wn.synset("hot.s.11"),
				wn.synset("hot.s.12"),
				wn.synset("hot.s.08"),
				wn.synset("hot.s.09"),
				wn.synset("hot.s.19"),
				wn.synset("hot.s.18"),
				wn.synset("hot.s.02"),
				wn.synset("hot.s.14"),
				wn.synset("hot.s.17"),
				wn.synset("hot.s.16"),
				wn.synset("hot.s.06"),
				wn.synset("hot.s.10"),
				wn.synset("hot.s.04"),
				wn.synset("hot.s.05")],

	# combine, connect, link
	"U+3755":   [wn.synset("compound.v.02")],

	# come, approach
	"U+3756":   [wn.synset("come.v.03"),
				wn.synset("come.v.01")],

	# comfortable, restful
	"U+3757":   [wn.synset("comfortable.a.02"),
				wn.synset("comfortable.a.01"),
				wn.synset("pleasant.a.01"),
				wn.synset("restful.a.01"),
				wn.synset("comfortable.s.03"),
				wn.synset("comfortable.s.05"),
				wn.synset("comfortable.s.04")],

	# rest, comfort
	"U+3758":   [wn.synset("respite.n.04"),
				wn.synset("rest.n.02")],

	# communicate
	"U+3759":   [wn.synset("communicate.v.02"),
				wn.synset("communicate.v.01"),
				wn.synset("communicate.v.04")],

	# communication
	"U+375a":   [wn.synset("communication.n.01"),
				wn.synset("communication.n.02"),
				wn.synset("communication.n.03")],

	# compare
	"U+375c":   [wn.synset("compare.v.01")],

	# compete, race
	"U+375e":   [wn.synset("compete.v.01")],

	# composer
	"U+375f":   [wn.synset("composer.n.01")],

	# tune, melody
	"U+3760":   [wn.synset("melody.n.02"),
				wn.synset("tune.n.01"),
				wn.synset("tune.n.03"),
				wn.synset("tune.n.02")],

	# conception, fertilization, fertilized egg
	"U+3761":   [wn.synset("conception.n.02")],

	# concert hall
	"U+3762":   [wn.synset("concert_hall.n.01")],

	# music
	"U+3763":   [wn.synset("music.n.01")],

	# concrete, cement
	"U+3764":   [wn.synset("concrete.n.01")],

	# condom
	"U+3765":   [wn.synset("condom.n.01")],

	# considerate, thoughtful
	"U+3766":   [wn.synset("heedful.a.01"),
				wn.synset("considerate.a.01")],

	# continuance, continuation
	"U+3769":   [wn.synset("lengthiness.n.02"),
				wn.synset("sequel.n.02"),
				wn.synset("duration.n.01"),
				wn.synset("good_continuation.n.01"),
				wn.synset("duration.n.02"),
				wn.synset("continuance.n.01")],

	# uterine contraction
	"U+376b":   [wn.synset("uterine_contraction.n.01"),
				wn.synset("cutback.n.01"),
				wn.synset("contraction.n.04")],

	# contrast
	"U+376c":   [wn.synset("contrast.v.01"),
				wn.synset("contrast.v.02")],

	# control oneself
	"U+376d":   [wn.synset("get_the_better_of.v.01"),
				wn.synset("check.v.22"),
				wn.synset("excel.v.01"),
				wn.synset("exceed.v.02"),
				wn.synset("outshine.v.02"),
				wn.synset("outclass.v.01"),
				wn.synset("outdo.v.02"),
				wn.synset("manipulate.v.05"),
				wn.synset("operate.v.03"),
				wn.synset("prevail.v.04"),
				wn.synset("see.v.10"),
				wn.synset("exceed.v.01"),
				wn.synset("dominate.v.02"),
				wn.synset("dominate.v.03"),
				wn.synset("administer.v.01"),
				wn.synset("surpass.v.02"),
				wn.synset("dominate.v.05"),
				wn.synset("prevail.v.03"),
				wn.synset("monitor.v.01"),
				wn.synset("predominate.v.01"),
				wn.synset("check.v.08"),
				wn.synset("govern.v.03"),
				wn.synset("outwit.v.01"),
				wn.synset("check.v.19"),
				wn.synset("control.v.06"),
				wn.synset("control.v.05"),
				wn.synset("master.v.04"),
				wn.synset("control.v.02"),
				wn.synset("control.v.01"),
				wn.synset("outpoint.v.02")],

	# cookie, biscuit
	"U+376f":   [wn.synset("cookie.n.03")],

	# sweet, confection
	"U+3770":   [wn.synset("sweet.a.01"),
				wn.synset("gratifying.s.01"),
				wn.synset("fresh.s.09"),
				wn.synset("sweet.a.07"),
				wn.synset("sugared.s.01"),
				wn.synset("dulcet.s.02"),
				wn.synset("odoriferous.s.03"),
				wn.synset("angelic.s.03"),
				wn.synset("fresh.a.06"),
				wn.synset("sweet.s.04")],

	# cool, chilly
	"U+3771":   [wn.synset("cool.a.03"),
				wn.synset("cool.a.01"),
				wn.synset("cool.a.04"),
				wn.synset("cool.s.05"),
				wn.synset("cool.s.06"),
				wn.synset("cool.s.02"),
				wn.synset("chilly.s.03"),
				wn.synset("chilly.s.02"),
				wn.synset("chilly.s.01")],

	# warm
	"U+3772":   [wn.synset("warm.a.01")],

	# cornmeal
	"U+3774":   [wn.synset("cornmeal.n.01")],

	# positive
	"U+3776":   [wn.synset("positive.a.01"),
				wn.synset("positive.n.01"),
				wn.synset("positive.n.02")],

	# cost, price
	"U+3777":   [wn.synset("cost.v.02"),
				wn.synset("cost.v.01")],

	# for, in order to
	"U+3778":   [wn.synset("by.r.01")],

	# costume, disguise
	"U+3779":   [wn.synset("costume.n.01"),
				wn.synset("costume.n.04")],

	# cough
	"U+377b":   [wn.synset("cough.v.01")],

	# counsellor, adviser
	"U+377d":   [wn.synset("adviser.n.01")],

	# count
	"U+377f":   [wn.synset("count.n.02")],

	# couple
	"U+3780":   [wn.synset("couple.n.05"),
				wn.synset("couple.n.01"),
				wn.synset("couple.n.02")],

	# family, couple
	"U+3781":   [wn.synset("class.n.01"),
				wn.synset("family.n.08"),
				wn.synset("syndicate.n.01"),
				wn.synset("family.n.01"),
				wn.synset("kin.n.01"),
				wn.synset("family.n.02"),
				wn.synset("family.n.04"),
				wn.synset("family.n.06")],

	# cousin
	"U+3782":   [wn.synset("cousin.n.01")],

	# sibling
	"U+3783":   [wn.synset("sibling.n.01")],

	# cow
	"U+3784":   [wn.synset("cow.n.01")],

	# craft
	"U+3786":   [wn.synset("trade.n.02")],

	# cramp, spasm
	"U+3787":   [wn.synset("spasm.n.01")],

	# cranberry
	"U+3788":   [wn.synset("cranberry.n.02")],

	# crane
	"U+378a":   [wn.synset("crane.n.04")],

	# up and down
	"U+378b":   [wn.synset("up_and_down.r.02"),
				wn.synset("up_and_down.r.01")],

	# bump, press, pressing
	"U+378f":   [wn.synset("compress.v.02"),
				wn.synset("crusade.v.01"),
				wn.synset("press.v.07"),
				wn.synset("weight-lift.v.01"),
				wn.synset("dislodge.v.03"),
				wn.synset("bid.v.03"),
				wn.synset("weigh.v.05"),
				wn.synset("press.v.08"),
				wn.synset("find.v.01"),
				wn.synset("iron.v.01"),
				wn.synset("press.v.01"),
				wn.synset("bump.v.03"),
				wn.synset("press.v.06"),
				wn.synset("bump.v.01"),
				wn.synset("press.v.04"),
				wn.synset("urge.v.01"),
				wn.synset("press.v.10"),
				wn.synset("press.v.11"),
				wn.synset("demote.v.01")],

	# crawl
	"U+3792":   [wn.synset("fawn.v.01"),
				wn.synset("crawl.v.05"),
				wn.synset("crawl.v.03"),
				wn.synset("crawl.v.02"),
				wn.synset("crawl.v.01")],

	# crayon, coloured pencil, marker
	"U+3793":   [wn.synset("marker.n.03")],

	# milk
	"U+3796":   [wn.synset("milk.n.01")],

	# create
	"U+3797":   [wn.synset("make.v.03"),
				wn.synset("create.v.02")],

	# creative
	"U+3799":   [wn.synset("creative.a.01")],

	# crescent
	"U+379a":   [wn.synset("crescent.n.01")],

	# crochet
	"U+379c":   [wn.synset("crochet.v.02"),
				wn.synset("crochet.v.01")],

	# hook, hanger
	"U+379e":   [wn.synset("hook.n.05")],

	# croquet
	"U+379f":   [wn.synset("croquet.n.01")],

	# compression, compressing, squeezing
	"U+37a0":   [wn.synset("print.n.02"),
				wn.synset("compaction.n.01"),
				wn.synset("squeeze.n.01"),
				wn.synset("pressure.n.01"),
				wn.synset("compression.n.02"),
				wn.synset("compression.n.03"),
				wn.synset("compression.n.04"),
				wn.synset("pressure.n.05")],

	# crutches
	"U+37a3":   [wn.synset("crutch.n.02"),
				wn.synset("crutch.n.01")],

	# cry, weep
	"U+37a5":   [wn.synset("cry.v.02")],

	# cucumber
	"U+37a6":   [wn.synset("cucumber.n.02")],

	# current
	"U+37a7":   [wn.synset("current.a.01")],

	# current events
	"U+37a8":   [wn.synset("news.n.01"),
				wn.synset("news.n.02"),
				wn.synset("topicality.n.01"),
				wn.synset("news_program.n.01"),
				wn.synset("newsworthiness.n.01")],

	# curtain, drape
	"U+37a9":   [wn.synset("drape.n.02"),
				wn.synset("drape.n.03"),
				wn.synset("curtain.n.01"),
				wn.synset("curtain.n.02")],

	# cut
	"U+37aa":   [wn.synset("cut.v.01"),
				wn.synset("cut.v.22")],

	# cutlery
	"U+37ab":   [wn.synset("cutter.n.06"),
				wn.synset("cutlery.n.02"),
				wn.synset("flatware.n.02")],

	# dance, dancing
	"U+37ad":   [wn.synset("dance.n.01"),
				wn.synset("dancing.n.01")],

	# dangerous
	"U+37ae":   [wn.synset("dangerous.a.01")],

	# date
	"U+37af":   [wn.synset("date.n.03")],

	# daycare
	"U+37b2":   [wn.synset("daycare.n.01")],

	# day care centre
	"U+37b4":   [wn.synset("day_nursery.n.01")],

	# dead, deceased
	"U+37b6":   [wn.synset("dead.a.01"),
				wn.synset("dead.s.15"),
				wn.synset("dead.s.14"),
				wn.synset("dead.s.04"),
				wn.synset("dead.s.16"),
				wn.synset("dead.s.11"),
				wn.synset("dead.s.10"),
				wn.synset("dead.s.13"),
				wn.synset("dead.s.12"),
				wn.synset("dead.s.08"),
				wn.synset("dead.s.09"),
				wn.synset("all_in.s.01"),
				wn.synset("dead.s.06"),
				wn.synset("dead.s.07"),
				wn.synset("dead.s.17"),
				wn.synset("dead.a.02"),
				wn.synset("dead.s.05"),
				wn.synset("asleep.s.03")],

	# deaf
	"U+37b7":   [wn.synset("deaf.a.01")],

	# dear
	"U+37b8":   [wn.synset("beloved.n.01"),
				wn.synset("lamb.n.04")],

	# decade
	"U+37ba":   [wn.synset("decade.n.01")],

	# December
	"U+37bc":   [wn.synset("december.n.01")],

	# decide
	"U+37bd":   [wn.synset("decide.v.01")],

	# decrease, reduce
	"U+37be":   [wn.synset("decrease.v.02"),
				wn.synset("decrease.v.01"),
				wn.synset("reduce.v.01")],

	# depth
	"U+37bf":   [wn.synset("astuteness.n.02"),
				wn.synset("depth.n.01"),
				wn.synset("depth.n.03"),
				wn.synset("depth.n.02"),
				wn.synset("depth.n.04"),
				wn.synset("depth.n.06"),
				wn.synset("deep.a.03")],

	# deep fry
	"U+37c0":   [wn.synset("french-fry.v.01"),
				wn.synset("fry.v.02")],

	# dental floss
	"U+37c2":   [wn.synset("dental_floss.n.01")],

	# dentist
	"U+37c3":   [wn.synset("dentist.n.01")],

	# doctor, physician, hab)
	"U+37c4":   [wn.synset("doctor.n.04"),
				wn.synset("doctor_of_the_church.n.01"),
				wn.synset("doctor.n.01")],

	# deodorant
	"U+37c6":   [wn.synset("deodorant.n.01")],

	# departure
	"U+37c8":   [wn.synset("departure.n.01")],

	# depression
	"U+37c9":   [wn.synset("depression.n.01"),
				wn.synset("low.n.01")],

	# mood
	"U+37ca":   [wn.synset("temper.n.02")],

	# descend, go down
	"U+37cb":   [wn.synset("descend.v.01"),
				wn.synset("fall.v.32")],

	# describe
	"U+37cc":   [wn.synset("describe.v.01")],

	# desirable
	"U+37ce":   [wn.synset("desirable.a.01")],

	# desk, worktable, work table
	"U+37d0":   [wn.synset("desk.n.01")],

	# dessert
	"U+37d2":   [wn.synset("dessert.n.01")],

	# deletion, cancellation, destruction
	"U+37d3":   [wn.synset("destruction.n.02"),
				wn.synset("end.n.06"),
				wn.synset("destruction.n.01")],

	# develop
	"U+37d6":   [wn.synset("develop.v.01")],

	# dhoti, lungi
	"U+37d7":   [wn.synset("dhoti.n.01")],

	# diamond, rhombus, rhomb
	"U+37d9":   [wn.synset("ball_field.n.01"),
				wn.synset("rhombus.n.01"),
				wn.synset("diamond.n.02"),
				wn.synset("baseball_diamond.n.01"),
				wn.synset("diamond.n.01"),
				wn.synset("diamond.n.04")],

	# diaper, nappy
	"U+37da":   [wn.synset("diaper.n.01")],

	# diaphragm, pessary, midriff
	"U+37dc":   [wn.synset("diaphragm.n.03"),
				wn.synset("diaphragm.n.02"),
				wn.synset("diaphragm.n.01")],

	# die
	"U+37dd":   [wn.synset("die.v.01")],

	# diet
	"U+37de":   [wn.synset("diet.v.01"),
				wn.synset("diet.v.02")],

	# plan, design, method, system
	"U+37df":   [wn.synset("plan.v.01"),
				wn.synset("design.v.07"),
				wn.synset("design.v.06"),
				wn.synset("design.v.05"),
				wn.synset("design.v.04"),
				wn.synset("design.v.03"),
				wn.synset("design.v.02"),
				wn.synset("plan.v.02"),
				wn.synset("plan.v.03")],

	# difficulty
	"U+37e4":   [wn.synset("trouble.n.04"),
				wn.synset("difficulty.n.02"),
				wn.synset("difficulty.n.03"),
				wn.synset("difficulty.n.04")],

	# digging, excavation
	"U+37e5":   [wn.synset("dig.n.01")],

	# digest
	"U+37e7":   [wn.synset("digest.v.01"),
				wn.synset("digest.v.03"),
				wn.synset("digest.v.02")],

	# digestion
	"U+37e8":   [wn.synset("digestion.n.02")],

	# dining room
	"U+37e9":   [wn.synset("dining_room.n.01")],

	# direction, cardinal point
	"U+37ea":   [wn.synset("guidance.n.01"),
				wn.synset("direction.n.01"),
				wn.synset("direction.n.03"),
				wn.synset("management.n.01"),
				wn.synset("direction.n.02")],

	# spot, mark
	"U+37ec":   [wn.synset("blot.n.02"),
				wn.synset("spot.n.05"),
				wn.synset("smudge.n.02")],

	# disco
	"U+37ed":   [wn.synset("disco.n.02")],

	# discuss, converse, debate
	"U+37ef":   [wn.synset("argue.v.02"),
				wn.synset("hash_out.v.01")],

	# dislike
	"U+37f0":   [wn.synset("disfavor.n.02"),
				wn.synset("dislike.n.02")],

	# divide
	"U+37f2":   [wn.synset("divide.v.01")],

	# divorce
	"U+37f3":   [wn.synset("disassociate.v.01"),
				wn.synset("divorce.v.02")],

	# do, act
	"U+37f4":   [wn.synset("make.v.01"),
				wn.synset("do.v.08"),
				wn.synset("do.v.03"),
				wn.synset("perform.v.01"),
				wn.synset("act.v.01")],

	# doll
	"U+37f5":   [wn.synset("doll.n.01")],

	# dollar
	"U+37f7":   [wn.synset("dollar.n.02"),
				wn.synset("dollar.n.01")],

	# donkey, mule
	"U+37f8":   [wn.synset("donkey.n.01"),
				wn.synset("domestic_ass.n.01")],

	# drain, sift, strain
	"U+37fa":   [wn.synset("drain.v.03")],

	# draw, sketch
	"U+37fb":   [wn.synset("draw.v.06")],

	# picture, image, icon, painting
	"U+37fc":   [wn.synset("painting.n.01")],

	# dream
	"U+37fd":   [wn.synset("dream.v.02"),
				wn.synset("dream.v.01")],

	# dress, wear
	"U+37ff":   [wn.synset("trim.v.06"),
				wn.synset("wear.v.09"),
				wn.synset("dress.v.13"),
				wn.synset("snip.v.02"),
				wn.synset("dress.v.14"),
				wn.synset("wear.v.01"),
				wn.synset("dress.v.15"),
				wn.synset("dress.v.10"),
				wn.synset("dress.v.06"),
				wn.synset("dress.v.12"),
				wn.synset("dress.v.04"),
				wn.synset("dress.v.03"),
				wn.synset("dress.v.02"),
				wn.synset("dress.v.16"),
				wn.synset("dress.v.07"),
				wn.synset("dress.v.09"),
				wn.synset("tire.v.02"),
				wn.synset("dress.v.01"),
				wn.synset("wear.v.04"),
				wn.synset("wear.v.05"),
				wn.synset("wear.v.06"),
				wn.synset("wear.v.03"),
				wn.synset("break.v.42"),
				wn.synset("wear.v.02"),
				wn.synset("preen.v.03")],

	# dress up, disguise
	"U+3801":   [wn.synset("disguise.v.01"),
				wn.synset("dress.v.04"),
				wn.synset("overdress.v.02"),
				wn.synset("dress_up.v.02"),
				wn.synset("costume.v.01"),
				wn.synset("caparison.v.01")],

	# dressing gown, housecoat, robe
	"U+3802":   [wn.synset("dressing_gown.n.01")],

	# drive
	"U+3804":   [wn.synset("drive.v.01")],

	# driver, chauffeur
	"U+3805":   [wn.synset("driver.n.01")],

	# drunk
	"U+3807":   [wn.synset("intoxicated.a.01")],

	# dump truck, dumper, tipper lorry, tipper
	"U+380a":   [wn.synset("dump_truck.n.01")],

	# truck, lorry
	"U+380b":   [wn.synset("truck.n.01")],

	# Durga
	"U+380c":   [wn.synset("durga.n.01")],

	# during, while
	"U+380e":   [wn.synset("while.n.01"),
				wn.synset("throughout.r.01")],

	# each, every
	"U+380f":   [wn.synset("every.s.01"),
				wn.synset("each.s.01")],

	# early
	"U+3811":   [wn.synset("early.a.01")],

	# earmuffs
	"U+3812":   [wn.synset("earmuff.n.01")],

	# earn
	"U+3814":   [wn.synset("earn.v.02"),
				wn.synset("gain.v.08")],

	# easter
	"U+3817":   [wn.synset("easter.n.01")],

	# eastern
	"U+3819":   [wn.synset("eastern.s.01"),
				wn.synset("easterly.s.01"),
				wn.synset("eastern.a.04")],

	# eat
	"U+381a":   [wn.synset("eat.v.01")],

	# education, didactics, pedagogy
	"U+381b":   [wn.synset("teaching_method.n.01")],

	# eel
	"U+381e":   [wn.synset("eel.n.02")],

	# eggplant
	"U+3821":   [wn.synset("eggplant.n.01"),
				wn.synset("eggplant.n.02")],

	# ejaculation
	"U+3823":   [wn.synset("ejaculation.n.02")],

	# electric, electrical
	"U+3825":   [wn.synset("electric.a.01")],

	# electric light, lamp
	"U+3826":   [wn.synset("lamp.n.01")],

	# electric wire, electric cord, cord, cable, lead
	"U+3828":   [wn.synset("lead.n.05"),
				wn.synset("lead.n.04"),
				wn.synset("lead.n.07"),
				wn.synset("lead.n.06"),
				wn.synset("lead.n.01"),
				wn.synset("lead.n.03"),
				wn.synset("lead.n.02"),
				wn.synset("lead.n.09"),
				wn.synset("cord.n.04"),
				wn.synset("cord.n.03"),
				wn.synset("lead.n.14"),
				wn.synset("cord.n.01"),
				wn.synset("cord.n.02"),
				wn.synset("leash.n.01"),
				wn.synset("lead.n.17"),
				wn.synset("lead.n.15"),
				wn.synset("conductor.n.04"),
				wn.synset("cable_television.n.01"),
				wn.synset("star.n.04"),
				wn.synset("duct.n.01"),
				wn.synset("spark_advance.n.01"),
				wn.synset("lead.n.11"),
				wn.synset("jumper_cable.n.01"),
				wn.synset("tip.n.03"),
				wn.synset("cable.n.04"),
				wn.synset("cable.n.06"),
				wn.synset("cable.n.01"),
				wn.synset("cable.n.03"),
				wn.synset("cable.n.02")],

	# elephant
	"U+3829":   [wn.synset("elephant.n.01")],

	# elevator, lift, raise, grow, bring up, cultivate
	"U+382a":   [wn.synset("lift.v.20"),
				wn.synset("originate.v.01"),
				wn.synset("domesticate.v.01"),
				wn.synset("lift.v.03"),
				wn.synset("cultivate.v.02"),
				wn.synset("develop.v.14"),
				wn.synset("educate.v.03"),
				wn.synset("grow.v.04"),
				wn.synset("raise.v.01"),
				wn.synset("raise.v.02"),
				wn.synset("raise.v.03"),
				wn.synset("raise.v.04"),
				wn.synset("grow.v.02"),
				wn.synset("raise.v.07"),
				wn.synset("raise.v.09"),
				wn.synset("raise.v.24"),
				wn.synset("raise.v.25"),
				wn.synset("grow.v.08"),
				wn.synset("raise.v.23"),
				wn.synset("raise.v.20"),
				wn.synset("raise.v.21"),
				wn.synset("mature.v.01"),
				wn.synset("recruit.v.03"),
				wn.synset("mention.v.01"),
				wn.synset("boot.v.02"),
				wn.synset("cultivate.v.01"),
				wn.synset("bring_up.v.03"),
				wn.synset("resurrect.v.01"),
				wn.synset("arouse.v.01"),
				wn.synset("lift.v.10"),
				wn.synset("grow.v.07"),
				wn.synset("enhance.v.01"),
				wn.synset("raise.v.17"),
				wn.synset("raise.v.16"),
				wn.synset("raise.v.15"),
				wn.synset("grow.v.10"),
				wn.synset("bring_up.v.05"),
				wn.synset("raise.v.11"),
				wn.synset("rear.v.02"),
				wn.synset("grow.v.03"),
				wn.synset("raise.v.19"),
				wn.synset("raise.v.22"),
				wn.synset("promote.v.02"),
				wn.synset("turn.v.07")],

	# Elul
	"U+382c":   [wn.synset("elul.n.01")],

	# shofar
	"U+382d":   [wn.synset("shofar.n.01")],

	# embarrassed
	"U+382e":   [wn.synset("abashed.s.01"),
				wn.synset("embarrassed.s.02"),
				wn.synset("coy.s.03")],

	# embarrassment
	"U+382f":   [wn.synset("embarrassment.n.01")],

	# embarrassing
	"U+3830":   [wn.synset("awkward.s.05")],

	# emergency
	"U+3831":   [wn.synset("rapid.s.01"),
				wn.synset("ad_hoc.s.01"),
				wn.synset("emergency.n.01"),
				wn.synset("hand_brake.n.01"),
				wn.synset("emergency.n.02")],

	# empathy
	"U+3832":   [wn.synset("empathy.n.01")],

	# understanding, comprehension
	"U+3833":   [wn.synset("sympathy.n.01")],

	# engaged
	"U+3835":   [wn.synset("busy.s.05"),
				wn.synset("booked.s.01"),
				wn.synset("engaged.s.01"),
				wn.synset("engaged.s.02"),
				wn.synset("engaged.s.07"),
				wn.synset("engaged.s.05"),
				wn.synset("engaged.s.06"),
				wn.synset("boyfriend.n.01")],

	# enjoy
	"U+3836":   [wn.synset("amuse.v.01"),
				wn.synset("love.v.02"),
				wn.synset("enjoy.v.01"),
				wn.synset("amuse.v.02"),
				wn.synset("enjoy.v.02"),
				wn.synset("enjoy.v.04"),
				wn.synset("delight.v.02")],

	# enough
	"U+3837":   [wn.synset("quite.r.02"),
				wn.synset("entire.s.01"),
				wn.synset("quite.r.01"),
				wn.synset("full.a.01"),
				wn.synset("enough.r.01"),
				wn.synset("reasonably.r.01"),
				wn.synset("filled.s.01"),
				wn.synset("sufficiently.r.01"),
				wn.synset("adequate.s.02")],

	# minus, no, without
	"U+3838":   [wn.synset("minus_sign.n.01"),
				wn.synset("subtraction.n.01"),
				wn.synset("nobelium.n.01"),
				wn.synset("no.n.01")],

	# enter, absorb, insert, penetrate, go through
	"U+3839":   [wn.synset("experience.v.01"),
				wn.synset("devour.v.03"),
				wn.synset("pass.v.01"),
				wn.synset("permeate.v.01"),
				wn.synset("follow_through.v.02"),
				wn.synset("penetrate.v.05"),
				wn.synset("penetrate.v.06"),
				wn.synset("infiltrate.v.02"),
				wn.synset("penetrate.v.01"),
				wn.synset("penetrate.v.02"),
				wn.synset("work_through.v.01"),
				wn.synset("click.v.07")],

	# envious
	"U+383a":   [wn.synset("covetous.s.01")],

	# equal, same
	"U+383c":   [wn.synset("equal.a.01")],

	# eternal life, immortality
	"U+383d":   [wn.synset("immortality.n.01")],

	# evaluate
	"U+383f":   [wn.synset("measure.v.04")],

	# appreciate, value, treasure
	"U+3841":   [wn.synset("care_for.v.02"),
				wn.synset("prize.v.01"),
				wn.synset("appreciate.v.05"),
				wn.synset("appreciate.v.04"),
				wn.synset("appreciate.v.02"),
				wn.synset("appreciate.v.01"),
				wn.synset("rate.v.03"),
				wn.synset("measure.v.04"),
				wn.synset("value.v.01"),
				wn.synset("respect.v.01")],

	# ecstatic
	"U+3846":   [wn.synset("excited.a.02"),
				wn.synset("ecstatic.s.01")],

	# ecstasy
	"U+3847":   [wn.synset("excitation.n.03"),
				wn.synset("ecstasy.n.02"),
				wn.synset("adam.n.03"),
				wn.synset("excitement.n.02"),
				wn.synset("inflammation.n.03"),
				wn.synset("ecstasy.n.01"),
				wn.synset("foreplay.n.01")],

	# exclude
	"U+3849":   [wn.synset("bar.v.01"),
				wn.synset("exclude.v.01"),
				wn.synset("exclude.v.02")],

	# excuse
	"U+384a":   [wn.synset("apologize.v.02"),
				wn.synset("excuse.v.06")],

	# exercise, work out
	"U+384c":   [wn.synset("drill.v.03")],

	# exhibitionism, immodesty, indecent exposure
	"U+384d":   [wn.synset("exhibitionism.n.01"),
				wn.synset("exhibitionism.n.02"),
				wn.synset("indecent_exposure.n.01"),
				wn.synset("immodesty.n.01")],

	# expect, anticipate
	"U+3850":   [wn.synset("expect.v.01")],

	# explain, give a reason
	"U+3851":   [wn.synset("explain.v.01")],

	# explode, blow up, detonate, burst
	"U+3852":   [wn.synset("explode.v.02")],

	# explosion, detonation, blowup
	"U+3853":   [wn.synset("explosion.n.01")],

	# eyebrow pencil
	"U+3854":   [wn.synset("eyebrow_pencil.n.01")],

	# eye makeup
	"U+3856":   [wn.synset("mascara.n.01")],

	# factory, plant
	"U+3857":   [wn.synset("factory.n.01")],

	# falafel
	"U+3858":   [wn.synset("falafel.n.01")],

	# fallopian tube
	"U+3859":   [wn.synset("fallopian_tube.n.01")],

	# police force, police
	"U+385b":   [wn.synset("police.n.01")],

	# family planning
	"U+385c":   [wn.synset("birth_control.n.01")],

	# farmer
	"U+385f":   [wn.synset("farmer.n.01")],

	# fast day
	"U+3860":   [wn.synset("fast_day.n.01")],

	# fasten, attach, join, append, connect
	"U+3862":   [wn.synset("connect.v.08"),
				wn.synset("fasten.v.01"),
				wn.synset("fasten.v.02"),
				wn.synset("fasten.v.03"),
				wn.synset("plug_in.v.01"),
				wn.synset("connect.v.01"),
				wn.synset("connect.v.11"),
				wn.synset("connect.v.03"),
				wn.synset("connect.v.04"),
				wn.synset("connect.v.05"),
				wn.synset("connect.v.06"),
				wn.synset("impound.v.01"),
				wn.synset("join.v.03"),
				wn.synset("join.v.02"),
				wn.synset("join.v.01"),
				wn.synset("append.v.02"),
				wn.synset("join.v.04"),
				wn.synset("connect.v.07"),
				wn.synset("attach.v.01"),
				wn.synset("attach.v.02"),
				wn.synset("attach.v.03"),
				wn.synset("associate.v.01"),
				wn.synset("tighten.v.01"),
				wn.synset("append.v.01"),
				wn.synset("get_in_touch.v.01"),
				wn.synset("bind.v.02"),
				wn.synset("add.v.02")],

	# together, attached, appended, fastened, joined
	"U+3863":   [wn.synset("affiliated.s.01"),
				wn.synset("coupled.s.02"),
				wn.synset("fastened.a.01"),
				wn.synset("add.v.02"),
				wn.synset("buttoned.a.01"),
				wn.synset("tied.a.03"),
				wn.synset("attached.s.04"),
				wn.synset("append.v.02"),
				wn.synset("together.r.04"),
				wn.synset("append.v.01"),
				wn.synset("together.s.01"),
				wn.synset("attached.a.02"),
				wn.synset("attached.a.03"),
				wn.synset("joined.s.01"),
				wn.synset("jointly.r.02")],

	# fastener, gripper, velcro, zipper
	"U+3864":   [wn.synset("fastener.n.02")],

	# favourite
	"U+3867":   [wn.synset("favorite.s.01"),
				wn.synset("favored.s.01")],

	# first, primary
	"U+3869":   [wn.synset("first.a.01")],

	# feather
	"U+386a":   [wn.synset("feather.n.01")],

	# February
	"U+386c":   [wn.synset("february.n.01")],

	# feed
	"U+386d":   [wn.synset("feed.v.02")],

	# feel
	"U+386e":   [wn.synset("feel.v.01")],

	# fertile
	"U+3870":   [wn.synset("fertile.a.01")],

	# fertility counselling
	"U+3871":   [wn.synset("fertility.n.02")],

	# fidelity, loyalty, solidarity
	"U+3872":   [wn.synset("fidelity.n.02")],

	# field hockey, hockey
	"U+3874":   [wn.synset("field_hockey.n.01")],

	# filling, fill, fullness
	"U+3876":   [wn.synset("fill.n.01"),
				wn.synset("filling.n.05"),
				wn.synset("woof.n.01"),
				wn.synset("filling.n.06"),
				wn.synset("filling.n.01"),
				wn.synset("filling.n.03"),
				wn.synset("filling.n.02"),
				wn.synset("fullness.n.04"),
				wn.synset("fullness.n.03"),
				wn.synset("fullness.n.02"),
				wn.synset("comprehensiveness.n.01")],

	# film
	"U+3877":   [wn.synset("movie.n.01")],

	# finally, at last
	"U+3879":   [wn.synset("ultimately.r.01"),
				wn.synset("finally.r.01")],

	# last, final, etc)
	"U+387a":   [wn.synset("concluding.s.01"),
				wn.synset("last.a.02"),
				wn.synset("last.s.01")],

	# find
	"U+387b":   [wn.synset("find.v.05"),
				wn.synset("find.v.10"),
				wn.synset("receive.v.02"),
				wn.synset("find.v.03"),
				wn.synset("detect.v.01"),
				wn.synset("determine.v.01"),
				wn.synset("discover.v.03"),
				wn.synset("find.v.01")],

	# finish, complete
	"U+387d":   [wn.synset("end.v.01"),
				wn.synset("finish_up.v.02")],

	# Finland
	"U+387f":   [wn.synset("finland.n.01")],

	# firefighter, fireman
	"U+3881":   [wn.synset("fireman.n.04")],

	# extinction, extinguishing
	"U+3882":   [wn.synset("extinction.n.02"),
				wn.synset("extinction.n.03"),
				wn.synset("extinction.n.01"),
				wn.synset("extinction.n.06"),
				wn.synset("extinction.n.04"),
				wn.synset("extinction.n.05")],

	# fire truck, fire engine
	"U+3884":   [wn.synset("fire_engine.n.01")],

	# fishing
	"U+3885":   [wn.synset("fishing.n.01")],

	# receiving
	"U+3886":   [wn.synset("receive.v.06"),
				wn.synset("receive.v.05"),
				wn.synset("receive.v.10"),
				wn.synset("receive.v.02"),
				wn.synset("receive.v.01"),
				wn.synset("receive.v.13"),
				wn.synset("welcome.v.02"),
				wn.synset("receive.v.12"),
				wn.synset("experience.v.03"),
				wn.synset("receive.v.08"),
				wn.synset("meet.v.11"),
				wn.synset("pick_up.v.09"),
				wn.synset("get.v.25")],

	# fix, mend, repair
	"U+3888":   [wn.synset("repair.v.01")],

	# fixing, fix, mending, mend, repair, reparation
	"U+3889":   [wn.synset("repair.n.01"),
				wn.synset("repair.n.02"),
				wn.synset("mending.n.01"),
				wn.synset("reparation.n.01"),
				wn.synset("fix.n.04"),
				wn.synset("fastener.n.02"),
				wn.synset("fix.n.01"),
				wn.synset("fix.n.02"),
				wn.synset("haunt.n.01"),
				wn.synset("reparation.n.02"),
				wn.synset("neutering.n.01"),
				wn.synset("localization.n.01"),
				wn.synset("mend.n.01"),
				wn.synset("reparation.n.04"),
				wn.synset("fixation.n.04")],

	# flame
	"U+388a":   [wn.synset("fire.n.03")],

	# burnable, combustible, ignitable
	"U+388b":   [wn.synset("burnable.s.01"),
				wn.synset("combustible.a.01")],

	# flashlight, lantern
	"U+388c":   [wn.synset("flashlight.n.01"),
				wn.synset("torch.n.01"),
				wn.synset("lantern.n.01")],

	# flavouring, condiment, seasoning
	"U+388d":   [wn.synset("flavorer.n.01")],

	# flea
	"U+388e":   [wn.synset("flea.n.01")],

	# louse, stinging insect
	"U+388f":   [wn.synset("bird_louse.n.01"),
				wn.synset("louse.n.01"),
				wn.synset("worm.n.02"),
				wn.synset("plant_louse.n.01")],

	# flood
	"U+3893":   [wn.synset("flood.n.01")],

	# flour
	"U+3895":   [wn.synset("flour.n.01")],

	# wildflower
	"U+3896":   [wn.synset("plant.n.02"),
				wn.synset("wildflower.n.01")],

	# flying
	"U+3897":   [wn.synset("fast-flying.s.01"),
				wn.synset("flying.s.02")],

	# food ball
	"U+3898":   [wn.synset("meatball.n.01"),
				wn.synset("meat_loaf.n.01")],

	# football, soccer
	"U+389a":   [wn.synset("soccer.n.01")],

	# forced, compelled, obliged
	"U+389b":   [wn.synset("forced.s.03"),
				wn.synset("forced.s.02"),
				wn.synset("duty-bound.s.01"),
				wn.synset("forced.a.01"),
				wn.synset("compel.v.02"),
				wn.synset("compel.v.01"),
				wn.synset("constrained.s.01")],

	# must, have to, be forced to
	"U+389c":   [wn.synset("must.s.01"),
				wn.synset("mustiness.n.01"),
				wn.synset("must.n.01"),
				wn.synset("must.n.02"),
				wn.synset("owe.v.03")],

	# foreskin
	"U+389d":   [wn.synset("prepuce.n.02")],

	# forest, bush, wood, woods, lumber, timber
	"U+389e":   [wn.synset("wood.n.01")],

	# forgetting, amnesia
	"U+38a0":   [wn.synset("amnesia.n.01")],

	# permission, allowance
	"U+38a2":   [wn.synset("license.n.04"),
				wn.synset("permission.n.01")],

	# foster mother
	"U+38a4":   [wn.synset("foster-mother.n.01")],

	# similar, like, alike
	"U+38a5":   [wn.synset("exchangeable.s.03"),
				wn.synset("similar.a.01"),
				wn.synset("similar.s.04"),
				wn.synset("alike.r.01"),
				wn.synset("alike.r.02"),
				wn.synset("like.a.01"),
				wn.synset("like.n.01"),
				wn.synset("like.n.02"),
				wn.synset("alike.a.01")],

	# foster parent
	"U+38a6":   [wn.synset("caregiver.n.02"),
				wn.synset("probation_officer.n.01"),
				wn.synset("foster-parent.n.01")],

	# fox
	"U+38a8":   [wn.synset("fox.n.01")],

	# free, freely
	"U+38a9":   [wn.synset("free.a.01")],

	# freezing, hardening, solidifying
	"U+38aa":   [wn.synset("hardening.n.02"),
				wn.synset("hardening.n.03"),
				wn.synset("hardening.n.01"),
				wn.synset("freeze.n.01")],

	# fresh
	"U+38ad":   [wn.synset("fresh.a.01")],

	# friend
	"U+38ae":   [wn.synset("friend.n.01")],

	# frog, toad
	"U+38b0":   [wn.synset("frog.n.01")],

	# fruit juice, juice
	"U+38b2":   [wn.synset("juice.n.04"),
				wn.synset("fruit_juice.n.01"),
				wn.synset("juice.n.01"),
				wn.synset("juice.n.02"),
				wn.synset("juice.n.03")],

	# yogurt, yoghurt
	"U+38b5":   [wn.synset("yogurt.n.01")],

	# frustrated
	"U+38b6":   [wn.synset("defeated.s.02")],

	# frustration
	"U+38b7":   [wn.synset("frustration.n.01")],

	# frustrating
	"U+38b8":   [wn.synset("frustrating.s.01"),
				wn.synset("frustrating.s.02")],

	# adversity, hardship, setback
	"U+38b9":   [wn.synset("reverse.n.03")],

	# fry, saute
	"U+38bc":   [wn.synset("fry.v.02")],

	# full, satisfied
	"U+38bd":   [wn.synset("full.a.01")],

	# funny, humorous
	"U+38be":   [wn.synset("amusing.s.02")],

	# laugh, laughter
	"U+38bf":   [wn.synset("laugh.n.01")],

	# furniture
	"U+38c1":   [wn.synset("furniture.n.01")],

	# game
	"U+38c2":   [wn.synset("game.n.01"),
				wn.synset("game.n.03"),
				wn.synset("game.n.02")],

	# Ganesh
	"U+38c5":   [wn.synset("ganesh.n.01")],

	# garbage can, rubbish bin, trash can
	"U+38c6":   [wn.synset("ashcan.n.01")],

	# garlic
	"U+38c7":   [wn.synset("garlic.n.02")],

	# smell, odour, give off odour, sense of smell, olfaction
	"U+38c8":   [wn.synset("smell.v.03"),
				wn.synset("smell.v.02"),
				wn.synset("smell.v.01")],

	# gasoline
	"U+38c9":   [wn.synset("gasoline.n.01")],

	# gather, assemble
	"U+38ca":   [wn.synset("assemble.v.03")],

	# indefinite
	"U+38cb":   [wn.synset("overall.s.01"),
				wn.synset("indefinite.a.01"),
				wn.synset("general.s.02"),
				wn.synset("general.a.01"),
				wn.synset("indefinite.s.02")],

	# gerbil, guinea pig, hamster
	"U+38cc":   [wn.synset("subject.n.06"),
				wn.synset("hamster.n.01"),
				wn.synset("gerbil.n.01"),
				wn.synset("guinea_pig.n.02")],

	# gift, offering, present
	"U+38cd":   [wn.synset("gift.n.01")],

	# giving, gift
	"U+38ce":   [wn.synset("give_away.v.01"),
				wn.synset("go.v.25"),
				wn.synset("bestow.v.02"),
				wn.synset("strike.v.05"),
				wn.synset("get.v.19"),
				wn.synset("give.v.29"),
				wn.synset("grant.v.05"),
				wn.synset("give.v.20"),
				wn.synset("give.v.21"),
				wn.synset("endowment.n.01"),
				wn.synset("afford.v.04"),
				wn.synset("hold.v.03"),
				wn.synset("give.v.04"),
				wn.synset("give.v.05"),
				wn.synset("give.v.03"),
				wn.synset("give.v.01"),
				wn.synset("give.v.41"),
				wn.synset("hit.v.15"),
				wn.synset("give.v.44"),
				wn.synset("give.v.09"),
				wn.synset("establish.v.05"),
				wn.synset("pass.v.05"),
				wn.synset("gift.n.01"),
				wn.synset("give.v.08"),
				wn.synset("bear.v.05"),
				wn.synset("giving.n.03"),
				wn.synset("giving.n.02"),
				wn.synset("giving.n.01"),
				wn.synset("find.v.01"),
				wn.synset("give.v.31"),
				wn.synset("give.v.37"),
				wn.synset("give.v.34"),
				wn.synset("sacrifice.v.01"),
				wn.synset("hit.v.09"),
				wn.synset("give.v.10"),
				wn.synset("breathe.v.03"),
				wn.synset("yield.v.10")],

	# glass material
	"U+38cf":   [wn.synset("glass.n.01")],

	# glasses, eyeglasses
	"U+38d0":   [wn.synset("spectacles.n.01")],

	# glassware
	"U+38d1":   [wn.synset("glassware.n.01"),
				wn.synset("glass.n.07")],

	# sports glove, glove, mitt, mitten
	"U+38d3":   [wn.synset("glove.n.02")],

	# glue, adhesive, paste, stick
	"U+38d4":   [wn.synset("glue.v.01")],

	# attachment, appendix, annex, cecum, caecum
	"U+38d5":   [wn.synset("fastening.n.02"),
				wn.synset("attachment.n.04"),
				wn.synset("attachment.n.05"),
				wn.synset("attachment.n.06"),
				wn.synset("attachment.n.01"),
				wn.synset("attachment.n.02"),
				wn.synset("attachment.n.03"),
				wn.synset("enclosure.n.04")],

	# goldfish, guppy, pet fish
	"U+38d6":   [wn.synset("guppy.n.01"),
				wn.synset("goldfish.n.01")],

	# golf
	"U+38d7":   [wn.synset("golf.n.01")],

	# goodbye, farewell
	"U+38d8":   [wn.synset("farewell.n.02"),
				wn.synset("farewell.n.01"),
				wn.synset("adieu.n.01")],

	# parting
	"U+38d9":   [wn.synset("farewell.n.02")],

	# Good Friday
	"U+38da":   [wn.synset("good_friday.n.01")],

	# goodness
	"U+38db":   [wn.synset("good.n.02")],

	# goose
	"U+38dd":   [wn.synset("goose.n.01")],

	# gopher, ground hog
	"U+38e1":   [wn.synset("gopher.n.04"),
				wn.synset("minnesotan.n.01"),
				wn.synset("ground_squirrel.n.02"),
				wn.synset("goffer.n.01"),
				wn.synset("rodent.n.01"),
				wn.synset("gopher_tortoise.n.01")],

	# govern, rule, regulation
	"U+38e2":   [wn.synset("rule.n.01")],

	# grape juice
	"U+38e4":   [wn.synset("grape_juice.n.01")],

	# grapefruit
	"U+38e6":   [wn.synset("grapefruit.n.02")],

	# grasshopper
	"U+38e7":   [wn.synset("grasshopper.n.01")],

	# reclining, lying
	"U+38e9":   [wn.synset("lying.n.01"),
				wn.synset("none.n.01"),
				wn.synset("none.n.02"),
				wn.synset("cipher.n.04"),
				wn.synset("person.n.01"),
				wn.synset("person.n.02"),
				wn.synset("person.n.03"),
				wn.synset("reclining.n.01"),
				wn.synset("no.n.01")],

	# gray, grey
	"U+38ec":   [wn.synset("grey.n.04"),
				wn.synset("grey.n.06"),
				wn.synset("grey.n.07"),
				wn.synset("grey.n.01"),
				wn.synset("grey.n.02"),
				wn.synset("grey.n.03"),
				wn.synset("gray.n.08"),
				wn.synset("gray.n.09"),
				wn.synset("gray.n.01"),
				wn.synset("gray.n.05"),
				wn.synset("gray.n.06"),
				wn.synset("gray.n.07")],

	# great experience
	"U+38ed":   [wn.synset("excellency.n.01"),
				wn.synset("excellence.n.01")],

	# greenhouse, glasshouse, hothouse
	"U+38f0":   [wn.synset("greenhouse.n.01")],

	# green onion, scallion, spring onion
	"U+38f1":   [wn.synset("green_onion.n.01")],

	# group of, much of, many of, quantity of
	"U+38f2":   [wn.synset("blood_group.n.01"),
				wn.synset("crowd.n.02"),
				wn.synset("group.n.03"),
				wn.synset("group.n.01"),
				wn.synset("bunch.n.01")],

	# grove
	"U+38f3":   [wn.synset("grove.n.02"),
				wn.synset("grove.n.01")],

	# grow
	"U+38f5":   [wn.synset("mature.v.01"),
				wn.synset("grow.v.02"),
				wn.synset("grow.v.03")],

	# growth, growing
	"U+38f6":   [wn.synset("increase.n.03"),
				wn.synset("growth.n.02"),
				wn.synset("growth.n.01"),
				wn.synset("growth.n.06"),
				wn.synset("growth.n.07"),
				wn.synset("growth.n.04"),
				wn.synset("growing.n.02"),
				wn.synset("emergence.n.01")],

	# guard duty
	"U+38f8":   [wn.synset("guard_duty.n.01")],

	# guess, estimate, estimation
	"U+38fa":   [wn.synset("estimate.n.01")],

	# guilt
	"U+38fc":   [wn.synset("guilt.n.02"),
				wn.synset("guilt.n.01")],

	# judgement, law
	"U+38fd":   [wn.synset("law.n.02"),
				wn.synset("law.n.03"),
				wn.synset("law.n.01"),
				wn.synset("law.n.04"),
				wn.synset("opinion.n.04"),
				wn.synset("judgment.n.03")],

	# guilty
	"U+38fe":   [wn.synset("guilty.a.01")],

	# gull, seagull, sea gull
	"U+38ff":   [wn.synset("gull.n.02")],

	# Haggadah
	"U+3900":   [wn.synset("haggadah.n.01")],

	# Passover
	"U+3901":   [wn.synset("passover.n.01")],

	# hamentasch
	"U+3903":   [wn.synset("malleus.n.01"),
				wn.synset("hammer.n.02")],

	# handball
	"U+3904":   [wn.synset("handball.n.02")],

	# handgun, pistol
	"U+3906":   [wn.synset("pistol.n.01")],

	# handkerchief
	"U+3907":   [wn.synset("handkerchief.n.01")],

	# handmade object, handicraft
	"U+3909":   [wn.synset("handicraft.n.02"),
				wn.synset("handicraft.n.01")],

	# hang, hook
	"U+390a":   [wn.synset("hang.v.02")],

	# happen, occur
	"U+390b":   [wn.synset("happen.v.01")],

	# happy, glad, gladly, happily
	"U+390c":   [wn.synset("happy.s.04"),
				wn.synset("felicitous.s.02"),
				wn.synset("glad.s.02"),
				wn.synset("glad.s.03"),
				wn.synset("gladly.r.01"),
				wn.synset("beaming.s.01"),
				wn.synset("happily.r.02"),
				wn.synset("happily.r.01"),
				wn.synset("glad.a.01"),
				wn.synset("happy.a.01")],

	# harassment
	"U+390d":   [wn.synset("anguish.n.01"),
				wn.synset("agony.n.01"),
				wn.synset("pest.n.03"),
				wn.synset("mistreatment.n.01"),
				wn.synset("harassment.n.01"),
				wn.synset("harassment.n.02")],

	# harmony, harmoniousness, concord, concordance
	"U+3910":   [wn.synset("harmony.n.01"),
				wn.synset("harmony.n.02"),
				wn.synset("harmony.n.03"),
				wn.synset("harmony.n.04")],

	# harvest
	"U+3911":   [wn.synset("crop.n.01")],

	# hat, cap, hood
	"U+3912":   [wn.synset("hat.n.01")],

	# have
	"U+3914":   [wn.synset("experience.v.03"),
				wn.synset("own.v.01"),
				wn.synset("have.v.01"),
				wn.synset("have.v.09"),
				wn.synset("have.v.11"),
				wn.synset("have.v.12"),
				wn.synset("have.v.10"),
				wn.synset("have.v.02")],

	# holding
	"U+3915":   [wn.synset("possession.n.01"),
				wn.synset("property.n.01"),
				wn.synset("retention.n.01")],

	# hawk, eagle
	"U+3916":   [wn.synset("hawk.n.02"),
				wn.synset("eagle.n.04"),
				wn.synset("hawk.n.01"),
				wn.synset("mortarboard.n.01"),
				wn.synset("eagle.n.01"),
				wn.synset("eagle.n.02"),
				wn.synset("eagle.n.03")],

	# he, him, himself, she, her, one, hers, herself
	"U+3917":   [wn.synset("one.n.02"),
				wn.synset("one.n.01"),
				wn.synset("he.n.02"),
				wn.synset("helium.n.01"),
				wn.synset("id.n.03")],

	# healthy, well
	"U+3918":   [wn.synset("good.s.13"),
				wn.synset("healthy.s.04"),
				wn.synset("healthy.a.01"),
				wn.synset("healthy.s.02"),
				wn.synset("healthy.s.03"),
				wn.synset("advantageous.a.01"),
				wn.synset("well.a.01"),
				wn.synset("well.s.03"),
				wn.synset("goodly.s.01")],

	# hear, listen
	"U+3919":   [wn.synset("hear.v.03"),
				wn.synset("hear.v.01"),
				wn.synset("listen.v.02"),
				wn.synset("listen.v.01"),
				wn.synset("heed.v.01"),
				wn.synset("hear.v.04"),
				wn.synset("learn.v.02")],

	# hearing aid
	"U+391a":   [wn.synset("hearing_aid.n.02"),
				wn.synset("hearing_aid.n.01")],

	# heart
	"U+391b":   [wn.synset("kernel.n.03"),
				wn.synset("heart.n.08"),
				wn.synset("heart.n.06"),
				wn.synset("heart.n.07"),
				wn.synset("heart.n.01"),
				wn.synset("heart.n.02"),
				wn.synset("heart.n.03"),
				wn.synset("heart.n.10"),
				wn.synset("affection.n.01"),
				wn.synset("center.n.01")],

	# heavy
	"U+391c":   [wn.synset("heavy.a.01")],

	# hello, greetings
	"U+391d":   [wn.synset("hello.n.01"),
				wn.synset("greeting.n.01")],

	# heterosexuality
	"U+391f":   [wn.synset("heterosexuality.n.01")],

	# height, tallness, altitude
	"U+3920":   [wn.synset("altitude.n.01")],

	# hill
	"U+3922":   [wn.synset("hill.n.01")],

	# hit
	"U+3924":   [wn.synset("shoot.v.01"),
				wn.synset("score.v.01"),
				wn.synset("reach.v.02"),
				wn.synset("reach.v.01"),
				wn.synset("strike.v.10"),
				wn.synset("hit.v.01"),
				wn.synset("strike.v.04"),
				wn.synset("stumble.v.03"),
				wn.synset("hit.v.09"),
				wn.synset("murder.v.01"),
				wn.synset("hit.v.16"),
				wn.synset("hit.v.03"),
				wn.synset("hit.v.02"),
				wn.synset("hit.v.12"),
				wn.synset("hit.v.15"),
				wn.synset("hit.v.05"),
				wn.synset("hit.v.17")],

	# hobby, pastime
	"U+3926":   [wn.synset("avocation.n.01")],

	# hoist, lift
	"U+3928":   [wn.synset("elevation.n.01"),
				wn.synset("hoist.n.01"),
				wn.synset("aerodynamic_lift.n.01"),
				wn.synset("elevator.n.01"),
				wn.synset("airlift.n.01"),
				wn.synset("lift.n.11"),
				wn.synset("face_lift.n.01"),
				wn.synset("lift.n.01"),
				wn.synset("lift.n.06"),
				wn.synset("lift.n.07"),
				wn.synset("lift.n.04"),
				wn.synset("ski_tow.n.01"),
				wn.synset("lift.n.12")],

	# hold, contain
	"U+3929":   [wn.synset("declare.v.04"),
				wn.synset("hold.v.36"),
				wn.synset("accommodate.v.04"),
				wn.synset("defend.v.03"),
				wn.synset("bear.v.11"),
				wn.synset("have.v.01"),
				wn.synset("hold.v.28"),
				wn.synset("hold.v.29"),
				wn.synset("carry.v.33"),
				wn.synset("defy.v.01"),
				wn.synset("oblige.v.02"),
				wn.synset("hold.v.22"),
				wn.synset("hold.v.23"),
				wn.synset("hold.v.26"),
				wn.synset("hold.v.02"),
				wn.synset("hold.v.03"),
				wn.synset("contain.v.04"),
				wn.synset("contain.v.05"),
				wn.synset("check.v.18"),
				wn.synset("control.v.02"),
				wn.synset("apply.v.02"),
				wn.synset("keep.v.01"),
				wn.synset("hold.v.31"),
				wn.synset("harbor.v.01"),
				wn.synset("deem.v.01"),
				wn.synset("retain.v.03"),
				wn.synset("incorporate.v.02"),
				wn.synset("restrain.v.03"),
				wn.synset("agree.v.01"),
				wn.synset("reserve.v.04"),
				wn.synset("halt.v.01"),
				wn.synset("hold.v.11"),
				wn.synset("hold.v.10"),
				wn.synset("hold.v.13"),
				wn.synset("hold.v.33"),
				wn.synset("hold.v.14"),
				wn.synset("hold.v.17"),
				wn.synset("prevail.v.02"),
				wn.synset("hold.v.16")],

	# home
	"U+392a":   [wn.synset("family.n.01"),
				wn.synset("dwelling.n.01"),
				wn.synset("home.n.03")],

	# home run
	"U+392b":   [wn.synset("bell_ringer.n.03")],

	# homosexuality, lesbianism
	"U+392c":   [wn.synset("homosexuality.n.01")],

	# honey
	"U+392d":   [wn.synset("honey.n.01")],

	# hop
	"U+392e":   [wn.synset("hop.v.01"),
				wn.synset("hop.v.03"),
				wn.synset("hop.v.02"),
				wn.synset("hop.v.05"),
				wn.synset("hop.v.04"),
				wn.synset("hop.v.06"),
				wn.synset("bounce.v.03")],

	# hope
	"U+392f":   [wn.synset("hope.v.01"),
				wn.synset("hope.v.03"),
				wn.synset("hope.v.02")],

	# trumpet, horn, cornet
	"U+3931":   [wn.synset("automobile_horn.n.01"),
				wn.synset("cornet.n.01")],

	# horseradish
	"U+3932":   [wn.synset("horseradish.n.02"),
				wn.synset("horseradish.n.03"),
				wn.synset("horseradish.n.01")],

	# hospital, clinic
	"U+3933":   [wn.synset("hospital.n.01")],

	# hot dog, frankfurter
	"U+3934":   [wn.synset("hotdog.n.02"),
				wn.synset("frank.n.02")],

	# meat, frozen meat, diced meat, chunks of meat, minced meat, ground meat, dried meat
	"U+3935":   [wn.synset("meat.n.01")],

	# hotel, motel
	"U+3936":   [wn.synset("hotel.n.01")],

	# hour, o'clock
	"U+3938":   [wn.synset("hour.n.01"),
				wn.synset("hour.n.02")],

	# who, that, which, whom
	"U+393c":   [wn.synset("world_health_organization.n.01")],

	# hug, cuddle, embrace, squeeze
	"U+3940":   [wn.synset("embrace.n.03"),
				wn.synset("embrace.n.02"),
				wn.synset("embrace.n.01"),
				wn.synset("squeeze.n.03"),
				wn.synset("squeeze.n.01"),
				wn.synset("squeeze.n.04"),
				wn.synset("squeeze.n.05"),
				wn.synset("power_play.n.01"),
				wn.synset("squeeze.n.08"),
				wn.synset("hug.n.01"),
				wn.synset("credit_crunch.n.01")],

	# humble, meek
	"U+3941":   [wn.synset("humble.a.02"),
				wn.synset("base.s.02"),
				wn.synset("humble.s.01")],

	# hummus
	"U+3943":   [wn.synset("hummus.n.01")],

	# hungry
	"U+3944":   [wn.synset("hungry.a.01"),
				wn.synset("athirst.s.01")],

	# hurt, pain, suffer
	"U+3945":   [wn.synset("hurt.v.02")],

	# hysterectomy
	"U+3946":   [wn.synset("hysterectomy.n.01")],

	# I, me, myself
	"U+3947":   [wn.synset("i.n.03"),
				wn.synset("maine.n.01"),
				wn.synset("ego.n.03"),
				wn.synset("iodine.n.01"),
				wn.synset("one.n.01")],

	# ice cream, sherbet, sorbet
	"U+3949":   [wn.synset("ice_cream.n.01")],

	# ice hockey
	"U+394a":   [wn.synset("ice_hockey.n.01")],

	# sport stick and puck, hockey stick
	"U+394b":   [wn.synset("hockey_stick.n.01")],

	# Iceland
	"U+394c":   [wn.synset("iceland.n.02")],

	# icy, frozen
	"U+394d":   [wn.synset("arctic.s.02"),
				wn.synset("frigid.s.03")],

	# bad conscience
	"U+3950":   [wn.synset("conscience.n.01")],

	# important, significant
	"U+3951":   [wn.synset("significant.a.01"),
				wn.synset("important.a.01")],

	# improve
	"U+3952":   [wn.synset("better.v.02")],

	# in, inside, interior, internal
	"U+3953":   [wn.synset("inside.n.01"),
				wn.synset("inside.n.02")],

	# incest
	"U+3954":   [wn.synset("incest.n.01")],

	# sexual intercourse, intercourse, copulation
	"U+3955":   [wn.synset("sexual_intercourse.n.01")],

	# include
	"U+3957":   [wn.synset("include.v.01")],

	# incorrect, bad, inaccurate, wrong
	"U+3958":   [wn.synset("incorrect.a.01")],

	# increase, enlarge
	"U+395a":   [wn.synset("increase.v.01")],

	# Independence Day
	"U+395b":   [wn.synset("independence_day.n.01")],

	# indigo
	"U+395d":   [wn.synset("anil.n.01"),
				wn.synset("indigo.n.03"),
				wn.synset("indigo.n.02")],

	# infertile, sterile
	"U+395f":   [wn.synset("aseptic.s.01"),
				wn.synset("sterile.s.03"),
				wn.synset("sterile.a.01")],

	# injure, hurt
	"U+3960":   [wn.synset("injure.v.01")],

	# instruction, teaching, direction
	"U+3961":   [wn.synset("teaching.n.01")],

	# interesting, interested
	"U+3963":   [wn.synset("interesting.a.01")],

	# international
	"U+3964":   [wn.synset("international.a.01")],

	# intimacy, closeness
	"U+3965":   [wn.synset("familiarity.n.03"),
				wn.synset("affair.n.02"),
				wn.synset("closeness.n.01")],

	# intimate, close
	"U+3967":   [wn.synset("close.a.01"),
				wn.synset("near.a.01"),
				wn.synset("close.a.02")],

	# invent
	"U+3968":   [wn.synset("invent.v.01"),
				wn.synset("fabricate.v.02")],

	# Ireland
	"U+3969":   [wn.synset("ireland.n.01"),
				wn.synset("ireland.n.02")],

	# ironing board
	"U+396b":   [wn.synset("ironing_board.n.01")],

	# Israel
	"U+396d":   [wn.synset("israel.n.01")],

	# apparent, clear, evident, obvious, plain
	"U+396f":   [wn.synset("clear.a.11"),
				wn.synset("plain.a.02"),
				wn.synset("clear.s.06"),
				wn.synset("clear.a.04"),
				wn.synset("clear.s.03"),
				wn.synset("clear.s.13"),
				wn.synset("clear.s.15"),
				wn.synset("plain.a.03"),
				wn.synset("clear.s.17"),
				wn.synset("clear.s.14"),
				wn.synset("clear.s.09"),
				wn.synset("clear.a.01"),
				wn.synset("homely.s.01"),
				wn.synset("absolved.s.01"),
				wn.synset("clean.s.02"),
				wn.synset("clean.s.03"),
				wn.synset("apparent.s.01"),
				wn.synset("clear.s.02"),
				wn.synset("apparent.s.02"),
				wn.synset("plain.s.05"),
				wn.synset("discernible.s.03"),
				wn.synset("clear.s.08"),
				wn.synset("obvious.a.01"),
				wn.synset("well-defined.a.02"),
				wn.synset("plain.s.06"),
				wn.synset("clear.s.05"),
				wn.synset("plain.s.04")],

	# its
	"U+3970":   [wn.synset("sus.n.01"),
				wn.synset("information_technology.n.01"),
				wn.synset("hog.n.03")],

	# intrauterine device, IUD
	"U+3971":   [wn.synset("spiral.n.04"),
				wn.synset("intrauterine_device.n.01"),
				wn.synset("coil.n.02"),
				wn.synset("coil.n.04"),
				wn.synset("spiral.n.01")],

	# Iyar
	"U+3972":   [wn.synset("iyar.n.01")],

	# jam, jelly, marmalade, preserves
	"U+3973":   [wn.synset("jam.n.01")],

	# January
	"U+3974":   [wn.synset("january.n.01")],

	# jealous
	"U+3975":   [wn.synset("covetous.s.01"),
				wn.synset("jealous.s.02")],

	# Jesus, Jesus Christ, Christ
	"U+3979":   [wn.synset("redeemer.n.02"),
				wn.synset("jesus.n.01")],

	# jet, jet plane
	"U+397a":   [wn.synset("jet.n.01")],

	# jewel
	"U+397b":   [wn.synset("jewel.n.02")],

	# Jewish
	"U+397d":   [wn.synset("jewish.a.01")],

	# joke
	"U+3980":   [wn.synset("joke.v.01"),
				wn.synset("joke.v.02")],

	# July
	"U+3981":   [wn.synset("july.n.01")],

	# jump rope, skipping rope
	"U+3982":   [wn.synset("jump_rope.n.01")],

	# June
	"U+3983":   [wn.synset("june.n.01")],

	# Kabbalat Shabbat
	"U+3984":   [wn.synset("kabbalah.n.02")],

	# Kali
	"U+3986":   [wn.synset("kali.n.02")],

	# keep, preserve, save
	"U+3987":   [wn.synset("keep_open.v.01"),
				wn.synset("salvage.v.01"),
				wn.synset("write.v.08"),
				wn.synset("save.v.02"),
				wn.synset("save.v.03"),
				wn.synset("deliver.v.08"),
				wn.synset("save.v.06"),
				wn.synset("save.v.04"),
				wn.synset("save.v.05"),
				wn.synset("save.v.09"),
				wn.synset("spare.v.01")],

	# kibbutz
	"U+3989":   [wn.synset("kibbutz.n.01")],

	# village
	"U+398a":   [wn.synset("village.n.01")],

	# wine
	"U+398d":   [wn.synset("wine.n.01")],

	# kill, murder
	"U+398e":   [wn.synset("murder.v.01")],

	# Kislev
	"U+3990":   [wn.synset("kislev.n.01")],

	# kitchen
	"U+3991":   [wn.synset("kitchen.n.01")],

	# kneeling
	"U+3993":   [wn.synset("kneel.n.01")],

	# kneel
	"U+3994":   [wn.synset("kneel.v.01")],

	# knit
	"U+3995":   [wn.synset("knit.v.01")],

	# know
	"U+3997":   [wn.synset("know.v.03")],

	# koala
	"U+3998":   [wn.synset("koala.n.01")],

	# eyeliner, kohl
	"U+3999":   [wn.synset("kohl.n.01")],

	# labour
	"U+399a":   [wn.synset("british_labour_party.n.01"),
				wn.synset("labor.n.02"),
				wn.synset("parturiency.n.01"),
				wn.synset("labor.n.01")],

	# Lag B'Omer
	"U+399c":   [wn.synset("lag_b'omer.n.01")],

	# lake, pond
	"U+399e":   [wn.synset("lake.n.01")],

	# Lakshmi
	"U+399f":   [wn.synset("lakshmi.n.01")],

	# lamb, mutton
	"U+39a0":   [wn.synset("lamb.n.05"),
				wn.synset("lamb.n.04"),
				wn.synset("lamb.n.03"),
				wn.synset("lamb.n.02"),
				wn.synset("lamb.n.01")],

	# sheep
	"U+39a1":   [wn.synset("sheep.n.01")],

	# landing, airplane landing
	"U+39a2":   [wn.synset("landing.n.01"),
				wn.synset("landing.n.03"),
				wn.synset("landing.n.02"),
				wn.synset("landing.n.04")],

	# week
	"U+39a6":   [wn.synset("week.n.03"),
				wn.synset("week.n.01")],

	# late
	"U+39a8":   [wn.synset("late.s.03"),
				wn.synset("late.s.04"),
				wn.synset("belated.s.01"),
				wn.synset("former.s.03"),
				wn.synset("late.a.01"),
				wn.synset("late.a.06"),
				wn.synset("late.a.05"),
				wn.synset("late.r.01")],

	# laundromat, launderette, laundry
	"U+39a9":   [wn.synset("laundry.n.02"),
				wn.synset("launderette.n.01"),
				wn.synset("laundry.n.01")],

	# bath, washing
	"U+39aa":   [wn.synset("sink.n.01"),
				wn.synset("wash.n.02"),
				wn.synset("bath.n.04"),
				wn.synset("bath.n.05"),
				wn.synset("bath.n.02"),
				wn.synset("bath.n.01"),
				wn.synset("bathroom.n.01"),
				wn.synset("laundry.n.01"),
				wn.synset("washbasin.n.02"),
				wn.synset("bathtub.n.01")],

	# leadership, guidance
	"U+39ac":   [wn.synset("leadership.n.01")],

	# leader, director, guide
	"U+39ae":   [wn.synset("guide.n.02"),
				wn.synset("guidebook.n.01"),
				wn.synset("leader.n.01")],

	# learn
	"U+39b0":   [wn.synset("learn.v.04")],

	# fewest, least
	"U+39b1":   [wn.synset("least.a.01"),
				wn.synset("few.a.01"),
				wn.synset("fewest.a.01")],

	# leather
	"U+39b2":   [wn.synset("leather.n.01")],

	# left turn, left
	"U+39b3":   [wn.synset("left_field.n.01"),
				wn.synset("left.n.05"),
				wn.synset("left.n.02"),
				wn.synset("left.n.03"),
				wn.synset("left.n.01")],

	# lemonade
	"U+39b4":   [wn.synset("lemonade.n.01")],

	# lend, loan
	"U+39b6":   [wn.synset("lend.v.02")],

	# leopard
	"U+39b7":   [wn.synset("leopard.n.02")],

	# fewer, less
	"U+39b8":   [wn.synset("fewer.a.01"),
				wn.synset("less.a.01")],

	# let, allow, permit
	"U+39b9":   [wn.synset("permit.v.01")],

	# letter, mail, post
	"U+39be":   [wn.synset("mail.v.01"),
				wn.synset("mail.v.02"),
				wn.synset("post.v.06"),
				wn.synset("post.v.08"),
				wn.synset("station.v.01"),
				wn.synset("stake.v.03"),
				wn.synset("post.v.01"),
				wn.synset("post.v.03"),
				wn.synset("post.v.02"),
				wn.synset("post.v.05"),
				wn.synset("post.v.10"),
				wn.synset("post.v.07"),
				wn.synset("post.v.12")],

	# letter carrier, postman, mailman
	"U+39bf":   [wn.synset("mailman.n.01")],

	# lettuce, leafy vegetable
	"U+39c1":   [wn.synset("lettuce.n.02")],

	# library
	"U+39c2":   [wn.synset("library.n.01"),
				wn.synset("library.n.02"),
				wn.synset("library.n.05")],

	# lie down, lie
	"U+39c3":   [wn.synset("lie.v.05")],

	# like
	"U+39c4":   [wn.synset("wish.v.02"),
				wn.synset("like.v.02"),
				wn.synset("like.v.03")],

	# lime
	"U+39c5":   [wn.synset("lime.n.06"),
				wn.synset("lime.n.04")],

	# linear, straight
	"U+39c7":   [wn.synset("square.s.05"),
				wn.synset("straight.a.02"),
				wn.synset("straight.a.03"),
				wn.synset("straight.a.06"),
				wn.synset("straight.a.08"),
				wn.synset("straight.s.10"),
				wn.synset("straight.s.01"),
				wn.synset("straight.s.14"),
				wn.synset("straight.s.04"),
				wn.synset("straight.s.05"),
				wn.synset("analogue.a.01"),
				wn.synset("square.s.06"),
				wn.synset("true.s.12"),
				wn.synset("uncoiled.a.01"),
				wn.synset("linear.a.01"),
				wn.synset("linear.a.02"),
				wn.synset("neat.s.06"),
				wn.synset("linear.s.05"),
				wn.synset("linear.s.04"),
				wn.synset("straight.s.09")],

	# lion
	"U+39c8":   [wn.synset("lion.n.01")],

	# mane
	"U+39c9":   [wn.synset("mane.n.01")],

	# lip
	"U+39ca":   [wn.synset("lip.n.01")],

	# lipstick
	"U+39cb":   [wn.synset("lipstick.n.01")],

	# list, inventory
	"U+39cc":   [wn.synset("list.n.01")],

	# live, dwell, reside
	"U+39cd":   [wn.synset("populate.v.01")],

	# living room, lounge, sitting room, front room, parlor, parlour, waiting room
	"U+39ce":   [wn.synset("living_room.n.01")],

	# lock
	"U+39cf":   [wn.synset("lock.v.01")],

	# lonely, lonesome
	"U+39d0":   [wn.synset("lonely.s.02")],

	# long
	"U+39d1":   [wn.synset("long.a.01"),
				wn.synset("long.a.02")],

	# longer
	"U+39d2":   [wn.synset("retentive.a.01"),
				wn.synset("long.a.05"),
				wn.synset("long.a.06"),
				wn.synset("long.a.01"),
				wn.synset("long.a.02"),
				wn.synset("long.s.07"),
				wn.synset("long.s.03"),
				wn.synset("farseeing.s.02"),
				wn.synset("long.s.09")],

	# longest
	"U+39d3":   [wn.synset("retentive.a.01"),
				wn.synset("long.a.05"),
				wn.synset("long.a.06"),
				wn.synset("long.a.01"),
				wn.synset("long.a.02"),
				wn.synset("long.s.07"),
				wn.synset("long.s.03"),
				wn.synset("farseeing.s.02"),
				wn.synset("long.s.09")],

	# lose
	"U+39d4":   [wn.synset("lose.v.07"),
				wn.synset("lose.v.05"),
				wn.synset("lose.v.02"),
				wn.synset("lose.v.01"),
				wn.synset("lose.v.08"),
				wn.synset("miss.v.01")],

	# loss
	"U+39d6":   [wn.synset("loss.n.01"),
				wn.synset("loss.n.06")],

	# loud, noisy
	"U+39d7":   [wn.synset("brassy.s.02"),
				wn.synset("forte.a.01"),
				wn.synset("noisy.s.02"),
				wn.synset("noisy.a.01"),
				wn.synset("loud.a.01")],

	# noise
	"U+39d8":   [wn.synset("noise.n.01")],

	# lovable
	"U+39d9":   [wn.synset("lovable.a.01"),
				wn.synset("pleasant.a.01")],

	# arrow
	"U+39da":   [wn.synset("arrow.n.02")],

	# lowness, shortness
	"U+39db":   [wn.synset("shortness.n.01"),
				wn.synset("shortness.n.03"),
				wn.synset("shortness.n.02"),
				wn.synset("shortness.n.05"),
				wn.synset("shortness.n.04"),
				wn.synset("foot.n.03"),
				wn.synset("bass.n.02"),
				wn.synset("bass.n.03"),
				wn.synset("abruptness.n.01"),
				wn.synset("short_circuit.n.01"),
				wn.synset("low_status.n.01"),
				wn.synset("bottom.n.02"),
				wn.synset("bottom.n.01"),
				wn.synset("lowness.n.03"),
				wn.synset("downheartedness.n.01"),
				wn.synset("lowness.n.04")],

	# shortness, length)
	"U+39dc":   [wn.synset("shortness.n.01"),
				wn.synset("shortness.n.03"),
				wn.synset("shortness.n.02"),
				wn.synset("shortness.n.05"),
				wn.synset("shortness.n.04"),
				wn.synset("abruptness.n.01")],

	# luck, fortune
	"U+39dd":   [wn.synset("fortune.n.02"),
				wn.synset("luck.n.02"),
				wn.synset("luck.n.03")],

	# lucky, fortunate
	"U+39de":   [wn.synset("lucky.s.01"),
				wn.synset("golden.s.06"),
				wn.synset("fortunate.a.01"),
				wn.synset("lucky.a.02"),
				wn.synset("fortunate.s.03"),
				wn.synset("fortunate.s.02")],

	# lunch, dinner
	"U+39e1":   [wn.synset("lunch.n.01")],

	# magazine, journal
	"U+39e2":   [wn.synset("magazine.n.01"),
				wn.synset("diary.n.01"),
				wn.synset("journal.n.02")],

	# often, frequent, frequently
	"U+39e3":   [wn.synset("frequently.r.01")],

	# mailbox, letterbox, postbox
	"U+39e4":   [wn.synset("postbox.n.01"),
				wn.synset("mailbox.n.01")],

	# making, production, fashioning
	"U+39e5":   [wn.synset("production.n.02"),
				wn.synset("production.n.07")],

	# make believe, pretend, imaginary
	"U+39e8":   [wn.synset("fanciful.s.02"),
				wn.synset("make-believe.s.01")],

	# fantasy, phantasy, imagination, illusion
	"U+39e9":   [wn.synset("illusion.n.01"),
				wn.synset("illusion.n.02"),
				wn.synset("imagination.n.01"),
				wn.synset("delusion.n.03"),
				wn.synset("fantasy.n.01"),
				wn.synset("fantasy.n.02")],

	# maker, manufacturer, producer
	"U+39ed":   [wn.synset("manufacturer.n.01")],

	# makeup
	"U+39ef":   [wn.synset("makeup.n.01")],

	# male genitals
	"U+39f0":   [wn.synset("male_genitalia.n.01"),
				wn.synset("man.n.01")],

	# manager, secretary
	"U+39f1":   [wn.synset("secretary.n.02")],

	# man made
	"U+39f2":   [wn.synset("man-made.s.01"),
				wn.synset("fat.s.05")],

	# map
	"U+39f3":   [wn.synset("map.n.01")],

	# March
	"U+39f5":   [wn.synset("march.n.01")],

	# margarine
	"U+39f6":   [wn.synset("margarine.n.01")],

	# marry
	"U+39f8":   [wn.synset("marry.v.01")],

	# mash, crush, squeeze, squash, pumpkin, mush, pulp
	"U+39f9":   [wn.synset("jam.v.03"),
				wn.synset("squash.v.01"),
				wn.synset("crush.v.04")],

	# mask, false face
	"U+39fd":   [wn.synset("mask.n.01")],

	# masturbation
	"U+39fe":   [wn.synset("masturbation.n.01")],

	# match
	"U+3a00":   [wn.synset("match.n.01")],

	# maturation
	"U+3a01":   [wn.synset("maturation.n.01")],

	# matzo
	"U+3a02":   [wn.synset("matzo.n.01")],

	# May
	"U+3a03":   [wn.synset("may.n.01")],

	# possibility
	"U+3a04":   [wn.synset("possibility.n.01"),
				wn.synset("possibility.n.02"),
				wn.synset("hypothesis.n.02"),
				wn.synset("possibility.n.04")],

	# existence, being
	"U+3a05":   [wn.synset("being.n.01")],

	# congratulate
	"U+3a06":   [wn.synset("congratulate.v.02")],

	# congratulations, best of luck, mazel tov
	"U+3a07":   [wn.synset("praise.n.01"),
				wn.synset("congratulation.n.02"),
				wn.synset("congratulation.n.01")],

	# mean, cruel, signify
	"U+3a08":   [wn.synset("mean.v.03")],

	# sharp, acid, sour
	"U+3a09":   [wn.synset("shrill.s.01"),
				wn.synset("crisp.s.01"),
				wn.synset("acuate.s.01"),
				wn.synset("sharp.s.05"),
				wn.synset("acute.s.03"),
				wn.synset("sharp.a.10"),
				wn.synset("sharp.s.11"),
				wn.synset("sharp.s.12"),
				wn.synset("sharp.a.09"),
				wn.synset("sharp.a.08"),
				wn.synset("abrupt.s.03"),
				wn.synset("astute.s.01")],

	# measure
	"U+3a0a":   [wn.synset("measure.v.03"),
				wn.synset("measure.v.01")],

	# meatball
	"U+3a0b":   [wn.synset("meatball.n.01")],

	# medical insurance
	"U+3a0c":   [wn.synset("health_care.n.01"),
				wn.synset("health_insurance.n.01")],

	# Megillah
	"U+3a0e":   [wn.synset("megillah.n.01"),
				wn.synset("megillah.n.02")],

	# menopause
	"U+3a0f":   [wn.synset("menopause.n.01")],

	# menstruation, menstrual period, period
	"U+3a10":   [wn.synset("menstruation.n.01")],

	# mental, intellectual, rational, thinking
	"U+3a11":   [wn.synset("cerebral.a.01"),
				wn.synset("mental.a.01"),
				wn.synset("mental.a.03"),
				wn.synset("mental.a.02"),
				wn.synset("intelligent.s.04"),
				wn.synset("rational.a.01"),
				wn.synset("rational.s.04"),
				wn.synset("rational.a.03"),
				wn.synset("mental.s.05"),
				wn.synset("intellectual.s.01"),
				wn.synset("genial.a.02"),
				wn.synset("intellectual.a.02")],

	# merry go round, carousel
	"U+3a12":   [wn.synset("carousel.n.02")],

	# metal
	"U+3a14":   [wn.synset("metallic_element.n.01"),
				wn.synset("alloy.n.01"),
				wn.synset("heavy_metal.n.02")],

	# mezuzah
	"U+3a16":   [wn.synset("mezuzah.n.01")],

	# microwave
	"U+3a18":   [wn.synset("microwave.v.01"),
				wn.synset("microwave.n.01"),
				wn.synset("microwave.n.02")],

	# middle, centre
	"U+3a19":   [wn.synset("center.n.01")],

	# midsummer
	"U+3a1a":   [wn.synset("summer_solstice.n.01")],

	# military plane
	"U+3a1c":   [wn.synset("warplane.n.01")],

	# soldier, warrior
	"U+3a1f":   [wn.synset("soldier.n.01")],

	# milkman
	"U+3a20":   [wn.synset("milkman.n.01")],

	# milkshake
	"U+3a22":   [wn.synset("milkshake.n.01")],

	# minister, pastor, preacher, priest, rabbi
	"U+3a24":   [wn.synset("priest.n.02"),
				wn.synset("priest.n.01")],

	# minute
	"U+3a26":   [wn.synset("minute.n.01")],

	# miss, lose
	"U+3a29":   [wn.synset("miss.v.02")],

	# mistake, error, fault, mishap
	"U+3a2a":   [wn.synset("mistake.n.01"),
				wn.synset("erroneousness.n.01"),
				wn.synset("error.n.07"),
				wn.synset("error.n.04"),
				wn.synset("error.n.05"),
				wn.synset("error.n.03")],

	# mite, tick
	"U+3a2c":   [wn.synset("mite.n.02"),
				wn.synset("touch.n.06"),
				wn.synset("tick.n.02"),
				wn.synset("tick.n.01"),
				wn.synset("check_mark.n.01"),
				wn.synset("tick.n.04")],

	# mixture
	"U+3a2d":   [wn.synset("concoction.n.01"),
				wn.synset("mixture.n.01"),
				wn.synset("mix.n.02")],

	# recreation room, moadan
	"U+3a2e":   [wn.synset("rumpus_room.n.01"),
				wn.synset("recreation_room.n.01")],

	# monkey, ape, gorilla, primate
	"U+3a2f":   [wn.synset("archpriest.n.01"),
				wn.synset("primate.n.02"),
				wn.synset("monkey.n.01"),
				wn.synset("imp.n.02"),
				wn.synset("ape.n.01"),
				wn.synset("anthropoid.n.01"),
				wn.synset("copycat.n.01"),
				wn.synset("gorilla.n.01")],

	# monster
	"U+3a31":   [wn.synset("monster.n.01"),
				wn.synset("monster.n.04"),
				wn.synset("freak.n.01")],

	# strange
	"U+3a32":   [wn.synset("strange.a.01"),
				wn.synset("strange.s.02")],

	# moose, elk
	"U+3a34":   [wn.synset("elk.n.01")],

	# good conscience
	"U+3a35":   [wn.synset("conscience.n.01")],

	# mortal
	"U+3a36":   [wn.synset("mortal.s.03"),
				wn.synset("deadly.s.01"),
				wn.synset("mortal.a.01"),
				wn.synset("deadly.s.04")],

	# moshav
	"U+3a37":   [wn.synset("moshav.n.01")],

	# Muslim, Moslem, Islamic
	"U+3a39":   [wn.synset("muslim.a.01")],

	# mosquito
	"U+3a3b":   [wn.synset("mosquito.n.01")],

	# mountain berry, cowberry, lingonberry
	"U+3a3f":   [wn.synset("cowberry.n.01")],

	# mouse, pointing device
	"U+3a40":   [wn.synset("mouse.n.04")],

	# move bowels, defecate, stool, shit, ca ca
	"U+3a41":   [wn.synset("denounce.v.04"),
				wn.synset("stool.v.04"),
				wn.synset("stool.v.03"),
				wn.synset("stool.v.02"),
				wn.synset("stool.v.01")],

	# movie, film
	"U+3a42":   [wn.synset("movie.n.01"),
				wn.synset("film.n.03")],

	# movie theatre, cinema
	"U+3a44":   [wn.synset("cinema.n.02")],

	# quantity
	"U+3a45":   [wn.synset("quantity.n.03")],

	# puddle, pool
	"U+3a46":   [wn.synset("pond.n.01"),
				wn.synset("puddle.n.01"),
				wn.synset("pool.n.08"),
				wn.synset("pool.n.05"),
				wn.synset("pool.n.07"),
				wn.synset("pool.n.06"),
				wn.synset("pool.n.01"),
				wn.synset("pool.n.03"),
				wn.synset("pool.n.09"),
				wn.synset("consortium.n.01")],

	# multiply
	"U+3a47":   [wn.synset("multiply.v.01")],

	# multitude
	"U+3a48":   [wn.synset("battalion.n.02")],

	# museum
	"U+3a49":   [wn.synset("museum.n.01")],

	# musical group
	"U+3a4b":   [wn.synset("musical_organization.n.01")],

	# musical instrument
	"U+3a4c":   [wn.synset("musical_instrument.n.01"),
				wn.synset("stringed_instrument.n.01"),
				wn.synset("bowed_stringed_instrument.n.01")],

	# musician
	"U+3a4e":   [wn.synset("musician.n.02"),
				wn.synset("musician.n.01")],

	# muskrat
	"U+3a4f":   [wn.synset("muskrat.n.02")],

	# my, mine
	"U+3a51":   [wn.synset("mine.n.01"),
				wn.synset("mine.n.02")],

	# nail polish, nail varnish
	"U+3a52":   [wn.synset("nail_polish.n.01")],

	# napkin, serviette
	"U+3a53":   [wn.synset("napkin.n.01")],

	# narrow
	"U+3a54":   [wn.synset("narrow.a.01")],

	# naughty, not nice
	"U+3a55":   [wn.synset("blue.s.05"),
				wn.synset("disobedient.a.01"),
				wn.synset("naughty.s.02")],

	# navy
	"U+3a56":   [wn.synset("navy.n.01")],

	# nearness, closeness, proximity
	"U+3a57":   [wn.synset("meanness.n.02"),
				wn.synset("proximity.n.02"),
				wn.synset("proximity.n.01"),
				wn.synset("stuffiness.n.02"),
				wn.synset("familiarity.n.03"),
				wn.synset("closeness.n.05"),
				wn.synset("nearness.n.01"),
				wn.synset("proximity.n.03"),
				wn.synset("closeness.n.01")],

	# necessary, necessarily, needed
	"U+3a58":   [wn.synset("necessary.a.01")],

	# need
	"U+3a59":   [wn.synset("need.n.01")],

	# neck
	"U+3a5a":   [wn.synset("neck.n.01")],

	# neighbour
	"U+3a5d":   [wn.synset("neighbor.n.01")],

	# neither
	"U+3a5f":   [wn.synset("neither.s.01")],

	# nephew
	"U+3a60":   [wn.synset("nephew.n.01")],

	# Netherlands, Holland
	"U+3a61":   [wn.synset("netherlands.n.01")],

	# newness, novelty
	"U+3a63":   [wn.synset("news.n.01"),
				wn.synset("news.n.04"),
				wn.synset("newness.n.01"),
				wn.synset("knickknack.n.01"),
				wn.synset("novelty.n.02"),
				wn.synset("bangle.n.02"),
				wn.synset("freshness.n.02"),
				wn.synset("news_program.n.01")],

	# New Year's Day
	"U+3a65":   [wn.synset("new_year's_day.n.01")],

	# newspaper, bulletin, newsletter
	"U+3a66":   [wn.synset("newspaper.n.03"),
				wn.synset("newspaper.n.02"),
				wn.synset("newspaper.n.01")],

	# next
	"U+3a68":   [wn.synset("following.s.02")],

	# next week
	"U+3a69":   [wn.synset("oil.n.01"),
				wn.synset("margarine.n.01"),
				wn.synset("petroleum.n.01"),
				wn.synset("vegetable_oil.n.01")],

	# nice, pleasant
	"U+3a6b":   [wn.synset("pleasant.a.01")],

	# niece
	"U+3a6c":   [wn.synset("niece.n.01")],

	# nipple
	"U+3a6d":   [wn.synset("nipple.n.01")],

	# Nisan, Nissan
	"U+3a6e":   [wn.synset("nisan.n.01")],

	# no one, nobody
	"U+3a70":   [wn.synset("cipher.n.04")],

	# nocturnal emission, wet dream
	"U+3a71":   [wn.synset("nocturnal_emission.n.01"),
				wn.synset("wet_dream.n.01")],

	# no speech, anarthria
	"U+3a73":   [wn.synset("anarthria.n.01")],

	# northern
	"U+3a77":   [wn.synset("northern.a.04")],

	# notebook, writing book
	"U+3a78":   [wn.synset("notebook.n.02"),
				wn.synset("notebook.n.01")],

	# November
	"U+3a7a":   [wn.synset("november.n.01")],

	# nuclear energy
	"U+3a7e":   [wn.synset("no.r.03"),
				wn.synset("not.r.01"),
				wn.synset("atomic_energy.n.01")],

	# nuclear fallout, radioactive dust
	"U+3a7f":   [wn.synset("fallout.n.01")],

	# nurse
	"U+3a82":   [wn.synset("nurse.n.01")],

	# nut
	"U+3a84":   [wn.synset("en.n.01"),
				wn.synset("testis.n.01"),
				wn.synset("crackpot.n.01"),
				wn.synset("nut.n.01"),
				wn.synset("addict.n.01"),
				wn.synset("nut.n.03"),
				wn.synset("nut.n.02")],

	# obey, comply
	"U+3a85":   [wn.synset("comply.v.01"),
				wn.synset("obey.v.01")],

	# ocean, sea
	"U+3a87":   [wn.synset("sea.n.01"),
				wn.synset("ocean.n.02")],

	# October
	"U+3a88":   [wn.synset("october.n.01")],

	# office
	"U+3a89":   [wn.synset("office.n.01"),
				wn.synset("agency.n.01")],

	# old, elderly
	"U+3a8a":   [wn.synset("old.a.01")],

	# young
	"U+3a8b":   [wn.synset("young.a.01")],

	# once
	"U+3a8c":   [wn.synset("once.r.02"),
				wn.synset("once.r.03"),
				wn.synset("once.r.01"),
				wn.synset("time.n.01")],

	# operation
	"U+3a8d":   [wn.synset("operation.n.06")],

	# opossum, possum
	"U+3a8e":   [wn.synset("opossum.n.02")],

	# oral sex
	"U+3a8f":   [wn.synset("oral_sex.n.01")],

	# orange, citrus fruit
	"U+3a91":   [wn.synset("orange.n.03"),
				wn.synset("orange.n.02"),
				wn.synset("citrus.n.01"),
				wn.synset("orange.n.05"),
				wn.synset("orange.n.04"),
				wn.synset("orange.n.01")],

	# orchard
	"U+3a93":   [wn.synset("grove.n.02")],

	# organize, arrange
	"U+3a94":   [wn.synset("stage.v.02"),
				wn.synset("dress.v.16"),
				wn.synset("unionize.v.02"),
				wn.synset("form.v.01"),
				wn.synset("format.v.01"),
				wn.synset("arrange.v.06"),
				wn.synset("mastermind.v.01"),
				wn.synset("organize.v.02"),
				wn.synset("arrange.v.07"),
				wn.synset("arrange.v.01"),
				wn.synset("arrange.v.02"),
				wn.synset("organize.v.04"),
				wn.synset("organize.v.05")],

	# orgasm
	"U+3a95":   [wn.synset("orgasm.n.01")],

	# ostrich
	"U+3a97":   [wn.synset("ostrich.n.02")],

	# our, ours
	"U+3a98":   [wn.synset("spring.n.01")],

	# we, us, ourselves
	"U+3a99":   [wn.synset("maine.n.01"),
				wn.synset("uranium.n.01"),
				wn.synset("united_states.n.01"),
				wn.synset("u.n.03"),
				wn.synset("uracil.n.01")],

	# out, exterior, external, outside
	"U+3a9a":   [wn.synset("outside.n.01"),
				wn.synset("outside.n.02")],

	# outing, excursion
	"U+3a9b":   [wn.synset("excursion.n.01")],

	# oval, ellipse, elliptic, elliptical
	"U+3a9d":   [wn.synset("ellipse.n.01")],

	# ovary
	"U+3a9f":   [wn.synset("ovary.n.02")],

	# owl, night bird
	"U+3aa0":   [wn.synset("owl.n.01")],

	# own, possess
	"U+3aa1":   [wn.synset("own.v.01"),
				wn.synset("possess.v.03")],

	# ownership, possession
	"U+3aa2":   [wn.synset("possession.n.01")],

	# ox
	"U+3aa4":   [wn.synset("ox.n.01")],

	# oyster, clam
	"U+3aa5":   [wn.synset("oyster.n.01")],

	# pail, bucket
	"U+3aa6":   [wn.synset("bucket.n.01")],

	# sick, ill
	"U+3aa7":   [wn.synset("ill.a.01")],

	# painful, painfully, sore
	"U+3aa8":   [wn.synset("painful.a.01")],

	# paint, dye
	"U+3aa9":   [wn.synset("paint.v.01"),
				wn.synset("paint.v.02")],

	# painter
	"U+3aab":   [wn.synset("painter.n.01")],

	# pair
	"U+3aac":   [wn.synset("couple.n.04"),
				wn.synset("pair.n.03"),
				wn.synset("pair.n.01")],

	# palm
	"U+3aad":   [wn.synset("palm.n.03")],

	# pants, jeans, slacks, trousers
	"U+3aae":   [wn.synset("gasp.n.01"),
				wn.synset("bloomers.n.01"),
				wn.synset("trouser.n.02"),
				wn.synset("trouser.n.01"),
				wn.synset("slacks.n.01"),
				wn.synset("slump.n.01"),
				wn.synset("jean.n.01"),
				wn.synset("mire.n.01"),
				wn.synset("slack.n.03"),
				wn.synset("slack.n.01"),
				wn.synset("denim.n.02"),
				wn.synset("slack.n.05"),
				wn.synset("slack.n.06"),
				wn.synset("pant.n.01")],

	# parakeet, budgie
	"U+3aaf":   [wn.synset("parakeet.n.01")],

	# parrot, myna, talking bird
	"U+3ab0":   [wn.synset("parrot.n.01")],

	# paratrooper
	"U+3ab1":   [wn.synset("paratrooper.n.01")],

	# parsnip
	"U+3ab4":   [wn.synset("parsnip.n.01"),
				wn.synset("parsnip.n.03"),
				wn.synset("parsnip.n.02")],

	# white
	"U+3ab5":   [wn.synset("white.n.01")],

	# party, festival
	"U+3ab6":   [wn.synset("party.n.02")],

	# patience
	"U+3ab8":   [wn.synset("patience.n.01")],

	# be patient
	"U+3aba":   [wn.synset("patient.n.01"),
				wn.synset("patient.a.01")],

	# pay, spend
	"U+3abb":   [wn.synset("pay.v.01")],

	# peaceful, serene, calm, lull
	"U+3abc":   [wn.synset("serene.s.02"),
				wn.synset("peaceful.a.01"),
				wn.synset("calm.s.01"),
				wn.synset("passive.s.02"),
				wn.synset("calm.a.02")],

	# peacock
	"U+3abd":   [wn.synset("peacock.n.02")],

	# peanut butter
	"U+3abe":   [wn.synset("peanut_butter.n.01")],

	# peel
	"U+3ac0":   [wn.synset("peel.n.02")],

	# pelican
	"U+3ac1":   [wn.synset("pelican.n.01")],

	# penguin
	"U+3ac2":   [wn.synset("penguin.n.01")],

	# adding, additive
	"U+3ac3":   [wn.synset("additive.n.01"),
				wn.synset("summation.n.04"),
				wn.synset("lend.v.01"),
				wn.synset("total.v.02"),
				wn.synset("add.v.04"),
				wn.synset("add.v.06"),
				wn.synset("add.v.01"),
				wn.synset("add.v.02")],

	# perfume, fragrance, aroma, scent
	"U+3ac5":   [wn.synset("olfactory_property.n.01"),
				wn.synset("aroma.n.02"),
				wn.synset("perfume.n.02")],

	# standing
	"U+3ac6":   [wn.synset("person.n.01"),
				wn.synset("person.n.02"),
				wn.synset("person.n.03"),
				wn.synset("standing.n.03"),
				wn.synset("standing.n.02"),
				wn.synset("standing.n.01")],

	# weakness
	"U+3ac7":   [wn.synset("failing.n.01")],

	# pet
	"U+3ac8":   [wn.synset("pet.n.01")],

	# photograph, photo, pic
	"U+3ac9":   [wn.synset("photograph.n.01")],

	# picnic
	"U+3aca":   [wn.synset("picnic.n.03")],

	# pie, tart
	"U+3acb":   [wn.synset("pie.n.01"),
				wn.synset("proto-indo_european.n.01"),
				wn.synset("tart.n.02"),
				wn.synset("tart.n.03"),
				wn.synset("prostitute.n.01")],

	# pillowcase
	"U+3acc":   [wn.synset("case.n.19")],

	# pilot
	"U+3ace":   [wn.synset("pilot.n.01")],

	# pink
	"U+3acf":   [wn.synset("pink.n.01")],

	# pizza slice, sector, circle sector
	"U+3ad0":   [wn.synset("sector.n.03")],

	# plastic
	"U+3ad3":   [wn.synset("plastic.n.01")],

	# play, recreation
	"U+3ad4":   [wn.synset("play.n.08"),
				wn.synset("turn.n.03"),
				wn.synset("fun.n.02"),
				wn.synset("play.n.01"),
				wn.synset("play.n.03"),
				wn.synset("play.n.02"),
				wn.synset("play.n.05"),
				wn.synset("play.n.17"),
				wn.synset("play.n.14"),
				wn.synset("play.n.06"),
				wn.synset("looseness.n.05"),
				wn.synset("free_rein.n.01"),
				wn.synset("gambling.n.01"),
				wn.synset("maneuver.n.03"),
				wn.synset("bid.n.02"),
				wn.synset("shimmer.n.01"),
				wn.synset("playing_period.n.01")],

	# playground
	"U+3ad7":   [wn.synset("playground.n.02")],

	# playroom, family room, recreation room
	"U+3ad9":   [wn.synset("rumpus_room.n.01")],

	# plug
	"U+3ada":   [wn.synset("bunghole.n.02"),
				wn.synset("ballyhoo.n.01"),
				wn.synset("hack.n.06"),
				wn.synset("spark_plug.n.01"),
				wn.synset("plug.n.01"),
				wn.synset("spine.n.03"),
				wn.synset("fireplug.n.01"),
				wn.synset("chew.n.01"),
				wn.synset("plug.n.05"),
				wn.synset("fishbone.n.01")],

	# pocket
	"U+3adb":   [wn.synset("pocket.n.01"),
				wn.synset("pouch.n.03")],

	# poem
	"U+3adc":   [wn.synset("poem.n.01")],

	# point of view
	"U+3ade":   [wn.synset("point_of_view.n.02"),
				wn.synset("point_of_view.n.01")],

	# position
	"U+3adf":   [wn.synset("status.n.01"),
				wn.synset("military_position.n.01"),
				wn.synset("position.n.06")],

	# poison
	"U+3ae0":   [wn.synset("poison.n.01"),
				wn.synset("poison.n.02")],

	# polenta
	"U+3ae1":   [wn.synset("polenta.n.01")],

	# police officer, policeman, policewoman
	"U+3ae2":   [wn.synset("policeman.n.01")],

	# pollution
	"U+3ae4":   [wn.synset("pollution.n.01")],

	# poor
	"U+3ae5":   [wn.synset("poor.a.02"),
				wn.synset("hapless.s.01")],

	# popcorn
	"U+3ae6":   [wn.synset("popcorn.n.02")],

	# greater than
	"U+3ae7":   [wn.synset("relationship.n.02")],

	# maybe, perhaps, possibly
	"U+3ae8":   [wn.synset("possibly.r.01")],

	# post office
	"U+3ae9":   [wn.synset("post_office.n.01")],

	# potato
	"U+3aea":   [wn.synset("potato.n.01")],

	# pound sterling
	"U+3aeb":   [wn.synset("british_pound.n.01")],

	# practise, practice, drill, exercise, rehearse
	"U+3aec":   [wn.synset("exercise.v.04"),
				wn.synset("practice.v.01"),
				wn.synset("drill.v.03"),
				wn.synset("exert.v.01")],

	# repetition, copying, duplication, replication
	"U+3aed":   [wn.synset("repeat.n.01")],

	# pray
	"U+3aee":   [wn.synset("pray.v.01")],

	# to, toward, towards
	"U+3aef":   [wn.synset("grain.n.10"),
				wn.synset("verse.n.03"),
				wn.synset("verse.n.02"),
				wn.synset("reverse.n.04"),
				wn.synset("cry.n.05"),
				wn.synset("line.n.05")],

	# prayer book, Siddur
	"U+3af0":   [wn.synset("prayer_book.n.01")],

	# pregnancy
	"U+3af2":   [wn.synset("pregnancy.n.01")],

	# pregnant
	"U+3af3":   [wn.synset("pregnant.a.01")],

	# prepare, set, set up, ready, gear up, fix, prepared
	"U+3af6":   [wn.synset("ready.a.01")],

	# preparation, readying, readiness, preparedness
	"U+3af7":   [wn.synset("training.n.01"),
				wn.synset("preparation.n.01")],

	# prepare food, cook
	"U+3afb":   [wn.synset("cook.v.02")],

	# cooking, cookery, preparation
	"U+3afc":   [wn.synset("cooking.n.01")],

	# prison, jail
	"U+3afe":   [wn.synset("jail.n.01"),
				wn.synset("prison.n.01")],

	# private
	"U+3b00":   [wn.synset("private.a.01")],

	# public
	"U+3b02":   [wn.synset("public.a.01")],

	# probable, likely, probably
	"U+3b03":   [wn.synset("probable.a.01")],

	# problem
	"U+3b05":   [wn.synset("problem.n.02")],

	# promise, pledge
	"U+3b06":   [wn.synset("promise.n.02"),
				wn.synset("promise.n.01")],

	# prostitution
	"U+3b07":   [wn.synset("prostitution.n.01")],

	# protect, cover, shelter, take care of, refuge
	"U+3b08":   [wn.synset("recourse.n.01"),
				wn.synset("recourse.n.02"),
				wn.synset("refuge.n.03"),
				wn.synset("remittance.n.01"),
				wn.synset("storeroom.n.01"),
				wn.synset("cupboard.n.01"),
				wn.synset("consignment.n.03"),
				wn.synset("throw-in.n.01"),
				wn.synset("shelter.n.01"),
				wn.synset("storehouse.n.01"),
				wn.synset("tax_shelter.n.01"),
				wn.synset("shelter.n.05"),
				wn.synset("shelter.n.02"),
				wn.synset("protection.n.04"),
				wn.synset("safety.n.02")],

	# protest, object, oppose, objection, opposition, resist, resistance
	"U+3b09":   [wn.synset("protest.v.01"),
				wn.synset("protest.v.02")],

	# proud
	"U+3b0a":   [wn.synset("proud.a.01")],

	# province, county, region, state
	"U+3b0b":   [wn.synset("country.n.02"),
				wn.synset("state.n.01"),
				wn.synset("state.n.03"),
				wn.synset("state.n.02"),
				wn.synset("state.n.04"),
				wn.synset("state_of_matter.n.01")],

	# puberty
	"U+3b0d":   [wn.synset("puberty.n.01")],

	# puncture, prick
	"U+3b0f":   [wn.synset("sting.v.02")],

	# puppet
	"U+3b10":   [wn.synset("puppet.n.03"),
				wn.synset("creature.n.03"),
				wn.synset("puppet.n.01")],

	# puppy
	"U+3b11":   [wn.synset("puppy.n.02"),
				wn.synset("puppy.n.01")],

	# Purim
	"U+3b12":   [wn.synset("purim.n.01")],

	# purple, violet
	"U+3b13":   [wn.synset("violet.n.02")],

	# purse, pocketbook, wallet
	"U+3b14":   [wn.synset("wallet.n.01"),
				wn.synset("purse.n.03")],

	# put, locate, place
	"U+3b15":   [wn.synset("invest.v.01"),
				wn.synset("situate.v.01"),
				wn.synset("set.v.09"),
				wn.synset("target.v.01"),
				wn.synset("place.v.09"),
				wn.synset("place.v.11"),
				wn.synset("place.v.06"),
				wn.synset("place.v.12"),
				wn.synset("place.v.05"),
				wn.synset("place.v.16"),
				wn.synset("locate.v.03"),
				wn.synset("locate.v.01"),
				wn.synset("frame.v.04"),
				wn.synset("settle.v.04"),
				wn.synset("put.v.08"),
				wn.synset("put.v.07"),
				wn.synset("put.v.04"),
				wn.synset("put.v.02"),
				wn.synset("put.v.01"),
				wn.synset("place.v.15"),
				wn.synset("rate.v.01"),
				wn.synset("station.v.01"),
				wn.synset("place.v.02"),
				wn.synset("arrange.v.07"),
				wn.synset("identify.v.01")],

	# jigsaw puzzle
	"U+3b16":   [wn.synset("jigsaw_puzzle.n.01")],

	# pyjama, nightgown, nightie, pajama
	"U+3b17":   [wn.synset("pajama.n.02")],

	# quick, fast, quickly, rapid, rapidly
	"U+3b18":   [wn.synset("fast.a.01"),
				wn.synset("fast.a.02"),
				wn.synset("flying.s.02"),
				wn.synset("rapid.s.01"),
				wn.synset("immediate.s.05"),
				wn.synset("debauched.s.01"),
				wn.synset("quick.s.04"),
				wn.synset("quick.s.06"),
				wn.synset("fast.a.03"),
				wn.synset("quick.s.01"),
				wn.synset("quickly.r.01"),
				wn.synset("cursorily.r.01"),
				wn.synset("rapid.s.02"),
				wn.synset("fast.s.04"),
				wn.synset("fast.s.05"),
				wn.synset("fast.s.10"),
				wn.synset("promptly.r.01"),
				wn.synset("agile.s.01"),
				wn.synset("fast.s.08"),
				wn.synset("firm.s.10")],

	# quickness, rapidity, speediness
	"U+3b19":   [wn.synset("fast.r.01"),
				wn.synset("express.n.02"),
				wn.synset("quickly.r.01"),
				wn.synset("cursorily.r.01"),
				wn.synset("mental_quickness.n.01"),
				wn.synset("fast.a.01"),
				wn.synset("celerity.n.01"),
				wn.synset("adeptness.n.01"),
				wn.synset("promptly.r.01"),
				wn.synset("quick.s.01")],

	# quiet, quietly
	"U+3b1c":   [wn.synset("placid.s.01"),
				wn.synset("hushed.s.01"),
				wn.synset("quietly.r.02"),
				wn.synset("quiet.s.03"),
				wn.synset("quiet.a.06"),
				wn.synset("quiet.a.01"),
				wn.synset("quiet.a.02"),
				wn.synset("restfully.r.01"),
				wn.synset("quietly.r.03"),
				wn.synset("softly.r.01")],

	# rabbit, hare
	"U+3b1d":   [wn.synset("rabbit.n.01")],

	# rabies
	"U+3b1e":   [wn.synset("rabies.n.01")],

	# racket, racquet
	"U+3b1f":   [wn.synset("racket.n.04")],

	# radio
	"U+3b20":   [wn.synset("radio_receiver.n.01")],

	# radish
	"U+3b21":   [wn.synset("radish.n.03")],

	# raincoat
	"U+3b22":   [wn.synset("raincoat.n.01")],

	# rainy
	"U+3b24":   [wn.synset("showery.s.01")],

	# rake
	"U+3b26":   [wn.synset("rake.n.03")],

	# rape
	"U+3b28":   [wn.synset("rape.n.01"),
				wn.synset("rape.n.03"),
				wn.synset("rape.n.02")],

	# raw, uncooked
	"U+3b29":   [wn.synset("raw.a.03")],

	# read
	"U+3b2a":   [wn.synset("read.v.01")],

	# reading
	"U+3b2b":   [wn.synset("reading.n.01")],

	# real, really
	"U+3b2d":   [wn.synset("real.a.01")],

	# recent, recently
	"U+3b2e":   [wn.synset("recent.s.01")],

	# recipe
	"U+3b2f":   [wn.synset("recipe.n.01")],

	# CD, record
	"U+3b31":   [wn.synset("magnetic_disk.n.01"),
				wn.synset("candle.n.02"),
				wn.synset("disk.n.01"),
				wn.synset("record.n.01"),
				wn.synset("record.n.03"),
				wn.synset("record.n.04"),
				wn.synset("record.n.05"),
				wn.synset("record.n.06"),
				wn.synset("record.n.07"),
				wn.synset("puck.n.02"),
				wn.synset("certificate_of_deposit.n.01"),
				wn.synset("compact_disk.n.01"),
				wn.synset("phonograph_record.n.01"),
				wn.synset("cadmium.n.01"),
				wn.synset("criminal_record.n.01"),
				wn.synset("discus.n.02")],

	# recording disk
	"U+3b32":   [wn.synset("disk.n.02"),
				wn.synset("slice.n.05")],

	# CD player, record player, stereo
	"U+3b33":   [wn.synset("record_player.n.01")],

	# rectangular, oblong
	"U+3b36":   [wn.synset("rectangular.s.01")],

	# sorry
	"U+3b38":   [wn.synset("apology.n.01"),
				wn.synset("excuse.n.01"),
				wn.synset("good-for-nothing.s.01"),
				wn.synset("blue.s.08"),
				wn.synset("regretful.a.01"),
				wn.synset("deplorable.s.01")],

	# reindeer, caribou
	"U+3b39":   [wn.synset("caribou.n.01")],

	# less than
	"U+3b3a":   [wn.synset("relationship.n.02")],

	# remembrance day
	"U+3b3b":   [wn.synset("commemoration.n.01"),
				wn.synset("remembrance_day.n.01")],

	# repeat, copy, duplicate, reproduce
	"U+3b3d":   [wn.synset("repeat.v.01"),
				wn.synset("repeat.v.04")],

	# reproduction
	"U+3b3e":   [wn.synset("reproduction.n.01")],

	# request
	"U+3b3f":   [wn.synset("request.v.01")],

	# resent
	"U+3b41":   [wn.synset("begrudge.v.02")],

	# resident
	"U+3b42":   [wn.synset("resident.n.01")],

	# residential institution, group home, hostel, residential home
	"U+3b43":   [wn.synset("internship.n.01"),
				wn.synset("hostel.n.02"),
				wn.synset("boarding_school.n.01"),
				wn.synset("hostel.n.01")],

	# respect, admiration
	"U+3b44":   [wn.synset("deference.n.01"),
				wn.synset("regard.n.06"),
				wn.synset("respect.n.01"),
				wn.synset("respect.n.03")],

	# rest period, break
	"U+3b45":   [wn.synset("pause.n.01")],

	# restaurant, cafeteria
	"U+3b47":   [wn.synset("restaurant.n.01")],

	# return, come back, reverse
	"U+3b48":   [wn.synset("return.v.01"),
				wn.synset("come_back.v.01")],

	# rhyme
	"U+3b49":   [wn.synset("rhyme.n.01")],

	# rhythm method
	"U+3b4b":   [wn.synset("rhythm_method_of_birth_control.n.01")],

	# ribbon, tape
	"U+3b4c":   [wn.synset("ribbon.n.01"),
				wn.synset("ribbon.n.03"),
				wn.synset("ribbon.n.04"),
				wn.synset("tape.n.03"),
				wn.synset("decoration.n.02"),
				wn.synset("tape.n.01"),
				wn.synset("tape.n.04"),
				wn.synset("magnetic_tape.n.01"),
				wn.synset("tape.n.02")],

	# rich, wealthy
	"U+3b4d":   [wn.synset("affluent.s.01"),
				wn.synset("abundance.n.01"),
				wn.synset("affluence.n.01"),
				wn.synset("prosperity.n.01"),
				wn.synset("rich.s.09"),
				wn.synset("rich.s.06"),
				wn.synset("full-bodied.s.01"),
				wn.synset("rich.s.11"),
				wn.synset("rich.s.03"),
				wn.synset("money.n.02"),
				wn.synset("deep.s.07"),
				wn.synset("profusion.n.01"),
				wn.synset("fat.s.05"),
				wn.synset("rich.a.07"),
				wn.synset("ample.s.02"),
				wn.synset("rich.a.01"),
				wn.synset("rich.a.02"),
				wn.synset("rich.a.08"),
				wn.synset("wealth.n.01"),
				wn.synset("wealth.n.03")],

	# rickshaw
	"U+3b4e":   [wn.synset("jinrikisha.n.01")],

	# rifle, shotgun
	"U+3b4f":   [wn.synset("rifle.n.01")],

	# right turn, right
	"U+3b50":   [wn.synset("right.n.08"),
				wn.synset("right.n.02"),
				wn.synset("right.n.01"),
				wn.synset("right.n.06"),
				wn.synset("right.n.07"),
				wn.synset("right.n.04"),
				wn.synset("right.n.05"),
				wn.synset("right_field.n.01")],

	# rise, ascend, go up
	"U+3b51":   [wn.synset("resurrect.v.03"),
				wn.synset("rise.v.11"),
				wn.synset("burn_down.v.01"),
				wn.synset("rise.v.12"),
				wn.synset("surface.v.01"),
				wn.synset("rebel.v.01"),
				wn.synset("ascend.v.05"),
				wn.synset("ascend.v.04"),
				wn.synset("ascend.v.03"),
				wn.synset("ascend.v.02"),
				wn.synset("ascend.v.01"),
				wn.synset("get_up.v.02"),
				wn.synset("arise.v.03"),
				wn.synset("ascend.v.08"),
				wn.synset("rise.v.02"),
				wn.synset("climb.v.01"),
				wn.synset("rise.v.13"),
				wn.synset("rise.v.01"),
				wn.synset("rise.v.15"),
				wn.synset("rise.v.04"),
				wn.synset("rise.v.16"),
				wn.synset("go_up.v.04"),
				wn.synset("originate.v.01"),
				wn.synset("ascend.v.06"),
				wn.synset("heighten.v.01"),
				wn.synset("approach.v.01"),
				wn.synset("wax.v.02")],

	# roadrunner
	"U+3b53":   [wn.synset("roadrunner.n.01")],

	# projectile, rocket, spacecraft
	"U+3b54":   [wn.synset("rocket.n.01"),
				wn.synset("projectile.n.01")],

	# rocking chair
	"U+3b56":   [wn.synset("rocking_chair.n.01")],

	# roller skate
	"U+3b58":   [wn.synset("roller_skate.v.01")],

	# roof, cover
	"U+3b5a":   [wn.synset("roof.n.01")],

	# root, rootage, root system
	"U+3b5b":   [wn.synset("root.n.01"),
				wn.synset("root.n.08")],

	# Rosh Hashana
	"U+3b5c":   [wn.synset("rosh_hashanah.n.01")],

	# rotation, circulation, orbit, lap, circle, round
	"U+3b5d":   [wn.synset("lick.n.02"),
				wn.synset("turn.n.09"),
				wn.synset("round.n.12"),
				wn.synset("round.n.11"),
				wn.synset("round.n.10"),
				wn.synset("lap.n.03"),
				wn.synset("lap.n.02"),
				wn.synset("lap.n.01"),
				wn.synset("lap.n.05"),
				wn.synset("lap.n.04"),
				wn.synset("rotation.n.01"),
				wn.synset("rotation.n.03"),
				wn.synset("rotation.n.02"),
				wn.synset("rotation.n.04"),
				wn.synset("r-2.n.01"),
				wn.synset("set.n.05"),
				wn.synset("beat.n.01"),
				wn.synset("circulation.n.01"),
				wn.synset("circulation.n.03"),
				wn.synset("circulation.n.02"),
				wn.synset("circulation.n.05"),
				wn.synset("circulation.n.04"),
				wn.synset("circulation.n.06"),
				wn.synset("circle.n.07"),
				wn.synset("circle.n.01"),
				wn.synset("scope.n.01"),
				wn.synset("circle.n.03"),
				wn.synset("rung.n.01"),
				wn.synset("circle.n.08"),
				wn.synset("round.n.01"),
				wn.synset("round.n.04"),
				wn.synset("round.n.06"),
				wn.synset("round.n.08"),
				wn.synset("round.n.09"),
				wn.synset("eye_socket.n.01"),
				wn.synset("orbit.n.01"),
				wn.synset("orbit.n.04"),
				wn.synset("cycle.n.01"),
				wn.synset("round_of_golf.n.01"),
				wn.synset("traffic_circle.n.01"),
				wn.synset("sphere.n.01")],

	# round, circular
	"U+3b60":   [wn.synset("round.a.01")],

	# roti, chapati, flatbread
	"U+3b61":   [wn.synset("chapatti.n.01"),
				wn.synset("flatbread.n.01"),
				wn.synset("grid.n.05"),
				wn.synset("grill.n.02")],

	# rouge, blusher
	"U+3b62":   [wn.synset("rouge.n.01")],

	# rub, massage
	"U+3b63":   [wn.synset("massage.v.01"),
				wn.synset("massage.v.02")],

	# rug, carpet, mat
	"U+3b64":   [wn.synset("rug.n.01")],

	# ruler, measuring stick, tapeline, tape measure
	"U+3b66":   [wn.synset("rule.n.12")],

	# run
	"U+3b67":   [wn.synset("run.v.01")],

	# sad, sadly, unhappily, unhappy
	"U+3b68":   [wn.synset("sad.a.01")],

	# sadness, sorrow, unhappiness
	"U+3b69":   [wn.synset("sadness.n.01")],

	# safe, safely, secure, securely
	"U+3b6b":   [wn.synset("safe.a.01")],

	# safety, security
	"U+3b6c":   [wn.synset("safety.n.01")],

	# sailor
	"U+3b6d":   [wn.synset("sailor.n.01")],

	# saliva, spit
	"U+3b6f":   [wn.synset("spit.n.04"),
				wn.synset("spit.n.01"),
				wn.synset("phlegm.n.02"),
				wn.synset("spit.n.03"),
				wn.synset("saliva.n.01")],

	# salty
	"U+3b72":   [wn.synset("salty.s.03"),
				wn.synset("salty.a.02"),
				wn.synset("piquant.s.02")],

	# sand
	"U+3b74":   [wn.synset("sand.n.01")],

	# rock
	"U+3b75":   [wn.synset("rock_candy.n.01"),
				wn.synset("rock.n.07"),
				wn.synset("rock.n.04"),
				wn.synset("rock_'n'_roll.n.01"),
				wn.synset("rock.n.02"),
				wn.synset("rock.n.03"),
				wn.synset("rock.n.01")],

	# sandal
	"U+3b76":   [wn.synset("sandal.n.01")],

	# shoe
	"U+3b77":   [wn.synset("shoe.n.01")],

	# sandbox, sandpit, sandtray
	"U+3b79":   [wn.synset("sandbox.n.02")],

	# foundation, base, fundament
	"U+3b7a":   [wn.synset("base.n.11"),
				wn.synset("foundation.n.01")],

	# sandwich
	"U+3b7b":   [wn.synset("sandwich.n.01")],

	# sanitary napkin, sanitary towel, tampon
	"U+3b7d":   [wn.synset("tampon.n.01")],

	# sari
	"U+3b7e":   [wn.synset("sari.n.01")],

	# satisfaction, contentment
	"U+3b7f":   [wn.synset("atonement.n.01"),
				wn.synset("gratification.n.01"),
				wn.synset("satisfaction.n.05"),
				wn.synset("satisfaction.n.04"),
				wn.synset("contentment.n.01"),
				wn.synset("satisfaction.n.01")],

	# sauerkraut
	"U+3b80":   [wn.synset("sauerkraut.n.01")],

	# sauna
	"U+3b82":   [wn.synset("sauna.n.01")],

	# sausage, frankfurter, hotdog, hot dog
	"U+3b84":   [wn.synset("sausage.n.01")],

	# say, speak, talk, tell, express
	"U+3b85":   [wn.synset("spill.v.05"),
				wn.synset("talk.v.01"),
				wn.synset("speak.v.03"),
				wn.synset("talk.v.02")],

	# scales
	"U+3b86":   [wn.synset("scale.n.07")],

	# scarf
	"U+3b88":   [wn.synset("scarf.n.01")],

	# scenery, landscape
	"U+3b8a":   [wn.synset("landscape.n.01")],

	# schedule, timetable
	"U+3b8d":   [wn.synset("timetable.n.02"),
				wn.synset("timetable.n.01"),
				wn.synset("notebook.n.01"),
				wn.synset("plan.n.01"),
				wn.synset("agenda.n.01"),
				wn.synset("agenda.n.02"),
				wn.synset("broadcast.n.02"),
				wn.synset("program.n.02"),
				wn.synset("playbill.n.01"),
				wn.synset("platform.n.02"),
				wn.synset("schedule.n.02"),
				wn.synset("program.n.07")],

	# school
	"U+3b8e":   [wn.synset("school.n.02")],

	# score
	"U+3b8f":   [wn.synset("score.n.10"),
				wn.synset("sexual_conquest.n.01"),
				wn.synset("grudge.n.01"),
				wn.synset("score.n.08"),
				wn.synset("mark.n.01"),
				wn.synset("score.n.02"),
				wn.synset("score.n.03"),
				wn.synset("score.n.06"),
				wn.synset("score.n.07"),
				wn.synset("score.n.04"),
				wn.synset("score.n.05")],

	# scorpion
	"U+3b91":   [wn.synset("scorpion.n.03")],

	# screwdriver
	"U+3b92":   [wn.synset("screwdriver.n.01")],

	# scrotum
	"U+3b94":   [wn.synset("scrotum.n.01")],

	# search
	"U+3b96":   [wn.synset("search.v.04"),
				wn.synset("research.v.02"),
				wn.synset("search.v.01"),
				wn.synset("search.v.02")],

	# second
	"U+3b98":   [wn.synset("second.a.02"),
				wn.synset("second.s.01")],

	# see you again
	"U+3b9b":   [wn.synset("revision.n.02")],

	# seem
	"U+3b9c":   [wn.synset("appear.v.04")],

	# self control
	"U+3b9f":   [wn.synset("self-denial.n.02")],

	# selfish, self centred, self centered, egoistic, egoistical, egocentric
	"U+3ba0":   [wn.synset("egoistic.a.01")],

	# sell
	"U+3ba1":   [wn.synset("sell.v.01")],

	# semen
	"U+3ba2":   [wn.synset("semen.n.01")],

	# seminal vesicle
	"U+3ba4":   [wn.synset("scrotum.n.01"),
				wn.synset("seminal_vesicle.n.01")],

	# send
	"U+3ba5":   [wn.synset("transport.v.04"),
				wn.synset("send.v.06"),
				wn.synset("send.v.02")],

	# sentence, clause, phrase, condemn
	"U+3ba6":   [wn.synset("sentence.v.01")],

	# word
	"U+3ba7":   [wn.synset("word.n.01"),
				wn.synset("parole.n.01")],

	# September
	"U+3ba8":   [wn.synset("september.n.01")],

	# several
	"U+3ba9":   [wn.synset("respective.s.01"),
				wn.synset("several.s.01"),
				wn.synset("several.s.03")],

	# sew
	"U+3baa":   [wn.synset("sew.v.02"),
				wn.synset("sew.v.01")],

	# sewing machine
	"U+3bac":   [wn.synset("sewing_machine.n.01")],

	# sex drive, sexual urge, libido
	"U+3bad":   [wn.synset("sex_drive.n.01")],

	# sexual abuse, sexual assault, sexual violence
	"U+3bae":   [wn.synset("sexual_assault.n.01"),
				wn.synset("rape.n.03")],

	# sexual arousal, sexual excitement
	"U+3bb0":   [wn.synset("sexual_arousal.n.01"),
				wn.synset("craving.n.01"),
				wn.synset("sexual_desire.n.01")],

	# excitement
	"U+3bb1":   [wn.synset("excitement.n.02"),
				wn.synset("excitation.n.03")],

	# sexual harassment
	"U+3bb2":   [wn.synset("sexual_harassment.n.01")],

	# sexual pleasure
	"U+3bb3":   [wn.synset("sexual_pleasure.n.01")],

	# sexuality
	"U+3bb4":   [wn.synset("sex.n.04")],

	# shake, jiggle
	"U+3bb5":   [wn.synset("shake.v.01")],

	# shallowness
	"U+3bb6":   [wn.synset("superficiality.n.01"),
				wn.synset("shallowness.n.02")],

	# shalom
	"U+3bb7":   [wn.synset("greeting.n.01")],

	# shame
	"U+3bb8":   [wn.synset("shame.n.01")],

	# shampoo
	"U+3bb9":   [wn.synset("shampoo.n.01")],

	# soap, detergent
	"U+3bba":   [wn.synset("soap.n.01")],

	# share
	"U+3bbb":   [wn.synset("share.v.02")],

	# shark
	"U+3bbc":   [wn.synset("shark.n.01")],

	# shave
	"U+3bbd":   [wn.synset("shave.v.01")],

	# shaver, razor
	"U+3bbe":   [wn.synset("razor.n.01")],

	# shaving soap, shaving cream
	"U+3bc0":   [wn.synset("shaving_cream.n.01")],

	# Shavuot
	"U+3bc1":   [wn.synset("shavous.n.01")],

	# sheet, bedclothes, bed linen
	"U+3bc3":   [wn.synset("sheet.n.03")],

	# shell, crust
	"U+3bc4":   [wn.synset("crust.n.01")],

	# case, casing
	"U+3bc5":   [wn.synset("subject.n.06"),
				wn.synset("shell.n.08"),
				wn.synset("sheath.n.02"),
				wn.synset("font.n.01"),
				wn.synset("event.n.02"),
				wn.synset("case.n.20"),
				wn.synset("casing.n.02"),
				wn.synset("casing.n.03"),
				wn.synset("character.n.05"),
				wn.synset("case.n.10"),
				wn.synset("case.n.11"),
				wn.synset("lawsuit.n.01"),
				wn.synset("case.n.09"),
				wn.synset("case.n.08"),
				wn.synset("case.n.18"),
				wn.synset("case.n.19"),
				wn.synset("case.n.05"),
				wn.synset("case.n.04"),
				wn.synset("case.n.01"),
				wn.synset("case.n.12"),
				wn.synset("case.n.06")],

	# shine, beam
	"U+3bc7":   [wn.synset("glitter.v.01")],

	# shirt, blouse
	"U+3bc8":   [wn.synset("shirt.n.01"),
				wn.synset("blouse.n.01")],

	# Shiva
	"U+3bc9":   [wn.synset("siva.n.01")],

	# shorts
	"U+3bcb":   [wn.synset("short_pants.n.01")],

	# shout
	"U+3bcd":   [wn.synset("shout.v.01"),
				wn.synset("shout.v.02"),
				wn.synset("exclaim.v.01")],

	# show, demonstrate
	"U+3bcf":   [wn.synset("indicate.v.02")],

	# exhibition hall, showplace
	"U+3bd0":   [wn.synset("scene.n.01"),
				wn.synset("showplace.n.01"),
				wn.synset("dramaturgy.n.01"),
				wn.synset("audience.n.01"),
				wn.synset("exhibition_hall.n.01"),
				wn.synset("theater.n.01")],

	# Shevat, Shvat
	"U+3bd1":   [wn.synset("shebat.n.01")],

	# side
	"U+3bd2":   [wn.synset("side.n.01")],

	# sign, advertisement, signal
	"U+3bd4":   [wn.synset("signal.n.01")],

	# signature
	"U+3bd5":   [wn.synset("signature.n.01")],

	# signature stamp
	"U+3bd6":   [wn.synset("buffer.n.01"),
				wn.synset("key_signature.n.01"),
				wn.synset("touch.n.04"),
				wn.synset("navy_seal.n.01"),
				wn.synset("tampon.n.01"),
				wn.synset("seal.n.02"),
				wn.synset("stamp.n.03"),
				wn.synset("stamp.n.02"),
				wn.synset("signature.n.05"),
				wn.synset("autograph.n.01"),
				wn.synset("polarity.n.02"),
				wn.synset("signature.n.01"),
				wn.synset("autograph.n.02"),
				wn.synset("signature.n.03")],

	# silence, quiet
	"U+3bd8":   [wn.synset("silence.n.02")],

	# silent
	"U+3bd9":   [wn.synset("dumb.s.04"),
				wn.synset("silent.s.05"),
				wn.synset("silent.s.04"),
				wn.synset("silent.s.03"),
				wn.synset("silent.s.01"),
				wn.synset("mum.s.01")],

	# Simchat Torah
	"U+3bda":   [wn.synset("succoth.n.01"),
				wn.synset("shimchath_torah.n.01")],

	# simmer, poach
	"U+3bdf":   [wn.synset("simmer.v.01")],

	# sin
	"U+3be0":   [wn.synset("sin.n.02")],

	# sing
	"U+3be1":   [wn.synset("sing.v.02")],

	# song
	"U+3be2":   [wn.synset("song.n.01")],

	# singer
	"U+3be3":   [wn.synset("singer.n.01")],

	# sinner
	"U+3be4":   [wn.synset("sinner.n.01")],

	# sister
	"U+3be5":   [wn.synset("sister.n.01")],

	# sit
	"U+3be6":   [wn.synset("seat.v.01"),
				wn.synset("sit_down.v.01"),
				wn.synset("sit.v.01")],

	# Sivan
	"U+3be7":   [wn.synset("sivan.n.01")],

	# skeleton
	"U+3be8":   [wn.synset("skeletal_system.n.01")],

	# ski boot
	"U+3be9":   [wn.synset("ski_boot.n.01")],

	# ski pole
	"U+3beb":   [wn.synset("ski_pole.n.01")],

	# skin
	"U+3bec":   [wn.synset("hide.n.02"),
				wn.synset("peel.n.02"),
				wn.synset("skin.n.01")],

	# skirt
	"U+3bed":   [wn.synset("skirt.n.02")],

	# skis
	"U+3bee":   [wn.synset("ski.n.01")],

	# skullcap, kipa, yarmulke
	"U+3bef":   [wn.synset("yarmulke.n.01"),
				wn.synset("skullcap.n.01"),
				wn.synset("skullcap.n.02"),
				wn.synset("calvaria.n.01")],

	# skunk
	"U+3bf0":   [wn.synset("skunk.n.04")],

	# sled, sledge, sleigh, toboggan
	"U+3bf2":   [wn.synset("sled.n.01")],

	# sleeping bag
	"U+3bf3":   [wn.synset("sleeping_bag.n.01")],

	# slide, skid, slip
	"U+3bf4":   [wn.synset("chute.n.02")],

	# slip, petticoat, half slip, underskirt
	"U+3bf5":   [wn.synset("petticoat.n.01")],

	# slipper
	"U+3bf7":   [wn.synset("slipper.n.01")],

	# smart, bright, clever, intelligent
	"U+3bf8":   [wn.synset("intelligent.a.01")],

	# smartness, brightness, cleverness, intelligence
	"U+3bf9":   [wn.synset("chic.n.01"),
				wn.synset("smart.n.01"),
				wn.synset("ingenuity.n.02"),
				wn.synset("news.n.01"),
				wn.synset("inventiveness.n.01"),
				wn.synset("intelligent.a.01"),
				wn.synset("able.a.01"),
				wn.synset("alacrity.n.01"),
				wn.synset("intelligence.n.01"),
				wn.synset("intelligence.n.02"),
				wn.synset("intelligence.n.03"),
				wn.synset("intelligence.n.05"),
				wn.synset("brainy.s.01"),
				wn.synset("brilliant.s.01"),
				wn.synset("entertaining.s.01"),
				wn.synset("brightness.n.02"),
				wn.synset("brightness.n.01"),
				wn.synset("luminosity.n.01")],

	# smash, grind, shatter, splinter
	"U+3bfd":   [wn.synset("sliver.v.01"),
				wn.synset("shatter.v.03"),
				wn.synset("shatter.v.02"),
				wn.synset("shatter.v.01"),
				wn.synset("smash.v.10"),
				wn.synset("smash.v.04"),
				wn.synset("smash.v.07"),
				wn.synset("smash.v.01"),
				wn.synset("smash.v.02"),
				wn.synset("splinter.v.03"),
				wn.synset("smash.v.08"),
				wn.synset("smash.v.09"),
				wn.synset("grate.v.04"),
				wn.synset("grind.v.06"),
				wn.synset("grind.v.07"),
				wn.synset("grind.v.04"),
				wn.synset("grind.v.05"),
				wn.synset("labor.v.02"),
				wn.synset("bang_up.v.01"),
				wn.synset("secede.v.01"),
				wn.synset("crunch.v.02"),
				wn.synset("crush.v.05"),
				wn.synset("bankrupt.v.01")],

	# smell bad, stink
	"U+3bfe":   [wn.synset("stink.v.01"),
				wn.synset("reek.v.02")],

	# smile, grin
	"U+3c00":   [wn.synset("smile.v.01")],

	# smoke
	"U+3c01":   [wn.synset("smoke.n.01"),
				wn.synset("smoke.n.02")],

	# smooth
	"U+3c02":   [wn.synset("legato.a.01"),
				wn.synset("placid.s.01"),
				wn.synset("smooth.a.06"),
				wn.synset("fluent.s.01"),
				wn.synset("smooth.a.03"),
				wn.synset("politic.s.02"),
				wn.synset("smooth.s.07"),
				wn.synset("smooth.a.01")],

	# snack
	"U+3c03":   [wn.synset("bite.n.04")],

	# water snake
	"U+3c04":   [wn.synset("water_snake.n.01"),
				wn.synset("hoop_snake.n.01"),
				wn.synset("colubrid_snake.n.01"),
				wn.synset("grass_snake.n.01"),
				wn.synset("whip-snake.n.01"),
				wn.synset("garter_snake.n.01")],

	# sneeze
	"U+3c05":   [wn.synset("sneeze.v.01")],

	# snowball
	"U+3c06":   [wn.synset("snowball.n.01"),
				wn.synset("snowball.n.03"),
				wn.synset("snowball.n.02"),
				wn.synset("snowball.n.04")],

	# snowman
	"U+3c07":   [wn.synset("snowman.n.01")],

	# snowstorm
	"U+3c08":   [wn.synset("blizzard.n.01")],

	# storm
	"U+3c09":   [wn.synset("storm.n.01")],

	# snowsuit, winter clothing
	"U+3c0b":   [wn.synset("snowsuit.n.01")],

	# social worker
	"U+3c0d":   [wn.synset("social_worker.n.01")],

	# worker
	"U+3c0e":   [wn.synset("worker.n.01")],

	# soda pop, pop, soft drink
	"U+3c0f":   [wn.synset("soft_drink.n.01"),
				wn.synset("pop.n.03"),
				wn.synset("pop.n.02"),
				wn.synset("pop_music.n.01"),
				wn.synset("dad.n.01")],

	# imprint, trace, track, depression
	"U+3c10":   [wn.synset("touch.n.03"),
				wn.synset("path.n.04"),
				wn.synset("lead.n.03"),
				wn.synset("track.n.03"),
				wn.synset("track.n.07"),
				wn.synset("track.n.06"),
				wn.synset("trace.n.05"),
				wn.synset("track.n.09"),
				wn.synset("track.n.08"),
				wn.synset("trace.n.01"),
				wn.synset("track.n.11"),
				wn.synset("trace.n.02"),
				wn.synset("trace.n.06"),
				wn.synset("tracing.n.02"),
				wn.synset("track.n.10"),
				wn.synset("cut.n.08"),
				wn.synset("depression.n.08"),
				wn.synset("imprint.n.05"),
				wn.synset("imprint.n.04"),
				wn.synset("imprint.n.03"),
				wn.synset("imprint.n.01"),
				wn.synset("racetrack.n.01")],

	# solve
	"U+3c11":   [wn.synset("solve.v.01")],

	# some, any
	"U+3c13":   [wn.synset("a_few.s.01"),
				wn.synset("any.s.01"),
				wn.synset("some.a.01"),
				wn.synset("some.s.04"),
				wn.synset("some.s.02"),
				wn.synset("some.s.03")],

	# sometimes
	"U+3c14":   [wn.synset("sometimes.r.01")],

	# songbird, finch, thrush
	"U+3c15":   [wn.synset("songbird.n.01"),
				wn.synset("thrush.n.03"),
				wn.synset("thrush.n.02"),
				wn.synset("thrush.n.01"),
				wn.synset("finch.n.01")],

	# soon
	"U+3c17":   [wn.synset("soon.r.01")],

	# wound, cut, sore
	"U+3c18":   [wn.synset("wound.n.01")],

	# sufganiya
	"U+3c1b":   [wn.synset("hanukkah.n.01")],

	# southern
	"U+3c1c":   [wn.synset("southerly.s.01"),
				wn.synset("southern.a.01")],

	# special, particular
	"U+3c1d":   [wn.synset("particular.s.01"),
				wn.synset("special.s.04"),
				wn.synset("especial.s.01"),
				wn.synset("special.s.02")],

	# specific
	"U+3c1e":   [wn.synset("specific.s.02"),
				wn.synset("specific.a.01")],

	# spermicide
	"U+3c1f":   [wn.synset("spermicide.n.01")],

	# spice box
	"U+3c21":   [wn.synset("pepper_shaker.n.01")],

	# spitting
	"U+3c24":   [wn.synset("spit.n.04")],

	# splash
	"U+3c25":   [wn.synset("spatter.v.01")],

	# spring
	"U+3c27":   [wn.synset("well.n.01"),
				wn.synset("leap.n.01"),
				wn.synset("spring.n.01"),
				wn.synset("spring.n.02"),
				wn.synset("spring.n.03"),
				wn.synset("spring.n.04"),
				wn.synset("give.n.01")],

	# square
	"U+3c28":   [wn.synset("square.s.05"),
				wn.synset("square.s.04"),
				wn.synset("square.a.01"),
				wn.synset("square.s.06"),
				wn.synset("straight.a.06"),
				wn.synset("hearty.s.02")],

	# staff
	"U+3c29":   [wn.synset("staff.n.01")],

	# stairs, steps
	"U+3c2b":   [wn.synset("footstep.n.03"),
				wn.synset("gradation.n.01"),
				wn.synset("steps.n.02"),
				wn.synset("dance_step.n.01"),
				wn.synset("footprint.n.01"),
				wn.synset("stairs.n.01"),
				wn.synset("measure.n.01"),
				wn.synset("tone.n.09"),
				wn.synset("step.n.03"),
				wn.synset("stairway.n.01"),
				wn.synset("footfall.n.01"),
				wn.synset("step.n.10"),
				wn.synset("step.n.04"),
				wn.synset("step.n.06")],

	# stand
	"U+3c2c":   [wn.synset("resist.v.04"),
				wn.synset("stand.v.01"),
				wn.synset("stand.v.02"),
				wn.synset("stand.v.03"),
				wn.synset("stand.v.04"),
				wn.synset("stand.v.12"),
				wn.synset("stand.v.06"),
				wn.synset("stand.v.10"),
				wn.synset("stand.v.08"),
				wn.synset("stand.v.09"),
				wn.synset("digest.v.03"),
				wn.synset("stand.v.07")],

	# stander
	"U+3c2d":   [wn.synset("stander.n.01")],

	# star of David
	"U+3c2f":   [wn.synset("star_of_david.n.01")],

	# stay, remain
	"U+3c30":   [wn.synset("stay.v.02")],

	# steel
	"U+3c31":   [wn.synset("steel.n.01")],

	# sterilization
	"U+3c32":   [wn.synset("sterilization.n.02"),
				wn.synset("sterilization.n.01")],

	# stocking, sock, pantyhose, tights
	"U+3c34":   [wn.synset("sock.n.01")],

	# stone material
	"U+3c35":   [wn.synset("rock.n.01")],

	# storeroom
	"U+3c37":   [wn.synset("storeroom.n.01")],

	# gale
	"U+3c39":   [wn.synset("gale.n.01"),
				wn.synset("storm.n.01")],

	# story, report, tale, historic story
	"U+3c3b":   [wn.synset("story.n.02"),
				wn.synset("history.n.02"),
				wn.synset("fib.n.01")],

	# stove, furnace, heater, oven
	"U+3c3c":   [wn.synset("heater.n.01"),
				wn.synset("furnace.n.01"),
				wn.synset("oven.n.01"),
				wn.synset("stove.n.01"),
				wn.synset("stove.n.02"),
				wn.synset("fastball.n.01")],

	# stranger, unknown
	"U+3c3d":   [wn.synset("unknown.n.03"),
				wn.synset("stranger.n.01"),
				wn.synset("unknown.n.01"),
				wn.synset("stranger.n.02")],

	# strap, string, velcro, rope, cord, hawser
	"U+3c3e":   [wn.synset("velcro.n.01"),
				wn.synset("cord.n.04"),
				wn.synset("cord.n.03"),
				wn.synset("cord.n.02"),
				wn.synset("cord.n.01"),
				wn.synset("string.n.08"),
				wn.synset("string.n.09"),
				wn.synset("string.n.04"),
				wn.synset("string.n.05"),
				wn.synset("strap.n.04"),
				wn.synset("string.n.07"),
				wn.synset("strap.n.02"),
				wn.synset("string.n.01"),
				wn.synset("chain.n.10"),
				wn.synset("string.n.03"),
				wn.synset("drawstring.n.01"),
				wn.synset("bowed_stringed_instrument.n.01"),
				wn.synset("strap.n.03"),
				wn.synset("rope.n.01"),
				wn.synset("r-2.n.01"),
				wn.synset("strap.n.01")],

	# straw, drinking straw
	"U+3c3f":   [wn.synset("straw.n.01"),
				wn.synset("chaff.n.01"),
				wn.synset("pale_yellow.n.01"),
				wn.synset("straw.n.04")],

	# string bean, green bean, runner bean, wax bean
	"U+3c40":   [wn.synset("green_bean.n.02"),
				wn.synset("green_bean.n.01"),
				wn.synset("wax_bean.n.01"),
				wn.synset("wax_bean.n.02"),
				wn.synset("cowpea.n.02"),
				wn.synset("scarlet_runner.n.01"),
				wn.synset("scarlet_runner.n.03"),
				wn.synset("string_bean.n.01")],

	# stroke
	"U+3c41":   [wn.synset("stroke.v.01")],

	# strength
	"U+3c42":   [wn.synset("strength.n.01")],

	# student, pupil
	"U+3c43":   [wn.synset("student.n.01"),
				wn.synset("scholar.n.01"),
				wn.synset("pupil.n.02"),
				wn.synset("schoolchild.n.01")],

	# subtract, remove, take away
	"U+3c45":   [wn.synset("subtract.v.01")],

	# succeed
	"U+3c46":   [wn.synset("succeed.v.01")],

	# suddenly, abrupt, sudden
	"U+3c47":   [wn.synset("suddenly.r.01"),
				wn.synset("abruptly.r.01")],

	# sugar, sweetener
	"U+3c48":   [wn.synset("sugar.n.01")],

	# sweetness, sweet
	"U+3c49":   [wn.synset("sweet.n.04"),
				wn.synset("sweet.n.01"),
				wn.synset("sweet.n.03"),
				wn.synset("sweetness.n.02"),
				wn.synset("pleasantness.n.02"),
				wn.synset("bouquet.n.02"),
				wn.synset("sweetmeat.n.01"),
				wn.synset("dessert.n.01")],

	# suggest, propose
	"U+3c4b":   [wn.synset("propose.v.01")],

	# suit
	"U+3c4d":   [wn.synset("courtship.n.01"),
				wn.synset("lawsuit.n.01"),
				wn.synset("suit.n.06"),
				wn.synset("suit.n.05"),
				wn.synset("suit.n.03"),
				wn.synset("suit.n.01")],

	# Sukkot
	"U+3c50":   [wn.synset("succoth.n.01")],

	# summer
	"U+3c52":   [wn.synset("summer.n.01")],

	# summer day camp
	"U+3c53":   [wn.synset("camp.n.08")],

	# sunscreen, sunblock, sun lotion
	"U+3c55":   [wn.synset("sunscreen.n.01")],

	# sunny
	"U+3c56":   [wn.synset("cheery.s.01")],

	# sunrise
	"U+3c57":   [wn.synset("dawn.n.01"),
				wn.synset("sunrise.n.02")],

	# sunset
	"U+3c58":   [wn.synset("sunset.n.03"),
				wn.synset("sunset.n.01")],

	# supper, dinner
	"U+3c59":   [wn.synset("supper.n.02"),
				wn.synset("dinner.n.01"),
				wn.synset("supper.n.01")],

	# with
	"U+3c5a":   [wn.synset("iodine.n.01")],

	# swallow
	"U+3c5b":   [wn.synset("swallow.v.01")],

	# sweat, perspire, perspiration
	"U+3c5c":   [wn.synset("sweat.v.01")],

	# sweet potato, yam
	"U+3c5d":   [wn.synset("sweet_potato.n.01"),
				wn.synset("yam.n.04"),
				wn.synset("yam.n.03"),
				wn.synset("yam.n.02"),
				wn.synset("sweet_potato.n.02")],

	# sweetheart, lover
	"U+3c5e":   [wn.synset("fan.n.03"),
				wn.synset("sweetheart.n.01"),
				wn.synset("lover.n.03"),
				wn.synset("lover.n.01"),
				wn.synset("smasher.n.02"),
				wn.synset("sweetheart.n.02")],

	# swim
	"U+3c60":   [wn.synset("swim.v.01")],

	# swimming, swim
	"U+3c61":   [wn.synset("swimming.n.01")],

	# swimming pool
	"U+3c62":   [wn.synset("swimming_pool.n.01")],

	# swimsuit, swimwear, bathing suit
	"U+3c64":   [wn.synset("swimsuit.n.01")],

	# handle
	"U+3c66":   [wn.synset("handle.n.01")],

	# switch
	"U+3c67":   [wn.synset("switch.v.04"),
				wn.synset("trade.v.04"),
				wn.synset("switch.v.06"),
				wn.synset("switch.v.03"),
				wn.synset("interchange.v.04"),
				wn.synset("switch_over.v.01"),
				wn.synset("throw.v.06")],

	# synagogue
	"U+3c6a":   [wn.synset("synagogue.n.01")],

	# syringe
	"U+3c6b":   [wn.synset("syringe.n.01")],

	# table game
	"U+3c6c":   [wn.synset("game.n.01"),
				wn.synset("table_game.n.01")],

	# tablecloth
	"U+3c6d":   [wn.synset("tablecloth.n.01")],

	# tahini, sesame seed spread
	"U+3c6f":   [wn.synset("tahini.n.01")],

	# portability
	"U+3c70":   [wn.synset("portability.n.01")],

	# takeoff, take off, airplane take off
	"U+3c71":   [wn.synset("take_off.v.03")],

	# talcum powder
	"U+3c73":   [wn.synset("talc.n.01"),
				wn.synset("talcum.n.02")],

	# tallith
	"U+3c75":   [wn.synset("prayer_shawl.n.01")],

	# Tammuz
	"U+3c77":   [wn.synset("tammuz.n.01")],

	# tangerine, clementine, mandarin
	"U+3c78":   [wn.synset("tangerine.n.01"),
				wn.synset("mandarin.n.01")],

	# tape recorder
	"U+3c79":   [wn.synset("recorder.n.01"),
				wn.synset("tape_recorder.n.01")],

	# taxi, cab
	"U+3c7b":   [wn.synset("cab.n.03")],

	# taxi driver, cab driver
	"U+3c7c":   [wn.synset("taxidriver.n.01")],

	# tea
	"U+3c7e":   [wn.synset("tea.n.01")],

	# teach, instruct
	"U+3c7f":   [wn.synset("teach.v.01")],

	# teacher, instructor, pedagogue, educator
	"U+3c80":   [wn.synset("teacher.n.01"),
				wn.synset("educator.n.01")],

	# team
	"U+3c81":   [wn.synset("team.n.01")],

	# tease
	"U+3c82":   [wn.synset("tease.v.08"),
				wn.synset("tease.v.09"),
				wn.synset("tease.v.06"),
				wn.synset("tease.v.07"),
				wn.synset("tease.v.04"),
				wn.synset("tease.v.05"),
				wn.synset("tease.v.02"),
				wn.synset("tease.v.03"),
				wn.synset("tease.v.01")],

	# telephone
	"U+3c84":   [wn.synset("telephone.n.01")],

	# television
	"U+3c85":   [wn.synset("television_receiver.n.01")],

	# tent
	"U+3c88":   [wn.synset("tent.n.01")],

	# termite
	"U+3c89":   [wn.synset("termite.n.01")],

	# terrified
	"U+3c8b":   [wn.synset("fearful.s.04"),
				wn.synset("tragic.s.01"),
				wn.synset("awful.s.02"),
				wn.synset("panicky.s.01")],

	# terror, panic
	"U+3c8c":   [wn.synset("panic.n.01")],

	# terrorist
	"U+3c8d":   [wn.synset("terrorist.n.01")],

	# terrorize
	"U+3c8f":   [wn.synset("terrify.v.01"),
				wn.synset("terrorize.v.01")],

	# terrorism
	"U+3c90":   [wn.synset("terrorism.n.01")],

	# test, assessment, exam
	"U+3c91":   [wn.synset("examination.n.02")],

	# testicle
	"U+3c93":   [wn.synset("testis.n.01")],

	# Tevet
	"U+3c94":   [wn.synset("tebet.n.01")],

	# winter
	"U+3c95":   [wn.synset("winter.n.01")],

	# tefillin
	"U+3c96":   [wn.synset("phylactery.n.01")],

	# thank
	"U+3c97":   [wn.synset("thank.v.01")],

	# thanks, thank you
	"U+3c98":   [wn.synset("thank_you.n.01"),
				wn.synset("thanks.n.01")],

	# thanksgiving
	"U+3c99":   [wn.synset("thanksgiving.n.01"),
				wn.synset("grace.n.06"),
				wn.synset("grace.n.07")],

	# too bad, I'm sorry, I'm so sorry
	"U+3c9a":   [wn.synset("regrettable.s.01"),
				wn.synset("damage.n.01"),
				wn.synset("damage.n.02"),
				wn.synset("damage.n.03"),
				wn.synset("price.n.02"),
				wn.synset("wrong.n.02"),
				wn.synset("pity.n.02")],

	# thaw, melt
	"U+3c9c":   [wn.synset("dissolve.v.09")],

	# thawing, melting
	"U+3c9d":   [wn.synset("thaw.n.02"),
				wn.synset("thaw.n.01")],

	# their, theirs
	"U+3c9f":   [wn.synset("sus.n.01"),
				wn.synset("hog.n.03")],

	# they, them, themselves
	"U+3ca0":   [wn.synset("he.n.02"),
				wn.synset("helium.n.01")],

	# thermometer
	"U+3ca1":   [wn.synset("thermometer.n.01")],

	# thermos, cooler, flask
	"U+3ca2":   [wn.synset("thermos.n.01")],

	# these
	"U+3ca3":   [wn.synset("tellurium.n.01")],

	# thinness, narrowness
	"U+3ca4":   [wn.synset("fineness.n.02"),
				wn.synset("narrowness.n.01"),
				wn.synset("narrowness.n.03"),
				wn.synset("leanness.n.02"),
				wn.synset("narrow_margin.n.01"),
				wn.synset("narrow-mindedness.n.01"),
				wn.synset("thinness.n.01"),
				wn.synset("thinness.n.05"),
				wn.synset("sparseness.n.01")],

	# think, reason
	"U+3ca6":   [wn.synset("think.v.01"),
				wn.synset("think.v.03")],

	# thirsty
	"U+3ca7":   [wn.synset("thirst.n.01"),
				wn.synset("thirsty.a.02"),
				wn.synset("athirst.s.01"),
				wn.synset("hunger.n.02"),
				wn.synset("thirsty.s.04"),
				wn.synset("thirsty.s.01")],

	# those
	"U+3cab":   [wn.synset("judgment.n.03"),
				wn.synset("verdict.n.01"),
				wn.synset("conviction.n.02")],

	# throw
	"U+3cac":   [wn.synset("throw.v.01")],

	# thunder
	"U+3cad":   [wn.synset("thunder.n.02")],

	# ticket, pass
	"U+3cae":   [wn.synset("ticket.n.01")],

	# tie, necktie, bind together, lash
	"U+3cb0":   [wn.synset("tie.v.01")],

	# tiger
	"U+3cb1":   [wn.synset("tiger.n.02")],

	# tiptoe
	"U+3cb2":   [wn.synset("tiptoe.v.01")],

	# tire, tyre
	"U+3cb3":   [wn.synset("tire.n.01")],

	# tired, exhausted, weary, worn out, raddled
	"U+3cb4":   [wn.synset("tired.a.01")],

	# Tisha B'Av
	"U+3cb6":   [wn.synset("tishah_b'av.n.01")],

	# Tishri
	"U+3cb7":   [wn.synset("tishri.n.01")],

	# tissue
	"U+3cb8":   [wn.synset("tissue.n.01")],

	# toaster
	"U+3cba":   [wn.synset("toaster.n.02")],

	# tobacco
	"U+3cbc":   [wn.synset("tobacco.n.01")],

	# today
	"U+3cbd":   [wn.synset("today.n.01")],

	# toilet paper
	"U+3cbe":   [wn.synset("toilet_tissue.n.01")],

	# tomato
	"U+3cc0":   [wn.synset("tomato.n.01")],

	# tomorrow
	"U+3cc2":   [wn.synset("tomorrow.n.02")],

	# tongue
	"U+3cc4":   [wn.synset("tongue.n.01")],

	# tonight
	"U+3cc5":   [wn.synset("tonight.n.01")],

	# too much, too many
	"U+3cc6":   [wn.synset("overmuch.r.01")],

	# toothpaste
	"U+3cc8":   [wn.synset("toothpaste.n.01")],

	# dreidel top
	"U+3cc9":   [wn.synset("top.n.08")],

	# touch, feel, touching, sense of touch, tactile sense
	"U+3cca":   [wn.synset("touch.n.10")],

	# toy
	"U+3ccb":   [wn.synset("plaything.n.01")],

	# traffic
	"U+3ccd":   [wn.synset("traffic.n.01")],

	# train
	"U+3cce":   [wn.synset("train.n.01")],

	# trampoline
	"U+3cd0":   [wn.synset("trampoline.n.01")],

	# platform, stage
	"U+3cd1":   [wn.synset("phase.n.01"),
				wn.synset("degree.n.02"),
				wn.synset("stage.n.08"),
				wn.synset("stage.n.06"),
				wn.synset("stage.n.07"),
				wn.synset("stage.n.04"),
				wn.synset("stagecoach.n.01"),
				wn.synset("stage.n.03"),
				wn.synset("platform.n.01"),
				wn.synset("platform.n.02"),
				wn.synset("platform.n.03"),
				wn.synset("platform.n.04"),
				wn.synset("chopine.n.01")],

	# translate
	"U+3cd2":   [wn.synset("translate.v.01")],

	# transvestite
	"U+3cd3":   [wn.synset("transvestite.n.01")],

	# travel
	"U+3cd5":   [wn.synset("travel.v.05"),
				wn.synset("travel.v.02")],

	# trip, journey, travel, voyage
	"U+3cd6":   [wn.synset("journey.n.01"),
				wn.synset("trip.n.01"),
				wn.synset("trip.n.02")],

	# treat, care for
	"U+3cd7":   [wn.synset("treat.v.03")],

	# triangle
	"U+3cd8":   [wn.synset("triangle.n.01")],

	# triangular
	"U+3cda":   [wn.synset("triangular.s.01")],

	# tricycle
	"U+3cdb":   [wn.synset("tricycle.n.01")],

	# trouble
	"U+3cdc":   [wn.synset("trouble.n.04")],

	# true, truly, truthful, truthfully
	"U+3cdd":   [wn.synset("truly.r.01"),
				wn.synset("in_truth.r.01"),
				wn.synset("on-key.s.01"),
				wn.synset("sincerely.r.01"),
				wn.synset("genuine.s.02"),
				wn.synset("true.s.08"),
				wn.synset("true.s.09"),
				wn.synset("dependable.s.02"),
				wn.synset("true.s.12"),
				wn.synset("true.s.05"),
				wn.synset("truthful.a.01"),
				wn.synset("rightfully.r.01"),
				wn.synset("true.s.03"),
				wn.synset("true.s.10"),
				wn.synset("truthful.s.02"),
				wn.synset("true.a.01"),
				wn.synset("true.s.02"),
				wn.synset("real.a.01"),
				wn.synset("truthfully.r.01")],

	# trust, confidence
	"U+3cde":   [wn.synset("hope.v.01"),
				wn.synset("trust.v.02"),
				wn.synset("believe.v.03"),
				wn.synset("trust.v.01"),
				wn.synset("entrust.v.01"),
				wn.synset("trust.v.06")],

	# try, attempt
	"U+3ce0":   [wn.synset("try.v.01")],

	# tubal ligation
	"U+3ce2":   [wn.synset("tubal_ligation.n.01")],

	# turkey
	"U+3ce4":   [wn.synset("turkey.n.01")],

	# turtle, tortoise
	"U+3ce6":   [wn.synset("turtle.n.02")],

	# twinkle, shine, sparkle
	"U+3ce7":   [wn.synset("reflect.v.04"),
				wn.synset("sparkle.v.02"),
				wn.synset("flash.v.01"),
				wn.synset("fall.v.08"),
				wn.synset("shine.v.02"),
				wn.synset("shine.v.07"),
				wn.synset("sparkle.v.01"),
				wn.synset("shine.v.05"),
				wn.synset("shine.v.04"),
				wn.synset("foam.v.01"),
				wn.synset("twinkle.v.02"),
				wn.synset("glitter.v.01"),
				wn.synset("glow.v.05"),
				wn.synset("glow.v.02"),
				wn.synset("polish.v.01"),
				wn.synset("spark.v.02")],

	# type, kind, sort
	"U+3ce8":   [wn.synset("type.n.01"),
				wn.synset("sort.n.03"),
				wn.synset("character.n.05")],

	# printer, typewriter
	"U+3ce9":   [wn.synset("printer.n.02")],

	# ugh, yuk
	"U+3cea":   [wn.synset("phi.n.01")],

	# ugly, unattractive
	"U+3ceb":   [wn.synset("ugly.a.01"),
				wn.synset("atrocious.s.03"),
				wn.synset("unattractive.a.01"),
				wn.synset("surly.s.01"),
				wn.synset("despicable.s.01"),
				wn.synset("unattractive.s.02"),
				wn.synset("unattractive.s.03")],

	# umbilical cord
	"U+3cec":   [wn.synset("umbilical_cord.n.01")],

	# uncomfortable
	"U+3ced":   [wn.synset("uncomfortable.a.01"),
				wn.synset("uncomfortable.a.02")],

	# bomb shelter
	"U+3cef":   [wn.synset("bomb_shelter.n.01")],

	# underpants, briefs, panties
	"U+3cf0":   [wn.synset("underpants.n.01")],

	# undershirt
	"U+3cf1":   [wn.synset("singlet.n.01")],

	# underwear, underclothes
	"U+3cf2":   [wn.synset("underwear.n.01")],

	# unemployment
	"U+3cf3":   [wn.synset("unemployment.n.01")],

	# United Kingdom
	"U+3cf6":   [wn.synset("united_kingdom.n.01")],

	# university
	"U+3cf8":   [wn.synset("university.n.03")],

	# urethra
	"U+3cfa":   [wn.synset("urethra.n.01")],

	# urinate, make water, pass water, micturate, pee, piddle, piss, wee
	"U+3cfb":   [wn.synset("make.v.49")],

	# urine, piss, pee, piddle, weewee, water
	"U+3cfc":   [wn.synset("urine.n.01")],

	# usage, use
	"U+3cfd":   [wn.synset("use.n.01"),
				wn.synset("use.n.03"),
				wn.synset("custom.n.01")],

	# usually, usual
	"U+3cfe":   [wn.synset("common.s.04"),
				wn.synset("usual.a.01"),
				wn.synset("normally.r.01")],

	# utensil
	"U+3cff":   [wn.synset("tool.n.01"),
				wn.synset("utensil.n.01")],

	# vacation, holiday
	"U+3d00":   [wn.synset("holiday.n.02"),
				wn.synset("vacation.n.01"),
				wn.synset("vacation.n.02")],

	# Valentine
	"U+3d01":   [wn.synset("valentine.n.02"),
				wn.synset("valentine.n.01")],

	# Valentine's Day
	"U+3d02":   [wn.synset("valentine_day.n.01")],

	# van, minibus
	"U+3d03":   [wn.synset("van.n.03"),
				wn.synset("van.n.05"),
				wn.synset("van.n.04"),
				wn.synset("vanguard.n.01"),
				wn.synset("avant-garde.n.01"),
				wn.synset("minibus.n.01")],

	# vas deferens
	"U+3d04":   [wn.synset("vas_deferens.n.01")],

	# vasectomy
	"U+3d05":   [wn.synset("vasectomy.n.01")],

	# veal
	"U+3d07":   [wn.synset("veal.n.01")],

	# video recorder
	"U+3d09":   [wn.synset("videocassette_recorder.n.01"),
				wn.synset("video.n.03"),
				wn.synset("video.n.01")],

	# vinegar
	"U+3d0b":   [wn.synset("vinegar.n.01"),
				wn.synset("vinegar.n.02")],

	# virginity
	"U+3d0e":   [wn.synset("virginity.n.01")],

	# Vishnu
	"U+3d0f":   [wn.synset("vishnu.n.01")],

	# visitor, guest
	"U+3d11":   [wn.synset("visitor.n.01")],

	# volcano
	"U+3d12":   [wn.synset("volcano.n.02")],

	# volunteer
	"U+3d13":   [wn.synset("volunteer.n.02")],

	# vomit, throw up, puke
	"U+3d14":   [wn.synset("vomit.v.01")],

	# vomiting, vomit, puking
	"U+3d15":   [wn.synset("vomit.n.03")],

	# voyeurism
	"U+3d16":   [wn.synset("voyeurism.n.01")],

	# vulture
	"U+3d18":   [wn.synset("vulture.n.01")],

	# vulva
	"U+3d19":   [wn.synset("vulva.n.01")],

	# wading pool, paddling pool
	"U+3d1b":   [wn.synset("wading_pool.n.01")],

	# wage, pay, salary
	"U+3d1c":   [wn.synset("wage.n.01")],

	# wait, waiting
	"U+3d1d":   [wn.synset("delay.n.01"),
				wn.synset("wait.n.02")],

	# walk, go
	"U+3d1e":   [wn.synset("walk.v.01")],

	# walker
	"U+3d1f":   [wn.synset("walker.n.06")],

	# want, desire
	"U+3d20":   [wn.synset("desire.n.03"),
				wn.synset("desire.n.02"),
				wn.synset("desire.n.01")],

	# wash, bathe, bath
	"U+3d23":   [wn.synset("wash.v.02"),
				wn.synset("wash.v.03")],

	# washable
	"U+3d24":   [wn.synset("washable.a.01")],

	# washcloth, washrag, flannel
	"U+3d25":   [wn.synset("flannel.n.03"),
				wn.synset("handle.n.01"),
				wn.synset("flannel.n.01"),
				wn.synset("knob.n.02"),
				wn.synset("washcloth.n.01"),
				wn.synset("gauntlet.n.02"),
				wn.synset("strap.n.02"),
				wn.synset("mitten.n.01")],

	# washer
	"U+3d26":   [wn.synset("washer.n.03")],

	# washing machine, washer
	"U+3d27":   [wn.synset("washer.n.03")],

	# watchful, alert
	"U+3d29":   [wn.synset("alert.s.02"),
				wn.synset("alert.s.03"),
				wn.synset("alert.a.01"),
				wn.synset("insomniac.s.01")],

	# weak
	"U+3d2a":   [wn.synset("weak.a.01")],

	# weave
	"U+3d2b":   [wn.synset("weave.v.02")],

	# weekend
	"U+3d2c":   [wn.synset("weekend.n.01")],

	# plus sign
	"U+3d2d":   [wn.synset("plus_sign.n.01")],

	# weigh
	"U+3d2e":   [wn.synset("weigh.v.01"),
				wn.synset("weigh.v.03")],

	# welcome
	"U+3d2f":   [wn.synset("welcome.n.02"),
				wn.synset("welcome.n.01")],

	# western
	"U+3d30":   [wn.synset("western.a.01"),
				wn.synset("western.s.03"),
				wn.synset("western.a.02"),
				wn.synset("westerly.s.01")],

	# wet, damp, moist, watery
	"U+3d31":   [wn.synset("wet.a.01")],

	# whale
	"U+3d32":   [wn.synset("whale.n.02")],

	# when, what time
	"U+3d35":   [wn.synset("equally.r.01"),
				wn.synset("once.r.02")],

	# whisper
	"U+3d36":   [wn.synset("whisper.v.01")],

	# whistle
	"U+3d37":   [wn.synset("whistle.v.05")],

	# whose
	"U+3d39":   [wn.synset("whence.r.01")],

	# why
	"U+3d3a":   [wn.synset("why.n.01")],

	# wideness, broadness
	"U+3d3b":   [wn.synset("enormousness.n.01"),
				wn.synset("width.n.01"),
				wn.synset("wideness.n.01")],

	# wiggle, squirm
	"U+3d3d":   [wn.synset("jiggle.v.01"),
				wn.synset("writhe.v.01")],

	# wiggly
	"U+3d3e":   [wn.synset("wavy.s.01"),
				wn.synset("sinuate.s.01"),
				wn.synset("wiggly.s.02"),
				wn.synset("crinkled.s.01")],

	# win
	"U+3d3f":   [wn.synset("win.v.01")],

	# wing
	"U+3d40":   [wn.synset("wing.n.01"),
				wn.synset("wing.n.02")],

	# wink, blink
	"U+3d41":   [wn.synset("wink.v.01"),
				wn.synset("palpebrate.v.01"),
				wn.synset("flash.v.01"),
				wn.synset("wink.v.04"),
				wn.synset("blink.v.01"),
				wn.synset("flicker.v.01")],

	# wipe, dust, polish
	"U+3d42":   [wn.synset("scatter.v.03"),
				wn.synset("clean.v.01"),
				wn.synset("wipe.v.01"),
				wn.synset("clean.v.02"),
				wn.synset("polish.v.01"),
				wn.synset("polish.v.02"),
				wn.synset("polish.v.03"),
				wn.synset("dry.v.02"),
				wn.synset("dry.v.01"),
				wn.synset("clear.v.05"),
				wn.synset("blot.v.01"),
				wn.synset("dust.v.03"),
				wn.synset("dust.v.02"),
				wn.synset("dust.v.01")],

	# wire, cable
	"U+3d43":   [wn.synset("cable.n.04"),
				wn.synset("cable.n.02")],

	# wolf, dingo, wild dog
	"U+3d44":   [wn.synset("wolf.n.01")],

	# wool
	"U+3d45":   [wn.synset("wool.n.01")],

	# workbook
	"U+3d47":   [wn.synset("workbook.n.01"),
				wn.synset("fascicle.n.01")],

	# worry
	"U+3d49":   [wn.synset("concern.n.04"),
				wn.synset("worry.n.02")],

	# wow, super, great, neat, cool, wonderful, fantastic
	"U+3d4a":   [wn.synset("great.n.01"),
				wn.synset("clean.s.17"),
				wn.synset("superintendent.n.02"),
				wn.synset("cool.n.01"),
				wn.synset("aplomb.n.01"),
				wn.synset("belly_laugh.n.02"),
				wn.synset("neat.s.06"),
				wn.synset("neat.s.01"),
				wn.synset("neat.s.02"),
				wn.synset("neat.s.03"),
				wn.synset("bang-up.s.01")],

	# slang
	"U+3d4b":   [wn.synset("slang.n.01"),
				wn.synset("slang.n.02")],

	# wrestling
	"U+3d4c":   [wn.synset("wrestle.n.01"),
				wn.synset("stock.n.02"),
				wn.synset("wrestling.n.02")],

	# write
	"U+3d4e":   [wn.synset("write.v.02"),
				wn.synset("write.v.01"),
				wn.synset("write.v.07"),
				wn.synset("publish.v.03"),
				wn.synset("spell.v.03")],

	# Yahrzeit
	"U+3d4f":   [wn.synset("season.n.02")],

	# yawn
	"U+3d50":   [wn.synset("yawn.v.01")],

	# yell, scream
	"U+3d51":   [wn.synset("shout.v.02")],

	# yellow
	"U+3d52":   [wn.synset("yellow.n.01")],

	# yen
	"U+3d54":   [wn.synset("yen.n.02")],

	# yes
	"U+3d55":   [wn.synset("yes.n.01"),
				wn.synset("ti.n.03")],

	# yesterday
	"U+3d56":   [wn.synset("yesterday.n.01")],

	# Yom Kippur
	"U+3d57":   [wn.synset("yom_kippur.n.01")],

	# you are welcome, you're welcome
	"U+3d5a":   [wn.synset("welcome.n.02"),
				wn.synset("welcome.n.01")],

	# zebra
	"U+3d5c":   [wn.synset("zebra.n.01")],

	# zoo
	"U+3d5d":   [wn.synset("menagerie.n.02")],

	# therapist
	"U+3d60":   [wn.synset("therapist.n.01")],

	# sport
	"U+3d63":   [wn.synset("sport.n.01")],

	# spaghetti
	"U+3d64":   [wn.synset("spaghetti.n.02")],

	# pasta
	"U+3d65":   [wn.synset("pasta.n.02"),
				wn.synset("pasta.n.01")],

	# sauce, gravy, relish, dressing
	"U+3d67":   [wn.synset("sauce.n.01")],

	# salt
	"U+3d68":   [wn.synset("salt.n.02")],

	# tasty, good, appetizing
	"U+3d69":   [wn.synset("adept.s.01"),
				wn.synset("estimable.s.02"),
				wn.synset("good.a.03"),
				wn.synset("good.a.01"),
				wn.synset("tasty.a.01"),
				wn.synset("effective.s.04"),
				wn.synset("beneficial.s.01"),
				wn.synset("dependable.s.04"),
				wn.synset("good.s.15"),
				wn.synset("good.s.19"),
				wn.synset("appetizing.a.01"),
				wn.synset("good.s.12"),
				wn.synset("good.s.13"),
				wn.synset("good.s.16"),
				wn.synset("good.s.17"),
				wn.synset("good.s.21"),
				wn.synset("good.s.06"),
				wn.synset("good.s.09"),
				wn.synset("good.s.18"),
				wn.synset("full.s.06"),
				wn.synset("good.s.07"),
				wn.synset("good.s.20"),
				wn.synset("dear.s.02")],

	# reflection, consideration
	"U+3d6a":   [wn.synset("consideration.n.04"),
				wn.synset("consideration.n.06"),
				wn.synset("consideration.n.01"),
				wn.synset("consideration.n.03"),
				wn.synset("retainer.n.01"),
				wn.synset("circumstance.n.03"),
				wn.synset("mirror_image.n.01"),
				wn.synset("reflection.n.08"),
				wn.synset("contemplation.n.02"),
				wn.synset("reflection.n.05"),
				wn.synset("reflection.n.06"),
				wn.synset("observation.n.03"),
				wn.synset("expression.n.02"),
				wn.synset("reflection.n.02")],

	# religion, naturalism, theology, philosophy of religion
	"U+3d6b":   [wn.synset("religion.n.01"),
				wn.synset("religion.n.02")],

	# religious
	"U+3d6c":   [wn.synset("religious.a.02")],

	# believer
	"U+3d6f":   [wn.synset("believer.n.02")],

	# devil
	"U+3d71":   [wn.synset("devil.n.02"),
				wn.synset("satan.n.01")],

	# spirit
	"U+3d72":   [wn.synset("spirit.n.04"),
				wn.synset("heart.n.06"),
				wn.synset("spirit.n.01"),
				wn.synset("spirit.n.02"),
				wn.synset("spirit.n.03")],

	# supernatural
	"U+3d73":   [wn.synset("supernatural.n.01")],

	# religious ceremony
	"U+3d75":   [wn.synset("religious_ceremony.n.01")],

	# ceremony
	"U+3d76":   [wn.synset("ceremony.n.01")],

	# funeral
	"U+3d78":   [wn.synset("funeral.n.01")],

	# burial
	"U+3d79":   [wn.synset("burial.n.01")],

	# burial site
	"U+3d7a":   [wn.synset("cemetery.n.01")],

	# poverty
	"U+3d7b":   [wn.synset("poverty.n.01")],

	# rugby, football
	"U+3d7e":   [wn.synset("rugby.n.01")],

	# rugby ball
	"U+3d7f":   [wn.synset("rugby_ball.n.01")],

	# judo
	"U+3d82":   [wn.synset("judo.n.01")],

	# skiing
	"U+3d83":   [wn.synset("skiing.n.01")],

	# hamburger
	"U+3d87":   [wn.synset("hamburger.n.01")],

	# chocolate, cocoa, cacao
	"U+3d89":   [wn.synset("cocoa.n.02")],

	# chocolate drink
	"U+3d8c":   [wn.synset("cocoa.n.01")],

	# monotheism
	"U+3d8d":   [wn.synset("monotheism.n.01")],

	# polytheism
	"U+3d8e":   [wn.synset("polytheism.n.01")],

	# Judaism
	"U+3d8f":   [wn.synset("judaism.n.02"),
				wn.synset("judaism.n.01")],

	# Islam
	"U+3d90":   [wn.synset("islam.n.02"),
				wn.synset("islam.n.01")],

	# Eastern Orthodox Church
	"U+3d91":   [wn.synset("orthodox_church.n.01")],

	# Christian
	"U+3d92":   [wn.synset("christian.n.01")],

	# Jew
	"U+3d93":   [wn.synset("jew.n.01")],

	# Muhammad, Mohammed, Muhammed
	"U+3d95":   [wn.synset("mohammed.n.01")],

	# Allah
	"U+3d96":   [wn.synset("allah.n.01")],

	# Vatican, Vatican City
	"U+3d98":   [wn.synset("vatican_city.n.01"),
				wn.synset("vatican.n.01")],

	# Roman Catholicism, Roman Catholic Church
	"U+3d99":   [wn.synset("romanism.n.01")],

	# protestantism
	"U+3d9a":   [wn.synset("protestantism.n.01")],

	# grace
	"U+3d9b":   [wn.synset("grace.n.01")],

	# divine, holy
	"U+3d9c":   [wn.synset("holy.a.01")],

	# bandy
	"U+3d9d":   [wn.synset("bandy.v.02"),
				wn.synset("bandy.v.03"),
				wn.synset("bandy.v.01"),
				wn.synset("bandy.s.01")],

	# Messiah
	"U+3d9e":   [wn.synset("messiah.n.01"),
				wn.synset("messiah.n.02")],

	# soul
	"U+3d9f":   [wn.synset("soul.n.01")],

	# Mary
	"U+3da0":   [wn.synset("mary.n.01")],

	# Joseph, Saint Joseph
	"U+3da1":   [wn.synset("joseph.n.02"),
				wn.synset("joseph.n.03")],

	# prophecy
	"U+3da2":   [wn.synset("prophecy.n.02")],

	# prophesy
	"U+3da3":   [wn.synset("prophesy.v.01"),
				wn.synset("profess.v.02"),
				wn.synset("profess.v.06"),
				wn.synset("preach.v.01")],

	# prophet
	"U+3da4":   [wn.synset("prophet.n.01"),
				wn.synset("prophet.n.02")],

	# predict
	"U+3da6":   [wn.synset("predict.v.01")],

	# follow
	"U+3da8":   [wn.synset("follow.v.01")],

	# religious leader
	"U+3daa":   [wn.synset("religious_leader.n.01")],

	# bishop
	"U+3dac":   [wn.synset("bishop.n.01")],

	# Pope
	"U+3dae":   [wn.synset("pope.n.01")],

	# disperse, disseminate, scatter, spread
	"U+3daf":   [wn.synset("spread.v.02"),
				wn.synset("spread.v.07"),
				wn.synset("disperse.v.02")],

	# dispersion, dissemination, scattering, spread, spreading
	"U+3db0":   [wn.synset("spread.n.08"),
				wn.synset("distribution.n.02"),
				wn.synset("dissemination.n.01"),
				wn.synset("bedspread.n.01"),
				wn.synset("dissemination.n.02"),
				wn.synset("banquet.n.02"),
				wn.synset("spread.n.01"),
				wn.synset("spread.n.07"),
				wn.synset("spread.n.05"),
				wn.synset("spread.n.10"),
				wn.synset("ranch.n.01"),
				wn.synset("gap.n.01"),
				wn.synset("dispersion.n.03"),
				wn.synset("scatter.n.01"),
				wn.synset("dispersion.n.01"),
				wn.synset("scatter.n.02"),
				wn.synset("scattering.n.03"),
				wn.synset("scattering.n.02"),
				wn.synset("scattering.n.01")],

	# apostle
	"U+3db5":   [wn.synset("apostle.n.03")],

	# missionary
	"U+3db7":   [wn.synset("missionary.n.02")],

	# hell
	"U+3db8":   [wn.synset("hell.n.01"),
				wn.synset("hell.n.03")],

	# Adam
	"U+3dba":   [wn.synset("adam.n.01")],

	# Eve
	"U+3dbb":   [wn.synset("eve.n.01")],

	# Noah
	"U+3dbc":   [wn.synset("noah.n.01")],

	# Abraham
	"U+3dbd":   [wn.synset("abraham.n.01")],

	# Moses
	"U+3dbe":   [wn.synset("moses.n.01")],

	# holy book
	"U+3dbf":   [wn.synset("bible.n.02"),
				wn.synset("bible.n.01")],

	# Bible
	"U+3dc1":   [wn.synset("bible.n.01")],

	# Old Testament
	"U+3dc2":   [wn.synset("old_testament.n.01")],

	# New Testament
	"U+3dc3":   [wn.synset("new_testament.n.01")],

	# Koran
	"U+3dc4":   [wn.synset("koran.n.01")],

	# hymnal, hymn book
	"U+3dc5":   [wn.synset("hymnal.n.01")],

	# hymn, psalm, gospel song
	"U+3dc6":   [wn.synset("hymn.n.01"),
				wn.synset("psalm.n.01")],

	# missal, liturgical book
	"U+3dc7":   [wn.synset("missal.n.01")],

	# gospel
	"U+3dc8":   [wn.synset("gospel.n.01")],

	# appearance, manifestation
	"U+3dc9":   [wn.synset("expression.n.02"),
				wn.synset("appearance.n.05"),
				wn.synset("demonstration.n.03"),
				wn.synset("appearance.n.02"),
				wn.synset("manifestation.n.01")],

	# appear
	"U+3dca":   [wn.synset("appear.v.02")],

	# disappearance
	"U+3dcb":   [wn.synset("disappearance.n.01")],

	# disappear
	"U+3dce":   [wn.synset("disappear.v.01")],

	# holiness
	"U+3dcf":   [wn.synset("holiness.n.01")],

	# sanctify, consecrate
	"U+3dd1":   [wn.synset("consecrate.v.04")],

	# saint
	"U+3dd2":   [wn.synset("saint.n.01")],

	# Holy City
	"U+3dd7":   [wn.synset("celestial_city.n.01")],

	# meditate
	"U+3dde":   [wn.synset("study.v.06"),
				wn.synset("chew_over.v.01")],

	# insight
	"U+3de0":   [wn.synset("insight.n.02"),
				wn.synset("penetration.n.02"),
				wn.synset("intuition.n.01"),
				wn.synset("insight.n.04"),
				wn.synset("insight.n.03")],

	# confess
	"U+3de1":   [wn.synset("concede.v.01"),
				wn.synset("confess.v.01"),
				wn.synset("confess.v.03")],

	# sacrament
	"U+3de5":   [wn.synset("sacrament.n.01")],

	# sacrament of baptism
	"U+3de6":   [wn.synset("christening.n.01"),
				wn.synset("baptize.v.01"),
				wn.synset("baptism.n.01"),
				wn.synset("dub.v.01"),
				wn.synset("name.v.01")],

	# sacrament of confirmation
	"U+3de7":   [wn.synset("confirmation.n.05")],

	# sacrament of communion
	"U+3de8":   [wn.synset("holy_eucharist.n.01")],

	# sacrament of absolution
	"U+3de9":   [wn.synset("absolution.n.01"),
				wn.synset("absolution.n.02")],

	# sacrament of marriage
	"U+3dec":   [wn.synset("matrimony.n.02"),
				wn.synset("marriage.n.02"),
				wn.synset("marriage.n.01")],

	# confirmation
	"U+3def":   [wn.synset("confirmation.n.05")],

	# bat mitzvah
	"U+3df0":   [wn.synset("bat_mitzvah.n.01")],

	# bar mitzvah
	"U+3df1":   [wn.synset("bar_mitzvah.n.01")],

	# coffin
	"U+3df3":   [wn.synset("coffin.n.01")],

	# mausoleum
	"U+3df4":   [wn.synset("mausoleum.n.01")],

	# urn
	"U+3df7":   [wn.synset("urn.n.01"),
				wn.synset("urn.n.02")],

	# vase, urn, trophy cup
	"U+3df8":   [wn.synset("urn.n.02"),
				wn.synset("urn.n.01"),
				wn.synset("vase.n.01")],

	# tomb
	"U+3df9":   [wn.synset("grave.n.02")],

	# tombstone
	"U+3dfb":   [wn.synset("gravestone.n.01")],

	# cremation
	"U+3dfc":   [wn.synset("cremation.n.01")],

	# cremate
	"U+3dfd":   [wn.synset("cremate.v.01")],

	# revelry
	"U+3dfe":   [wn.synset("disclosure.n.01"),
				wn.synset("revelation.n.02"),
				wn.synset("revel.n.01")],

	# religious gathering
	"U+3dff":   [wn.synset("meeting.n.03"),
				wn.synset("service.n.03")],

	# awful
	"U+3e00":   [wn.synset("amazing.s.02"),
				wn.synset("frightful.s.02"),
				wn.synset("awed.s.01"),
				wn.synset("atrocious.s.02"),
				wn.synset("nasty.a.01"),
				wn.synset("awful.s.02")],

	# celebration
	"U+3e01":   [wn.synset("celebration.n.01")],

	# celebration of life
	"U+3e02":   [wn.synset("celebration.n.02"),
				wn.synset("celebration.n.03"),
				wn.synset("celebration.n.01")],

	# misericordia
	"U+3e04":   [wn.synset("mercifulness.n.02"),
				wn.synset("mercifulness.n.01"),
				wn.synset("commiseration.n.01"),
				wn.synset("compassion.n.02")],

	# forgiveness, pardon
	"U+3e05":   [wn.synset("forgiveness.n.02")],

	# unforgivable, inexcusable
	"U+3e06":   [wn.synset("inexcusable.a.01"),
				wn.synset("inexcusable.s.02"),
				wn.synset("unpardonable.a.01")],

	# shiva
	"U+3e07":   [wn.synset("siva.n.01")],

	# mourn
	"U+3e09":   [wn.synset("mourn.v.02"),
				wn.synset("mourn.v.01")],

	# mystery, unknown
	"U+3e0a":   [wn.synset("mystery.n.01")],

	# mysterious, unknown
	"U+3e0b":   [wn.synset("unknown.a.01"),
				wn.synset("cryptic.s.01")],

	# miracle
	"U+3e0c":   [wn.synset("miracle.n.02")],

	# vision, apparition
	"U+3e0d":   [wn.synset("vision.n.01"),
				wn.synset("vision.n.05"),
				wn.synset("sight.n.03"),
				wn.synset("apparition.n.01"),
				wn.synset("apparition.n.02"),
				wn.synset("apparition.n.03")],

	# atheism
	"U+3e0e":   [wn.synset("atheism.n.02"),
				wn.synset("atheism.n.01")],

	# Christian faith
	"U+3e0f":   [wn.synset("creed.n.01"),
				wn.synset("impression.n.01"),
				wn.synset("belief.n.01"),
				wn.synset("religion.n.01")],

	# Christian hope
	"U+3e10":   [wn.synset("jump.n.01")],

	# Christian love
	"U+3e11":   [wn.synset("love.n.02")],

	# Christian charity
	"U+3e12":   [wn.synset("charity.n.05"),
				wn.synset("charity.n.03")],

	# impoverish
	"U+3e13":   [wn.synset("impoverish.v.01"),
				wn.synset("get_worse.v.01"),
				wn.synset("devolve.v.03"),
				wn.synset("worsen.v.02"),
				wn.synset("worsen.v.01"),
				wn.synset("deprive.v.03")],

	# abstention
	"U+3e14":   [wn.synset("abstinence.n.01")],

	# obedience
	"U+3e15":   [wn.synset("obedience.n.01"),
				wn.synset("obedience.n.02"),
				wn.synset("obedience.n.03")],

	# preach
	"U+3e16":   [wn.synset("preach.v.01")],

	# persuade, convince
	"U+3e18":   [wn.synset("convert.v.09")],

	# persuasion
	"U+3e19":   [wn.synset("conviction.n.01"),
				wn.synset("persuasion.n.01"),
				wn.synset("opinion.n.01")],

	# amen
	"U+3e1a":   [wn.synset("amen.n.01")],

	# dead person
	"U+3e1b":   [wn.synset("body.n.03"),
				wn.synset("dead_person.n.01"),
				wn.synset("cadaver.n.01")],

	# corpse, cadaver
	"U+3e1d":   [wn.synset("cadaver.n.01")],

	# resurrection
	"U+3e1e":   [wn.synset("resurrection.n.02")],

	# ritual
	"U+3e1f":   [wn.synset("ritual.n.02"),
				wn.synset("ritual.n.01")],

	# perseverance
	"U+3e20":   [wn.synset("perseverance.n.02"),
				wn.synset("doggedness.n.01")],

	# persevere
	"U+3e21":   [wn.synset("persevere.v.01")],

	# convert
	"U+3e22":   [wn.synset("convert.v.05")],

	# conversion
	"U+3e23":   [wn.synset("conversion.n.04"),
				wn.synset("conversion.n.01")],

	# Ramadan
	"U+3e25":   [wn.synset("ramadan.n.01")],

	# forefather
	"U+3e26":   [wn.synset("forefather.n.01"),
				wn.synset("forefather.n.02"),
				wn.synset("ancestor.n.01")],

	# foremother
	"U+3e27":   [wn.synset("foremother.n.01")],

	# ancestor
	"U+3e28":   [wn.synset("ancestor.n.01")],

	# all powerful
	"U+3e2a":   [wn.synset("almighty.s.01")],

	# unending
	"U+3e2b":   [wn.synset("ageless.s.01")],

	# interrogate
	"U+3e2c":   [wn.synset("interrogate.v.02")],

	# beg, plead
	"U+3e2d":   [wn.synset("beg.v.01"),
				wn.synset("beg.v.03"),
				wn.synset("beg.v.04"),
				wn.synset("solicit.v.01"),
				wn.synset("plead.v.04"),
				wn.synset("plead.v.02"),
				wn.synset("plead.v.03"),
				wn.synset("plead.v.01")],

	# demand
	"U+3e2e":   [wn.synset("demand.v.01")],

	# proclaim, announce
	"U+3e2f":   [wn.synset("announce.v.02"),
				wn.synset("proclaim.v.02")],

	# proclamation, announcement
	"U+3e30":   [wn.synset("announcement.n.01")],

	# flyer
	"U+3e32":   [wn.synset("aviator.n.01"),
				wn.synset("flier.n.01"),
				wn.synset("circular.n.01")],

	# correctness
	"U+3e34":   [wn.synset("correctness.n.02"),
				wn.synset("correctness.n.01")],

	# excellence
	"U+3e36":   [wn.synset("excellence.n.01")],

	# excellent
	"U+3e37":   [wn.synset("excellent.s.01")],

	# perfection
	"U+3e38":   [wn.synset("perfection.n.01")],

	# perfect
	"U+3e39":   [wn.synset("perfect.a.01")],

	# evangelise
	"U+3e3a":   [wn.synset("evangelize.v.02"),
				wn.synset("evangelize.v.01")],

	# drown
	"U+3e3b":   [wn.synset("drown.v.03")],

	# drowning
	"U+3e3c":   [wn.synset("drown.v.02"),
				wn.synset("drown.v.03"),
				wn.synset("swim.v.04"),
				wn.synset("drown.v.04"),
				wn.synset("submerge.v.02")],

	# desert
	"U+3e3d":   [wn.synset("desert.n.01")],

	# wilderness
	"U+3e3e":   [wn.synset("wilderness.n.03")],

	# huge
	"U+3e40":   [wn.synset("huge.s.01")],

	# enormous
	"U+3e41":   [wn.synset("enormous.s.01")],

	# gigantic
	"U+3e42":   [wn.synset("gigantic.s.01"),
				wn.synset("elephantine.s.01")],

	# manna
	"U+3e43":   [wn.synset("miraculous_food.n.01")],

	# uninhabited
	"U+3e44":   [wn.synset("uninhabited.a.01")],

	# fishnet
	"U+3e45":   [wn.synset("fishnet.n.01")],

	# incense
	"U+3e46":   [wn.synset("incense.n.01")],

	# calling, vocation, profession, career
	"U+3e48":   [wn.synset("career.n.01")],

	# nag
	"U+3e49":   [wn.synset("nag.v.01"),
				wn.synset("nag.v.02"),
				wn.synset("nag.v.03")],

	# oil lamp
	"U+3e4a":   [wn.synset("oil_lamp.n.01")],

	# goblet, wineglass
	"U+3e4b":   [wn.synset("wineglass.n.01"),
				wn.synset("goblet.n.01"),
				wn.synset("chalice.n.01")],

	# chalice
	"U+3e4c":   [wn.synset("chalice.n.01")],

	# ampullae
	"U+3e4d":   [wn.synset("ampulla.n.02"),
				wn.synset("ampulla.n.01")],

	# paten, holy tray
	"U+3e4e":   [wn.synset("patina.n.01")],

	# Host, wafer
	"U+3e4f":   [wn.synset("master_of_ceremonies.n.01"),
				wn.synset("wafer.n.01"),
				wn.synset("horde.n.01"),
				wn.synset("server.n.03"),
				wn.synset("host.n.09"),
				wn.synset("host.n.08"),
				wn.synset("wafer.n.03"),
				wn.synset("host.n.01"),
				wn.synset("host.n.03"),
				wn.synset("wafer.n.02"),
				wn.synset("host.n.05"),
				wn.synset("host.n.07"),
				wn.synset("host.n.06")],

	# altar
	"U+3e50":   [wn.synset("altar.n.02")],

	# vestment
	"U+3e53":   [wn.synset("vestment.n.01"),
				wn.synset("chasuble.n.01")],

	# Christmas tree
	"U+3e54":   [wn.synset("christmas_tree.n.05")],

	# interview
	"U+3e55":   [wn.synset("interview.n.01")],

	# interviewer
	"U+3e56":   [wn.synset("interviewer.n.01")],

	# universal, world wide
	"U+3e58":   [wn.synset("universal.s.02"),
				wn.synset("universal.s.03"),
				wn.synset("global.s.01"),
				wn.synset("worldwide.s.01"),
				wn.synset("cosmopolitan.s.03")],

	# forgiven
	"U+3e59":   [wn.synset("forgive.v.01")],

	# sign language
	"U+3e5a":   [wn.synset("sign_language.n.01")],

	# polder
	"U+3e5b":   [wn.synset("polder.n.01")],

	# dryness, drought
	"U+3e5c":   [wn.synset("dryness.n.01")],

	# cell
	"U+3e5d":   [wn.synset("cell.n.02")],

	# Euro
	"U+3e5e":   [wn.synset("euro.n.01")],

	# astronomy
	"U+3e5f":   [wn.synset("astronomy.n.01")],

	# economics
	"U+3e60":   [wn.synset("economics.n.01")],

	# chemistry
	"U+3e61":   [wn.synset("chemistry.n.02"),
				wn.synset("chemistry.n.03"),
				wn.synset("chemistry.n.01")],

	# biochemistry
	"U+3e62":   [wn.synset("biochemistry.n.01")],

	# biochemical product, organic compound
	"U+3e63":   [wn.synset("organic_compound.n.01")],

	# biology
	"U+3e64":   [wn.synset("biology.n.01")],

	# botany
	"U+3e66":   [wn.synset("botany.n.02")],

	# anthropology
	"U+3e67":   [wn.synset("anthropology.n.01")],

	# zoology
	"U+3e68":   [wn.synset("zoology.n.02")],

	# geology
	"U+3e69":   [wn.synset("geology.n.01")],

	# sociology
	"U+3e6a":   [wn.synset("sociology.n.01")],

	# history
	"U+3e6b":   [wn.synset("history.n.04"),
				wn.synset("history.n.05"),
				wn.synset("history.n.02"),
				wn.synset("history.n.03"),
				wn.synset("history.n.01")],

	# archeology
	"U+3e6c":   [wn.synset("archeology.n.01")],

	# meteorology
	"U+3e6d":   [wn.synset("meteorology.n.02")],

	# physics
	"U+3e6e":   [wn.synset("physics.n.01")],

	# linguistics
	"U+3e6f":   [wn.synset("linguistics.n.01")],

	# scientist, academic, researcher
	"U+3e70":   [wn.synset("scientist.n.01"),
				wn.synset("research_worker.n.01")],

	# astronomer
	"U+3e72":   [wn.synset("astronomer.n.01")],

	# economist
	"U+3e74":   [wn.synset("economist.n.01")],

	# chemist
	"U+3e76":   [wn.synset("chemist.n.01")],

	# biochemist
	"U+3e78":   [wn.synset("biochemist.n.01")],

	# biologist
	"U+3e7a":   [wn.synset("biologist.n.01")],

	# botanist
	"U+3e7c":   [wn.synset("botanist.n.01")],

	# zoologist
	"U+3e7e":   [wn.synset("zoologist.n.01")],

	# geologist
	"U+3e80":   [wn.synset("geologist.n.01")],

	# sociologist
	"U+3e82":   [wn.synset("sociologist.n.01")],

	# historian
	"U+3e84":   [wn.synset("historian.n.01")],

	# archeologist
	"U+3e86":   [wn.synset("archeologist.n.01")],

	# meteorologist
	"U+3e88":   [wn.synset("meteorologist.n.01")],

	# linguist
	"U+3e8a":   [wn.synset("linguist.n.01")],

	# mathematician
	"U+3e8c":   [wn.synset("mathematician.n.01")],

	# paediatrician
	"U+3e8d":   [wn.synset("baby_doctor.n.01")],

	# surgeon
	"U+3e8e":   [wn.synset("surgeon.n.01")],

	# otolaryngologist
	"U+3e8f":   [wn.synset("ent_man.n.01")],

	# orthopaedist
	"U+3e90":   [wn.synset("orthopedist.n.01")],

	# ophthalmologist, oculist
	"U+3e92":   [wn.synset("ophthalmologist.n.01")],

	# gynecologist
	"U+3e93":   [wn.synset("gynecologist.n.01")],

	# general practitioner
	"U+3e94":   [wn.synset("general_practitioner.n.01")],

	# cardiologist
	"U+3e95":   [wn.synset("cardiologist.n.01")],

	# neurologist
	"U+3e96":   [wn.synset("neurologist.n.01")],

	# central nervous system, CNS
	"U+3e97":   [wn.synset("central_nervous_system.n.01")],

	# psychiatrist
	"U+3e98":   [wn.synset("psychiatrist.n.01")],

	# therapy
	"U+3e9a":   [wn.synset("therapy.n.01")],

	# speech therapist
	"U+3e9b":   [wn.synset("speech_therapist.n.01")],

	# physiotherapist
	"U+3e9e":   [wn.synset("physical_therapist.n.01")],

	# audiologist
	"U+3ea0":   [wn.synset("audiology.n.01")],

	# orthoptist
	"U+3ea1":   [wn.synset("orthoptist.n.01")],

	# podiatrist, chiropodist
	"U+3ea4":   [wn.synset("chiropodist.n.01")],

	# osteopath
	"U+3eab":   [wn.synset("osteopath.n.01")],

	# chiropractor
	"U+3eac":   [wn.synset("chiropractor.n.01")],

	# masseur
	"U+3ead":   [wn.synset("massager.n.01"),
				wn.synset("masseur.n.01")],

	# culture
	"U+3eb2":   [wn.synset("culture.n.01"),
				wn.synset("culture.n.02")],

	# people, tribe, clan, folk
	"U+3eb3":   [wn.synset("kin.n.02")],

	# nation
	"U+3eb4":   [wn.synset("nation.n.02"),
				wn.synset("state.n.04")],

	# folk music
	"U+3eb5":   [wn.synset("folk_music.n.01")],

	# genocide, holocaust
	"U+3eb7":   [wn.synset("genocide.n.01")],

	# headscarf
	"U+3eba":   [wn.synset("fichu.n.01"),
				wn.synset("handkerchief.n.01"),
				wn.synset("headscarf.n.01")],

	# veil
	"U+3ebc":   [wn.synset("head_covering.n.01")],

	# helmet
	"U+3ebe":   [wn.synset("helmet.n.02")],

	# bicycle helmet, crash helmet
	"U+3ec1":   [wn.synset("helmet.n.02"),
				wn.synset("crash_helmet.n.01")],

	# knee pad
	"U+3ec3":   [wn.synset("knee_pad.n.01")],

	# elbow pad
	"U+3ec5":   [wn.synset("elbow_pad.n.01")],

	# protective mask
	"U+3ec7":   [wn.synset("face_guard.n.01"),
				wn.synset("face_mask.n.01")],

	# suit of armour
	"U+3ec8":   [wn.synset("armor.n.01"),
				wn.synset("body_armor.n.01")],

	# water sports
	"U+3ecd":   [wn.synset("water_sport.n.01")],

	# contact sports
	"U+3ece":   [wn.synset("contact_sport.n.01"),
				wn.synset("martial_art.n.01")],

	# athletics
	"U+3ecf":   [wn.synset("athletic_contest.n.01")],

	# equestrian sports
	"U+3ed0":   [wn.synset("equestrian_sport.n.01")],

	# sky sports
	"U+3ed6":   [wn.synset("parasailing.n.01")],

	# shooting sports
	"U+3ed7":   [wn.synset("gunfire.n.01"),
				wn.synset("fusillade.n.01"),
				wn.synset("shooting.n.01"),
				wn.synset("discharge.n.09"),
				wn.synset("fire.n.02")],

	# gymnastics
	"U+3ed9":   [wn.synset("gymnastics.n.01")],

	# boating
	"U+3edd":   [wn.synset("boating.n.01")],

	# stickball
	"U+3ede":   [wn.synset("stickball.n.01")],

	# volleyball
	"U+3edf":   [wn.synset("volleyball.n.01")],

	# water polo
	"U+3ee1":   [wn.synset("water_polo.n.01")],

	# boules
	"U+3ee2":   [wn.synset("boulle.n.01"),
				wn.synset("lawn_bowling.n.01")],

	# cricket
	"U+3ee4":   [wn.synset("cricket.n.02")],

	# wicket
	"U+3ee6":   [wn.synset("wicket.n.04"),
				wn.synset("wicket.n.02"),
				wn.synset("wicket.n.03"),
				wn.synset("wicket.n.01")],

	# motorcycle, scooter
	"U+3ee7":   [wn.synset("iceboat.n.02"),
				wn.synset("scoter.n.01"),
				wn.synset("scooter.n.02"),
				wn.synset("water_scooter.n.01"),
				wn.synset("motor_scooter.n.01"),
				wn.synset("motorcycle.n.01")],

	# prone board, scooter board
	"U+3ee9":   [wn.synset("skateboard.n.01")],

	# tandem bicycle
	"U+3eec":   [wn.synset("bicycle-built-for-two.n.01")],

	# mountain bike
	"U+3eed":   [wn.synset("mountain_bike.n.01")],

	# ATB, all terrain bike
	"U+3eee":   [wn.synset("mountain_bike.n.01")],

	# sidecar
	"U+3ef2":   [wn.synset("sidecar.n.01"),
				wn.synset("sidecar.n.02")],

	# go kart, kart
	"U+3ef3":   [wn.synset("go-kart.n.01")],

	# cycling
	"U+3ef4":   [wn.synset("cycling.n.01"),
				wn.synset("bicycling.n.01")],

	# motorcycling, motocross
	"U+3ef9":   [wn.synset("motorcycling.n.01")],

	# car racing, auto racing
	"U+3efe":   [wn.synset("auto_racing.n.01")],

	# Formula One, NASCAR Kart
	"U+3eff":   [wn.synset("rally.n.01")],

	# cycle, ride a bike
	"U+3f01":   [wn.synset("bicycle.v.01")],

	# go by airplane
	"U+3f03":   [wn.synset("fly.v.01")],

	# riding, horseback riding
	"U+3f05":   [wn.synset("riding.n.02")],

	# fencing
	"U+3f07":   [wn.synset("fencing.n.03")],

	# martial arts
	"U+3f09":   [wn.synset("martial_art.n.01")],

	# running
	"U+3f0b":   [wn.synset("run.n.07")],

	# hurdles
	"U+3f0c":   [wn.synset("hurdles.n.01")],

	# relay
	"U+3f0e":   [wn.synset("relay.n.04")],

	# high jump
	"U+3f10":   [wn.synset("high_jump.n.01"),
				wn.synset("high_jump.n.02")],

	# pole vaulting
	"U+3f12":   [wn.synset("pole_vault.n.01")],

	# shot put
	"U+3f13":   [wn.synset("shot_put.n.01")],

	# discus
	"U+3f14":   [wn.synset("magnetic_disk.n.01"),
				wn.synset("disk.n.02"),
				wn.synset("disk.n.01"),
				wn.synset("phonograph_record.n.01"),
				wn.synset("disco.n.02"),
				wn.synset("discus.n.01"),
				wn.synset("discus.n.02"),
				wn.synset("disco.n.01")],

	# hammer throw
	"U+3f16":   [wn.synset("hammer_throw.n.01")],

	# chain
	"U+3f18":   [wn.synset("chain.n.03")],

	# dart
	"U+3f19":   [wn.synset("flit.n.01"),
				wn.synset("dart.n.02"),
				wn.synset("dart.n.01")],

	# javelin throw
	"U+3f1a":   [wn.synset("javelin.n.01")],

	# javelin, spear
	"U+3f1b":   [wn.synset("spear.n.01"),
				wn.synset("spear.n.02"),
				wn.synset("javelin.n.01"),
				wn.synset("javelin.n.02")],

	# darts
	"U+3f1c":   [wn.synset("darts.n.01")],

	# bow and arrow
	"U+3f1d":   [wn.synset("bow_and_arrow.n.01")],

	# archery
	"U+3f1e":   [wn.synset("archery.n.01")],

	# weight lifting
	"U+3f23":   [wn.synset("weightlift.n.01")],

	# skating
	"U+3f24":   [wn.synset("skating.n.01")],

	# speed skating
	"U+3f26":   [wn.synset("speed_skating.n.01")],

	# figure skating
	"U+3f27":   [wn.synset("figure_skating.n.01")],

	# slalom
	"U+3f29":   [wn.synset("slalom.n.01")],

	# downhill skiing
	"U+3f2b":   [wn.synset("downhill.n.02")],

	# ski jumping
	"U+3f2e":   [wn.synset("ski_jump.n.01"),
				wn.synset("ski_jumping.n.01")],

	# freestyle skiing
	"U+3f2f":   [wn.synset("ski.n.01"),
				wn.synset("skiing.n.01")],

	# snowboarding
	"U+3f30":   [wn.synset("snowboarding.n.01")],

	# snowboard
	"U+3f32":   [wn.synset("snowboard.n.01")],

	# sled sport
	"U+3f33":   [wn.synset("sledding.n.01"),
				wn.synset("toboggan.n.01")],

	# bobsleigh
	"U+3f35":   [wn.synset("bobsled.n.02"),
				wn.synset("bobsled.n.01")],

	# horse sled, horse drawn sleigh
	"U+3f36":   [wn.synset("sled.n.01")],

	# dog sled
	"U+3f37":   [wn.synset("dogsled.n.01")],

	# rocking horse
	"U+3f3b":   [wn.synset("hobby.n.02")],

	# sled dog
	"U+3f40":   [wn.synset("sled_dog.n.01")],

	# curling
	"U+3f41":   [wn.synset("curling.n.01")],

	# wave
	"U+3f42":   [wn.synset("wave.n.01")],

	# surfboard
	"U+3f43":   [wn.synset("surfboard.n.01")],

	# water ski
	"U+3f47":   [wn.synset("water_ski.n.01")],

	# jet ski
	"U+3f48":   [wn.synset("water_scooter.n.01")],

	# water skiing
	"U+3f4b":   [wn.synset("water_ski.v.01"),
				wn.synset("water-skiing.n.01")],

	# sailing
	"U+3f4d":   [wn.synset("seafaring.n.01"),
				wn.synset("sailing.n.03"),
				wn.synset("sailing.n.02"),
				wn.synset("glide.n.03"),
				wn.synset("cruise.n.01")],

	# canoeing
	"U+3f4f":   [wn.synset("canoe.v.01")],

	# rowing
	"U+3f51":   [wn.synset("rowing.n.01")],

	# diving, activity under water
	"U+3f55":   [wn.synset("diving.n.01"),
				wn.synset("dive.n.02")],

	# snorkeling, scuba diving, deep sea diving
	"U+3f58":   [wn.synset("snorkeling.n.01"),
				wn.synset("dip.n.08"),
				wn.synset("scuba_diving.n.01"),
				wn.synset("dive.n.02"),
				wn.synset("dive.n.03")],

	# mast
	"U+3f5a":   [wn.synset("mast.n.01")],

	# boom
	"U+3f5b":   [wn.synset("boom.n.04"),
				wn.synset("boom.n.05"),
				wn.synset("boom.n.01"),
				wn.synset("boom.n.02"),
				wn.synset("boom.n.03")],

	# deck
	"U+3f5c":   [wn.synset("deck.n.01")],

	# stern
	"U+3f5d":   [wn.synset("stern.n.01")],

	# keel
	"U+3f5e":   [wn.synset("keel.n.02"),
				wn.synset("keel.n.03")],

	# hull, body
	"U+3f5f":   [wn.synset("hull.n.06")],

	# rudder
	"U+3f60":   [wn.synset("rudder.n.02"),
				wn.synset("rudder.n.01")],

	# paddle, oar
	"U+3f61":   [wn.synset("paddle.n.01"),
				wn.synset("oar.n.01"),
				wn.synset("paddle.n.03"),
				wn.synset("paddle.n.02"),
				wn.synset("paddle.n.04")],

	# freighter
	"U+3f62":   [wn.synset("bottom.n.07")],

	# tanker
	"U+3f63":   [wn.synset("oil_tanker.n.01")],

	# oil tanker
	"U+3f64":   [wn.synset("oil_tanker.n.01")],

	# barge, river boat
	"U+3f65":   [wn.synset("barge.n.01"),
				wn.synset("river_boat.n.01")],

	# schooner
	"U+3f67":   [wn.synset("schooner.n.02")],

	# motorboat
	"U+3f69":   [wn.synset("motorboat.n.01")],

	# canoe
	"U+3f6a":   [wn.synset("canoe.n.01")],

	# rowing boat
	"U+3f6b":   [wn.synset("rowing_boat.n.01"),
				wn.synset("skiff.n.01"),
				wn.synset("dinghy.n.01")],

	# kayak
	"U+3f6c":   [wn.synset("kayak.n.01")],

	# lifeboat
	"U+3f6d":   [wn.synset("lifeboat.n.01")],

	# pilot boat
	"U+3f6f":   [wn.synset("pilot_boat.n.01")],

	# towboat, tugboat
	"U+3f71":   [wn.synset("tugboat.n.01")],

	# pushboat
	"U+3f72":   [wn.synset("tugboat.n.01")],

	# cruise ship
	"U+3f74":   [wn.synset("cruise_ship.n.01")],

	# ferry
	"U+3f76":   [wn.synset("ferry.n.01")],

	# steamship
	"U+3f77":   [wn.synset("steamer.n.03")],

	# hovercraft
	"U+3f79":   [wn.synset("hovercraft.n.01")],

	# rubber boat, dinghy
	"U+3f7a":   [wn.synset("dinghy.n.01")],

	# catamaran, pontoon boat
	"U+3f7b":   [wn.synset("catamaran.n.01")],

	# houseboat
	"U+3f7e":   [wn.synset("houseboat.n.01")],

	# boathouse
	"U+3f80":   [wn.synset("boathouse.n.01")],

	# horse rider, equestrian
	"U+3f81":   [wn.synset("horseman.n.01")],

	# jockey
	"U+3f82":   [wn.synset("jockey.n.01")],

	# sulky
	"U+3f83":   [wn.synset("sulky.n.01")],

	# horse racing
	"U+3f84":   [wn.synset("horse_racing.n.01")],

	# carriage racing
	"U+3f85":   [wn.synset("harness_race.n.01")],

	# showjumping
	"U+3f87":   [wn.synset("showjumping.n.01")],

	# dressage
	"U+3f88":   [wn.synset("dressage.n.01"),
				wn.synset("skillfulness.n.01"),
				wn.synset("skill.n.01"),
				wn.synset("skill.n.02"),
				wn.synset("craft.n.04"),
				wn.synset("dexterity.n.01")],

	# polo
	"U+3f89":   [wn.synset("polo.n.02")],

	# billiards
	"U+3f8a":   [wn.synset("billiards.n.01")],

	# glider
	"U+3f8c":   [wn.synset("glider.n.01")],

	# seaplane
	"U+3f8d":   [wn.synset("seaplane.n.01")],

	# parachute
	"U+3f8e":   [wn.synset("parachute.n.01")],

	# parachuting
	"U+3f8f":   [wn.synset("jump.n.05")],

	# ballooning
	"U+3f91":   [wn.synset("ballooning.n.01"),
				wn.synset("hot-air_balloon.n.01"),
				wn.synset("balloon.n.02")],

	# mountain climbing
	"U+3f92":   [wn.synset("mountain_climbing.n.01")],

	# abseiling, rappelling
	"U+3f94":   [wn.synset("descent.n.01"),
				wn.synset("descent.n.03"),
				wn.synset("descent.n.05"),
				wn.synset("demotion.n.01"),
				wn.synset("downhill.n.02"),
				wn.synset("decrease.n.01"),
				wn.synset("rappel.v.01"),
				wn.synset("drop.n.03"),
				wn.synset("downfall.n.01")],

	# parasailing
	"U+3f97":   [wn.synset("parasailing.n.01")],

	# paraskiing
	"U+3f98":   [wn.synset("parasailing.n.01")],

	# hang gliding
	"U+3f9a":   [wn.synset("hang_gliding.n.01")],

	# kite flying
	"U+3f9b":   [wn.synset("libration.n.01")],

	# indoor, indoors
	"U+3f9d":   [wn.synset("inside.r.01"),
				wn.synset("indoor.a.01"),
				wn.synset("indoor.s.02")],

	# outdoor, outdoors
	"U+3f9e":   [wn.synset("outdoor.a.01")],

	# appetizer, starter, entree
	"U+3f9f":   [wn.synset("crank.n.04"),
				wn.synset("entrance.n.01"),
				wn.synset("appetizer.n.01"),
				wn.synset("hors_d'oeuvre.n.01"),
				wn.synset("newcomer.n.01"),
				wn.synset("entree.n.04"),
				wn.synset("entree.n.02"),
				wn.synset("starter.n.01"),
				wn.synset("starter.n.03"),
				wn.synset("starter.n.02"),
				wn.synset("entree.n.01"),
				wn.synset("starter.n.07")],

	# main course
	"U+3fa1":   [wn.synset("entree.n.01"),
				wn.synset("piece_de_resistance.n.02"),
				wn.synset("main_course.n.02")],

	# muffin, bun
	"U+3fa5":   [wn.synset("muffin.n.01")],

	# cupcake, fancy cake, pastry
	"U+3fa6":   [wn.synset("cake.n.03"),
				wn.synset("pastry.n.01"),
				wn.synset("pastry.n.02"),
				wn.synset("cupcake.n.01")],

	# doughnut
	"U+3fa7":   [wn.synset("doughnut.n.02")],

	# bagel
	"U+3fa8":   [wn.synset("bagel.n.01")],

	# waffle
	"U+3fa9":   [wn.synset("waffle.n.01"),
				wn.synset("wafer.n.02")],

	# grid, matrix
	"U+3faa":   [wn.synset("matrix.n.01")],

	# fishball
	"U+3fac":   [wn.synset("gefilte_fish.n.01")],

	# dumpling
	"U+3fad":   [wn.synset("dumpling.n.01"),
				wn.synset("dumpling.n.02")],

	# macaroni
	"U+3fae":   [wn.synset("macaroni.n.02")],

	# farfalle
	"U+3fb0":   [wn.synset("farfalle.n.01")],

	# pasta wheel
	"U+3fb2":   [wn.synset("pasta.n.02"),
				wn.synset("pastry.n.01")],

	# lasagne, lasagna
	"U+3fb4":   [wn.synset("lasagna.n.02"),
				wn.synset("lasagna.n.01")],

	# ravioli
	"U+3fb6":   [wn.synset("ravioli.n.01")],

	# omelette, omelet
	"U+3fbc":   [wn.synset("omelet.n.01")],

	# scrambled eggs
	"U+3fbe":   [wn.synset("scrambled_eggs.n.01")],

	# fruit salad
	"U+3fbf":   [wn.synset("fruit_salad.n.01")],

	# pasta salad
	"U+3fc3":   [wn.synset("pasta_salad.n.01")],

	# pudding, cream
	"U+3fc4":   [wn.synset("pudding.n.03"),
				wn.synset("pudding.n.02")],

	# Christmas pudding
	"U+3fc5":   [wn.synset("plum_pudding.n.01")],

	# bark
	"U+3fc6":   [wn.synset("bark.v.04")],

	# cinnamon
	"U+3fc8":   [wn.synset("cinnamon.n.01"),
				wn.synset("cinnamon.n.02"),
				wn.synset("cinnamon.n.03")],

	# vanilla
	"U+3fc9":   [wn.synset("vanilla.n.01"),
				wn.synset("vanilla.n.03"),
				wn.synset("vanilla.n.02")],

	# pod
	"U+3fca":   [wn.synset("pod.n.01")],

	# vanilla sauce
	"U+3fcb":   [wn.synset("vanilla.n.01"),
				wn.synset("vanilla.n.02")],

	# ginger
	"U+3fcc":   [wn.synset("ginger.n.01"),
				wn.synset("ginger.n.03")],

	# ginger sauce
	"U+3fcd":   [wn.synset("ginger.n.01"),
				wn.synset("ginger.n.03")],

	# salad dressing
	"U+3fd0":   [wn.synset("dressing.n.01")],

	# pepper sauce
	"U+3fd2":   [wn.synset("pepper_sauce.n.01")],

	# curry
	"U+3fd3":   [wn.synset("curry.n.01")],

	# curry sauce
	"U+3fd5":   [wn.synset("curry_sauce.n.01"),
				wn.synset("curry.n.01")],

	# mustard
	"U+3fd6":   [wn.synset("mustard.n.01"),
				wn.synset("mustard.n.02"),
				wn.synset("mustard.n.03"),
				wn.synset("powdered_mustard.n.01")],

	# mustard sauce
	"U+3fd8":   [wn.synset("mustard_sauce.n.01")],

	# sap
	"U+3fd9":   [wn.synset("sap.n.01"),
				wn.synset("fool.n.01"),
				wn.synset("blackjack.n.02"),
				wn.synset("lifeblood.n.01"),
				wn.synset("juice.n.04"),
				wn.synset("juice.n.01"),
				wn.synset("juice.n.02"),
				wn.synset("juice.n.03")],

	# maple syrup flavouring
	"U+3fda":   [wn.synset("maple_syrup.n.01")],

	# syrup
	"U+3fdc":   [wn.synset("syrup.n.01")],

	# maple syrup
	"U+3fde":   [wn.synset("maple_syrup.n.01")],

	# corn syrup
	"U+3fdf":   [wn.synset("corn_syrup.n.01")],

	# chocolate sauce
	"U+3fe0":   [wn.synset("chocolate_sauce.n.01")],

	# sweet drink
	"U+3fe1":   [wn.synset("beverage.n.01")],

	# sparkling wine
	"U+3fe2":   [wn.synset("sparkling_wine.n.01"),
				wn.synset("champagne.n.01")],

	# champagne
	"U+3fe4":   [wn.synset("champagne.n.01")],

	# cider
	"U+3fe5":   [wn.synset("cider.n.01")],

	# juicy
	"U+3fe7":   [wn.synset("juicy.a.01")],

	# pickled
	"U+3fe8":   [wn.synset("pickled.s.01"),
				wn.synset("unpalatable.a.01"),
				wn.synset("bitter.s.06"),
				wn.synset("cutting.s.03"),
				wn.synset("acerb.s.01")],

	# fried
	"U+3fe9":   [wn.synset("fried.s.01")],

	# delicious, scrumptious, yummy
	"U+3fea":   [wn.synset("delightful.s.01"),
				wn.synset("delectable.s.01")],

	# tasteless
	"U+3fec":   [wn.synset("tasteless.a.02"),
				wn.synset("tasteless.a.01"),
				wn.synset("bland.s.01")],

	# disgusting
	"U+3fed":   [wn.synset("disgusting.s.01")],

	# hard cheese
	"U+3ff0":   [wn.synset("cheese.n.01"),
				wn.synset("hard_cheese.n.01")],

	# soft cheese
	"U+3ff2":   [wn.synset("cheese.n.01")],

	# fresh cheese
	"U+3ff5":   [wn.synset("quark_cheese.n.01")],

	# lump
	"U+3ff7":   [wn.synset("swelling.n.01")],

	# lumpy
	"U+3ff9":   [wn.synset("chunky.s.01")],

	# cottage cheese
	"U+3ffa":   [wn.synset("cottage_cheese.n.01")],

	# lollipop, sucker
	"U+3ffb":   [wn.synset("lollipop.n.02")],

	# water ice lollipop
	"U+3ffc":   [wn.synset("ice_lolly.n.01"),
				wn.synset("icicle.n.01")],

	# popsicle
	"U+3ffd":   [wn.synset("ice_lolly.n.01")],

	# candy bar
	"U+3fff":   [wn.synset("candy_bar.n.01")],

	# chocolate bar
	"U+4000":   [wn.synset("chocolate_bar.n.01")],

	# reflect, consider
	"U+4001":   [wn.synset("consider.v.05"),
				wn.synset("study.v.03"),
				wn.synset("chew_over.v.01")],

	# candy, sweets
	"U+4002":   [wn.synset("sweet.n.03")],

	# dough
	"U+4004":   [wn.synset("dough.n.01")],

	# batter
	"U+4005":   [wn.synset("batter.n.02")],

	# ingredient
	"U+4006":   [wn.synset("ingredient.n.01")],

	# slice
	"U+4007":   [wn.synset("slice.v.04"),
				wn.synset("carve.v.02"),
				wn.synset("edit.v.03"),
				wn.synset("traverse.v.01"),
				wn.synset("snip.v.02"),
				wn.synset("reduce.v.01"),
				wn.synset("piece.n.08"),
				wn.synset("slash.v.04"),
				wn.synset("mow.v.01"),
				wn.synset("cut.v.01"),
				wn.synset("slash.v.01"),
				wn.synset("slash.v.03"),
				wn.synset("slice.n.01"),
				wn.synset("slice.n.06"),
				wn.synset("slice.n.04"),
				wn.synset("slice.n.05"),
				wn.synset("slit.v.01"),
				wn.synset("dilute.v.01"),
				wn.synset("divide.v.01"),
				wn.synset("cut_off.v.03"),
				wn.synset("interrupt.v.01"),
				wn.synset("break.v.43"),
				wn.synset("cut.n.05")],

	# sliced
	"U+4008":   [wn.synset("sliced.s.02"),
				wn.synset("chopped.s.01")],

	# reflector
	"U+4009":   [wn.synset("reflector.n.01")],

	# shiny, glossy
	"U+400b":   [wn.synset("glossy.s.01"),
				wn.synset("glossy.s.03"),
				wn.synset("glistening.s.01"),
				wn.synset("glazed.a.03"),
				wn.synset("bright.s.05")],

	# polisher
	"U+400d":   [wn.synset("buffer.n.05")],

	# vacuum cleaner
	"U+400f":   [wn.synset("vacuum.n.04")],

	# mixer, blender
	"U+4011":   [wn.synset("mixer.n.03")],

	# food processor, kitchen machine
	"U+4012":   [wn.synset("mixer.n.04"),
				wn.synset("food_processor.n.01")],

	# opener
	"U+4013":   [wn.synset("opener.n.03"),
				wn.synset("opener.n.01"),
				wn.synset("undoer.n.02")],

	# bottle opener
	"U+4015":   [wn.synset("bottle_opener.n.01")],

	# can opener
	"U+4017":   [wn.synset("can_opener.n.01")],

	# cleaning tool
	"U+4019":   [wn.synset("purifier.n.01")],

	# cleaning cloth
	"U+401a":   [wn.synset("dishrag.n.01"),
				wn.synset("dishtowel.n.01"),
				wn.synset("rag.n.01")],

	# kitchen tool, utensils
	"U+401b":   [wn.synset("utensil.n.01")],

	# grater, grinder
	"U+401c":   [wn.synset("bomber.n.03"),
				wn.synset("molar.n.01"),
				wn.synset("grater.n.01"),
				wn.synset("mill.n.04"),
				wn.synset("grinder.n.04")],

	# whisk, beater
	"U+401e":   [wn.synset("whisk.n.01"),
				wn.synset("whisk.n.02"),
				wn.synset("beater.n.02"),
				wn.synset("beater.n.01")],

	# corkscrew
	"U+4020":   [wn.synset("corkscrew.n.01")],

	# kitchen tongs
	"U+4021":   [wn.synset("pliers.n.01"),
				wn.synset("tongs.n.01"),
				wn.synset("hook.n.04"),
				wn.synset("mouse-tooth_forceps.n.01"),
				wn.synset("pump-type_pliers.n.01"),
				wn.synset("lion-jaw_forceps.n.01"),
				wn.synset("rib_joint_pliers.n.01"),
				wn.synset("forceps.n.01")],

	# nutcracker
	"U+4023":   [wn.synset("nutcracker.n.01")],

	# reaching aid, grabber
	"U+4025":   [wn.synset("grasping.n.02"),
				wn.synset("grabber.n.01"),
				wn.synset("handle.n.01"),
				wn.synset("clasp.n.02")],

	# teaspoon
	"U+4029":   [wn.synset("teaspoon.n.01"),
				wn.synset("teaspoon.n.02")],

	# tablespoon
	"U+402a":   [wn.synset("tablespoon.n.01"),
				wn.synset("tablespoon.n.02")],

	# mixing spoon
	"U+402d":   [wn.synset("spoon.n.01")],

	# ladle
	"U+402e":   [wn.synset("ladle.n.01")],

	# funnel
	"U+402f":   [wn.synset("funnel.n.02")],

	# oven tray
	"U+4030":   [wn.synset("phonograph_record.n.01"),
				wn.synset("platinum.n.01"),
				wn.synset("platter.n.01")],

	# baking tin, baking pan, ovenware
	"U+4032":   [wn.synset("ovenware.n.01")],

	# stovetop
	"U+4033":   [wn.synset("stove.n.01"),
				wn.synset("hot_plate.n.01"),
				wn.synset("firebox.n.01")],

	# saucepan
	"U+4034":   [wn.synset("saucepan.n.01"),
				wn.synset("pot.n.01"),
				wn.synset("pot.n.03")],

	# electric pan
	"U+4035":   [wn.synset("saucepan.n.01")],

	# frying pan
	"U+4036":   [wn.synset("frying_pan.n.01")],

	# woking
	"U+4037":   [wn.synset("wok.n.01")],

	# wok, wok pan
	"U+4038":   [wn.synset("wok.n.01")],

	# lid
	"U+403a":   [wn.synset("lid.n.02")],

	# steamer
	"U+403c":   [wn.synset("soft-shell_clam.n.02"),
				wn.synset("soft-shell_clam.n.01"),
				wn.synset("steamer.n.03"),
				wn.synset("steamer.n.02")],

	# glass jar
	"U+4040":   [wn.synset("canister.n.02"),
				wn.synset("can.n.01"),
				wn.synset("jar.n.01"),
				wn.synset("jar.n.02")],

	# cookie jar, biscuit tin
	"U+4041":   [wn.synset("cookie_jar.n.01"),
				wn.synset("cookie.n.01")],

	# rolling pin
	"U+4043":   [wn.synset("rolling_pin.n.01")],

	# table mat, placemat
	"U+4046":   [wn.synset("table_mat.n.01")],

	# pot stand, trivet
	"U+4047":   [wn.synset("trivet.n.02")],

	# potholder, oven mitt
	"U+4048":   [wn.synset("potholder.n.01"),
				wn.synset("handle.n.01"),
				wn.synset("holder.n.01")],

	# equator
	"U+404a":   [wn.synset("equator.n.01")],

	# South Pole
	"U+404b":   [wn.synset("south_pole.n.01")],

	# North Pole
	"U+404c":   [wn.synset("north_pole.n.01")],

	# continent
	"U+404d":   [wn.synset("continent.n.01")],

	# Africa
	"U+404e":   [wn.synset("africa.n.01")],

	# Antarctic
	"U+404f":   [wn.synset("antarctic.n.01")],

	# Asia
	"U+4050":   [wn.synset("asia.n.01")],

	# Australia
	"U+4051":   [wn.synset("australia.n.02"),
				wn.synset("australia.n.01")],

	# Europe
	"U+4052":   [wn.synset("europe.n.01")],

	# North America
	"U+4054":   [wn.synset("north_america.n.01"),
				wn.synset("north_america.n.02")],

	# South America
	"U+4056":   [wn.synset("south_america.n.02"),
				wn.synset("south_america.n.01")],

	# Belgium
	"U+4057":   [wn.synset("belgium.n.01")],

	# England
	"U+4058":   [wn.synset("england.n.01")],

	# rose
	"U+405a":   [wn.synset("rose.n.01")],

	# Norway
	"U+405c":   [wn.synset("norway.n.01")],

	# fjord
	"U+405e":   [wn.synset("fjord.n.01")],

	# Scotland
	"U+405f":   [wn.synset("scotland.n.01")],

	# South Africa
	"U+4060":   [wn.synset("south_africa.n.01")],

	# springbok
	"U+4062":   [wn.synset("springbok.n.01"),
				wn.synset("gazelle.n.01")],

	# Sweden
	"U+4063":   [wn.synset("sweden.n.01")],

	# The Nordic countries
	"U+4064":   [wn.synset("scandinavia.n.02")],

	# earthquake
	"U+4065":   [wn.synset("earthquake.n.01")],

	# continental drift
	"U+4067":   [wn.synset("continental_drift.n.01")],

	# waterfall
	"U+4069":   [wn.synset("waterfall.n.01")],

	# rapids
	"U+406b":   [wn.synset("rapid.n.01")],

	# tidal wave
	"U+406c":   [wn.synset("tidal_wave.n.01"),
				wn.synset("tidal_wave.n.03"),
				wn.synset("tidal_wave.n.02")],

	# inlet
	"U+406e":   [wn.synset("inlet.n.01"),
				wn.synset("intake.n.02")],

	# tide
	"U+406f":   [wn.synset("tide.n.01")],

	# low tide, ebb
	"U+4070":   [wn.synset("low_tide.n.01")],

	# high tide
	"U+4071":   [wn.synset("high_tide.n.01")],

	# low water
	"U+4072":   [wn.synset("low_tide.n.01"),
				wn.synset("neap_tide.n.01")],

	# high water
	"U+4073":   [wn.synset("ocean_trip.n.01"),
				wn.synset("sea.n.01"),
				wn.synset("sea.n.03"),
				wn.synset("high_tide.n.01"),
				wn.synset("ocean.n.02")],

	# hot spring
	"U+4075":   [wn.synset("hot_spring.n.01"),
				wn.synset("geyser.n.01")],

	# constellation of stars
	"U+4077":   [wn.synset("constellation.n.02")],

	# light year
	"U+4079":   [wn.synset("light_year.n.01")],

	# telescope
	"U+407b":   [wn.synset("telescope.n.01")],

	# astrology
	"U+407c":   [wn.synset("astrology.n.01")],

	# weather forecast
	"U+407d":   [wn.synset("weather_forecast.n.01")],

	# Aries
	"U+4080":   [wn.synset("aries.n.02"),
				wn.synset("aries.n.03"),
				wn.synset("aries.n.01")],

	# Taurus
	"U+4082":   [wn.synset("taurus.n.03"),
				wn.synset("taurus.n.02"),
				wn.synset("sanchez.n.01"),
				wn.synset("taurus.n.04")],

	# Cancer
	"U+4084":   [wn.synset("cancer.n.01"),
				wn.synset("cancer.n.03"),
				wn.synset("cancer.n.02"),
				wn.synset("cancer.n.05"),
				wn.synset("cancer.n.04")],

	# Leo
	"U+4085":   [wn.synset("leo.n.02"),
				wn.synset("leo.n.03"),
				wn.synset("leo.n.01")],

	# Virgo
	"U+4087":   [wn.synset("virgo.n.03"),
				wn.synset("virgo.n.02"),
				wn.synset("virgo.n.01")],

	# Libra
	"U+4088":   [wn.synset("libra.n.03")],

	# Scorpio
	"U+4089":   [wn.synset("scorpion.n.03"),
				wn.synset("scorpius.n.01"),
				wn.synset("scorpio.n.03"),
				wn.synset("scorpio.n.01")],

	# Sagittarius
	"U+408b":   [wn.synset("sagittarius.n.01"),
				wn.synset("sagittarius.n.02"),
				wn.synset("sagittarius.n.03"),
				wn.synset("sagittarius.n.04")],

	# Capricorn
	"U+408c":   [wn.synset("capricorn.n.03"),
				wn.synset("capricorn.n.01"),
				wn.synset("capricornus.n.01")],

	# Aquarius
	"U+408d":   [wn.synset("aquarius.n.02"),
				wn.synset("aquarius.n.03"),
				wn.synset("aquarius.n.01")],

	# Pisces
	"U+408e":   [wn.synset("pisces.n.01")],

	# Nordic God
	"U+408f":   [wn.synset("deity.n.01"),
				wn.synset("godhead.n.01"),
				wn.synset("god.n.03")],

	# Woden
	"U+4090":   [wn.synset("woden.n.01"),
				wn.synset("odin.n.01")],

	# Frigg
	"U+4091":   [wn.synset("frigg.n.01")],

	# Thor
	"U+4093":   [wn.synset("thor.n.01")],

	# Sif
	"U+4094":   [wn.synset("sif.n.01")],

	# Gemini
	"U+4097":   [wn.synset("gemini.n.02"),
				wn.synset("gemini.n.03"),
				wn.synset("gemini.n.01")],

	# Balder
	"U+4099":   [wn.synset("balder.n.01")],

	# Frey
	"U+409a":   [wn.synset("frey.n.01")],

	# Freya
	"U+409b":   [wn.synset("freya.n.01")],

	# Tyr
	"U+409c":   [wn.synset("tyr.n.01")],

	# Aegir
	"U+409d":   [wn.synset("tidal_bore.n.01")],

	# Valhalla
	"U+40a4":   [wn.synset("valhalla.n.01")],

	# Viking
	"U+40a5":   [wn.synset("viking.n.01")],

	# runes
	"U+40a9":   [wn.synset("alphabet.n.01"),
				wn.synset("rune.n.01")],

	# blot
	"U+40ab":   [wn.synset("blot.n.02"),
				wn.synset("smudge.n.02")],

	# planet
	"U+40ad":   [wn.synset("planet.n.01")],

	# lawn bowling, bowls
	"U+40ae":   [wn.synset("stadium.n.01"),
				wn.synset("lawn_bowling.n.01"),
				wn.synset("bowling_ball.n.01"),
				wn.synset("bowl.n.03"),
				wn.synset("bowl.n.02"),
				wn.synset("bowl.n.01"),
				wn.synset("bowl.n.07"),
				wn.synset("bowl.n.04"),
				wn.synset("bowl.n.08"),
				wn.synset("roll.n.15")],

	# solar system
	"U+40b0":   [wn.synset("solar_system.n.01")],

	# saddle
	"U+40b2":   [wn.synset("saddle.n.01")],

	# court, field, courthouse, courtroom
	"U+40b3":   [wn.synset("court.n.11"),
				wn.synset("court.n.10"),
				wn.synset("court.n.06"),
				wn.synset("court.n.05"),
				wn.synset("court.n.04"),
				wn.synset("court.n.03"),
				wn.synset("court.n.02"),
				wn.synset("court.n.01"),
				wn.synset("court.n.08"),
				wn.synset("courthouse.n.02"),
				wn.synset("courthouse.n.01"),
				wn.synset("court.n.09"),
				wn.synset("motor_hotel.n.01")],

	# astrologer, astrologist
	"U+40b6":   [wn.synset("astrologer.n.01")],

	# call, telephone, ring
	"U+40b8":   [wn.synset("call.v.03")],

	# dirt, soil
	"U+40ba":   [wn.synset("land.n.02"),
				wn.synset("territory.n.03"),
				wn.synset("soil.n.02"),
				wn.synset("scandal.n.01"),
				wn.synset("crap.n.01"),
				wn.synset("dirt.n.02")],

	# uncertain, unsure
	"U+40be":   [wn.synset("diffident.a.02"),
				wn.synset("uncertain.a.04"),
				wn.synset("uncertain.a.02"),
				wn.synset("uncertain.s.06"),
				wn.synset("uncertain.a.01"),
				wn.synset("unsealed.a.01"),
				wn.synset("changeable.s.03"),
				wn.synset("uncertain.s.07")],

	# accusation, charge, prosecution
	"U+40bf":   [wn.synset("commission.n.06"),
				wn.synset("accusation.n.02"),
				wn.synset("accusation.n.01"),
				wn.synset("pursuance.n.02"),
				wn.synset("care.n.05"),
				wn.synset("charge.n.08"),
				wn.synset("charge.n.14"),
				wn.synset("charge.n.15"),
				wn.synset("prosecution.n.02"),
				wn.synset("prosecution.n.01"),
				wn.synset("mission.n.03"),
				wn.synset("charge.n.01"),
				wn.synset("charge.n.07"),
				wn.synset("charge.n.03"),
				wn.synset("charge.n.02"),
				wn.synset("cathexis.n.01"),
				wn.synset("charge.n.04"),
				wn.synset("charge.n.11"),
				wn.synset("bang.n.04")],

	# accuse, charge, prosecute
	"U+40c1":   [wn.synset("blame.v.03"),
				wn.synset("indict.v.01"),
				wn.synset("load.v.02"),
				wn.synset("charge.v.24"),
				wn.synset("tear.v.03"),
				wn.synset("consign.v.02"),
				wn.synset("prosecute.v.01"),
				wn.synset("accuse.v.01"),
				wn.synset("agitate.v.02"),
				wn.synset("commit.v.03"),
				wn.synset("charge.v.06"),
				wn.synset("prosecute.v.03"),
				wn.synset("appoint.v.02"),
				wn.synset("charge.v.18"),
				wn.synset("charge.v.19"),
				wn.synset("charge.v.12"),
				wn.synset("charge.v.13"),
				wn.synset("charge.v.25"),
				wn.synset("charge.v.17"),
				wn.synset("prosecute.v.02"),
				wn.synset("charge.v.15"),
				wn.synset("charge.v.23"),
				wn.synset("charge.v.22"),
				wn.synset("charge.v.07"),
				wn.synset("charge.v.20"),
				wn.synset("charge.v.01"),
				wn.synset("charge.v.03"),
				wn.synset("charge.v.02"),
				wn.synset("charge.v.09"),
				wn.synset("charge.v.08")],

	# act in favour of
	"U+40c2":   [wn.synset("represent.v.04")],

	# advocate, speaking), spokesperson
	"U+40c6":   [wn.synset("advocate.n.02")],

	# advocacy, representation
	"U+40c8":   [wn.synset("representation.n.08"),
				wn.synset("representation.n.09"),
				wn.synset("representation.n.10"),
				wn.synset("representation.n.01"),
				wn.synset("representation.n.02"),
				wn.synset("representation.n.03"),
				wn.synset("advocacy.n.01"),
				wn.synset("representation.n.05"),
				wn.synset("representation.n.06"),
				wn.synset("apology.n.02"),
				wn.synset("representation.n.04"),
				wn.synset("theatrical_performance.n.01")],

	# legal person
	"U+40c9":   [wn.synset("lawyer.n.01"),
				wn.synset("judge.n.01"),
				wn.synset("jurist.n.01")],

	# altimeter
	"U+40ca":   [wn.synset("altimeter.n.01")],

	# gauge
	"U+40cb":   [wn.synset("gauge.n.02")],

	# anemometer
	"U+40cc":   [wn.synset("anemometer.n.01")],

	# any day, someday
	"U+40ce":   [wn.synset("someday.r.01")],

	# apartment block
	"U+40d0":   [wn.synset("apartment.n.01"),
				wn.synset("suite.n.02")],

	# archipelago
	"U+40d1":   [wn.synset("archipelago.n.01")],

	# arrest
	"U+40d4":   [wn.synset("collar.v.01")],

	# capture, catch, seize
	"U+40d5":   [wn.synset("get.v.11"),
				wn.synset("catch.v.04")],

	# attic
	"U+40d6":   [wn.synset("attic.n.03"),
				wn.synset("attic.n.02"),
				wn.synset("loft.n.02"),
				wn.synset("attic.n.04")],

	# bakery
	"U+40d7":   [wn.synset("bakery.n.01")],

	# store, shop
	"U+40d8":   [wn.synset("shop.n.01")],

	# barometer, manometer
	"U+40d9":   [wn.synset("barometer.n.01")],

	# pressure
	"U+40da":   [wn.synset("pressure.n.01")],

	# basement, cellar
	"U+40db":   [wn.synset("basement.n.01")],

	# Bliss, Bliss language, Blissymbolics
	"U+40dc":   [wn.synset("bliss.n.01")],

	# board and lodging, room and board
	"U+40de":   [wn.synset("pension.n.01"),
				wn.synset("housing.n.01"),
				wn.synset("suite.n.02"),
				wn.synset("billet.n.02"),
				wn.synset("boarding_house.n.01"),
				wn.synset("living_quarters.n.01"),
				wn.synset("diggings.n.02")],

	# bookshop
	"U+40e0":   [wn.synset("bookshop.n.01")],

	# bronze
	"U+40e2":   [wn.synset("bronze.n.01"),
				wn.synset("bronze.n.02")],

	# copper
	"U+40e3":   [wn.synset("copper.n.01")],

	# bronze age
	"U+40e4":   [wn.synset("bronze_age.n.01"),
				wn.synset("bronze_age.n.02")],

	# butcher shop
	"U+40e5":   [wn.synset("butcher.n.01"),
				wn.synset("butcher_shop.n.01"),
				wn.synset("butcher.n.03")],

	# care centre
	"U+40e7":   [wn.synset("hospice.n.02")],

	# cheap, inexpensive
	"U+40e8":   [wn.synset("cheap.a.01")],

	# cockerel
	"U+40ec":   [wn.synset("cockerel.n.01"),
				wn.synset("cock.n.04")],

	# cod
	"U+40ed":   [wn.synset("cod.n.03")],

	# control tower
	"U+40ee":   [wn.synset("control_tower.n.01")],

	# tower
	"U+40ef":   [wn.synset("tower.n.01")],

	# corridor, hall
	"U+40f1":   [wn.synset("manor_hall.n.01"),
				wn.synset("hall.n.10"),
				wn.synset("hallway.n.01"),
				wn.synset("hall.n.03"),
				wn.synset("mansion.n.02"),
				wn.synset("hall.n.08"),
				wn.synset("hall.n.09"),
				wn.synset("hall.n.13"),
				wn.synset("hall.n.12"),
				wn.synset("dormitory.n.01"),
				wn.synset("hall.n.07"),
				wn.synset("hall.n.06"),
				wn.synset("anteroom.n.01")],

	# cotton
	"U+40f2":   [wn.synset("cotton.n.04"),
				wn.synset("cotton.n.02"),
				wn.synset("cotton.n.03"),
				wn.synset("cotton.n.01")],

	# crayfish
	"U+40f5":   [wn.synset("spiny_lobster.n.01"),
				wn.synset("crayfish.n.02"),
				wn.synset("spiny_lobster.n.02"),
				wn.synset("crayfish.n.03")],

	# day and night
	"U+40f6":   [wn.synset("day.n.01")],

	# day centre
	"U+40f9":   [wn.synset("community_center.n.01"),
				wn.synset("common_room.n.01")],

	# care, protection, defence, protect, defend, legal)
	"U+40fa":   [wn.synset("defensive_structure.n.01"),
				wn.synset("defense.n.01")],

	# caregiver, protector, defender, guard
	"U+40fd":   [wn.synset("defender.n.01"),
				wn.synset("guard.n.10"),
				wn.synset("guard_duty.n.01"),
				wn.synset("guard.n.01"),
				wn.synset("guard.n.03"),
				wn.synset("guard.n.02"),
				wn.synset("guard.n.05"),
				wn.synset("guard.n.04"),
				wn.synset("guard.n.06"),
				wn.synset("guard.n.09"),
				wn.synset("precaution.n.01")],

	# deflation
	"U+40fe":   [wn.synset("deflation.n.02")],

	# department store
	"U+40ff":   [wn.synset("department_store.n.01")],

	# discount
	"U+4101":   [wn.synset("discount.n.01"),
				wn.synset("discount_rate.n.02"),
				wn.synset("deduction.n.02"),
				wn.synset("rebate.n.01")],

	# discount store
	"U+4105":   [wn.synset("discount_house.n.01")],

	# drugstore, pharmacy
	"U+4106":   [wn.synset("drugstore.n.01")],

	# eaves
	"U+4107":   [wn.synset("eaves.n.01")],

	# electricity meter
	"U+410a":   [wn.synset("tensiometer.n.03"),
				wn.synset("tensiometer.n.02")],

	# elementary school, primary school
	"U+410b":   [wn.synset("grade_school.n.01")],

	# English
	"U+410d":   [wn.synset("english.n.01")],

	# evidence
	"U+410f":   [wn.synset("evidence.n.02")],

	# expensive
	"U+4110":   [wn.synset("expensive.a.01")],

	# flatfish
	"U+4114":   [wn.synset("flatfish.n.02")],

	# flax
	"U+4115":   [wn.synset("flax.n.01"),
				wn.synset("flax.n.02"),
				wn.synset("linen.n.01")],

	# florist
	"U+4117":   [wn.synset("florist.n.02")],

	# fuel gauge
	"U+4119":   [wn.synset("fuel_gauge.n.01")],

	# garden centre
	"U+411a":   [wn.synset("hatchery.n.01")],

	# scale, measurement
	"U+411b":   [wn.synset("scale.n.07")],

	# geography
	"U+411c":   [wn.synset("geography.n.01")],

	# gift shop
	"U+411d":   [wn.synset("gift_shop.n.01")],

	# goat
	"U+411f":   [wn.synset("goat.n.01")],

	# God the father
	"U+4120":   [wn.synset("deity.n.01")],

	# gold
	"U+4124":   [wn.synset("gold.n.04"),
				wn.synset("amber.n.01"),
				wn.synset("gold.n.01"),
				wn.synset("gold.n.03")],

	# greengrocer
	"U+4126":   [wn.synset("greengrocer.n.01")],

	# grocery store, food store, supermarket
	"U+4128":   [wn.synset("supermarket.n.01"),
				wn.synset("grocery_store.n.01")],

	# gutter, eaves trough
	"U+412b":   [wn.synset("gutter.n.01")],

	# handwriting, penmanship
	"U+4131":   [wn.synset("calligraphy.n.01")],

	# health goods shop
	"U+4132":   [wn.synset("ecological.a.01"),
				wn.synset("ecological.a.02")],

	# Hebrew
	"U+4134":   [wn.synset("jew.n.01"),
				wn.synset("hebraic.a.02"),
				wn.synset("jewish.a.01"),
				wn.synset("hebrew.n.01")],

	# herb, spice plant
	"U+4136":   [wn.synset("herb.n.02")],

	# Holy Spirit
	"U+4139":   [wn.synset("holy_ghost.n.01")],

	# Holy Trinity
	"U+413a":   [wn.synset("trinity.n.02")],

	# horizontal
	"U+413b":   [wn.synset("horizontal.a.01"),
				wn.synset("horizontal.n.01")],

	# illegal, criminal
	"U+413c":   [wn.synset("criminal.n.01")],

	# law, The Law
	"U+413d":   [wn.synset("law.n.01")],

	# inflation
	"U+413f":   [wn.synset("inflation.n.01")],

	# innocence
	"U+4140":   [wn.synset("innocence.n.03")],

	# innocent, not guilty
	"U+4141":   [wn.synset("innocent.a.01")],

	# iron age
	"U+4143":   [wn.synset("iron_age.n.01")],

	# jellyfish
	"U+4144":   [wn.synset("jellyfish.n.02")],

	# juridical
	"U+4146":   [wn.synset("judicial.a.03")],

	# jury
	"U+4147":   [wn.synset("jury.n.02"),
				wn.synset("jury.n.01")],

	# peer
	"U+4148":   [wn.synset("peer.n.02"),
				wn.synset("peer.n.01")],

	# legal
	"U+4149":   [wn.synset("legal.a.01")],

	# justice
	"U+414a":   [wn.synset("justice.n.01")],

	# lawyer
	"U+414c":   [wn.synset("lawyer.n.01")],

	# leisure time
	"U+4151":   [wn.synset("leisure.n.01"),
				wn.synset("leisure.n.02")],

	# light meter
	"U+4153":   [wn.synset("light_meter.n.01")],

	# lighthouse
	"U+4154":   [wn.synset("beacon.n.03")],

	# linen, flax fabric
	"U+4155":   [wn.synset("linen.n.03")],

	# liquor shop
	"U+4156":   [wn.synset("package_store.n.01")],

	# lobster
	"U+4158":   [wn.synset("lobster.n.02"),
				wn.synset("lobster.n.01")],

	# market
	"U+415a":   [wn.synset("market.n.01"),
				wn.synset("market.n.02"),
				wn.synset("marketplace.n.02")],

	# mercury
	"U+415b":   [wn.synset("mercury.n.01")],

	# metal bar
	"U+415c":   [wn.synset("metallic_element.n.01"),
				wn.synset("ingot.n.01")],

	# midnight
	"U+415e":   [wn.synset("midnight.n.01")],

	# multi storey building
	"U+4160":   [wn.synset("building.n.01")],

	# multi storey home
	"U+4162":   [wn.synset("dwelling.n.01"),
				wn.synset("home.n.03"),
				wn.synset("business.n.01"),
				wn.synset("house.n.01"),
				wn.synset("sign_of_the_zodiac.n.01"),
				wn.synset("dynasty.n.01"),
				wn.synset("family.n.01"),
				wn.synset("square.n.07")],

	# noon
	"U+4166":   [wn.synset("noon.n.01")],

	# notary
	"U+4168":   [wn.synset("notary.n.01")],

	# octopus
	"U+4169":   [wn.synset("octopus.n.02"),
				wn.synset("octopus.n.01")],

	# water creature
	"U+416a":   [wn.synset("marine_animal.n.01")],

	# one storey building, bungalow
	"U+416d":   [wn.synset("bungalow.n.01"),
				wn.synset("building.n.01")],

	# one storey home
	"U+416e":   [wn.synset("dwelling.n.01")],

	# pencil case, pencil box
	"U+416f":   [wn.synset("pencil_box.n.01")],

	# prawn
	"U+4170":   [wn.synset("prawn.n.01"),
				wn.synset("prawn.n.02"),
				wn.synset("shrimp.n.03")],

	# pressure gauge
	"U+4172":   [wn.synset("pressure_gauge.n.01")],

	# price rise
	"U+4173":   [wn.synset("inflation.n.02"),
				wn.synset("inflation.n.01")],

	# promote
	"U+4175":   [wn.synset("promote.v.01")],

	# promotion
	"U+4176":   [wn.synset("promotion.n.01"),
				wn.synset("promotion.n.03"),
				wn.synset("promotion.n.02")],

	# prosecutor
	"U+4178":   [wn.synset("prosecutor.n.01")],

	# protractor
	"U+417b":   [wn.synset("protractor.n.01")],

	# psychologist
	"U+417c":   [wn.synset("psychologist.n.01")],

	# psychology
	"U+417d":   [wn.synset("psychology.n.01")],

	# quarter of an hour
	"U+4182":   [wn.synset("quarter.n.04")],

	# rain gauge
	"U+4184":   [wn.synset("rain_gauge.n.01")],

	# lesson, lecture, class
	"U+4187":   [wn.synset("lesson.n.01")],

	# religious service
	"U+4189":   [wn.synset("service.n.03")],

	# service
	"U+418a":   [wn.synset("service.n.01"),
				wn.synset("service.n.15"),
				wn.synset("service.n.05"),
				wn.synset("service.n.04"),
				wn.synset("serve.n.01")],

	# row house, attached houses
	"U+418b":   [wn.synset("row_house.n.01")],

	# sale
	"U+418c":   [wn.synset("sale.n.01")],

	# salmon
	"U+418e":   [wn.synset("salmon.n.04"),
				wn.synset("salmon.n.03"),
				wn.synset("salmon.n.02"),
				wn.synset("salmon.n.01")],

	# season
	"U+4190":   [wn.synset("season.n.01"),
				wn.synset("season.n.02")],

	# semi detached house
	"U+4193":   [wn.synset("dwelling.n.01"),
				wn.synset("home.n.03"),
				wn.synset("business.n.01"),
				wn.synset("house.n.01"),
				wn.synset("sign_of_the_zodiac.n.01"),
				wn.synset("mansion.n.02"),
				wn.synset("residence.n.01"),
				wn.synset("dynasty.n.01"),
				wn.synset("family.n.01"),
				wn.synset("square.n.07"),
				wn.synset("diggings.n.02"),
				wn.synset("semi-detached_house.n.01")],

	# sheltered workshop
	"U+4195":   [wn.synset("sheltered_workshop.n.01")],

	# shoal, school
	"U+4196":   [wn.synset("school.n.07")],

	# shopping centre, mall, plaza
	"U+4197":   [wn.synset("plaza.n.02"),
				wn.synset("promenade.n.02"),
				wn.synset("plaza.n.01"),
				wn.synset("hypermarket.n.01")],

	# shopping mall
	"U+419a":   [wn.synset("plaza.n.02")],

	# short time home
	"U+419c":   [wn.synset("tenement.n.01"),
				wn.synset("dwelling.n.01"),
				wn.synset("living_quarters.n.01")],

	# shrimp
	"U+419d":   [wn.synset("prawn.n.01")],

	# silk
	"U+419e":   [wn.synset("silk.n.01")],

	# silk fabric
	"U+419f":   [wn.synset("silk.n.02"),
				wn.synset("silk.n.01")],

	# silver
	"U+41a0":   [wn.synset("silver.n.01")],

	# size
	"U+41a2":   [wn.synset("size.n.01")],

	# skyscraper
	"U+41a3":   [wn.synset("skyscraper.n.01")],

	# speed
	"U+41a4":   [wn.synset("speed.n.01")],

	# speedometer
	"U+41a5":   [wn.synset("speedometer.n.01")],

	# sport lesson
	"U+41a6":   [wn.synset("athletic_contest.n.01"),
				wn.synset("agitation.n.05"),
				wn.synset("gymnastics.n.01"),
				wn.synset("exercise.n.01"),
				wn.synset("calisthenics.n.02"),
				wn.synset("calisthenics.n.01"),
				wn.synset("sport.n.01")],

	# starfish
	"U+41a9":   [wn.synset("starfish.n.01")],

	# statement
	"U+41ac":   [wn.synset("instruction.n.04"),
				wn.synset("affirmation.n.02"),
				wn.synset("statement.n.04"),
				wn.synset("statement.n.07"),
				wn.synset("statement.n.01"),
				wn.synset("argument.n.01"),
				wn.synset("statement.n.03")],

	# stone age
	"U+41ad":   [wn.synset("stone_age.n.01")],

	# Swedish
	"U+41ae":   [wn.synset("swedish.n.01")],

	# sweet shop, candy store
	"U+41b0":   [wn.synset("confectionery.n.02")],

	# synthetic fabric
	"U+41b1":   [wn.synset("synthetic.n.01")],

	# tax, regional)
	"U+41b2":   [wn.synset("tax.n.01")],

	# testify
	"U+41b4":   [wn.synset("testify.v.02")],

	# testimony
	"U+41b5":   [wn.synset("testimony.n.03")],

	# theatre
	"U+41b6":   [wn.synset("theater.n.01"),
				wn.synset("dramaturgy.n.01")],

	# timer
	"U+41b8":   [wn.synset("stopwatch.n.01"),
				wn.synset("timekeeper.n.01"),
				wn.synset("timer.n.01"),
				wn.synset("timer.n.03")],

	# trial
	"U+41bb":   [wn.synset("test.n.05"),
				wn.synset("test.n.04"),
				wn.synset("trial.n.04"),
				wn.synset("trial.n.05"),
				wn.synset("trial.n.06"),
				wn.synset("trial.n.02")],

	# two storey building
	"U+41bc":   [wn.synset("building.n.01")],

	# unfair, unjust
	"U+41bd":   [wn.synset("unfair.a.01"),
				wn.synset("inequitable.a.01"),
				wn.synset("unjust.a.02")],

	# watch tower, observation tower
	"U+41be":   [wn.synset("barbican.n.01"),
				wn.synset("lookout.n.03"),
				wn.synset("watchtower.n.01")],

	# water meter
	"U+41c0":   [wn.synset("water_meter.n.01")],

	# water tower
	"U+41c1":   [wn.synset("water_tower.n.01")],

	# vertical
	"U+41c3":   [wn.synset("headstand.n.01"),
				wn.synset("vertical.n.01"),
				wn.synset("upright.n.01"),
				wn.synset("handstand.n.01")],

	# witness
	"U+41c4":   [wn.synset("witness.n.01"),
				wn.synset("witness.n.05"),
				wn.synset("witness.n.03"),
				wn.synset("spectator.n.01"),
				wn.synset("witness.n.04")],

	# workplace
	"U+41c5":   [wn.synset("workplace.n.01")],

	# writing
	"U+41c6":   [wn.synset("writing.n.04"),
				wn.synset("writing.n.05"),
				wn.synset("writing.n.02"),
				wn.synset("writing.n.03"),
				wn.synset("writing.n.01"),
				wn.synset("script.n.03")],

	# aboard, on board
	"U+41c7":   [wn.synset("aboard.r.01"),
				wn.synset("aboard.r.02"),
				wn.synset("aboard.r.03"),
				wn.synset("aboard.r.04"),
				wn.synset("piggyback.r.01")],

	# address
	"U+41c9":   [wn.synset("address.n.02")],

	# anti virus program
	"U+41cb":   [wn.synset("anti-virus_program.n.01")],

	# ashore
	"U+41cd":   [wn.synset("ashore.r.01")],

	# debarkation, disembarkation
	"U+41ce":   [wn.synset("debarkation.n.01")],

	# ATM, cash machine
	"U+41d0":   [wn.synset("asynchronous_transfer_mode.n.01"),
				wn.synset("standard_atmosphere.n.01"),
				wn.synset("cash_machine.n.01")],

	# backspace
	"U+41d3":   [wn.synset("erase.v.03"),
				wn.synset("backspace.v.01")],

	# baker
	"U+41d6":   [wn.synset("baker.n.01"),
				wn.synset("baker.n.02")],

	# ballet
	"U+41d8":   [wn.synset("ballet.n.01")],

	# bank card, money card
	"U+41d9":   [wn.synset("bank_card.n.01")],

	# barrow, grave mound
	"U+41da":   [wn.synset("barrow.n.03")],

	# brave, courageous
	"U+41db":   [wn.synset("brave.a.01")],

	# courage
	"U+41dc":   [wn.synset("courage.n.01")],

	# bricklayer
	"U+41dd":   [wn.synset("bricklayer.n.01")],

	# briefcase
	"U+41df":   [wn.synset("briefcase.n.01")],

	# Brontosaurus
	"U+41e1":   [wn.synset("apatosaur.n.01")],

	# dinosaur
	"U+41e2":   [wn.synset("dinosaur.n.01")],

	# brownie, house elf
	"U+41e3":   [wn.synset("brownie.n.01"),
				wn.synset("elf.n.01"),
				wn.synset("brownie.n.03")],

	# little person
	"U+41e4":   [wn.synset("gnome.n.01")],

	# Buddha
	"U+41e5":   [wn.synset("buddha.n.02"),
				wn.synset("buddha.n.01")],

	# Buddhism
	"U+41e7":   [wn.synset("buddhism.n.02")],

	# buddhist
	"U+41e9":   [wn.synset("buddhist.a.01")],

	# budget, business plan
	"U+41eb":   [wn.synset("budget.n.02")],

	# butcher
	"U+41ec":   [wn.synset("butcher.n.01")],

	# car mechanic
	"U+41ed":   [wn.synset("automobile_mechanic.n.01")],

	# mechanic, technician
	"U+41ee":   [wn.synset("technician.n.02"),
				wn.synset("technician.n.01"),
				wn.synset("automobile_mechanic.n.01"),
				wn.synset("machinist.n.01")],

	# track
	"U+41f0":   [wn.synset("racetrack.n.01"),
				wn.synset("lead.n.03")],

	# card game
	"U+41f1":   [wn.synset("card_game.n.01")],

	# cartographer
	"U+41f3":   [wn.synset("cartographer.n.01")],

	# cartography
	"U+41f5":   [wn.synset("mapmaking.n.01")],

	# cartoon, animated picture
	"U+41f7":   [wn.synset("cartoon.n.01"),
				wn.synset("cartoon.n.02"),
				wn.synset("animation.n.05")],

	# casserole
	"U+41f8":   [wn.synset("casserole.n.01"),
				wn.synset("casserole.n.02")],

	# castle, palace
	"U+41f9":   [wn.synset("castle.n.02")],

	# causality
	"U+41fb":   [wn.synset("causality.n.01")],

	# civil engineer
	"U+41fc":   [wn.synset("civil_engineer.n.01"),
				wn.synset("engineer.n.01")],

	# designer, planner
	"U+41fd":   [wn.synset("interior_designer.n.01"),
				wn.synset("couturier.n.01"),
				wn.synset("architect.n.01"),
				wn.synset("planner.n.02"),
				wn.synset("graphic_designer.n.01"),
				wn.synset("planner.n.01"),
				wn.synset("designer.n.04")],

	# clown
	"U+41ff":   [wn.synset("clown.n.01"),
				wn.synset("clown.n.02")],

	# comedy
	"U+4202":   [wn.synset("comedy.n.01")],

	# community centre, town hall, village hall
	"U+4203":   [wn.synset("town_hall.n.01")],

	# computer
	"U+4205":   [wn.synset("computer.n.01")],

	# computer game
	"U+4208":   [wn.synset("computer_game.n.01")],

	# computer peripheral
	"U+4209":   [wn.synset("peripheral.n.01")],

	# computer screen, monitor
	"U+420a":   [wn.synset("monitor.n.04")],

	# concert
	"U+420b":   [wn.synset("concert.n.01")],

	# conjure, turn to, transform
	"U+420c":   [wn.synset("translate.v.02"),
				wn.synset("transform.v.02"),
				wn.synset("bid.v.03"),
				wn.synset("raise.v.07")],

	# constructional blocks, lego
	"U+420d":   [wn.synset("lego.n.01")],

	# copier, photocopier
	"U+4210":   [wn.synset("photocopier.n.01"),
				wn.synset("duplicator.n.01")],

	# coral
	"U+4211":   [wn.synset("coral.n.02"),
				wn.synset("coral.n.04")],

	# coral reef
	"U+4212":   [wn.synset("coral_reef.n.01"),
				wn.synset("breakwater.n.01"),
				wn.synset("stumbling_block.n.01")],

	# cordless phone
	"U+4214":   [wn.synset("telephone.n.01")],

	# coward
	"U+4216":   [wn.synset("coward.n.01"),
				wn.synset("coward.n.02")],

	# cowardice
	"U+4218":   [wn.synset("cowardice.n.01"),
				wn.synset("coward.n.01")],

	# cowardly
	"U+421a":   [wn.synset("cowardly.a.01")],

	# currency
	"U+421b":   [wn.synset("currency.n.01")],

	# cut and paste
	"U+421c":   [wn.synset("slice.v.04"),
				wn.synset("carve.v.02"),
				wn.synset("edit.v.03"),
				wn.synset("traverse.v.01"),
				wn.synset("snip.v.02"),
				wn.synset("reduce.v.01"),
				wn.synset("slash.v.04"),
				wn.synset("mow.v.01"),
				wn.synset("cut.v.01"),
				wn.synset("slash.v.01"),
				wn.synset("slash.v.03"),
				wn.synset("slit.v.01"),
				wn.synset("dilute.v.01"),
				wn.synset("divide.v.01"),
				wn.synset("cut_off.v.03"),
				wn.synset("interrupt.v.01"),
				wn.synset("break.v.43")],

	# dare
	"U+421d":   [wn.synset("defy.v.03"),
				wn.synset("make_bold.v.01"),
				wn.synset("dare.v.02")],

	# data
	"U+421f":   [wn.synset("data.n.01"),
				wn.synset("datum.n.01"),
				wn.synset("corpus.n.02")],

	# information
	"U+4220":   [wn.synset("information.n.01")],

	# desktop computer
	"U+4221":   [wn.synset("computer.n.01"),
				wn.synset("desktop_computer.n.01")],

	# detach, take apart
	"U+4223":   [wn.synset("analyze.v.02"),
				wn.synset("disassemble.v.01"),
				wn.synset("dismember.v.02"),
				wn.synset("detach.v.03"),
				wn.synset("detach.v.01"),
				wn.synset("detach.v.02")],

	# detachment, separation, breakup
	"U+4224":   [wn.synset("withdrawal.n.04"),
				wn.synset("dissolution.n.05"),
				wn.synset("separation.n.01"),
				wn.synset("separation.n.09"),
				wn.synset("insulation.n.01"),
				wn.synset("separation.n.02"),
				wn.synset("separation.n.05"),
				wn.synset("separation.n.04"),
				wn.synset("separation.n.07"),
				wn.synset("separation.n.06"),
				wn.synset("detachment.n.02"),
				wn.synset("interval.n.03"),
				wn.synset("legal_separation.n.02"),
				wn.synset("detachment.n.04")],

	# digital
	"U+4228":   [wn.synset("digital.a.01")],

	# digital processing, artificial intelligence, AI
	"U+4229":   [wn.synset("army_intelligence.n.01"),
				wn.synset("artificial_intelligence.n.01"),
				wn.synset("artificial_insemination.n.01"),
				wn.synset("three-toed_sloth.n.01")],

	# disembark
	"U+422a":   [wn.synset("disembark.v.01")],

	# document, written record, digital document
	"U+422c":   [wn.synset("document.n.01")],

	# drama
	"U+422e":   [wn.synset("play.n.01"),
				wn.synset("drama.n.02"),
				wn.synset("drama.n.03"),
				wn.synset("drama.n.04")],

	# dwarf, gnome
	"U+422f":   [wn.synset("dwarf.n.01"),
				wn.synset("gnome.n.02"),
				wn.synset("dwarf.n.03"),
				wn.synset("gnome.n.01")],

	# electrical engineer
	"U+4230":   [wn.synset("electrical_engineer.n.01")],

	# elf
	"U+4231":   [wn.synset("elf.n.01")],

	# e mail, email
	"U+4233":   [wn.synset("electronic_mail.n.01")],

	# embark, board
	"U+4237":   [wn.synset("board.v.01"),
				wn.synset("board.v.02"),
				wn.synset("board.v.03"),
				wn.synset("embark.v.01"),
				wn.synset("embark.v.02"),
				wn.synset("venture.v.01"),
				wn.synset("board.v.04")],

	# export
	"U+4238":   [wn.synset("export.v.01")],

	# exported
	"U+423a":   [wn.synset("export.v.03"),
				wn.synset("export.v.02"),
				wn.synset("export.v.01")],

	# fairy, fairy godmother
	"U+423d":   [wn.synset("fairy.n.01")],

	# fall asleep
	"U+4240":   [wn.synset("fall_asleep.v.01")],

	# fashion designer
	"U+4241":   [wn.synset("couturier.n.01")],

	# fax
	"U+4243":   [wn.synset("facsimile.n.02")],

	# file, data file
	"U+4246":   [wn.synset("file.n.04"),
				wn.synset("file.n.01"),
				wn.synset("file.n.03"),
				wn.synset("file.n.02")],

	# filled, stuffed
	"U+4247":   [wn.synset("stuffed.s.01"),
				wn.synset("stuffed.s.02"),
				wn.synset("filled.s.03"),
				wn.synset("filled.a.02"),
				wn.synset("filled.s.01")],

	# filled cabbage, stuffed cabbage
	"U+4248":   [wn.synset("stuffed_cabbage.n.01")],

	# filled food, stuffed food
	"U+4249":   [wn.synset("mast.n.03"),
				wn.synset("commissariat.n.01"),
				wn.synset("nutriment.n.01"),
				wn.synset("mess.n.03"),
				wn.synset("fare.n.04"),
				wn.synset("diet.n.01")],

	# filled vegetable, stuffed vegetable
	"U+424b":   [wn.synset("greens.n.01")],

	# finger spelling, finger alphabet
	"U+424c":   [wn.synset("manual_alphabet.n.01"),
				wn.synset("finger_spelling.n.01")],

	# fingerspell
	"U+424d":   [wn.synset("bless.v.03"),
				wn.synset("sign.v.04"),
				wn.synset("sign.v.06"),
				wn.synset("sign.v.07"),
				wn.synset("fingerspell.v.01"),
				wn.synset("sign.v.05"),
				wn.synset("sign.v.02"),
				wn.synset("sign.v.03"),
				wn.synset("sign.v.01")],

	# fish finger
	"U+424e":   [wn.synset("fish_stick.n.01")],

	# fisherman
	"U+424f":   [wn.synset("fisherman.n.01")],

	# folder
	"U+4251":   [wn.synset("catalog.n.01"),
				wn.synset("booklet.n.01"),
				wn.synset("folder.n.02")],

	# foster home
	"U+4252":   [wn.synset("foster_home.n.01")],

	# freezer
	"U+4254":   [wn.synset("deep-freeze.n.01")],

	# fruit cream, compote
	"U+4255":   [wn.synset("compote.n.01")],

	# function
	"U+4256":   [wn.synset("function.v.01")],

	# functional
	"U+4257":   [wn.synset("functional.a.01"),
				wn.synset("functional.a.03"),
				wn.synset("functional.a.02"),
				wn.synset("running.s.06"),
				wn.synset("functional.s.04"),
				wn.synset("functional.s.05")],

	# gardener
	"U+4258":   [wn.synset("gardener.n.01"),
				wn.synset("gardener.n.02")],

	# ghost, phantom
	"U+4259":   [wn.synset("touch.n.03"),
				wn.synset("ghostwriter.n.01"),
				wn.synset("ghost.n.03"),
				wn.synset("apparition.n.01"),
				wn.synset("ghost.n.01"),
				wn.synset("apparition.n.03")],

	# giant
	"U+425d":   [wn.synset("giant.n.01"),
				wn.synset("giant.n.03"),
				wn.synset("giant.n.05"),
				wn.synset("giant.n.04"),
				wn.synset("giant.n.06"),
				wn.synset("colossus.n.02"),
				wn.synset("giant_star.n.01")],

	# go ashore
	"U+425f":   [wn.synset("get_off.v.01"),
				wn.synset("disembark.v.01")],

	# go to sea
	"U+4260":   [wn.synset("embark.v.01")],

	# boarding, embarkation
	"U+4261":   [wn.synset("boarding.n.02"),
				wn.synset("boarding.n.01")],

	# goblin
	"U+4263":   [wn.synset("goblin.n.01")],

	# hero
	"U+4265":   [wn.synset("hero.n.02")],

	# heroic
	"U+4267":   [wn.synset("epic.s.01"),
				wn.synset("heroic.a.02")],

	# herring, sardine
	"U+4268":   [wn.synset("sardine.n.02"),
				wn.synset("herring.n.02"),
				wn.synset("herring.n.01"),
				wn.synset("pilchard.n.02")],

	# hobbit
	"U+4269":   [wn.synset("hobbit.n.01")],

	# homework, home studying
	"U+426a":   [wn.synset("homework.n.01")],

	# hopeful
	"U+426b":   [wn.synset("bright.s.10")],

	# house work, housekeeping, housework
	"U+426c":   [wn.synset("housework.n.01")],

	# hunt, hunting
	"U+426d":   [wn.synset("hunt.v.01")],

	# import
	"U+426e":   [wn.synset("import.n.01")],

	# imported
	"U+426f":   [wn.synset("imported.s.01")],

	# internet
	"U+4270":   [wn.synset("internet.n.01")],

	# intranet
	"U+4272":   [wn.synset("intranet.n.01")],

	# introduce, present
	"U+4274":   [wn.synset("introduce.v.01")],

	# journalist
	"U+4275":   [wn.synset("journalist.n.01")],

	# writer, author
	"U+4276":   [wn.synset("writer.n.01")],

	# joystick
	"U+4277":   [wn.synset("joystick.n.02")],

	# Kazakhstan
	"U+4278":   [wn.synset("kazakhstan.n.01")],

	# ketchup
	"U+4279":   [wn.synset("catsup.n.01")],

	# tomato sauce
	"U+427a":   [wn.synset("tomato_sauce.n.01")],

	# key guard
	"U+427c":   [wn.synset("pegboard.n.01")],

	# keyboard
	"U+427d":   [wn.synset("keyboard.n.02"),
				wn.synset("keyboard.n.01")],

	# kindergarten, preschool, nursery, play group
	"U+427f":   [wn.synset("playschool.n.01"),
				wn.synset("nursery.n.01"),
				wn.synset("preschool.n.01"),
				wn.synset("greenhouse.n.01"),
				wn.synset("kindergarten.n.01")],

	# king
	"U+4280":   [wn.synset("king.n.01"),
				wn.synset("king.n.10")],

	# laptop
	"U+4283":   [wn.synset("notebook.n.02"),
				wn.synset("laptop.n.01")],

	# lecture
	"U+4287":   [wn.synset("lecture.n.01"),
				wn.synset("lecture.n.02"),
				wn.synset("lecture.n.03")],

	# leprechaun
	"U+4288":   [wn.synset("leprechaun.n.01"),
				wn.synset("elf.n.01"),
				wn.synset("puck.n.01"),
				wn.synset("imp.n.02")],

	# librarian
	"U+4289":   [wn.synset("librarian.n.01")],

	# lotto, bingo
	"U+428c":   [wn.synset("lotto.n.01")],

	# lumberjack
	"U+428d":   [wn.synset("lumberman.n.01")],

	# lunch box
	"U+428e":   [wn.synset("musette.n.01"),
				wn.synset("bagpipe.n.01")],

	# magician
	"U+4290":   [wn.synset("magician.n.01"),
				wn.synset("sorcerer.n.01")],

	# make believe man
	"U+4294":   [wn.synset("imaginary_being.n.01")],

	# make believe person, imaginary person, water nymph
	"U+4296":   [wn.synset("imaginary_being.n.01")],

	# make believe woman
	"U+4297":   [wn.synset("imaginary_being.n.01")],

	# man doll
	"U+4298":   [wn.synset("doll.n.01")],

	# subject
	"U+429b":   [wn.synset("topic.n.02"),
				wn.synset("subject.n.05"),
				wn.synset("subject.n.02"),
				wn.synset("subject.n.01")],

	# mechanical engineer
	"U+429f":   [wn.synset("mechanical_engineer.n.01")],

	# memory
	"U+42a0":   [wn.synset("memory.n.04"),
				wn.synset("memory.n.02"),
				wn.synset("memory.n.03"),
				wn.synset("memory.n.01")],

	# mermaid
	"U+42a1":   [wn.synset("mermaid.n.01")],

	# mobile phone, cellphone
	"U+42a3":   [wn.synset("cellular_telephone.n.01")],

	# musical
	"U+42a5":   [wn.synset("musical.n.01")],

	# noisemaker, musical toy
	"U+42a7":   [wn.synset("noisemaker.n.01")],

	# opera
	"U+42a8":   [wn.synset("opera.n.03"),
				wn.synset("opera.n.01")],

	# optician
	"U+42a9":   [wn.synset("optician.n.01")],

	# oval shape
	"U+42ab":   [wn.synset("ellipse.n.01")],

	# overlay
	"U+42ac":   [wn.synset("overlay.n.02"),
				wn.synset("sheathing.n.01"),
				wn.synset("covering.n.02")],

	# palmtop, PDA
	"U+42af":   [wn.synset("personal_digital_assistant.n.01")],

	# pancake, crepe, tortilla
	"U+42b0":   [wn.synset("pancake.n.01")],

	# paper money, bill
	"U+42b1":   [wn.synset("bill.n.03")],

	# passenger
	"U+42b2":   [wn.synset("passenger.n.01")],

	# educationalist, educationist
	"U+42b4":   [wn.synset("educationist.n.01")],

	# Pegasus
	"U+42b5":   [wn.synset("pegasus.n.01")],

	# perform
	"U+42b6":   [wn.synset("perform.v.03")],

	# performance, show
	"U+42b7":   [wn.synset("show.n.01"),
				wn.synset("performance.n.01"),
				wn.synset("performance.n.02"),
				wn.synset("show.n.03")],

	# pharmacist
	"U+42b9":   [wn.synset("pharmacist.n.01")],

	# philosopher
	"U+42bb":   [wn.synset("philosopher.n.01")],

	# philosophy
	"U+42be":   [wn.synset("philosophy.n.02"),
				wn.synset("philosophy.n.03"),
				wn.synset("doctrine.n.01")],

	# pirate
	"U+42bf":   [wn.synset("plagiarist.n.01"),
				wn.synset("pirate.n.02"),
				wn.synset("pirate.n.03")],

	# porcupine
	"U+42c1":   [wn.synset("porcupine.n.01")],

	# porridge
	"U+42c2":   [wn.synset("porridge.n.01")],

	# prince
	"U+42c3":   [wn.synset("prince.n.01")],

	# princess
	"U+42c4":   [wn.synset("princess.n.01")],

	# print
	"U+42c5":   [wn.synset("print.v.03"),
				wn.synset("print.v.02"),
				wn.synset("print.v.01"),
				wn.synset("print.v.04")],

	# Pterosaur, Pterodactyl
	"U+42c6":   [wn.synset("pterodactyl.n.01")],

	# queen
	"U+42c7":   [wn.synset("queen.n.02")],

	# quills, spines
	"U+42c8":   [wn.synset("quill.n.04"),
				wn.synset("quill.n.01"),
				wn.synset("spur.n.02"),
				wn.synset("flight_feather.n.01"),
				wn.synset("quill.n.02"),
				wn.synset("spine.n.03"),
				wn.synset("spine.n.05"),
				wn.synset("spine.n.04"),
				wn.synset("spinal_column.n.01")],

	# ramp
	"U+42cb":   [wn.synset("ramp.n.01")],

	# redo
	"U+42cc":   [wn.synset("remake.v.01")],

	# refrigerator, fridge
	"U+42ce":   [wn.synset("refrigerator.n.01"),
				wn.synset("electric_refrigerator.n.01")],

	# remember, recall
	"U+42d1":   [wn.synset("remember.v.01")],

	# research
	"U+42d4":   [wn.synset("research.v.02"),
				wn.synset("research.v.01")],

	# rob
	"U+42d6":   [wn.synset("pilfer.v.01"),
				wn.synset("rob.v.01"),
				wn.synset("overcharge.v.01"),
				wn.synset("steal.v.01")],

	# robber
	"U+42d8":   [wn.synset("robber.n.01"),
				wn.synset("thief.n.01")],

	# robot doll
	"U+42da":   [wn.synset("automaton.n.02")],

	# ruin, wreck, wreckage, castle ruin
	"U+42db":   [wn.synset("ruin.n.02")],

	# Russia
	"U+42dd":   [wn.synset("soviet_union.n.01"),
				wn.synset("russia.n.04"),
				wn.synset("soviet_russia.n.01"),
				wn.synset("russia.n.03")],

	# samosa, pirogue
	"U+42de":   [wn.synset("samosa.n.01"),
				wn.synset("dugout_canoe.n.01")],

	# Sandman
	"U+42e2":   [wn.synset("sandman.n.01")],

	# Santa Claus, Father Christmas
	"U+42e3":   [wn.synset("santa_claus.n.01")],

	# schoolbag
	"U+42e6":   [wn.synset("schoolbag.n.01")],

	# sea anemone
	"U+42e8":   [wn.synset("sea_anemone.n.01")],

	# sea cucumber
	"U+42e9":   [wn.synset("sea_cucumber.n.01")],

	# sea lion
	"U+42ea":   [wn.synset("sea_lion.n.01")],

	# sea urchin
	"U+42ed":   [wn.synset("sea_urchin.n.01")],

	# seal
	"U+42ef":   [wn.synset("seal.n.09")],

	# seaweed
	"U+42f1":   [wn.synset("seaweed.n.01")],

	# shepherd
	"U+42f5":   [wn.synset("shepherd.n.01"),
				wn.synset("sheepherder.n.01")],

	# shoot
	"U+42f7":   [wn.synset("blast.v.07")],

	# siren of the woods
	"U+42f8":   [wn.synset("dryad.n.01")],

	# software, computer program, application, app
	"U+42f9":   [wn.synset("software.n.01")],

	# spell
	"U+42fa":   [wn.synset("spell.v.02"),
				wn.synset("spell.v.03"),
				wn.synset("spell.v.01"),
				wn.synset("spell.v.06"),
				wn.synset("spell.v.04"),
				wn.synset("spell.v.05")],

	# steal
	"U+42fc":   [wn.synset("steal.v.01")],

	# stew
	"U+42fe":   [wn.synset("stew.n.02")],

	# swordfish
	"U+42ff":   [wn.synset("swordfish.n.02")],

	# tablet computer, tablet, tablet PC
	"U+4300":   [wn.synset("tablet.n.01"),
				wn.synset("pad.n.01"),
				wn.synset("tablet.n.03"),
				wn.synset("pill.n.02")],

	# tabletop
	"U+4302":   [wn.synset("tabletop.n.01")],

	# tailor, dressmaker, seamstress
	"U+4303":   [wn.synset("tailor.n.01")],

	# theologian, theologist
	"U+4307":   [wn.synset("theologian.n.01")],

	# thief
	"U+430b":   [wn.synset("thief.n.01")],

	# Tibet
	"U+430c":   [wn.synset("tibet.n.01")],

	# tooth fairy
	"U+430e":   [wn.synset("tooth_fairy.n.01")],

	# touch screen
	"U+430f":   [wn.synset("touch_screen.n.01")],

	# touchpad, trackpad
	"U+4310":   [wn.synset("smooth_plane.n.01")],

	# trackball
	"U+4312":   [wn.synset("trackball.n.01")],

	# tragedy
	"U+4313":   [wn.synset("tragedy.n.02")],

	# traveller
	"U+4314":   [wn.synset("traveler.n.01")],

	# Triceratops
	"U+4316":   [wn.synset("triceratops.n.01")],

	# troll
	"U+4318":   [wn.synset("troll.n.01")],

	# tuna fish
	"U+431a":   [wn.synset("tuna.n.03"),
				wn.synset("tuna.n.02")],

	# Tyrannosaurus Rex
	"U+431c":   [wn.synset("tyrannosaur.n.01")],

	# undo
	"U+431d":   [wn.synset("unmake.v.01")],

	# unicorn
	"U+431e":   [wn.synset("unicorn.n.01")],

	# wake up
	"U+431f":   [wn.synset("wake_up.v.02")],

	# walrus
	"U+4320":   [wn.synset("walrus.n.01")],

	# wash up, do the dishes
	"U+4321":   [wn.synset("wash_up.v.03")],

	# website
	"U+4324":   [wn.synset("web_site.n.01"),
				wn.synset("world_wide_web.n.01")],

	# virus
	"U+4326":   [wn.synset("virus.n.01")],

	# program, programme, presentation
	"U+4327":   [wn.synset("plan.n.01"),
				wn.synset("program.n.08"),
				wn.synset("course_of_study.n.01"),
				wn.synset("program.n.02"),
				wn.synset("broadcast.n.02"),
				wn.synset("platform.n.02"),
				wn.synset("program.n.07"),
				wn.synset("program.n.05")],

	# witch
	"U+4329":   [wn.synset("enchantress.n.02"),
				wn.synset("witch.n.02")],

	# wizard
	"U+432b":   [wn.synset("ace.n.03"),
				wn.synset("sorcerer.n.01")],

	# woman doll
	"U+432c":   [wn.synset("doll.n.01")],

	# worksheet
	"U+432d":   [wn.synset("worksheet.n.01"),
				wn.synset("worksheet.n.02")],

	# accordion
	"U+432e":   [wn.synset("accordion.n.01")],

	# wind instrument
	"U+432f":   [wn.synset("wind_instrument.n.01")],

	# alto
	"U+4330":   [wn.synset("alto.n.01")],

	# stave, staff
	"U+4331":   [wn.synset("staff.n.06")],

	# amplifier
	"U+4332":   [wn.synset("amplifier.n.01")],

	# autoharp, zither, kantele
	"U+4333":   [wn.synset("zither.n.01")],

	# bagpipe
	"U+4334":   [wn.synset("bagpipe.n.01")],

	# banjo
	"U+4336":   [wn.synset("banjo.n.01")],

	# bass
	"U+4338":   [wn.synset("bass.n.06"),
				wn.synset("bass.n.07"),
				wn.synset("bass.n.03")],

	# bass clarinet
	"U+4339":   [wn.synset("bass_clarinet.n.01")],

	# clarinet, reed instrument
	"U+433a":   [wn.synset("clarinet.n.01")],

	# bass guitar
	"U+433b":   [wn.synset("bass_guitar.n.01")],

	# bassoon
	"U+433d":   [wn.synset("bassoon.n.01")],

	# oboe
	"U+433e":   [wn.synset("oboe.n.01")],

	# bells, chime bars, tubular bells
	"U+4341":   [wn.synset("doorbell.n.01"),
				wn.synset("bell.n.10"),
				wn.synset("chime.n.01"),
				wn.synset("bell.n.08"),
				wn.synset("bell.n.06"),
				wn.synset("bell.n.07"),
				wn.synset("bell.n.04"),
				wn.synset("bell.n.05"),
				wn.synset("bell.n.03"),
				wn.synset("bell.n.01")],

	# bongo drum, hand drum
	"U+4343":   [wn.synset("bongo.n.01")],

	# bow and string
	"U+4345":   [wn.synset("bow.n.02"),
				wn.synset("snare.n.05")],

	# brake
	"U+4348":   [wn.synset("brake.v.02"),
				wn.synset("brake.v.01")],

	# brass instrument
	"U+434b":   [wn.synset("brass.n.02")],

	# breeze
	"U+434c":   [wn.synset("breeze.n.01")],

	# bugle
	"U+434d":   [wn.synset("bugle.n.01"),
				wn.synset("bugle.n.03"),
				wn.synset("bugle.n.02")],

	# burned out, burnt out
	"U+434f":   [wn.synset("burned-out.s.01")],

	# castanets
	"U+4351":   [wn.synset("bones.n.01")],

	# celeriac, celery
	"U+4354":   [wn.synset("celery.n.02"),
				wn.synset("celery.n.01")],

	# cello
	"U+4357":   [wn.synset("cello.n.01")],

	# children's song, nursery rhyme
	"U+4359":   [wn.synset("nursery_rhyme.n.01")],

	# flute, recorder, transverse flute
	"U+435b":   [wn.synset("flute.n.01")],

	# recorder
	"U+435c":   [wn.synset("recorder.n.01"),
				wn.synset("fipple_flute.n.01"),
				wn.synset("recorder.n.03"),
				wn.synset("registrar.n.03")],

	# condensation
	"U+435e":   [wn.synset("condensation.n.02")],

	# condense
	"U+4360":   [wn.synset("condense.v.04"),
				wn.synset("condense.v.05"),
				wn.synset("condense.v.06"),
				wn.synset("condense.v.07"),
				wn.synset("condense.v.01"),
				wn.synset("condense.v.03"),
				wn.synset("digest.v.07")],

	# country music
	"U+4361":   [wn.synset("country_music.n.01")],

	# cymbal
	"U+4362":   [wn.synset("cymbal.n.01")],

	# dance music
	"U+4363":   [wn.synset("dance_music.n.01"),
				wn.synset("dance_music.n.02")],

	# dark
	"U+4364":   [wn.synset("dark.a.02"),
				wn.synset("dark.s.08"),
				wn.synset("dark.a.01"),
				wn.synset("dark.s.06")],

	# detest, despise
	"U+4365":   [wn.synset("abhor.v.01"),
				wn.synset("hate.v.01"),
				wn.synset("contemn.v.01")],

	# disaster, catastrophe
	"U+4366":   [wn.synset("calamity.n.01")],

	# district, neighbourhood, city district
	"U+4367":   [wn.synset("neighborhood.n.02"),
				wn.synset("district.n.01"),
				wn.synset("vicinity.n.01")],

	# double bass, bass fiddle, contrabass
	"U+4369":   [wn.synset("bass_fiddle.n.01")],

	# double bassoon
	"U+436b":   [wn.synset("contrabassoon.n.01")],

	# dried
	"U+436d":   [wn.synset("dried.s.02"),
				wn.synset("dried.s.01")],

	# driving license
	"U+436f":   [wn.synset("driver's_license.n.01")],

	# drum
	"U+4371":   [wn.synset("drum.n.01")],

	# percussion instrument
	"U+4372":   [wn.synset("percussion_instrument.n.01")],

	# drumstick
	"U+4374":   [wn.synset("mallet.n.02"),
				wn.synset("drumstick.n.01"),
				wn.synset("drumstick.n.02")],

	# dry
	"U+4376":   [wn.synset("dry.v.01")],

	# eager, keen, willing
	"U+4377":   [wn.synset("willing.a.01")],

	# easy, easily
	"U+4378":   [wn.synset("easily.r.01"),
				wn.synset("easy.a.01")],

	# ease, easiness, simplicity
	"U+4379":   [wn.synset("ease.n.01"),
				wn.synset("ease.n.02"),
				wn.synset("ease.n.04"),
				wn.synset("chasteness.n.01"),
				wn.synset("easiness.n.03"),
				wn.synset("relief.n.02"),
				wn.synset("easiness.n.01"),
				wn.synset("simplicity.n.01"),
				wn.synset("simplicity.n.02"),
				wn.synset("simplicity.n.03"),
				wn.synset("rest.n.02")],

	# electric piano
	"U+437e":   [wn.synset("piano.n.01")],

	# empty, evacuate, throw away, void
	"U+437f":   [wn.synset("empty.a.01")],

	# emptying, voidance, evacuation
	"U+4380":   [wn.synset("evacuation.n.02"),
				wn.synset("emptying.n.01"),
				wn.synset("elimination.n.02")],

	# exciting, excitingly, excited, excitedly
	"U+4383":   [wn.synset("excited.a.02")],

	# foam, mousse
	"U+4386":   [wn.synset("foam.n.01")],

	# French horn
	"U+4388":   [wn.synset("french_horn.n.01")],

	# gong
	"U+4389":   [wn.synset("gong.n.01")],

	# guitar, string instrument
	"U+438a":   [wn.synset("guitar.n.01")],

	# hair spray
	"U+438c":   [wn.synset("hair_spray.n.01")],

	# spray, vaporize, vaporization
	"U+438d":   [wn.synset("vaporization.n.01"),
				wn.synset("vaporization.n.02")],

	# harp
	"U+438e":   [wn.synset("harp.n.01")],

	# harpsichord
	"U+438f":   [wn.synset("harpsichord.n.01")],

	# hate, hatred
	"U+4390":   [wn.synset("hate.n.01")],

	# hum
	"U+4391":   [wn.synset("hum.v.04"),
				wn.synset("hum.v.01"),
				wn.synset("hum.v.02"),
				wn.synset("hum.v.03")],

	# humid, damp, moist
	"U+4392":   [wn.synset("humid.s.01"),
				wn.synset("damp.s.01")],

	# humidity
	"U+4393":   [wn.synset("humidity.n.01")],

	# hurricane
	"U+4394":   [wn.synset("hurricane.n.01")],

	# kazoo
	"U+4395":   [wn.synset("kazoo.n.01")],

	# kebab, NL)
	"U+4396":   [wn.synset("kabob.n.01")],

	# loudspeaker
	"U+439e":   [wn.synset("loudspeaker.n.01")],

	# mandolin
	"U+43a0":   [wn.synset("mandolin.n.01")],

	# maracas, calabash
	"U+43a2":   [wn.synset("calabash.n.01")],

	# microphone
	"U+43a5":   [wn.synset("microphone.n.01")],

	# MP3 player, iPod
	"U+43a6":   [wn.synset("ipod.n.01")],

	# never
	"U+43a9":   [wn.synset("never.r.01")],

	# nothing, none
	"U+43aa":   [wn.synset("nothing.n.01")],

	# organ, pipe organ, inner organ, inner body part
	"U+43ad":   [wn.synset("organ.n.05")],

	# panpipe
	"U+43ae":   [wn.synset("panpipe.n.01")],

	# parking lot
	"U+43b0":   [wn.synset("parking_lot.n.01")],

	# parking ticket
	"U+43b3":   [wn.synset("parking_ticket.n.01")],

	# participant
	"U+43b5":   [wn.synset("participant.n.01")],

	# participate
	"U+43b7":   [wn.synset("participate.v.01")],

	# participation, involvement
	"U+43b8":   [wn.synset("involvement.n.02"),
				wn.synset("engagement.n.07")],

	# pennywhistle, tin whistle
	"U+43ba":   [wn.synset("pennywhistle.n.01")],

	# soprano
	"U+43bc":   [wn.synset("soprano.n.01")],

	# piano
	"U+43be":   [wn.synset("piano.n.01")],

	# piccolo
	"U+43c1":   [wn.synset("piccolo.n.01")],

	# pitch
	"U+43c4":   [wn.synset("sales_talk.n.01"),
				wn.synset("pitch.n.06"),
				wn.synset("pitch.n.07"),
				wn.synset("lurch.n.03"),
				wn.synset("pitch.n.02"),
				wn.synset("pitch.n.03"),
				wn.synset("pitch.n.01"),
				wn.synset("pitch.n.05"),
				wn.synset("pitch.n.08"),
				wn.synset("pitch.n.10")],

	# pop music
	"U+43c5":   [wn.synset("pop_music.n.01")],

	# punk rock
	"U+43c6":   [wn.synset("punk_rock.n.01")],

	# rainbow
	"U+43c7":   [wn.synset("rainbow.n.01")],

	# rap
	"U+43c8":   [wn.synset("pat.n.01"),
				wn.synset("blame.n.02"),
				wn.synset("knock.n.05"),
				wn.synset("rap.n.02"),
				wn.synset("rap.n.05"),
				wn.synset("rap.n.04")],

	# rattle
	"U+43c9":   [wn.synset("rattle.n.03"),
				wn.synset("rattle.n.02"),
				wn.synset("rattle.n.01")],

	# reed, bamboo
	"U+43ca":   [wn.synset("beating-reed_instrument.n.01"),
				wn.synset("reed.n.03"),
				wn.synset("reed.n.02"),
				wn.synset("reed.n.01"),
				wn.synset("reed.n.04"),
				wn.synset("bamboo.n.01"),
				wn.synset("bamboo.n.02"),
				wn.synset("sharp.a.09")],

	# roe deer
	"U+43cc":   [wn.synset("roe_deer.n.01")],

	# rotisserie, spit
	"U+43cd":   [wn.synset("rotisserie.n.02")],

	# saxophone
	"U+43cf":   [wn.synset("sax.n.02")],

	# small pancake, blini
	"U+43d0":   [wn.synset("pancake.n.01"),
				wn.synset("blini.n.01"),
				wn.synset("crape.n.01")],

	# snowmobile
	"U+43d2":   [wn.synset("snowmobile.n.01")],

	# snowplow, snowplough
	"U+43d3":   [wn.synset("snowplow.n.01")],

	# spray bottle, vaporizer, spray can
	"U+43d4":   [wn.synset("aerosol.n.02"),
				wn.synset("atomizer.n.01"),
				wn.synset("vaporizer.n.01")],

	# stressed
	"U+43d5":   [wn.synset("stressed.a.02"),
				wn.synset("stressed.s.01"),
				wn.synset("taut.s.01")],

	# stress
	"U+43d6":   [wn.synset("stress.n.04")],

	# surprise
	"U+43d7":   [wn.synset("storm.v.05"),
				wn.synset("surprise.v.01"),
				wn.synset("surprise.v.02")],

	# surprised
	"U+43d8":   [wn.synset("surprised.a.01")],

	# synthesizer, synthesiser, keyboard
	"U+43d9":   [wn.synset("keyboard.n.02"),
				wn.synset("synthesizer.n.02"),
				wn.synset("synthesist.n.01"),
				wn.synset("keyboard.n.01")],

	# tambourine
	"U+43da":   [wn.synset("tambourine.n.01")],

	# tenor
	"U+43dc":   [wn.synset("tenor.n.03"),
				wn.synset("tenor.n.01")],

	# tornado
	"U+43dd":   [wn.synset("tornado.n.01")],

	# trombone
	"U+43df":   [wn.synset("trombone.n.01")],

	# tsunami
	"U+43e0":   [wn.synset("tsunami.n.01")],

	# tuba
	"U+43e1":   [wn.synset("bass_horn.n.01")],

	# tuning fork
	"U+43e3":   [wn.synset("tuning_fork.n.01")],

	# twin brother
	"U+43e4":   [wn.synset("twin.n.01"),
				wn.synset("counterpart.n.02")],

	# twin sister
	"U+43e5":   [wn.synset("twin.n.01"),
				wn.synset("binoculars.n.01"),
				wn.synset("gemini.n.01"),
				wn.synset("counterpart.n.02")],

	# twins
	"U+43e6":   [wn.synset("gemini.n.03"),
				wn.synset("gemini.n.01")],

	# ukulele
	"U+43e7":   [wn.synset("uke.n.01")],

	# unfold
	"U+43e8":   [wn.synset("unfold.v.04")],

	# unfolding
	"U+43e9":   [wn.synset("unfolding.n.01")],

	# viola
	"U+43ea":   [wn.synset("viola.n.03")],

	# violin
	"U+43eb":   [wn.synset("violin.n.01")],

	# voice
	"U+43ec":   [wn.synset("part.n.11"),
				wn.synset("voice.n.10"),
				wn.synset("articulation.n.03"),
				wn.synset("voice.n.02"),
				wn.synset("voice.n.03"),
				wn.synset("voice.n.01"),
				wn.synset("voice.n.06"),
				wn.synset("voice.n.07"),
				wn.synset("spokesperson.n.01"),
				wn.synset("voice.n.05"),
				wn.synset("voice.n.09")],

	# woodwind instrument
	"U+43ed":   [wn.synset("woodwind.n.01")],

	# xylophone, vibraphone
	"U+43ee":   [wn.synset("marimba.n.01")],

	# acrobat
	"U+43ef":   [wn.synset("acrobat.n.01")],

	# acrobatics
	"U+43f0":   [wn.synset("acrobatics.n.01")],

	# Advent
	"U+43f1":   [wn.synset("advent.n.02"),
				wn.synset("advent.n.01"),
				wn.synset("second_coming.n.01")],

	# agnosticism
	"U+43f3":   [wn.synset("agnosticism.n.01")],

	# aid store room
	"U+43f4":   [wn.synset("deposit.n.09"),
				wn.synset("sediment.n.01"),
				wn.synset("storehouse.n.01")],

	# Ascension
	"U+43fb":   [wn.synset("ascension.n.03"),
				wn.synset("ascension.n.01")],

	# Ascension Day
	"U+43fd":   [wn.synset("ascension.n.01")],

	# asparagus
	"U+43ff":   [wn.synset("asparagus.n.02"),
				wn.synset("asparagus.n.01")],

	# at one's destination, there
	"U+4402":   [wn.synset("there.n.01"),
				wn.synset("there.r.02"),
				wn.synset("there.r.03"),
				wn.synset("there.r.01")],

	# auditor, accountant
	"U+4403":   [wn.synset("accountant.n.01")],

	# avalanche
	"U+4404":   [wn.synset("avalanche.n.01")],

	# bisexual
	"U+4408":   [wn.synset("bisexual.a.01")],

	# bisexuality
	"U+4409":   [wn.synset("bisexuality.n.02")],

	# bleat, baa
	"U+440c":   [wn.synset("bleat.v.02")],

	# fanatic
	"U+440e":   [wn.synset("fanatic.n.01")],

	# blood vessel
	"U+440f":   [wn.synset("blood_vessel.n.01")],

	# blush
	"U+4410":   [wn.synset("blush.v.01")],

	# body brace, corset
	"U+4411":   [wn.synset("corset.n.01")],

	# body fluid
	"U+4412":   [wn.synset("liquid_body_substance.n.01")],

	# body hair
	"U+4413":   [wn.synset("body_hair.n.01")],

	# body part
	"U+4414":   [wn.synset("body_part.n.01")],

	# body temperature
	"U+4415":   [wn.synset("body_temperature.n.01")],

	# bolt
	"U+4416":   [wn.synset("run_off.v.02"),
				wn.synset("abscond.v.01"),
				wn.synset("pack.v.01"),
				wn.synset("gobble.v.01"),
				wn.synset("box.v.01"),
				wn.synset("bolt.v.07"),
				wn.synset("bolt.v.01"),
				wn.synset("bolt.v.02"),
				wn.synset("bolt.v.03")],

	# bomb, explosive
	"U+4418":   [wn.synset("bomb.n.01")],

	# bridle, headstall
	"U+4419":   [wn.synset("bridle.n.01")],

	# harness
	"U+441a":   [wn.synset("harness.n.02"),
				wn.synset("harness.n.01")],

	# muzzle
	"U+441b":   [wn.synset("gun_muzzle.n.01"),
				wn.synset("muzzle.n.03"),
				wn.synset("muzzle.n.02"),
				wn.synset("gag.n.02")],

	# bus lane
	"U+441c":   [wn.synset("bus_lane.n.01")],

	# bus station
	"U+441d":   [wn.synset("bus_terminal.n.01")],

	# station
	"U+441e":   [wn.synset("station.n.01")],

	# bus stop, bus bay
	"U+441f":   [wn.synset("bus_stop.n.01")],

	# cable car
	"U+4422":   [wn.synset("cable_car.n.01"),
				wn.synset("telpherage.n.01")],

	# cancer
	"U+4424":   [wn.synset("cancer.n.01"),
				wn.synset("cancer.n.03"),
				wn.synset("cancer.n.02"),
				wn.synset("cancer.n.05"),
				wn.synset("cancer.n.04")],

	# canter
	"U+4426":   [wn.synset("canter.v.01"),
				wn.synset("canter.v.02"),
				wn.synset("canter.v.03")],

	# trot
	"U+4427":   [wn.synset("trot.v.02"),
				wn.synset("trot.v.03"),
				wn.synset("trot.v.01")],

	# ceramics, pottery
	"U+4428":   [wn.synset("ceramic.n.01"),
				wn.synset("pottery.n.03"),
				wn.synset("pottery.n.02"),
				wn.synset("pottery.n.01"),
				wn.synset("ceramics.n.01")],

	# certain, sure
	"U+442a":   [wn.synset("sure.s.04"),
				wn.synset("certain.s.01"),
				wn.synset("sure.s.06"),
				wn.synset("certain.a.04"),
				wn.synset("certain.a.03"),
				wn.synset("certain.a.02")],

	# chairlift
	"U+442b":   [wn.synset("chairlift.n.01")],

	# chairman
	"U+442c":   [wn.synset("president.n.04")],

	# challenge
	"U+442d":   [wn.synset("challenge.n.01")],

	# charm
	"U+442e":   [wn.synset("appeal.n.02")],

	# personality
	"U+442f":   [wn.synset("personality.n.01")],

	# charming
	"U+4430":   [wn.synset("charming.s.01"),
				wn.synset("charming.s.02")],

	# checked
	"U+4431":   [wn.synset("checked.s.01"),
				wn.synset("row.n.05")],

	# child care
	"U+4434":   [wn.synset("childcare.n.01")],

	# chirp, twitter
	"U+4438":   [wn.synset("peep.v.03")],

	# circus
	"U+4439":   [wn.synset("circus.n.02"),
				wn.synset("circus.n.03"),
				wn.synset("circus.n.01"),
				wn.synset("circus.n.06"),
				wn.synset("circus.n.04"),
				wn.synset("circus.n.05")],

	# cloakroom, walk in closet
	"U+443a":   [wn.synset("cloakroom.n.02")],

	# cloudberry
	"U+443b":   [wn.synset("cloudberry.n.01")],

	# common, mutual, shared
	"U+443d":   [wn.synset("common.s.03")],

	# commuter train
	"U+443e":   [wn.synset("commuter.n.01")],

	# conductor, therapist)
	"U+4440":   [wn.synset("conductor.n.02")],

	# constipation
	"U+4442":   [wn.synset("constipation.n.01")],

	# constitution
	"U+4444":   [wn.synset("fundamental_law.n.01")],

	# croak
	"U+4445":   [wn.synset("murmur.v.02"),
				wn.synset("croak.v.02"),
				wn.synset("die.v.01")],

	# crown prince
	"U+4446":   [wn.synset("crown_prince.n.01")],

	# crown princess
	"U+4447":   [wn.synset("crown_princess.n.02"),
				wn.synset("crown_princess.n.01")],

	# cure
	"U+4448":   [wn.synset("bring_around.v.02")],

	# decoration, ornament
	"U+444a":   [wn.synset("decoration.n.03"),
				wn.synset("decoration.n.01")],

	# democracy
	"U+444b":   [wn.synset("majority_rule.n.01"),
				wn.synset("democracy.n.01"),
				wn.synset("democracy.n.02")],

	# depending on
	"U+444e":   [wn.synset("contingent.s.02")],

	# devoted
	"U+444f":   [wn.synset("attached.s.04"),
				wn.synset("devoted.s.01"),
				wn.synset("devoted.s.02"),
				wn.synset("attached.a.03")],

	# devotion
	"U+4450":   [wn.synset("idolatry.n.01"),
				wn.synset("devotion.n.04"),
				wn.synset("devotion.n.01"),
				wn.synset("devotion.n.02")],

	# devotee, fan
	"U+4451":   [wn.synset("fan.n.03")],

	# diarrhea, diarrhoea
	"U+4454":   [wn.synset("diarrhea.n.01")],

	# domestic
	"U+4455":   [wn.synset("domestic.s.04"),
				wn.synset("domestic.s.05"),
				wn.synset("domestic.a.02"),
				wn.synset("domestic.a.03"),
				wn.synset("domestic.a.01")],

	# dotted
	"U+4456":   [wn.synset("dotted.s.01")],

	# drying cupboard, airing cupboard
	"U+4457":   [wn.synset("airing_cupboard.n.01"),
				wn.synset("clothes_dryer.n.01"),
				wn.synset("hand_blower.n.01")],

	# drying room, drying chamber
	"U+445a":   [wn.synset("dryer.n.01")],

	# dump, dispose
	"U+445b":   [wn.synset("shed.v.01"),
				wn.synset("qualify.v.04"),
				wn.synset("dump.v.04"),
				wn.synset("dump.v.01"),
				wn.synset("dump.v.03"),
				wn.synset("dump.v.02"),
				wn.synset("plunge.v.06"),
				wn.synset("deck.v.03"),
				wn.synset("dispose.v.03"),
				wn.synset("throw.v.01"),
				wn.synset("dispose.v.01"),
				wn.synset("waste.v.01"),
				wn.synset("discard.v.01"),
				wn.synset("dispose.v.04")],

	# elbow splint
	"U+445c":   [wn.synset("cubitiere.n.01")],

	# voter, elector
	"U+445d":   [wn.synset("voter.n.01")],

	# electorate
	"U+445e":   [wn.synset("electorate.n.01")],

	# endangered
	"U+445f":   [wn.synset("endangered.s.01")],

	# Epiphany
	"U+4460":   [wn.synset("epiphany.n.02")],

	# escalator, moving stairs
	"U+4461":   [wn.synset("escalator_clause.n.01"),
				wn.synset("escalator.n.02")],

	# Estonia
	"U+4462":   [wn.synset("estonia.n.01")],

	# experiment
	"U+4463":   [wn.synset("experiment.n.01")],

	# exploded
	"U+4464":   [wn.synset("exploded.s.01")],

	# facial hair
	"U+4465":   [wn.synset("facial_hair.n.01")],

	# farrier
	"U+4468":   [wn.synset("farrier.n.01")],

	# Father's Day
	"U+446a":   [wn.synset("father's_day.n.01")],

	# fee
	"U+446b":   [wn.synset("fee.n.02"),
				wn.synset("fee.n.01")],

	# fertilized
	"U+446c":   [wn.synset("inseminate.v.02"),
				wn.synset("fertilize.v.01"),
				wn.synset("fertilize.v.02")],

	# few, little
	"U+446d":   [wn.synset("little.a.02"),
				wn.synset("few.a.01")],

	# fever, temperature
	"U+446e":   [wn.synset("fever.n.01")],

	# financial support
	"U+446f":   [wn.synset("support.n.11")],

	# fingernail, nail
	"U+4470":   [wn.synset("nail.n.01")],

	# flu, influenza
	"U+4471":   [wn.synset("influenza.n.01")],

	# foreign
	"U+4472":   [wn.synset("foreign.a.02"),
				wn.synset("foreign.a.01")],

	# fort, fortress
	"U+4473":   [wn.synset("garrison.n.01"),
				wn.synset("fortress.n.01")],

	# fundamental, basic
	"U+4474":   [wn.synset("fundamental.s.02"),
				wn.synset("fundamental.s.03"),
				wn.synset("basic.a.01"),
				wn.synset("basic.s.04"),
				wn.synset("cardinal.s.01"),
				wn.synset("basic.s.03"),
				wn.synset("basic.s.02")],

	# fundamental law
	"U+4475":   [wn.synset("fundamental_law.n.01")],

	# fundamental rule
	"U+4477":   [wn.synset("constitution.n.04"),
				wn.synset("constitution.n.02"),
				wn.synset("fundamental_law.n.01")],

	# fundamentalism
	"U+4478":   [wn.synset("fundamentalism.n.01")],

	# fundamentalist
	"U+4479":   [wn.synset("fundamentalist.n.01")],

	# gallop
	"U+447b":   [wn.synset("gallop.n.01")],

	# gelding
	"U+447c":   [wn.synset("gelding.n.01")],

	# stallion, entire
	"U+447d":   [wn.synset("stallion.n.01")],

	# general
	"U+447f":   [wn.synset("general.a.01")],

	# girth, cinch
	"U+4480":   [wn.synset("cinch.n.02")],

	# glacier
	"U+4481":   [wn.synset("glacier.n.01")],

	# glow
	"U+4483":   [wn.synset("burn.v.02"),
				wn.synset("blaze.v.01"),
				wn.synset("glow.v.02"),
				wn.synset("glow.v.04"),
				wn.synset("glow.v.05"),
				wn.synset("glare.v.03"),
				wn.synset("glow.v.01"),
				wn.synset("shine.v.02"),
				wn.synset("blaze.v.04")],

	# groom
	"U+4484":   [wn.synset("stableman.n.01")],

	# horse brush, body brush
	"U+4485":   [wn.synset("currycomb.n.01")],

	# growl
	"U+4486":   [wn.synset("grumble.v.03"),
				wn.synset("snap.v.01")],

	# grunt
	"U+4487":   [wn.synset("grunt.v.01")],

	# hair drier, blow dryer
	"U+4488":   [wn.synset("hand_blower.n.01")],

	# hay
	"U+448c":   [wn.synset("hay.n.01")],

	# heal
	"U+448d":   [wn.synset("bring_around.v.02"),
				wn.synset("mend.v.02")],

	# Heaven, Kingdom of God
	"U+448f":   [wn.synset("eden.n.01")],

	# hibernation
	"U+4490":   [wn.synset("hibernation.n.01")],

	# hiss
	"U+4492":   [wn.synset("boo.v.01"),
				wn.synset("hiss.v.02"),
				wn.synset("hiss.v.03"),
				wn.synset("hiss.v.01")],

	# hitch, tie up, fix up
	"U+4493":   [wn.synset("tie_down.v.01")],

	# homosexual, lesbian, gay
	"U+4494":   [wn.synset("homosexual.a.01")],

	# hoof
	"U+4495":   [wn.synset("hoof.n.01")],

	# horse box, stall
	"U+4497":   [wn.synset("stall.n.01")],

	# horse cloth
	"U+4498":   [wn.synset("warp.n.04"),
				wn.synset("bard.n.02"),
				wn.synset("manta.n.01"),
				wn.synset("caparison.n.01")],

	# horse trailer, horsebox
	"U+449a":   [wn.synset("horsebox.n.01")],

	# trailer, container transport
	"U+449b":   [wn.synset("trailer.n.03"),
				wn.synset("preview.n.01"),
				wn.synset("dawdler.n.01"),
				wn.synset("trailer.n.04")],

	# horsehair
	"U+449d":   [wn.synset("horsehair.n.01"),
				wn.synset("horsehair.n.02")],

	# horseshoe
	"U+449e":   [wn.synset("horseshoe.n.02"),
				wn.synset("horseshoe.n.01")],

	# Hungary
	"U+44a1":   [wn.synset("hungary.n.01")],

	# hurry, rush, hurried, rushed
	"U+44a3":   [wn.synset("rush.v.01"),
				wn.synset("rush.v.03"),
				wn.synset("rush.v.02"),
				wn.synset("rush.v.05"),
				wn.synset("rush.v.04"),
				wn.synset("induce.v.03"),
				wn.synset("race.v.04"),
				wn.synset("travel_rapidly.v.01")],

	# hydrotherapy
	"U+44a4":   [wn.synset("hydropathy.n.01")],

	# ice field
	"U+44a5":   [wn.synset("ice_rink.n.01"),
				wn.synset("ice_field.n.01")],

	# iceberg
	"U+44a6":   [wn.synset("iceberg.n.01")],

	# independent
	"U+44a7":   [wn.synset("independent.a.01")],

	# invisible
	"U+44a8":   [wn.synset("invisible.a.01")],

	# jaguar
	"U+44a9":   [wn.synset("jaguar.n.01")],

	# kidney
	"U+44aa":   [wn.synset("kidney.n.01")],

	# knot
	"U+44ab":   [wn.synset("knot.n.04"),
				wn.synset("knot.n.03"),
				wn.synset("knot.n.02")],

	# Lent
	"U+44ac":   [wn.synset("lent.n.01")],

	# liberation
	"U+44ae":   [wn.synset("liberation.n.01")],

	# long time
	"U+44b0":   [wn.synset("long.r.01"),
				wn.synset("long_time.n.01")],

	# lower body
	"U+44b1":   [wn.synset("underbelly.n.02")],

	# sign of the cross
	"U+44b4":   [wn.synset("sign_of_the_cross.n.01")],

	# manure, fertilizer
	"U+44b6":   [wn.synset("manure.n.01"),
				wn.synset("fertilizer.n.01")],

	# mare
	"U+44b7":   [wn.synset("mare.n.01")],

	# medical treatment, medical care
	"U+44b8":   [wn.synset("treatment.n.02"),
				wn.synset("checkup.n.01"),
				wn.synset("medical_care.n.01")],

	# menstrual blood
	"U+44b9":   [wn.synset("menstruation.n.01"),
				wn.synset("menorrhea.n.01")],

	# metal craft
	"U+44ba":   [wn.synset("metalworking.n.01")],

	# mew, meow
	"U+44bb":   [wn.synset("meow.v.01"),
				wn.synset("mew.v.02")],

	# monarchy
	"U+44bc":   [wn.synset("monarchy.n.01")],

	# moo, bellow
	"U+44be":   [wn.synset("moo.v.01")],

	# Mother's Day
	"U+44bf":   [wn.synset("mother's_day.n.01")],

	# navel
	"U+44c3":   [wn.synset("navel.n.01")],

	# neigh, whinny
	"U+44c4":   [wn.synset("neigh.v.01")],

	# occupational therapy
	"U+44c5":   [wn.synset("occupational_therapy.n.01")],

	# paddock
	"U+44c8":   [wn.synset("paddock.n.01")],

	# passport
	"U+44cb":   [wn.synset("passport.n.02")],

	# pasture, enclosed field, put out to pasture
	"U+44cc":   [wn.synset("pasture.n.01")],

	# pavement, sidewalk
	"U+44ce":   [wn.synset("sidewalk.n.01")],

	# physiotherapy
	"U+44d0":   [wn.synset("physical_therapy.n.01")],

	# politician
	"U+44d3":   [wn.synset("politician.n.02")],

	# politics
	"U+44d5":   [wn.synset("politics.n.03")],

	# pram straps, safety harness
	"U+44d6":   [wn.synset("safety_belt.n.01")],

	# preceding, previous, former, earlier
	"U+44d7":   [wn.synset("former.s.03")],

	# prescription
	"U+44d8":   [wn.synset("prescription.n.03"),
				wn.synset("prescription.n.01"),
				wn.synset("prescription_drug.n.01"),
				wn.synset("prescription.n.04")],

	# president
	"U+44d9":   [wn.synset("president.n.03")],

	# prime minister
	"U+44da":   [wn.synset("chancellor.n.02")],

	# protected, saved, sheltered
	"U+44db":   [wn.synset("protected.a.01")],

	# prune
	"U+44de":   [wn.synset("prune.n.01")],

	# public transport
	"U+44e0":   [wn.synset("public_transport.n.01")],

	# purr
	"U+44e1":   [wn.synset("whizz.v.01")],

	# rack, single foot
	"U+44e2":   [wn.synset("extort.v.02"),
				wn.synset("torment.v.01"),
				wn.synset("rack.v.07"),
				wn.synset("rack.v.02"),
				wn.synset("rack.v.03"),
				wn.synset("single-foot.v.01"),
				wn.synset("rack.v.06"),
				wn.synset("scud.v.02"),
				wn.synset("rack.v.09"),
				wn.synset("rack.v.10"),
				wn.synset("rack.v.11")],

	# raisins, currants
	"U+44e3":   [wn.synset("raisin.n.01")],

	# rash
	"U+44e4":   [wn.synset("dermatitis.n.01"),
				wn.synset("rash.n.01"),
				wn.synset("rash.n.02")],

	# reclaim
	"U+44e5":   [wn.synset("reclaim.v.01"),
				wn.synset("drain.v.03"),
				wn.synset("reclaim.v.02"),
				wn.synset("domesticate.v.02"),
				wn.synset("reclaim.v.04"),
				wn.synset("reform.v.02")],

	# religious fanatic
	"U+44e6":   [wn.synset("fanatic.n.01")],

	# repair room
	"U+44e7":   [wn.synset("workshop.n.02")],

	# repair shop
	"U+44e9":   [wn.synset("repair_shop.n.01")],

	# republic
	"U+44ea":   [wn.synset("republic.n.02")],

	# respirator
	"U+44eb":   [wn.synset("respirator.n.01")],

	# responsibility
	"U+44ed":   [wn.synset("responsibility.n.03"),
				wn.synset("duty.n.01")],

	# responsible
	"U+44ee":   [wn.synset("creditworthy.s.01"),
				wn.synset("responsible.a.01"),
				wn.synset("responsible.s.02")],

	# Resurrection of Christ
	"U+44ef":   [wn.synset("resurrection.n.01")],

	# riding boots
	"U+44f0":   [wn.synset("riding_boot.n.01")],

	# riding school, manege
	"U+44f4":   [wn.synset("carousel.n.02"),
				wn.synset("riding_school.n.01"),
				wn.synset("carousel.n.01"),
				wn.synset("merry-go-round.n.01")],

	# roar
	"U+44f6":   [wn.synset("bellow.v.02"),
				wn.synset("howl.v.01"),
				wn.synset("thunder.v.02"),
				wn.synset("roar.v.06"),
				wn.synset("roar.v.04"),
				wn.synset("roar.v.01")],

	# royal
	"U+44f7":   [wn.synset("royal.a.01")],

	# royal family
	"U+44f8":   [wn.synset("royalty.n.02")],

	# saddle pad, saddle blanket
	"U+44f9":   [wn.synset("saddle_blanket.n.01")],

	# salvation
	"U+44fb":   [wn.synset("redemption.n.01")],

	# scabies
	"U+44fd":   [wn.synset("scabies.n.01")],

	# seat belt
	"U+44fe":   [wn.synset("seat_belt.n.01")],

	# sexual activity
	"U+4500":   [wn.synset("sexual_activity.n.01")],

	# shall, will
	"U+4505":   [wn.synset("desire.v.01"),
				wn.synset("bequeath.v.01"),
				wn.synset("will.v.02"),
				wn.synset("will.v.01"),
				wn.synset("volition.n.01"),
				wn.synset("wish.v.03"),
				wn.synset("wish.v.04")],

	# should, would
	"U+4506":   [wn.synset("need.v.03"),
				wn.synset("owe.v.03"),
				wn.synset("have.v.10")],

	# skin disease, eczema
	"U+4507":   [wn.synset("skin_disease.n.01"),
				wn.synset("eczema.n.01")],

	# skytrain, monorail
	"U+4508":   [wn.synset("monorail.n.01")],

	# slow, slowly
	"U+450a":   [wn.synset("slow.a.01")],

	# social
	"U+450b":   [wn.synset("social.a.03"),
				wn.synset("social.a.02"),
				wn.synset("social.a.01"),
				wn.synset("social.s.05"),
				wn.synset("social.s.04"),
				wn.synset("social.s.06")],

	# society
	"U+450c":   [wn.synset("society.n.01")],

	# somersault
	"U+450e":   [wn.synset("somersault.n.01")],

	# spark
	"U+450f":   [wn.synset("spark.n.06")],

	# speech therapy
	"U+4511":   [wn.synset("speech_therapy.n.01")],

	# spiritual awareness
	"U+4514":   [wn.synset("spiritualty.n.01"),
				wn.synset("spirituality.n.02")],

	# splint
	"U+4516":   [wn.synset("splint.n.02"),
				wn.synset("splint.n.01")],

	# sport fanatic
	"U+4517":   [wn.synset("sports_fan.n.01"),
				wn.synset("athlete.n.01")],

	# starvation
	"U+4518":   [wn.synset("starvation.n.02"),
				wn.synset("dearth.n.01"),
				wn.synset("starvation.n.01"),
				wn.synset("famine.n.02")],

	# still, continuing, ongoing, continuously, calm, peaceful, tranquil
	"U+451a":   [wn.synset("endlessly.r.02"),
				wn.synset("continuously.r.01")],

	# stirrup
	"U+451b":   [wn.synset("stirrup.n.01"),
				wn.synset("stapes.n.01")],

	# stomach flu
	"U+451c":   [wn.synset("gastroenteritis.n.01"),
				wn.synset("vomit.n.03")],

	# stomach illness
	"U+451e":   [wn.synset("stomachache.n.01")],

	# stretch
	"U+4522":   [wn.synset("unfold.v.03")],

	# striped
	"U+4523":   [wn.synset("striped.s.01")],

	# study
	"U+4524":   [wn.synset("study.v.03"),
				wn.synset("study.v.02"),
				wn.synset("analyze.v.01")],

	# stupid, dumb
	"U+4526":   [wn.synset("stupid.a.01")],

	# subway, metro, underground, tube
	"U+4527":   [wn.synset("metro.n.01")],

	# sunflower
	"U+4528":   [wn.synset("sunflower.n.01")],

	# swash
	"U+4529":   [wn.synset("swash.n.01")],

	# switch off, turn off
	"U+452a":   [wn.synset("switch_off.v.01")],

	# switch on, turn on
	"U+452b":   [wn.synset("switch_on.v.01")],

	# tadpole
	"U+452d":   [wn.synset("tadpole.n.01")],

	# tail lift, lift
	"U+452f":   [wn.synset("elevator.n.01")],

	# teamwork
	"U+4530":   [wn.synset("teamwork.n.01")],

	# teetotalism
	"U+4531":   [wn.synset("abstinence.n.01"),
				wn.synset("teetotaling.n.01")],

	# temporary
	"U+4533":   [wn.synset("irregular.s.07"),
				wn.synset("impermanent.a.01")],

	# towel
	"U+4539":   [wn.synset("towel.n.01")],

	# train station
	"U+453a":   [wn.synset("railway_station.n.01")],

	# tram
	"U+453b":   [wn.synset("streetcar.n.01")],

	# trolleybus
	"U+453e":   [wn.synset("trolleybus.n.01")],

	# tumble drier, tumble dryer
	"U+453f":   [wn.synset("tumble-dryer.n.01")],

	# tunnel, subway, underpass
	"U+4540":   [wn.synset("tunnel.n.01")],

	# underground station, subway station
	"U+4541":   [wn.synset("subway_station.n.01")],

	# unharness
	"U+4542":   [wn.synset("unharness.v.01")],

	# union
	"U+4544":   [wn.synset("union.n.07")],

	# vaginal discharge
	"U+4547":   [wn.synset("vaginal_discharge.n.01")],

	# walkway, footpath
	"U+4548":   [wn.synset("pathway.n.02"),
				wn.synset("walk.n.05")],

	# wart, papilloma
	"U+4549":   [wn.synset("papilloma.n.01")],

	# water bucket
	"U+454a":   [wn.synset("watering_can.n.01")],

	# venereal disease
	"U+454b":   [wn.synset("venereal_disease.n.01")],

	# venereal papilloma
	"U+454c":   [wn.synset("papilloma.n.01")],

	# wild strawberry
	"U+454e":   [wn.synset("wild_strawberry.n.01")],

	# visa
	"U+454f":   [wn.synset("visa.n.01")],

	# volte
	"U+4550":   [wn.synset("volta.n.02"),
				wn.synset("about-face.n.01"),
				wn.synset("about-face.n.02"),
				wn.synset("volta.n.01")],

	# woodcraft
	"U+4551":   [wn.synset("woodcraft.n.01"),
				wn.synset("woodcraft.n.02"),
				wn.synset("carpentry.n.01")],

	# achieve
	"U+4554":   [wn.synset("achieve.v.01")],

	# achievement
	"U+4555":   [wn.synset("accomplishment.n.01"),
				wn.synset("operation.n.07")],

	# addict
	"U+4557":   [wn.synset("drug_addict.n.01"),
				wn.synset("addict.n.01"),
				wn.synset("addict.n.02"),
				wn.synset("drug_user.n.01")],

	# addiction
	"U+4559":   [wn.synset("addiction.n.01"),
				wn.synset("addiction.n.03"),
				wn.synset("addiction.n.02")],

	# alcoholism, alcohol addiction
	"U+455b":   [wn.synset("alcoholism.n.01")],

	# alcohol abuse, alcohol addiction
	"U+455c":   [wn.synset("alcoholism.n.01")],

	# allergy, hypersensitivity
	"U+455e":   [wn.synset("allergy.n.01")],

	# reaction
	"U+455f":   [wn.synset("reaction.n.03"),
				wn.synset("reaction.n.05")],

	# baby bottle, feeding bottle
	"U+4561":   [wn.synset("bottle.n.03")],

	# bacterium
	"U+4564":   [wn.synset("bacteria.n.01")],

	# bend
	"U+4566":   [wn.synset("fold.v.01"),
				wn.synset("deflect.v.02"),
				wn.synset("flex.v.04"),
				wn.synset("flex.v.05"),
				wn.synset("crouch.v.01"),
				wn.synset("bend.v.01"),
				wn.synset("bend.v.02")],

	# bet
	"U+4567":   [wn.synset("stake.n.04")],

	# betting
	"U+4568":   [wn.synset("bet.v.01"),
				wn.synset("dissipated.s.02"),
				wn.synset("bet.v.02"),
				wn.synset("count.v.08")],

	# blacksmith
	"U+456a":   [wn.synset("blacksmith.n.01")],

	# bottle nipple, teat
	"U+456b":   [wn.synset("bottle.n.03"),
				wn.synset("bottle.n.02"),
				wn.synset("nipple.n.01")],

	# bottleneck, bottle opening
	"U+456c":   [wn.synset("bottleneck.n.02"),
				wn.synset("constriction.n.01")],

	# bruise, contusion, haematoma, dent
	"U+456e":   [wn.synset("incision.n.01"),
				wn.synset("dent.n.03"),
				wn.synset("bruise.n.01"),
				wn.synset("dent.n.01")],

	# bruised, dented
	"U+4570":   [wn.synset("bent.s.03"),
				wn.synset("bruise.v.04"),
				wn.synset("bruise.v.03"),
				wn.synset("bruise.v.01"),
				wn.synset("hurt.v.05")],

	# cease fire, armistice
	"U+4571":   [wn.synset("armistice.n.01")],

	# Ceres
	"U+4572":   [wn.synset("ceres.n.02"),
				wn.synset("ceres.n.01"),
				wn.synset("cere.n.01")],

	# dwarf planet
	"U+4573":   [wn.synset("planet.n.01")],

	# chance, risk
	"U+4574":   [wn.synset("risk.n.02")],

	# chive
	"U+4575":   [wn.synset("chives.n.01")],

	# dependency
	"U+4576":   [wn.synset("addiction.n.01"),
				wn.synset("colony.n.05"),
				wn.synset("dependence.n.01")],

	# dish rack
	"U+4577":   [wn.synset("dish_rack.n.01"),
				wn.synset("drainboard.n.01")],

	# domino
	"U+4579":   [wn.synset("domino.n.04"),
				wn.synset("domino.n.01"),
				wn.synset("domino.n.03"),
				wn.synset("dominoes.n.01"),
				wn.synset("domino.n.02")],

	# dribble
	"U+457b":   [wn.synset("drivel.v.01")],

	# drug addict
	"U+457c":   [wn.synset("drug_addict.n.01")],

	# drug addiction
	"U+457d":   [wn.synset("drug_addiction.n.01")],

	# drug dependency
	"U+457f":   [wn.synset("drug_addiction.n.01")],

	# Earth, Tellus
	"U+4580":   [wn.synset("earth.n.04"),
				wn.synset("earth.n.01")],

	# rock planet, terrestrial planet
	"U+4581":   [wn.synset("planet.n.01"),
				wn.synset("terrestrial_planet.n.01"),
				wn.synset("chasuble.n.01")],

	# eating disorder
	"U+4582":   [wn.synset("eating_disorder.n.01"),
				wn.synset("anorexia.n.01")],

	# mental illness
	"U+4583":   [wn.synset("mental_illness.n.01")],

	# Eris
	"U+4584":   [wn.synset("eris.n.01")],

	# examination, investigation
	"U+4585":   [wn.synset("examination.n.02"),
				wn.synset("examination.n.01"),
				wn.synset("probe.n.01"),
				wn.synset("examen.n.01"),
				wn.synset("examination.n.05"),
				wn.synset("investigation.n.02"),
				wn.synset("interrogation.n.03")],

	# examine
	"U+4586":   [wn.synset("examine.v.02")],

	# medical examination
	"U+4587":   [wn.synset("checkup.n.01")],

	# fail
	"U+4588":   [wn.synset("fail.v.02")],

	# failure
	"U+4589":   [wn.synset("stumble.v.04"),
				wn.synset("bankruptcy.n.02"),
				wn.synset("failure.n.01"),
				wn.synset("failure.n.04"),
				wn.synset("failure.n.05"),
				wn.synset("failure.n.07"),
				wn.synset("miss.v.07"),
				wn.synset("fail.v.02"),
				wn.synset("failure.n.02"),
				wn.synset("failure.n.03")],

	# fledgeling
	"U+458b":   [wn.synset("nestling.n.01"),
				wn.synset("newcomer.n.01"),
				wn.synset("fledgling.n.02")],

	# foal
	"U+458d":   [wn.synset("foal.n.01")],

	# football team
	"U+458f":   [wn.synset("football_team.n.01")],

	# galaxy
	"U+4590":   [wn.synset("galaxy.n.03")],

	# gamble
	"U+4591":   [wn.synset("gamble.v.01"),
				wn.synset("bet.v.01"),
				wn.synset("play.v.10"),
				wn.synset("gamble.v.02"),
				wn.synset("bet.v.02")],

	# gambler
	"U+4592":   [wn.synset("gambler.n.01"),
				wn.synset("gambler.n.02")],

	# gas planet
	"U+4594":   [wn.synset("planet.n.01")],

	# goldsmith
	"U+4595":   [wn.synset("goldsmith.n.01"),
				wn.synset("goldsmith.n.02")],

	# Good day
	"U+4596":   [wn.synset("adieu.n.01")],

	# Good morning
	"U+4599":   [wn.synset("good_morning.n.01")],

	# Good night
	"U+459b":   [wn.synset("good_night.n.01")],

	# guest room
	"U+459c":   [wn.synset("guestroom.n.01")],

	# impact
	"U+459f":   [wn.synset("impact.n.02")],

	# infect
	"U+45a0":   [wn.synset("infect.v.01"),
				wn.synset("infect.v.02"),
				wn.synset("infect.v.03"),
				wn.synset("infect.v.04")],

	# infection
	"U+45a1":   [wn.synset("infection.n.01")],

	# infected
	"U+45a3":   [wn.synset("infection.n.01"),
				wn.synset("septic.a.01")],

	# infectious, contagious
	"U+45a5":   [wn.synset("infectious.a.02")],

	# itch
	"U+45a7":   [wn.synset("urge.n.02"),
				wn.synset("tinea.n.01"),
				wn.synset("itch.n.03"),
				wn.synset("scabies.n.01")],

	# Jupiter
	"U+45a9":   [wn.synset("jupiter.n.01")],

	# kitten
	"U+45aa":   [wn.synset("kitten.n.01")],

	# leek
	"U+45ad":   [wn.synset("leek.n.01")],

	# lottery, game of chance
	"U+45af":   [wn.synset("lottery.n.02")],

	# magnifier, magnifying glass
	"U+45b0":   [wn.synset("hand_glass.n.02")],

	# Mars
	"U+45b2":   [wn.synset("mars.n.01")],

	# meeting room, auditorium
	"U+45b4":   [wn.synset("auditorium.n.01")],

	# Mercury
	"U+45b5":   [wn.synset("mercury.n.03")],

	# message, content
	"U+45b6":   [wn.synset("message.n.01")],

	# substance
	"U+45b7":   [wn.synset("kernel.n.03"),
				wn.synset("means.n.03"),
				wn.synset("message.n.02"),
				wn.synset("substance.n.01"),
				wn.synset("substance.n.07"),
				wn.synset("substance.n.04"),
				wn.synset("meaning.n.02")],

	# micro organism
	"U+45b8":   [wn.synset("microorganism.n.01")],

	# microscope
	"U+45b9":   [wn.synset("microscope.n.01")],

	# drug, mind altering drug
	"U+45bb":   [wn.synset("psychoactive_drug.n.01"),
				wn.synset("drug.n.01")],

	# money on a regular basis
	"U+45bc":   [wn.synset("pension.n.01")],

	# Neptune
	"U+45bd":   [wn.synset("neptune.n.02"),
				wn.synset("neptune.n.01")],

	# old age pension
	"U+45be":   [wn.synset("pension.n.01"),
				wn.synset("old-age_pension.n.01"),
				wn.synset("boarding_house.n.01")],

	# organism
	"U+45c0":   [wn.synset("organism.n.02"),
				wn.synset("organism.n.01")],

	# outcome, result
	"U+45c1":   [wn.synset("resultant_role.n.01"),
				wn.synset("solution.n.02"),
				wn.synset("consequence.n.01"),
				wn.synset("result.n.03")],

	# pacifier, dummy
	"U+45c2":   [wn.synset("comforter.n.04")],

	# pensioner
	"U+45c3":   [wn.synset("pensioner.n.01")],

	# Pluto
	"U+45c5":   [wn.synset("pluto.n.03")],

	# react
	"U+45c7":   [wn.synset("react.v.03"),
				wn.synset("react.v.02"),
				wn.synset("react.v.01")],

	# reception
	"U+45c9":   [wn.synset("reception.n.05"),
				wn.synset("reception.n.04"),
				wn.synset("reception.n.01"),
				wn.synset("reception.n.03"),
				wn.synset("reception.n.02")],

	# retirement pension
	"U+45cc":   [wn.synset("pension.n.01"),
				wn.synset("old-age_pension.n.01"),
				wn.synset("boarding_house.n.01")],

	# Saturn
	"U+45cd":   [wn.synset("saturn.n.01")],

	# scratch
	"U+45ce":   [wn.synset("scratch.n.10")],

	# senior citizen
	"U+45cf":   [wn.synset("retiree.n.01"),
				wn.synset("oldster.n.01"),
				wn.synset("old-age_pensioner.n.01"),
				wn.synset("old-timer.n.02"),
				wn.synset("patriarch.n.04"),
				wn.synset("old_man.n.01"),
				wn.synset("old_man.n.03")],

	# short message system, text message
	"U+45d0":   [wn.synset("verbatim.r.01"),
				wn.synset("literally.r.01"),
				wn.synset("literally.r.02")],

	# silversmith
	"U+45d1":   [wn.synset("silversmith.n.01")],

	# sink, basin
	"U+45d2":   [wn.synset("sink.n.01")],

	# tap
	"U+45d5":   [wn.synset("pat.n.01"),
				wn.synset("tap.n.08"),
				wn.synset("tap.n.06"),
				wn.synset("tap.n.05"),
				wn.synset("tap.n.04"),
				wn.synset("rap.n.02"),
				wn.synset("water_faucet.n.01"),
				wn.synset("wiretap.n.01")],

	# tile
	"U+45d7":   [wn.synset("tile.n.01")],

	# treatment
	"U+45d8":   [wn.synset("treatment.n.01"),
				wn.synset("treatment.n.02"),
				wn.synset("treatment.n.03"),
				wn.synset("discussion.n.01")],

	# Universe
	"U+45d9":   [wn.synset("universe.n.01")],

	# Uranus
	"U+45db":   [wn.synset("uranus.n.02")],

	# Venus
	"U+45dc":   [wn.synset("venus.n.01")],

	# viral infection
	"U+45de":   [wn.synset("viral_infection.n.01")],

	# aerial, antenna
	"U+45e1":   [wn.synset("antenna.n.01"),
				wn.synset("antenna.n.03")],

	# signal, broadcast, transmitting
	"U+45e2":   [wn.synset("signal.n.01")],

	# agenda
	"U+45e3":   [wn.synset("agenda.n.02")],

	# anchor
	"U+45e4":   [wn.synset("anchor.n.01")],

	# Bangladesh
	"U+45e6":   [wn.synset("bangladesh.n.01")],

	# barley
	"U+45e8":   [wn.synset("barley.n.01"),
				wn.synset("barley.n.02")],

	# berth, bunk
	"U+45e9":   [wn.synset("bunk.n.03")],

	# broadcast, transmit
	"U+45ec":   [wn.synset("broadcast.v.02"),
				wn.synset("convey.v.03"),
				wn.synset("transmit.v.04"),
				wn.synset("circulate.v.02"),
				wn.synset("air.v.03"),
				wn.synset("impart.v.03")],

	# buzzer
	"U+45ed":   [wn.synset("doorbell.n.01")],

	# camper van, RV
	"U+45ef":   [wn.synset("recreational_vehicle.n.01")],

	# canal
	"U+45f0":   [wn.synset("duct.n.01")],

	# channel
	"U+45f3":   [wn.synset("distribution_channel.n.01"),
				wn.synset("duct.n.01"),
				wn.synset("groove.n.01"),
				wn.synset("channel.n.01"),
				wn.synset("channel.n.02"),
				wn.synset("channel.n.05"),
				wn.synset("channel.n.04"),
				wn.synset("channel.n.07")],

	# Christmas song, carol
	"U+45f4":   [wn.synset("carol.n.01"),
				wn.synset("carol.n.02")],

	# satellite
	"U+45f6":   [wn.synset("satellite.n.01")],

	# compartment
	"U+45f7":   [wn.synset("compartment.n.02"),
				wn.synset("compartment.n.01")],

	# compass
	"U+45f8":   [wn.synset("scope.n.01"),
				wn.synset("compass.n.04"),
				wn.synset("compass.n.03"),
				wn.synset("compass.n.01")],

	# connector, interface box
	"U+45f9":   [wn.synset("connection.n.03")],

	# crater
	"U+45fb":   [wn.synset("crater.n.03")],

	# credit
	"U+45fd":   [wn.synset("credit.n.02")],

	# credit card
	"U+45fe":   [wn.synset("credit_card.n.01")],

	# crew, staff
	"U+4600":   [wn.synset("crew.n.04"),
				wn.synset("crew.n.01"),
				wn.synset("gang.n.03"),
				wn.synset("crowd.n.02")],

	# dependent
	"U+4602":   [wn.synset("dependent.a.03"),
				wn.synset("dependent.a.01"),
				wn.synset("pendent.s.01"),
				wn.synset("dependent.s.06"),
				wn.synset("subject.s.02"),
				wn.synset("dependent.s.02")],

	# digital memory, digital storage, RAM
	"U+4606":   [wn.synset("memory.n.04"),
				wn.synset("aries.n.03"),
				wn.synset("ram.n.04"),
				wn.synset("aries.n.01"),
				wn.synset("ram.n.05"),
				wn.synset("random-access_memory.n.01"),
				wn.synset("memory.n.03")],

	# dizzy
	"U+4609":   [wn.synset("dizzy.s.01"),
				wn.synset("airheaded.s.01")],

	# drop anchor
	"U+460a":   [wn.synset("anchor.v.02")],

	# DVD, movie disc
	"U+460b":   [wn.synset("videodisk.n.01")],

	# erupt
	"U+460d":   [wn.synset("erupt.v.05")],

	# eruption
	"U+460e":   [wn.synset("volcanic_eruption.n.01")],

	# exchanger
	"U+460f":   [wn.synset("exchanger.n.01")],

	# firework
	"U+4611":   [wn.synset("firework.n.01")],

	# French fries, chips
	"U+4613":   [wn.synset("french_fries.n.01")],

	# galley
	"U+4614":   [wn.synset("galley.n.04")],

	# GPS, satnav
	"U+4616":   [wn.synset("global_positioning_system.n.01")],

	# hammock
	"U+4618":   [wn.synset("hammock.n.02")],

	# hard rock
	"U+4619":   [wn.synset("rock_'n'_roll.n.01")],

	# inflammable, flammable
	"U+4628":   [wn.synset("flammable.s.01")],

	# invoice
	"U+4629":   [wn.synset("bill.n.02")],

	# jackfruit
	"U+462a":   [wn.synset("jackfruit.n.02")],

	# janitor, caretaker
	"U+462c":   [wn.synset("janitor.n.01"),
				wn.synset("caretaker.n.01"),
				wn.synset("caretaker.n.02")],

	# lava, magma
	"U+462d":   [wn.synset("lava.n.01")],

	# lee, shelter
	"U+462e":   [wn.synset("shelter.n.05")],

	# let fall, drop
	"U+462f":   [wn.synset("drop.v.02"),
				wn.synset("drop.v.03"),
				wn.synset("drop.v.01"),
				wn.synset("drop.v.06"),
				wn.synset("drop.v.07"),
				wn.synset("drop.v.17"),
				wn.synset("drop.v.05"),
				wn.synset("devolve.v.03"),
				wn.synset("drop.v.18"),
				wn.synset("drop.v.08"),
				wn.synset("fell.v.01"),
				wn.synset("drop.v.10"),
				wn.synset("flatten.v.03"),
				wn.synset("spend.v.02"),
				wn.synset("chicken_out.v.01"),
				wn.synset("shed.v.01"),
				wn.synset("dribble.v.02"),
				wn.synset("drop.v.23"),
				wn.synset("neglect.v.01"),
				wn.synset("dismiss.v.03"),
				wn.synset("blurt_out.v.01"),
				wn.synset("drop.v.20"),
				wn.synset("drop.v.21"),
				wn.synset("dangle.v.01"),
				wn.synset("sink.v.01")],

	# life jacket
	"U+4630":   [wn.synset("life_jacket.n.01")],

	# lower
	"U+4631":   [wn.synset("lower.v.01"),
				wn.synset("turn_down.v.05"),
				wn.synset("lower.v.04")],

	# lullaby
	"U+4632":   [wn.synset("lullaby.n.01")],

	# lunar eclipse
	"U+4634":   [wn.synset("lunar_eclipse.n.01")],

	# member
	"U+4636":   [wn.synset("member.n.01")],

	# memo, reminder note
	"U+4639":   [wn.synset("memo.n.01")],

	# rock music
	"U+463c":   [wn.synset("rock_'n'_roll.n.01")],

	# minutes
	"U+463d":   [wn.synset("minute.n.01"),
				wn.synset("hour.n.04"),
				wn.synset("minutes.n.01"),
				wn.synset("minute.n.05"),
				wn.synset("minute.n.04"),
				wn.synset("moment.n.01"),
				wn.synset("moment.n.02")],

	# misuse
	"U+463e":   [wn.synset("pervert.v.03"),
				wn.synset("misapply.v.01")],

	# MMS
	"U+4640":   [wn.synset("millimeter.n.01")],

	# monument, commemorative work
	"U+4641":   [wn.synset("memorial.n.03")],

	# movement, motion
	"U+4642":   [wn.synset("movement.n.04"),
				wn.synset("movement.n.05"),
				wn.synset("movement.n.10"),
				wn.synset("motion.n.03"),
				wn.synset("gesture.n.02"),
				wn.synset("motion.n.06")],

	# navigational sign
	"U+4644":   [wn.synset("beacon.n.03")],

	# oats
	"U+4645":   [wn.synset("oat.n.02")],

	# okra, lady's finger
	"U+4647":   [wn.synset("okra.n.02")],

	# overspend, buy over budget
	"U+4648":   [wn.synset("overspend.v.02"),
				wn.synset("spend.v.02"),
				wn.synset("overspend.v.01")],

	# plug in, connect
	"U+464a":   [wn.synset("associate.v.01"),
				wn.synset("get_in_touch.v.01"),
				wn.synset("connect.v.01"),
				wn.synset("connect.v.03"),
				wn.synset("connect.v.04"),
				wn.synset("plug_in.v.01"),
				wn.synset("connect.v.06")],

	# port
	"U+464b":   [wn.synset("larboard.n.01"),
				wn.synset("seaport.n.01"),
				wn.synset("pass.n.04"),
				wn.synset("interface.n.04"),
				wn.synset("port.n.01"),
				wn.synset("port.n.02"),
				wn.synset("port.n.03")],

	# portable
	"U+464c":   [wn.synset("portable.s.02"),
				wn.synset("portable.a.01")],

	# potato chip, chip, crisp
	"U+464d":   [wn.synset("chip.n.04")],

	# potty, chamber pot, bedpan
	"U+4650":   [wn.synset("chamberpot.n.01")],

	# quality
	"U+4651":   [wn.synset("quality.n.03"),
				wn.synset("quality.n.02"),
				wn.synset("quality.n.01"),
				wn.synset("timbre.n.01")],

	# receipt
	"U+4654":   [wn.synset("receipt.n.02"),
				wn.synset("reception.n.04")],

	# receiver, dish
	"U+4655":   [wn.synset("liquidator.n.02"),
				wn.synset("cup_of_tea.n.01"),
				wn.synset("receiver.n.06"),
				wn.synset("receiver.n.05"),
				wn.synset("recipient.n.01"),
				wn.synset("receiver.n.01"),
				wn.synset("dish.n.05"),
				wn.synset("dish.n.03"),
				wn.synset("dish.n.02"),
				wn.synset("dish.n.01"),
				wn.synset("telephone_receiver.n.01"),
				wn.synset("smasher.n.02")],

	# reef
	"U+4656":   [wn.synset("reef.v.01"),
				wn.synset("reef.v.03"),
				wn.synset("reef.v.02")],

	# rein
	"U+4657":   [wn.synset("rein.n.01"),
				wn.synset("rein.n.02")],

	# remote control
	"U+4658":   [wn.synset("remote_control.n.01")],

	# rent, lease, let, hire, charter
	"U+4659":   [wn.synset("rent.v.04"),
				wn.synset("lease.v.03"),
				wn.synset("rent.v.01")],

	# respiratory illness
	"U+465a":   [wn.synset("respiratory_disease.n.01"),
				wn.synset("asthma.n.01")],

	# road sign
	"U+465b":   [wn.synset("signpost.n.01"),
				wn.synset("fingerpost.n.01"),
				wn.synset("traffic_light.n.01")],

	# rye
	"U+465d":   [wn.synset("rye.n.01")],

	# school uniform
	"U+4663":   [wn.synset("uniform.n.01")],

	# sea captain, skipper
	"U+4664":   [wn.synset("captain.n.02"),
				wn.synset("master.n.07")],

	# sea chart
	"U+4665":   [wn.synset("chart.n.02")],

	# shadow, shade
	"U+4666":   [wn.synset("tad.n.01"),
				wn.synset("shadow.n.04"),
				wn.synset("shadow.n.07"),
				wn.synset("shadow.n.06"),
				wn.synset("shadow.n.01"),
				wn.synset("ghost.n.01"),
				wn.synset("apparition.n.03"),
				wn.synset("shadow.n.09"),
				wn.synset("trace.n.02"),
				wn.synset("shade.n.08"),
				wn.synset("nuance.n.01"),
				wn.synset("shade.n.05"),
				wn.synset("tail.n.05"),
				wn.synset("shade.n.01"),
				wn.synset("shade.n.03"),
				wn.synset("shade.n.02"),
				wn.synset("darkness.n.02")],

	# signal reception
	"U+466c":   [wn.synset("reception.n.04"),
				wn.synset("reception.n.01"),
				wn.synset("reception_room.n.01")],

	# singalong
	"U+4670":   [wn.synset("singalong.n.01")],

	# solar eclipse
	"U+4672":   [wn.synset("solar_eclipse.n.01")],

	# speech
	"U+4674":   [wn.synset("address.n.03")],

	# spending spree
	"U+4675":   [wn.synset("thriftlessness.n.01"),
				wn.synset("spending_spree.n.01")],

	# splurge
	"U+4677":   [wn.synset("splurge.v.01"),
				wn.synset("splurge.v.02")],

	# stand in, substitute, alternate
	"U+4679":   [wn.synset("substitute.n.01"),
				wn.synset("stand-in.n.01"),
				wn.synset("substitute.n.02"),
				wn.synset("deputy.n.02"),
				wn.synset("surrogate.n.01")],

	# starboard
	"U+467b":   [wn.synset("starboard.n.01")],

	# step, stair
	"U+467c":   [wn.synset("step.n.04")],

	# sun lounger, deck chair
	"U+467f":   [wn.synset("deck_chair.n.01")],

	# sunbathe
	"U+4680":   [wn.synset("sun.v.01")],

	# sunburn
	"U+4682":   [wn.synset("tan.n.01")],

	# suntan
	"U+4683":   [wn.synset("tan.n.01")],

	# sunglasses
	"U+4684":   [wn.synset("sunglasses.n.01")],

	# toilet chair, commode chair
	"U+4686":   [wn.synset("toilet.n.02")],

	# tourist
	"U+4687":   [wn.synset("tourist.n.01")],

	# TV programme, TV show, radio programme
	"U+4688":   [wn.synset("television_program.n.01"),
				wn.synset("show.n.01")],

	# USA
	"U+468c":   [wn.synset("united_states.n.01"),
				wn.synset("united_states_army.n.01")],

	# waiter, waitress
	"U+468d":   [wn.synset("waiter.n.01")],

	# water flower, water lily
	"U+468e":   [wn.synset("water_lily.n.01")],

	# weather satellite, spy satellite
	"U+468f":   [wn.synset("spy_satellite.n.01"),
				wn.synset("weather_satellite.n.01")],

	# wheat
	"U+4690":   [wn.synset("wheat.n.01")],

	# wireless connection, WiFi
	"U+4692":   [wn.synset("wireless_local_area_network.n.01")],

	# man made item, artefact, artifact, product
	"U+4693":   [wn.synset("merchandise.n.01"),
				wn.synset("intersection.n.04"),
				wn.synset("product.n.05"),
				wn.synset("product.n.04"),
				wn.synset("artifact.n.01"),
				wn.synset("product.n.03"),
				wn.synset("product.n.02")],

	# eagerness, keenness, willingness
	"U+4694":   [wn.synset("eagerness.n.01"),
				wn.synset("readiness.n.02"),
				wn.synset("willingness.n.01"),
				wn.synset("enthusiasm.n.01"),
				wn.synset("sharpness.n.05"),
				wn.synset("acuteness.n.02")],

	# agreed, in agreement, harmonious
	"U+4695":   [wn.synset("harmonious.s.04"),
				wn.synset("unresentful.a.01"),
				wn.synset("harmonious.s.03"),
				wn.synset("harmonious.s.02"),
				wn.synset("harmonious.a.01"),
				wn.synset("agreed.s.01")],

	# bathtub, bath, tub
	"U+4696":   [wn.synset("bathtub.n.01")],

	# government
	"U+4697":   [wn.synset("government.n.02"),
				wn.synset("government.n.01")],

	# in love
	"U+469a":   [wn.synset("enamored.s.01"),
				wn.synset("fall_in_love.v.01")],

	# niece or nephew
	"U+469b":   [wn.synset("grandchild.n.01"),
				wn.synset("nephew.n.01"),
				wn.synset("grandson.n.01")],

	# troublesome
	"U+469c":   [wn.synset("troublesome.s.01")],

	# cry out, call
	"U+469d":   [wn.synset("shout.v.02")],

	# jewelry, jewellery
	"U+469e":   [wn.synset("jewelry.n.01")],

	# boring, dull, depressing
	"U+46a0":   [wn.synset("boring.s.01")],

	# geyser
	"U+46a1":   [wn.synset("geyser.n.01")],

	# anthropologist
	"U+46a3":   [wn.synset("anthropologist.n.01")],

	# children's room
	"U+46a5":   [wn.synset("child's_room.n.01"),
				wn.synset("nursery.n.01")],

	# expose oneself indecently
	"U+46a6":   [wn.synset("produce.v.04")],

	# finished, complete, completed
	"U+46a7":   [wn.synset("complete.s.05")],

	# boss, supervisor
	"U+46a9":   [wn.synset("foreman.n.01")],

	# improvement
	"U+46aa":   [wn.synset("improvement.n.02"),
				wn.synset("improvement.n.03"),
				wn.synset("improvement.n.01")],

	# band, orchestra
	"U+46ab":   [wn.synset("dance_band.n.01"),
				wn.synset("band.n.02"),
				wn.synset("band.n.03"),
				wn.synset("band.n.04"),
				wn.synset("band.n.06"),
				wn.synset("band.n.07"),
				wn.synset("band.n.13"),
				wn.synset("band.n.12"),
				wn.synset("band.n.11"),
				wn.synset("band.n.10"),
				wn.synset("ring.n.08"),
				wn.synset("isthmus.n.02"),
				wn.synset("orchestra.n.02"),
				wn.synset("orchestra.n.01"),
				wn.synset("set.n.05")],

	# build, construct
	"U+46ad":   [wn.synset("construct.v.01"),
				wn.synset("manufacture.v.01"),
				wn.synset("construct.v.03")],

	# disgust
	"U+46b1":   [wn.synset("disgust.n.01")],

	# divided
	"U+46b2":   [wn.synset("divided.s.03")],

	# fountain
	"U+46b4":   [wn.synset("fountain.n.03"),
				wn.synset("fountain.n.01"),
				wn.synset("fountain.n.04")],

	# geographer
	"U+46b5":   [wn.synset("geographer.n.01")],

	# half, one half
	"U+46b6":   [wn.synset("one-half.n.01")],

	# heterosexual
	"U+46b8":   [wn.synset("heterosexual.a.01")],

	# hitchrack, hitching bar
	"U+46b9":   [wn.synset("hitchrack.n.01"),
				wn.synset("handbarrow.n.01")],

	# littleness, smallness
	"U+46ba":   [wn.synset("pettiness.n.03"),
				wn.synset("smallness.n.01"),
				wn.synset("smallness.n.02"),
				wn.synset("smallness.n.03")],

	# malodor, malodour, stench
	"U+46bb":   [wn.synset("malodor.n.01")],

	# physicist
	"U+46be":   [wn.synset("physicist.n.01")],

	# quarter, one quarter
	"U+46c0":   [wn.synset("one-fourth.n.01")],

	# coarse slang
	"U+46c3":   [wn.synset("ordinary.n.03")],

	# astarboard
	"U+46c5":   [wn.synset("starboard.n.01")],

	# army, regular army, ground forces
	"U+46c6":   [wn.synset("army.n.01")],

	# destroyed, ruined, demolished, deleted, erased, cancelled
	"U+46c7":   [wn.synset("destroyed.a.01"),
				wn.synset("off.a.03"),
				wn.synset("destroyed.s.02"),
				wn.synset("delete.v.01"),
				wn.synset("edit.v.04"),
				wn.synset("erase.v.02"),
				wn.synset("erase.v.03"),
				wn.synset("finished.s.05"),
				wn.synset("demolished.s.01"),
				wn.synset("done_for.s.02"),
				wn.synset("erase.v.01")],

	# access
	"U+46c8":   [wn.synset("access.v.02"),
				wn.synset("access.v.01")],

	# accessibility
	"U+46c9":   [wn.synset("handiness.n.02")],

	# accessible
	"U+46ca":   [wn.synset("approachable.a.02"),
				wn.synset("accessible.s.02"),
				wn.synset("accessible.a.01"),
				wn.synset("accessible.s.04"),
				wn.synset("accessible.s.03")],

	# adopt
	"U+46cb":   [wn.synset("adopt.v.05")],

	# adoption
	"U+46cc":   [wn.synset("adoption.n.02")],

	# adventure
	"U+46cd":   [wn.synset("adventure.n.01")],

	# thrilling, scary
	"U+46ce":   [wn.synset("chilling.s.01")],

	# adventurous
	"U+46d1":   [wn.synset("adventurous.a.01")],

	# Afghanistan
	"U+46d2":   [wn.synset("afghanistan.n.01")],

	# ajar
	"U+46d3":   [wn.synset("ajar.s.01")],

	# alcohol, ethanol
	"U+46d4":   [wn.synset("alcohol.n.01")],

	# applaud, clap
	"U+46d5":   [wn.synset("applaud.v.02"),
				wn.synset("applaud.v.01")],

	# applause, clapping
	"U+46d6":   [wn.synset("applause.n.01")],

	# armed
	"U+46d7":   [wn.synset("armed.a.01")],

	# weapon
	"U+46d8":   [wn.synset("weapon.n.01")],

	# Austria
	"U+46d9":   [wn.synset("austria.n.01")],

	# bandit, armed robber
	"U+46da":   [wn.synset("bandit.n.01")],

	# bazaar
	"U+46dc":   [wn.synset("bazaar.n.03")],

	# beggar
	"U+46dd":   [wn.synset("beggar.n.01")],

	# Belarus
	"U+46de":   [wn.synset("belarus.n.01")],

	# braid, plait, pigtail
	"U+46e0":   [wn.synset("braid.n.02"),
				wn.synset("pigtail.n.01"),
				wn.synset("braid.n.01"),
				wn.synset("pleat.n.01")],

	# Brazil
	"U+46e2":   [wn.synset("brazil.n.01")],

	# cheer
	"U+46e3":   [wn.synset("cheer.v.01"),
				wn.synset("cheer.v.05")],

	# cheering
	"U+46e4":   [wn.synset("cheering.n.01")],

	# cheerleader
	"U+46e5":   [wn.synset("cheerleader.n.02"),
				wn.synset("cheerleader.n.01")],

	# cheers
	"U+46e7":   [wn.synset("cheer.n.01"),
				wn.synset("cheerfulness.n.01")],

	# China
	"U+46e8":   [wn.synset("china.n.01")],

	# climate
	"U+46ea":   [wn.synset("climate.n.01")],

	# code, password
	"U+46ec":   [wn.synset("code.n.03")],

	# collection, pile, tussock
	"U+46ee":   [wn.synset("atomic_pile.n.01"),
				wn.synset("pile.n.03"),
				wn.synset("solicitation.n.02"),
				wn.synset("pile.n.01"),
				wn.synset("collection.n.02"),
				wn.synset("pile.n.07"),
				wn.synset("collection.n.04"),
				wn.synset("voltaic_pile.n.01"),
				wn.synset("collection.n.01"),
				wn.synset("batch.n.02"),
				wn.synset("pile.n.06"),
				wn.synset("down.n.05"),
				wn.synset("tuft.n.01")],

	# coup, hijack, takeover, coup d'etat, make a coup
	"U+46ef":   [wn.synset("hijack.n.01")],

	# theft
	"U+46f0":   [wn.synset("larceny.n.01")],

	# crime
	"U+46f1":   [wn.synset("crime.n.01")],

	# criminality, crime
	"U+46f2":   [wn.synset("crime.n.01"),
				wn.synset("crime.n.02"),
				wn.synset("criminalism.n.01")],

	# curiosity, curiousness, inquisitiveness
	"U+46f3":   [wn.synset("foreignness.n.01"),
				wn.synset("curio.n.01"),
				wn.synset("curiosity.n.01"),
				wn.synset("curiousness.n.01")],

	# curious, inquisitive
	"U+46f4":   [wn.synset("curious.a.02")],

	# Czech Republic
	"U+46f6":   [wn.synset("czech_republic.n.01")],

	# deflate, let out air
	"U+46f8":   [wn.synset("deflate.v.01"),
				wn.synset("deflate.v.03"),
				wn.synset("deflate.v.02"),
				wn.synset("deflate.v.05"),
				wn.synset("deflate.v.04"),
				wn.synset("deflate.v.06"),
				wn.synset("leak.v.03")],

	# detective, investigator
	"U+46fa":   [wn.synset("detective.n.01")],

	# disinfectant, antiseptic
	"U+46fb":   [wn.synset("antiseptic.n.01")],

	# drilling rig
	"U+46fd":   [wn.synset("drill_rig.n.01")],

	# each other, one another
	"U+46fe":   [wn.synset("together.r.01")],

	# encourage
	"U+46ff":   [wn.synset("encourage.v.03")],

	# encouragement
	"U+4700":   [wn.synset("encouragement.n.01"),
				wn.synset("encouragement.n.03"),
				wn.synset("boost.n.01")],

	# escape
	"U+4701":   [wn.synset("escape.n.06"),
				wn.synset("escape.n.07"),
				wn.synset("escape.n.04"),
				wn.synset("escape.n.05"),
				wn.synset("escape.n.02"),
				wn.synset("escape.n.01"),
				wn.synset("evasion.n.03")],

	# espionage, spying
	"U+4702":   [wn.synset("spying.n.02"),
				wn.synset("spying.n.01"),
				wn.synset("espionage.n.01"),
				wn.synset("detection.n.02")],

	# explore
	"U+4705":   [wn.synset("explore.v.04"),
				wn.synset("research.v.02"),
				wn.synset("explore.v.03"),
				wn.synset("explore.v.02")],

	# explorer, enquirer
	"U+4706":   [wn.synset("internet_explorer.n.01"),
				wn.synset("explorer.n.01"),
				wn.synset("inquirer.n.01")],

	# fart, wind
	"U+4708":   [wn.synset("fart.n.01")],

	# fatal, lethal
	"U+4709":   [wn.synset("fatal.a.01")],

	# fossil fuel, coal
	"U+470a":   [wn.synset("coal.n.01")],

	# France
	"U+470c":   [wn.synset("france.n.01")],

	# Friday
	"U+470e":   [wn.synset("friday.n.01")],

	# geothermal energy
	"U+470f":   [wn.synset("geothermal_energy.n.01")],

	# gravity, gravitation
	"U+4711":   [wn.synset("gravity.n.01")],

	# Greece
	"U+4712":   [wn.synset("greece.n.01")],

	# habit, custom
	"U+4713":   [wn.synset("habit.n.02"),
				wn.synset("habit.n.01")],

	# hiccup
	"U+4717":   [wn.synset("hiccup.n.01")],

	# hiding place, cache
	"U+471a":   [wn.synset("hiding_place.n.01")],

	# hide and seek
	"U+471b":   [wn.synset("hide-and-seek.n.01")],

	# hijacker, coup maker
	"U+471d":   [wn.synset("highjacker.n.01"),
				wn.synset("highjacker.n.02")],

	# hostage
	"U+471e":   [wn.synset("hostage.n.01")],

	# oppression, captivity, slavery
	"U+471f":   [wn.synset("enslavement.n.01"),
				wn.synset("bondage.n.02"),
				wn.synset("captivity.n.01"),
				wn.synset("slavery.n.02"),
				wn.synset("slavery.n.03"),
				wn.synset("oppression.n.01"),
				wn.synset("oppression.n.03"),
				wn.synset("oppression.n.02")],

	# hunter
	"U+4723":   [wn.synset("hunter.n.01")],

	# hydropower, hydro energy
	"U+4724":   [wn.synset("waterpower.n.01")],

	# identity card
	"U+4725":   [wn.synset("card.n.02")],

	# index, list of contents
	"U+4726":   [wn.synset("index.n.04"),
				wn.synset("index.n.05"),
				wn.synset("index.n.02"),
				wn.synset("exponent.n.03")],

	# India
	"U+4728":   [wn.synset("india.n.01")],

	# inflate
	"U+472a":   [wn.synset("inflate.v.04"),
				wn.synset("balloon.v.02"),
				wn.synset("inflate.v.01"),
				wn.synset("inflate.v.03"),
				wn.synset("inflate.v.02")],

	# invitation
	"U+472c":   [wn.synset("invitation.n.01")],

	# Iraq
	"U+472e":   [wn.synset("iraq.n.01")],

	# Italy
	"U+472f":   [wn.synset("italy.n.01")],

	# Japan
	"U+4731":   [wn.synset("japan.n.01")],

	# kidnap
	"U+4733":   [wn.synset("kidnap.v.01")],

	# kidnapper
	"U+4734":   [wn.synset("kidnapper.n.01")],

	# killer, murderer
	"U+4735":   [wn.synset("murderer.n.01")],

	# killing, murder, slaughter
	"U+4737":   [wn.synset("thrashing.n.01"),
				wn.synset("slaughter.n.01"),
				wn.synset("slaughter.n.03")],

	# knock, tap
	"U+4738":   [wn.synset("knock.v.02")],

	# knocking
	"U+4739":   [wn.synset("knock.n.01")],

	# load
	"U+473b":   [wn.synset("burden.n.01"),
				wn.synset("load.n.02"),
				wn.synset("load.n.01"),
				wn.synset("cargo.n.01")],

	# Monday
	"U+473e":   [wn.synset("monday.n.01")],

	# mummy
	"U+4743":   [wn.synset("mummy.n.02")],

	# nosy
	"U+4745":   [wn.synset("nosy.s.01")],

	# nuclear fuel
	"U+4746":   [wn.synset("nuclear_fuel.n.01")],

	# OK, alright
	"U+4748":   [wn.synset("all_right.s.01")],

	# Olympics, Olympic games
	"U+4749":   [wn.synset("olympic_games.n.01")],

	# oppressed, unfree
	"U+474a":   [wn.synset("unfree.a.01")],

	# passive
	"U+474b":   [wn.synset("passive.a.01")],

	# passivity
	"U+474c":   [wn.synset("passivity.n.01")],

	# Poland
	"U+474e":   [wn.synset("poland.n.01")],

	# Portugal
	"U+474f":   [wn.synset("portugal.n.01")],

	# power plant, power station
	"U+4750":   [wn.synset("power_station.n.01")],

	# precious, treasured
	"U+4752":   [wn.synset("precious.s.02"),
				wn.synset("valued.s.02"),
				wn.synset("cherished.s.01"),
				wn.synset("valuable.a.01"),
				wn.synset("cute.s.02")],

	# precious thing, treasure
	"U+4753":   [wn.synset("treasure.n.04")],

	# prison officer
	"U+4755":   [wn.synset("warder.n.01"),
				wn.synset("prison_guard.n.01")],

	# prisoner
	"U+4756":   [wn.synset("prisoner.n.01")],

	# pump
	"U+4757":   [wn.synset("pump.v.03")],

	# rag
	"U+4759":   [wn.synset("rag.n.01")],

	# rags
	"U+475b":   [wn.synset("rag.n.05"),
				wn.synset("ragtime.n.01"),
				wn.synset("rag.n.01"),
				wn.synset("rag.n.02"),
				wn.synset("tabloid.n.02")],

	# resign, quit
	"U+475c":   [wn.synset("leave_office.v.01")],

	# resignation
	"U+475d":   [wn.synset("resignation.n.01")],

	# retire
	"U+475f":   [wn.synset("adjourn.v.02"),
				wn.synset("go_to_bed.v.01")],

	# retirement
	"U+4760":   [wn.synset("retirement.n.02"),
				wn.synset("retirement.n.03"),
				wn.synset("retirement.n.01"),
				wn.synset("pension.n.01")],

	# retired
	"U+4761":   [wn.synset("retired.s.01")],

	# robot
	"U+4762":   [wn.synset("automaton.n.02")],

	# sacked, dismissed
	"U+4764":   [wn.synset("discharged.s.01")],

	# sacking, dismissal
	"U+4765":   [wn.synset("dismissal.n.02"),
				wn.synset("dismissal.n.03"),
				wn.synset("judgment_of_dismissal.n.01"),
				wn.synset("sacking.n.01"),
				wn.synset("dismissal.n.04")],

	# safari, wildlife expedition
	"U+4767":   [wn.synset("campaign.n.04")],

	# Saturday
	"U+4768":   [wn.synset("saturday.n.01")],

	# scoundrel, villain
	"U+4769":   [wn.synset("rogue.n.01"),
				wn.synset("villain.n.01"),
				wn.synset("villain.n.02")],

	# Sniff
	"U+476a":   [wn.synset("sniff.n.01")],

	# solar energy, solar power
	"U+476e":   [wn.synset("solar_energy.n.01")],

	# space travel, space voyage, space flight
	"U+476f":   [wn.synset("spaceflight.n.01")],

	# secret agent, spy
	"U+4770":   [wn.synset("secret_agent.n.01"),
				wn.synset("spy.n.01"),
				wn.synset("spy.n.02")],

	# steak
	"U+4771":   [wn.synset("steak.n.01")],

	# summary, abstract
	"U+4774":   [wn.synset("summary.n.01")],

	# Sunday
	"U+4775":   [wn.synset("sunday.n.01")],

	# supporters, cheering section
	"U+4776":   [wn.synset("following.n.01"),
				wn.synset("supporter.n.01"),
				wn.synset("garter.n.01"),
				wn.synset("patron.n.03"),
				wn.synset("athletic_supporter.n.01"),
				wn.synset("assistant.n.01"),
				wn.synset("fandom.n.01")],

	# Switzerland
	"U+4777":   [wn.synset("switzerland.n.01")],

	# technology
	"U+4778":   [wn.synset("technology.n.01")],

	# The Groke
	"U+4779":   [wn.synset("bugbear.n.02"),
				wn.synset("bogeyman.n.01"),
				wn.synset("bogey.n.01")],

	# Thursday
	"U+477a":   [wn.synset("thursday.n.01")],

	# tour, sightseeing
	"U+477c":   [wn.synset("tour.n.01")],

	# trap
	"U+477d":   [wn.synset("trap.v.04"),
				wn.synset("trap.v.01"),
				wn.synset("trap.v.02"),
				wn.synset("trap.v.03")],

	# hidden treasure, treasure trove
	"U+477e":   [wn.synset("tax.n.01"),
				wn.synset("treasure_trove.n.01"),
				wn.synset("treasure.n.04"),
				wn.synset("treasure_trove.n.02")],

	# tropical rain forest, jungle
	"U+477f":   [wn.synset("jungle.n.03"),
				wn.synset("hobo_camp.n.01"),
				wn.synset("jungle.n.01"),
				wn.synset("tropical_rain_forest.n.01")],

	# Tuesday
	"U+4780":   [wn.synset("tuesday.n.01")],

	# Turkey
	"U+4781":   [wn.synset("turkey.n.02")],

	# Ukraine
	"U+4783":   [wn.synset("ukraine.n.01")],

	# usually do, habitually do
	"U+4785":   [wn.synset("domesticate.v.01")],

	# vampire
	"U+4786":   [wn.synset("vampire.n.01")],

	# warn
	"U+4788":   [wn.synset("warn.v.01")],

	# warning
	"U+4789":   [wn.synset("warning.n.03"),
				wn.synset("warning.n.01"),
				wn.synset("admonition.n.01")],

	# Wednesday
	"U+478c":   [wn.synset("wednesday.n.01")],

	# werewolf
	"U+478e":   [wn.synset("werewolf.n.01")],

	# wind power, wind energy, wind farm
	"U+4790":   [wn.synset("wind_generation.n.01")],

	# zombie
	"U+4791":   [wn.synset("automaton.n.01"),
				wn.synset("zombi.n.01"),
				wn.synset("zombie.n.05")],

	# airforce, air force
	"U+4793":   [wn.synset("air_force.n.01")],

	# airport terminal
	"U+4794":   [wn.synset("air_terminal.n.01")],

	# alarm
	"U+4796":   [wn.synset("alarm.n.01"),
				wn.synset("alarm.n.03"),
				wn.synset("alarm.n.02")],

	# alternation
	"U+4797":   [wn.synset("alternation.n.01")],

	# alternating
	"U+4798":   [wn.synset("varied.a.01"),
				wn.synset("alternate.s.03"),
				wn.synset("alternating.a.01")],

	# alternating current, AC
	"U+4799":   [wn.synset("alternating_current.n.01")],

	# ammeter
	"U+479b":   [wn.synset("ammeter.n.01")],

	# electric current
	"U+479c":   [wn.synset("current.n.01")],

	# amplitude
	"U+479d":   [wn.synset("amplitude.n.01"),
				wn.synset("amplitude.n.03")],

	# Arabic
	"U+479e":   [wn.synset("arabic.n.01")],

	# Batman
	"U+479f":   [wn.synset("batman.n.01")],

	# bedbug, wall louse
	"U+47a0":   [wn.synset("bedbug.n.01")],

	# beige
	"U+47a2":   [wn.synset("beige.n.01")],

	# bird of prey, raptor
	"U+47a5":   [wn.synset("bird_of_prey.n.01")],

	# bless
	"U+47a6":   [wn.synset("bless.v.01")],

	# carve
	"U+47ab":   [wn.synset("carve.v.01")],

	# chase
	"U+47ac":   [wn.synset("chase.v.01")],

	# cipher
	"U+47ae":   [wn.synset("code.n.02"),
				wn.synset("zero.n.02"),
				wn.synset("nothing.n.01"),
				wn.synset("cipher.n.01"),
				wn.synset("cipher.n.04"),
				wn.synset("cipher.n.05")],

	# closed
	"U+47af":   [wn.synset("closed.a.04"),
				wn.synset("shut.a.01"),
				wn.synset("closed.a.01")],

	# clue
	"U+47b0":   [wn.synset("hint.n.02")],

	# direct current, DC
	"U+47b1":   [wn.synset("direct_current.n.01")],

	# Egypt
	"U+47b4":   [wn.synset("egypt.n.01")],

	# electric circuit
	"U+47b6":   [wn.synset("circuit.n.01")],

	# electric field
	"U+47b8":   [wn.synset("electric_field.n.01")],

	# impermeable material, insulation
	"U+47ba":   [wn.synset("insulation.n.03"),
				wn.synset("insulation.n.01"),
				wn.synset("insulating_material.n.01"),
				wn.synset("insulator.n.01")],

	# electro magnet
	"U+47bc":   [wn.synset("electromagnet.n.01")],

	# magnetism
	"U+47bd":   [wn.synset("magnetism.n.02")],

	# engagement
	"U+47be":   [wn.synset("betrothal.n.01"),
				wn.synset("battle.n.01"),
				wn.synset("engagement.n.06"),
				wn.synset("engagement.n.07"),
				wn.synset("engagement.n.05"),
				wn.synset("date.n.03"),
				wn.synset("employment.n.03")],

	# Estonian
	"U+47bf":   [wn.synset("estonian.n.01")],

	# fiance, groom to be
	"U+47c1":   [wn.synset("fiance.n.01")],

	# fiancee, bride to be
	"U+47c3":   [wn.synset("fiancee.n.01")],

	# fingerprint
	"U+47c4":   [wn.synset("fingermark.n.01"),
				wn.synset("fingerprint.n.02"),
				wn.synset("fingerprint.n.01")],

	# Finnish
	"U+47c5":   [wn.synset("finnish.n.01")],

	# fire extinguisher
	"U+47c7":   [wn.synset("fire_extinguisher.n.01")],

	# fire place, campfire site
	"U+47c8":   [wn.synset("fire.n.04")],

	# firecraft
	"U+47ca":   [wn.synset("campfire.n.01")],

	# first aid
	"U+47cb":   [wn.synset("first_aid.n.01")],

	# fish bone
	"U+47cc":   [wn.synset("skeletal_structure.n.01"),
				wn.synset("skeletal_system.n.01")],

	# flight deck, cockpit
	"U+47ce":   [wn.synset("cockpit.n.03"),
				wn.synset("flight_deck.n.01"),
				wn.synset("cockpit.n.01"),
				wn.synset("cockpit.n.02")],

	# footprint
	"U+47d0":   [wn.synset("footprint.n.01")],

	# French
	"U+47d1":   [wn.synset("french.n.01")],

	# frequency
	"U+47d2":   [wn.synset("frequency.n.01")],

	# front, front of a thing
	"U+47d3":   [wn.synset("front.n.03"),
				wn.synset("front.n.01"),
				wn.synset("front.n.07"),
				wn.synset("front.n.06"),
				wn.synset("front.n.04"),
				wn.synset("front.n.09"),
				wn.synset("movement.n.04"),
				wn.synset("battlefront.n.01"),
				wn.synset("front_man.n.01"),
				wn.synset("presence.n.02")],

	# fuse
	"U+47d4":   [wn.synset("fuse.n.01")],

	# fuselage
	"U+47d5":   [wn.synset("fuselage.n.01")],

	# gathering of scouts, jamboree
	"U+47d7":   [wn.synset("gala.n.01")],

	# hangar
	"U+47d9":   [wn.synset("airdock.n.01")],

	# head louse
	"U+47da":   [wn.synset("head_louse.n.01")],

	# headset
	"U+47db":   [wn.synset("headset.n.01")],

	# hike
	"U+47dd":   [wn.synset("subtract.v.01"),
				wn.synset("scale.v.04"),
				wn.synset("call_at.v.01"),
				wn.synset("layer.v.01"),
				wn.synset("hike.v.01"),
				wn.synset("hike.v.02")],

	# hiking
	"U+47de":   [wn.synset("hike.n.01")],

	# Icelandic
	"U+47df":   [wn.synset("icelandic.n.01")],

	# illustrate
	"U+47e0":   [wn.synset("illustrate.v.03")],

	# illustrated, illustrating
	"U+47e2":   [wn.synset("exemplify.v.02"),
				wn.synset("illustrate.v.02"),
				wn.synset("illustrate.v.03"),
				wn.synset("pictorial.a.01")],

	# illustration
	"U+47e3":   [wn.synset("illustration.n.04"),
				wn.synset("illustration.n.01"),
				wn.synset("exemplification.n.01")],

	# inhaler
	"U+47e6":   [wn.synset("inhaler.n.01")],

	# insomnia
	"U+47e7":   [wn.synset("insomnia.n.01")],

	# Iran
	"U+47e8":   [wn.synset("iran.n.01")],

	# Irish
	"U+47e9":   [wn.synset("irish.n.01"),
				wn.synset("irish.n.03"),
				wn.synset("irish.n.02")],

	# Italian
	"U+47ea":   [wn.synset("italian.n.02")],

	# ladybird
	"U+47eb":   [wn.synset("ladybug.n.01")],

	# landing gear
	"U+47ed":   [wn.synset("landing_gear.n.01")],

	# lifeline
	"U+47ee":   [wn.synset("lifeline.n.04"),
				wn.synset("line_of_life.n.01"),
				wn.synset("lifeline.n.03"),
				wn.synset("lifeline.n.02")],

	# magnet
	"U+47ef":   [wn.synset("magnet.n.01")],

	# magnetic field
	"U+47f1":   [wn.synset("magnetic_field.n.01")],

	# memory game, Kim's game
	"U+47f4":   [wn.synset("memory.n.04"),
				wn.synset("memory.n.05"),
				wn.synset("memory.n.02"),
				wn.synset("memory.n.03"),
				wn.synset("memory.n.01"),
				wn.synset("mind.n.02"),
				wn.synset("remembrance.n.01"),
				wn.synset("recollection.n.03"),
				wn.synset("recall.n.04")],

	# national
	"U+47f5":   [wn.synset("national.a.01"),
				wn.synset("national.a.02"),
				wn.synset("national.a.03"),
				wn.synset("national.a.06"),
				wn.synset("national.a.07"),
				wn.synset("national.s.04"),
				wn.synset("home.s.03")],

	# navigate airplane
	"U+47f8":   [wn.synset("voyage.v.01")],

	# Norwegian
	"U+47fa":   [wn.synset("norwegian.n.02")],

	# organization, organizing
	"U+47fb":   [wn.synset("mastermind.v.01"),
				wn.synset("organization.n.06"),
				wn.synset("unionize.v.02"),
				wn.synset("form.v.01"),
				wn.synset("organization.n.01"),
				wn.synset("organization.n.04"),
				wn.synset("organization.n.05"),
				wn.synset("constitution.n.02"),
				wn.synset("organize.v.02"),
				wn.synset("organize.v.05"),
				wn.synset("administration.n.02"),
				wn.synset("organize.v.04"),
				wn.synset("arrangement.n.03")],

	# orienteer, read map
	"U+47fc":   [wn.synset("adviser.n.01")],

	# map reading
	"U+47fe":   [wn.synset("orientation.n.03")],

	# breathing aid
	"U+4800":   [wn.synset("respirator.n.01"),
				wn.synset("breathing_device.n.01")],

	# perch
	"U+4801":   [wn.synset("perch.n.06")],

	# Persian
	"U+4803":   [wn.synset("persian.n.02"),
				wn.synset("irani.n.01")],

	# plant louse
	"U+4805":   [wn.synset("plant_louse.n.01"),
				wn.synset("ant_cow.n.01"),
				wn.synset("pale_chrysanthemum_aphid.n.01"),
				wn.synset("greenfly.n.01"),
				wn.synset("aphid.n.01")],

	# propeller, rotor
	"U+4806":   [wn.synset("propeller.n.01"),
				wn.synset("rotor.n.03")],

	# rowdy
	"U+4807":   [wn.synset("raucous.s.02")],

	# runway
	"U+4809":   [wn.synset("runway.n.04")],

	# Russian
	"U+480b":   [wn.synset("russian.n.02")],

	# scout
	"U+480f":   [wn.synset("browser.n.02"),
				wn.synset("scout.n.04"),
				wn.synset("lookout.n.01"),
				wn.synset("scout.n.02"),
				wn.synset("scout.n.03"),
				wn.synset("camper.n.01")],

	# scouting
	"U+4810":   [wn.synset("scouting.n.01")],

	# sleepy
	"U+4812":   [wn.synset("sleepy.s.01")],

	# Spain
	"U+4816":   [wn.synset("spain.n.01")],

	# Spanish, Castilian
	"U+4818":   [wn.synset("spanish.n.01")],

	# suicide
	"U+481b":   [wn.synset("suicide.n.02"),
				wn.synset("suicide.n.01")],

	# Superman
	"U+481c":   [wn.synset("acid.n.02"),
				wn.synset("hero.n.02"),
				wn.synset("demigod.n.01"),
				wn.synset("hero.n.01")],

	# Tarzan
	"U+481f":   [wn.synset("tarzan.n.01"),
				wn.synset("tarzan.n.02")],

	# tie whipping knot
	"U+4821":   [wn.synset("barrel.v.01")],

	# tracker
	"U+4823":   [wn.synset("tracker.n.01")],

	# turquoise
	"U+4824":   [wn.synset("greenish_blue.n.01")],

	# uniform
	"U+4825":   [wn.synset("uniform.n.01")],

	# wave length
	"U+4826":   [wn.synset("wavelength.n.01")],

	# veterinarian
	"U+4828":   [wn.synset("veterinarian.n.01")],

	# wind turbine
	"U+4829":   [wn.synset("wind_turbine.n.01")],

	# windmill
	"U+482a":   [wn.synset("windmill.n.02"),
				wn.synset("windmill.n.01")],

	# voltage
	"U+482b":   [wn.synset("voltage.n.01"),
				wn.synset("electric_potential.n.01")],

	# voltmeter
	"U+482c":   [wn.synset("voltmeter.n.01")],

	# wrap, wind
	"U+482d":   [wn.synset("wind.v.05"),
				wn.synset("weave.v.04"),
				wn.synset("scent.v.02"),
				wn.synset("wind.v.03"),
				wn.synset("wind.v.02"),
				wn.synset("wreathe.v.03"),
				wn.synset("hoist.v.01"),
				wn.synset("envelop.v.01"),
				wn.synset("wrap.v.04"),
				wn.synset("wrap.v.01")],

	# magnetic pole
	"U+482f":   [wn.synset("magnetic_pole.n.01"),
				wn.synset("pole.n.10")],

	# sleepless
	"U+4831":   [wn.synset("insomniac.s.01")],

	# Germany
	"U+4832":   [wn.synset("germany.n.01")],

	# German
	"U+4836":   [wn.synset("german.n.02")],

	# Thailand
	"U+4838":   [wn.synset("thailand.n.01")],

	# Romania
	"U+483c":   [wn.synset("romania.n.01")],

	# artillery
	"U+483f":   [wn.synset("artillery.n.02"),
				wn.synset("artillery.n.01")],

	# Romanian
	"U+4840":   [wn.synset("romanian.n.02")],

	# armoured force, tank force
	"U+4842":   [wn.synset("cavalry.n.02")],

	# Thai
	"U+4844":   [wn.synset("thai.n.02")],

	# intestine, bowel, gut
	"U+4846":   [wn.synset("intestine.n.01")],

	# bracelet
	"U+484b":   [wn.synset("bracelet.n.02")],

	# breastbone, sternum
	"U+484c":   [wn.synset("sternum.n.01")],

	# brooch
	"U+484d":   [wn.synset("brooch.n.01")],

	# cannula
	"U+484e":   [wn.synset("cannula.n.01")],

	# medical tube, catheter, cannula
	"U+484f":   [wn.synset("catheter.n.01"),
				wn.synset("cannula.n.01")],

	# catheter
	"U+4850":   [wn.synset("catheter.n.01")],

	# cardiovascular system
	"U+4852":   [wn.synset("circulatory_system.n.01")],

	# Christmas Eve
	"U+4855":   [wn.synset("christmas_eve.n.01")],

	# circulatory system
	"U+4856":   [wn.synset("circulatory_system.n.01")],

	# collarbone, clavicle
	"U+4857":   [wn.synset("clavicle.n.01")],

	# day before holiday
	"U+4858":   [wn.synset("eve.n.02"),
				wn.synset("eve.n.03")],

	# earring
	"U+485a":   [wn.synset("earring.n.01")],

	# endocrine system
	"U+485c":   [wn.synset("endocrine_system.n.01")],

	# gland
	"U+485d":   [wn.synset("gland.n.01")],

	# gastrointestinal system
	"U+485f":   [wn.synset("digestive_system.n.01")],

	# glitter
	"U+4860":   [wn.synset("glitter.n.02"),
				wn.synset("glitter.n.01")],

	# humerus, upper arm bone
	"U+4863":   [wn.synset("humerus.n.01")],

	# insulin
	"U+4866":   [wn.synset("insulin.n.01")],

	# large intestine
	"U+4869":   [wn.synset("large_intestine.n.01"),
				wn.synset("colon.n.01")],

	# liver
	"U+486a":   [wn.synset("liver.n.01")],

	# lower arm
	"U+486b":   [wn.synset("forearm.n.01")],

	# lower arm bone
	"U+486c":   [wn.synset("radio.n.03"),
				wn.synset("radio.n.01"),
				wn.synset("radius.n.04"),
				wn.synset("radius.n.03"),
				wn.synset("radius.n.02"),
				wn.synset("radius.n.01"),
				wn.synset("spoke.n.01"),
				wn.synset("radium.n.01"),
				wn.synset("radio_receiver.n.01")],

	# lung
	"U+486e":   [wn.synset("lung.n.01")],

	# lymph
	"U+486f":   [wn.synset("lymph.n.01")],

	# lymph node, lymph gland
	"U+4870":   [wn.synset("lymph_node.n.01")],

	# lymphatic system
	"U+4871":   [wn.synset("lymphatic_system.n.01")],

	# necklace
	"U+4873":   [wn.synset("necklace.n.01")],

	# nerve
	"U+4874":   [wn.synset("nerve.n.01")],

	# nervous system
	"U+4876":   [wn.synset("nervous_system.n.01")],

	# neuron
	"U+4877":   [wn.synset("nerve_cell.n.01")],

	# New Year
	"U+4878":   [wn.synset("new_year.n.01")],

	# New Year's eve, end of year
	"U+4879":   [wn.synset("new_year's_eve.n.01")],

	# oesophagus, gullet
	"U+487a":   [wn.synset("esophagus.n.01")],

	# pancreas
	"U+487c":   [wn.synset("pancreas.n.01")],

	# pierce
	"U+487d":   [wn.synset("pierce.v.05"),
				wn.synset("pierce.v.04")],

	# piercing
	"U+487e":   [wn.synset("pierce.v.05"),
				wn.synset("pierce.v.04"),
				wn.synset("pierce.v.01"),
				wn.synset("cutting.s.03"),
				wn.synset("pierce.v.03"),
				wn.synset("pierce.v.02"),
				wn.synset("acute.s.03"),
				wn.synset("perforation.n.03")],

	# rectum
	"U+487f":   [wn.synset("rectum.n.01")],

	# respiratory system
	"U+4881":   [wn.synset("respiratory_system.n.01")],

	# rib
	"U+4882":   [wn.synset("rib.n.02")],

	# salivary gland
	"U+4883":   [wn.synset("salivary_gland.n.01")],

	# sequin, spangle
	"U+4884":   [wn.synset("sequin.n.01")],

	# shoulder blade, scapula
	"U+4885":   [wn.synset("scapula.n.01")],

	# skull, cranium
	"U+4887":   [wn.synset("skull.n.01")],

	# small intestine
	"U+4888":   [wn.synset("small_intestine.n.01")],

	# snuff, kat, coca
	"U+4889":   [wn.synset("snuff.n.03")],

	# spleen
	"U+488a":   [wn.synset("spleen.n.01")],

	# stoma, medical hole
	"U+488b":   [wn.synset("stoma.n.02"),
				wn.synset("ostomy.n.01"),
				wn.synset("stoma.n.01"),
				wn.synset("fistula.n.02")],

	# tattoo, picture on skin
	"U+488c":   [wn.synset("tattoo.n.02")],

	# tea break, coffee break
	"U+488d":   [wn.synset("coffee_break.n.01")],

	# tendon
	"U+488e":   [wn.synset("tendon.n.01")],

	# trachea, wind pipe
	"U+488f":   [wn.synset("trachea.n.01")],

	# upper arm
	"U+4891":   [wn.synset("brachium.n.01")],

	# vascular system
	"U+4892":   [wn.synset("bloodstream.n.01"),
				wn.synset("vascular_system.n.01")],

	# work day
	"U+4893":   [wn.synset("workday.n.01")],

	# away, at a distance, off
	"U+4894":   [wn.synset("away.s.03"),
				wn.synset("off.s.02"),
				wn.synset("away.s.01"),
				wn.synset("off.s.04"),
				wn.synset("off.s.05"),
				wn.synset("path.n.02"),
				wn.synset("starting_signal.n.01"),
				wn.synset("off.r.03"),
				wn.synset("off.r.02"),
				wn.synset("away.a.02"),
				wn.synset("aside.r.06"),
				wn.synset("off.a.03"),
				wn.synset("aside.r.02"),
				wn.synset("off.a.01"),
				wn.synset("street.n.01"),
				wn.synset("road.n.01"),
				wn.synset("road.n.02"),
				wn.synset("come_away.v.02"),
				wn.synset("murder.v.01"),
				wn.synset("away.r.09"),
				wn.synset("away.r.08"),
				wn.synset("away.r.04"),
				wn.synset("away.r.07"),
				wn.synset("away.r.06"),
				wn.synset("away.r.01"),
				wn.synset("away.r.10"),
				wn.synset("away.r.02")],

	# limit, limitation, restriction, restrict, restrain, confine
	"U+4898":   [wn.synset("restrict.v.03")],

	# farness, remoteness, farawayness
	"U+489b":   [wn.synset("farness.n.01"),
				wn.synset("aloofness.n.02")],

	# fatness, thickness
	"U+489c":   [wn.synset("thickness.n.04"),
				wn.synset("thickness.n.01"),
				wn.synset("thickness.n.02"),
				wn.synset("thickness.n.03"),
				wn.synset("fatness.n.01")],

	# actor
	"U+48ab":   [wn.synset("actor.n.01")],

	# altruism, selflessness
	"U+48ae":   [wn.synset("altruism.n.01"),
				wn.synset("selflessness.n.02")],

	# artist
	"U+48b2":   [wn.synset("artist.n.01")],

	# baguette
	"U+48b4":   [wn.synset("baguet.n.01")],

	# baking powder
	"U+48b5":   [wn.synset("baking_powder.n.01")],

	# ballot, voting slip
	"U+48b6":   [wn.synset("vote.n.01"),
				wn.synset("ballot.n.01")],

	# bird nest, birdnest
	"U+48b8":   [wn.synset("bird's_nest.n.01")],

	# birdhouse, house for bird
	"U+48b9":   [wn.synset("birdhouse.n.01")],

	# blog, web blog
	"U+48ba":   [wn.synset("web_log.n.01")],

	# boar
	"U+48bb":   [wn.synset("wild_boar.n.01"),
				wn.synset("boar.n.02")],

	# boyfriend
	"U+48bc":   [wn.synset("boyfriend.n.01")],

	# bread knife
	"U+48be":   [wn.synset("bread_knife.n.01")],

	# brother in law
	"U+48c1":   [wn.synset("brother-in-law.n.01")],

	# cactus
	"U+48c6":   [wn.synset("cactus.n.01")],

	# cheat
	"U+48c7":   [wn.synset("cheat.v.02")],

	# cheating
	"U+48c8":   [wn.synset("shoddy.n.01"),
				wn.synset("cheat.n.05")],

	# chick
	"U+48ca":   [wn.synset("dame.n.01"),
				wn.synset("chick.n.01"),
				wn.synset("chicken.n.02")],

	# classmate
	"U+48cb":   [wn.synset("schoolmate.n.01")],

	# client, customer
	"U+48cc":   [wn.synset("customer.n.01")],

	# colleague
	"U+48cd":   [wn.synset("colleague.n.01")],

	# cowshed
	"U+48d0":   [wn.synset("cowbarn.n.01")],

	# daughter in law
	"U+48d1":   [wn.synset("daughter-in-law.n.01")],

	# definition
	"U+48d2":   [wn.synset("definition.n.01"),
				wn.synset("definition.n.02")],

	# explanation, reason
	"U+48d3":   [wn.synset("rationality.n.01"),
				wn.synset("explanation.n.03")],

	# dice, die
	"U+48d4":   [wn.synset("die.n.01"),
				wn.synset("die.n.02"),
				wn.synset("die.n.03")],

	# dichotomy, duality
	"U+48d5":   [wn.synset("duality.n.02"),
				wn.synset("duality.n.03"),
				wn.synset("dichotomy.n.01")],

	# dictator
	"U+48d6":   [wn.synset("dictator.n.02"),
				wn.synset("dictator.n.01"),
				wn.synset("authoritarian.n.01")],

	# dictatorship
	"U+48d8":   [wn.synset("dictatorship.n.01")],

	# dilemma
	"U+48d9":   [wn.synset("dilemma.n.01")],

	# dollhouse, doll house
	"U+48db":   [wn.synset("dollhouse.n.02"),
				wn.synset("dollhouse.n.01")],

	# domestic science, home economics
	"U+48dd":   [wn.synset("home_economics.n.01")],

	# dormouse
	"U+48de":   [wn.synset("dormouse.n.01")],

	# employed, working
	"U+48df":   [wn.synset("employed.a.01"),
				wn.synset("working.s.01"),
				wn.synset("running.s.06"),
				wn.synset("working.s.05"),
				wn.synset("working.s.02"),
				wn.synset("employed.s.02"),
				wn.synset("working.s.03")],

	# employee
	"U+48e0":   [wn.synset("employee.n.01")],

	# equilateral triangle
	"U+48e2":   [wn.synset("equilateral_triangle.n.01"),
				wn.synset("triangle.n.01")],

	# ewe
	"U+48e3":   [wn.synset("ewe.n.01"),
				wn.synset("thank.v.01"),
				wn.synset("ewe.n.03"),
				wn.synset("ewe.n.02")],

	# excavator, digger, power shovel
	"U+48e5":   [wn.synset("power_shovel.n.01"),
				wn.synset("excavator.n.01"),
				wn.synset("digger.n.01")],

	# experience
	"U+48e6":   [wn.synset("experience.n.01")],

	# farmhouse
	"U+48e7":   [wn.synset("farmhouse.n.01")],

	# father in law
	"U+48e9":   [wn.synset("father-in-law.n.01")],

	# female friend
	"U+48ea":   [wn.synset("acquaintance.n.03")],

	# girlfriend
	"U+48ee":   [wn.synset("girlfriend.n.02")],

	# grandchild
	"U+48ef":   [wn.synset("grandchild.n.01")],

	# graze
	"U+48f1":   [wn.synset("crop.v.04")],

	# handcraft, craft
	"U+48f3":   [wn.synset("craft.v.01"),
				wn.synset("handcraft.v.01")],

	# handmade figure, handicraft
	"U+48f4":   [wn.synset("handicraft.n.02"),
				wn.synset("handicraft.n.01")],

	# hen
	"U+48f5":   [wn.synset("hen.n.01")],

	# henhouse, chicken coop
	"U+48f6":   [wn.synset("chicken_coop.n.01")],

	# housekeep, housework
	"U+48f8":   [wn.synset("housework.n.01"),
				wn.synset("housekeep.v.01")],

	# housekeeper
	"U+48f9":   [wn.synset("housekeeper.n.01")],

	# layer, level
	"U+48fb":   [wn.synset("layer.n.02")],

	# icing
	"U+48fd":   [wn.synset("frosting.n.01"),
				wn.synset("frost.n.03"),
				wn.synset("icing.n.03")],

	# powdered sugar, icing sugar
	"U+48fe":   [wn.synset("powdered_sugar.n.01"),
				wn.synset("icing_sugar.n.01")],

	# influence, affect
	"U+4900":   [wn.synset("affect.v.01")],

	# influenced, affected
	"U+4901":   [wn.synset("affected.a.02"),
				wn.synset("influence.v.01"),
				wn.synset("affected.a.01"),
				wn.synset("charm.v.04"),
				wn.synset("determine.v.02"),
				wn.synset("moved.a.01")],

	# inspiration
	"U+4902":   [wn.synset("inspiration.n.03")],

	# inspire
	"U+4903":   [wn.synset("inspire.v.02")],

	# inspired
	"U+4904":   [wn.synset("divine.s.06")],

	# interrupt
	"U+4905":   [wn.synset("interrupt.v.03")],

	# interruption
	"U+4906":   [wn.synset("interruption.n.02"),
				wn.synset("pause.n.01"),
				wn.synset("break.n.13")],

	# intuition
	"U+4908":   [wn.synset("intuition.n.01"),
				wn.synset("intuition.n.02")],

	# isosceles triangle
	"U+490a":   [wn.synset("triangle.n.01"),
				wn.synset("isosceles_triangle.n.01")],

	# jobcentre, job centre
	"U+490c":   [wn.synset("jobcentre.n.01")],

	# knight
	"U+490d":   [wn.synset("knight.n.01"),
				wn.synset("knight.n.02")],

	# lawn mower, mower
	"U+490e":   [wn.synset("lawn_mower.n.01")],

	# long for, yearn
	"U+490f":   [wn.synset("hanker.v.01")],

	# longing, yearning
	"U+4910":   [wn.synset("longing.n.01")],

	# male friend
	"U+4914":   [wn.synset("acquaintance.n.03")],

	# married
	"U+4915":   [wn.synset("marital.a.01"),
				wn.synset("married.a.01")],

	# measuring cup
	"U+4916":   [wn.synset("measuring_cup.n.01"),
				wn.synset("measuring_stick.n.01")],

	# mislead
	"U+4918":   [wn.synset("misinform.v.01")],

	# molasses, dark syrup, black treacle
	"U+4919":   [wn.synset("molasses.n.01")],

	# mother in law
	"U+491a":   [wn.synset("mother-in-law.n.01")],

	# motivate
	"U+491b":   [wn.synset("motivate.v.01")],

	# motivation
	"U+491c":   [wn.synset("motivation.n.01"),
				wn.synset("motivation.n.03"),
				wn.synset("motivation.n.02")],

	# motivated
	"U+491d":   [wn.synset("motivated.a.01")],

	# patient, enduring
	"U+491f":   [wn.synset("patient.n.01")],

	# piggery
	"U+4920":   [wn.synset("piggery.n.01")],

	# piglet
	"U+4922":   [wn.synset("piglet.n.01")],

	# playhouse, play house
	"U+4923":   [wn.synset("playhouse.n.01")],

	# principal, headteacher
	"U+4924":   [wn.synset("principal.n.06"),
				wn.synset("principal.n.04"),
				wn.synset("principal.n.05"),
				wn.synset("principal.n.02"),
				wn.synset("principal.n.01"),
				wn.synset("star.n.04")],

	# prize, award, trophy
	"U+4925":   [wn.synset("trophy.n.02")],

	# publication
	"U+4926":   [wn.synset("issue.n.11"),
				wn.synset("publication.n.01")],

	# publish
	"U+4927":   [wn.synset("publish.v.02")],

	# publisher
	"U+4928":   [wn.synset("publisher.n.01")],

	# ram
	"U+492a":   [wn.synset("ram.n.05"),
				wn.synset("random-access_memory.n.01"),
				wn.synset("aries.n.03"),
				wn.synset("ram.n.04"),
				wn.synset("aries.n.01")],

	# reality
	"U+492b":   [wn.synset("reality.n.02")],

	# rescue
	"U+492c":   [wn.synset("rescue.n.01")],

	# right triangle
	"U+492d":   [wn.synset("triangle.n.01"),
				wn.synset("right_triangle.n.01")],

	# salesperson, shop owner
	"U+492e":   [wn.synset("salesperson.n.01"),
				wn.synset("salesman.n.01"),
				wn.synset("seller.n.01")],

	# scalene triangle
	"U+492f":   [wn.synset("triangle.n.01"),
				wn.synset("scalene_triangle.n.01")],

	# sceptical, skeptical, questioning
	"U+4931":   [wn.synset("questioning.s.01"),
				wn.synset("disbelieving.s.01"),
				wn.synset("doubting.s.01"),
				wn.synset("inquisitive.s.01")],

	# scepticism, skepticism
	"U+4932":   [wn.synset("agnosticism.n.02")],

	# schoolmate
	"U+4934":   [wn.synset("schoolmate.n.01")],

	# sculpture
	"U+4935":   [wn.synset("sculpture.n.02"),
				wn.synset("sculpture.n.01")],

	# self raising flour
	"U+4937":   [wn.synset("self-rising_flour.n.01")],

	# set square
	"U+4938":   [wn.synset("set_square.n.01")],

	# sheath
	"U+4939":   [wn.synset("sheath.n.01"),
				wn.synset("sheath.n.02"),
				wn.synset("cocktail_dress.n.01")],

	# sister in law
	"U+493b":   [wn.synset("sister-in-law.n.01")],

	# slaughterer
	"U+493c":   [wn.synset("butcher.n.03")],

	# slaughterhouse, abattoir
	"U+493e":   [wn.synset("abattoir.n.01")],

	# smartphone, digital phone
	"U+4940":   [wn.synset("cellular_telephone.n.01")],

	# son in law
	"U+4941":   [wn.synset("son-in-law.n.01")],

	# sow
	"U+4942":   [wn.synset("sow.n.01")],

	# speaker, lecturer
	"U+4943":   [wn.synset("speaker.n.01")],

	# spider web, cobweb, orb web
	"U+4945":   [wn.synset("cobweb.n.03"),
				wn.synset("cobweb.n.02"),
				wn.synset("cobweb.n.01"),
				wn.synset("spider_web.n.01"),
				wn.synset("spider_web.n.02"),
				wn.synset("orb_web.n.01")],

	# stepdaughter
	"U+4947":   [wn.synset("stepdaughter.n.01")],

	# stepparent, step parent
	"U+4949":   [wn.synset("stepparent.n.01")],

	# stepson
	"U+494a":   [wn.synset("stepson.n.01")],

	# strategy
	"U+494b":   [wn.synset("tactic.n.01"),
				wn.synset("scheme.n.01"),
				wn.synset("strategy.n.02")],

	# sugar lump, cube
	"U+494c":   [wn.synset("cube.n.03"),
				wn.synset("cube.n.01"),
				wn.synset("cube.n.04"),
				wn.synset("block.n.03"),
				wn.synset("cube.n.05")],

	# surrounded, encircled, surrounding
	"U+494d":   [wn.synset("surrounded.s.01"),
				wn.synset("encompassing.s.02")],

	# synthetic speech, text to speech, tts
	"U+4950":   [wn.synset("micronesia.n.01"),
				wn.synset("terrestrial_time.n.01"),
				wn.synset("palau.n.01")],

	# taco, taco shell
	"U+4951":   [wn.synset("taco.n.02"),
				wn.synset("greaser.n.01")],

	# unemployed
	"U+4952":   [wn.synset("unemployed.a.01")],

	# voluntary
	"U+4953":   [wn.synset("voluntary.a.01"),
				wn.synset("voluntary.a.02")],

	# volunteering
	"U+4954":   [wn.synset("volunteer.v.02"),
				wn.synset("volunteer.v.03"),
				wn.synset("volunteer.v.01")],

	# yeast
	"U+4958":   [wn.synset("yeast.n.02"),
				wn.synset("yeast.n.01")],

	# possible
	"U+4959":   [wn.synset("potential.a.01")],

	# age
	"U+495a":   [wn.synset("age.n.01")],

	# asteroid
	"U+495b":   [wn.synset("asteroid.n.01")],

	# balance, sense of balance, poise, standing)
	"U+495d":   [wn.synset("poise.v.03"),
				wn.synset("brace.v.01"),
				wn.synset("balance.v.02"),
				wn.synset("poise.v.01"),
				wn.synset("balance.v.01"),
				wn.synset("poise.v.04"),
				wn.synset("balance.v.04")],

	# birch
	"U+4962":   [wn.synset("birch.n.02"),
				wn.synset("birch.n.03"),
				wn.synset("birch.n.01")],

	# birdfeeder, bird table
	"U+4963":   [wn.synset("bird_feeder.n.01")],

	# cardboard, paperboard
	"U+4964":   [wn.synset("cardboard.n.01"),
				wn.synset("paperboard.n.01")],

	# chess
	"U+4966":   [wn.synset("chess.n.01"),
				wn.synset("chess.n.02"),
				wn.synset("check.n.13")],

	# collar
	"U+4968":   [wn.synset("collar.n.06")],

	# cornea
	"U+4969":   [wn.synset("cornea.n.01")],

	# covered, hidden
	"U+496a":   [wn.synset("hidden.s.02"),
				wn.synset("hidden.s.03"),
				wn.synset("covered.a.01"),
				wn.synset("concealed.s.01")],

	# dairy
	"U+496b":   [wn.synset("dairy.n.01")],

	# darkness
	"U+496c":   [wn.synset("dark.n.01")],

	# den, lair
	"U+496d":   [wn.synset("hideout.n.01"),
				wn.synset("bullet.n.01"),
				wn.synset("lair.n.01"),
				wn.synset("burrow.n.01"),
				wn.synset("den.n.03"),
				wn.synset("den.n.04")],

	# dense, thick, compact, tight, jammed
	"U+496e":   [wn.synset("compact.a.01"),
				wn.synset("thick.a.01"),
				wn.synset("thick.a.03")],

	# density, denseness, compactness, tightness, concentration
	"U+496f":   [wn.synset("concentration.n.01"),
				wn.synset("concentration.n.05")],

	# disagree, discord, disaccord
	"U+4971":   [wn.synset("disagree.v.02"),
				wn.synset("disagree.v.01")],

	# disagreement, discord
	"U+4972":   [wn.synset("disagreement.n.01")],

	# discordant
	"U+4973":   [wn.synset("discordant.s.02"),
				wn.synset("discordant.a.01")],

	# diver
	"U+4974":   [wn.synset("diver.n.01"),
				wn.synset("diver.n.02"),
				wn.synset("loon.n.02")],

	# doorway, gate
	"U+4976":   [wn.synset("gate.n.01")],

	# dove
	"U+4978":   [wn.synset("dove.n.02"),
				wn.synset("dove.n.01"),
				wn.synset("columba.n.01"),
				wn.synset("dove.n.05"),
				wn.synset("squab.n.01"),
				wn.synset("pigeon.n.01")],

	# dust storm, duster, sirocco
	"U+497a":   [wn.synset("duster.n.04"),
				wn.synset("duster.n.02"),
				wn.synset("dustcloth.n.01"),
				wn.synset("dust_storm.n.01")],

	# eastward
	"U+497b":   [wn.synset("eastbound.s.01")],

	# equipment, gear
	"U+497c":   [wn.synset("equipment.n.01")],

	# fable, allegory, parable
	"U+497d":   [wn.synset("fabrication.n.01"),
				wn.synset("fable.n.02"),
				wn.synset("legend.n.01"),
				wn.synset("simile.n.01"),
				wn.synset("emblem.n.02"),
				wn.synset("allegory.n.03"),
				wn.synset("parable.n.02")],

	# fairy tale
	"U+497e":   [wn.synset("fairytale.n.01"),
				wn.synset("fairytale.n.02"),
				wn.synset("saga.n.01")],

	# fiber, fibre, fibril, filament, strand
	"U+4980":   [wn.synset("fiber.n.01")],

	# folk tale, legend
	"U+4981":   [wn.synset("legend.n.01"),
				wn.synset("caption.n.03")],

	# free of charge, gratis, for free
	"U+4984":   [wn.synset("complimentary.s.02")],

	# give birth
	"U+4986":   [wn.synset("give_birth.v.02"),
				wn.synset("food.n.01"),
				wn.synset("give_birth.v.01")],

	# habitation, dwelling place, site
	"U+4988":   [wn.synset("dwelling.n.01"),
				wn.synset("site.n.02"),
				wn.synset("habitation.n.01"),
				wn.synset("site.n.01"),
				wn.synset("web_site.n.01"),
				wn.synset("inhabitancy.n.01")],

	# hearing, audition, auditory sense
	"U+498c":   [wn.synset("hearing.n.06"),
				wn.synset("hearing.n.05"),
				wn.synset("hearing.n.02"),
				wn.synset("earshot.n.01"),
				wn.synset("audition.n.02"),
				wn.synset("hearing.n.01"),
				wn.synset("listening.n.01")],

	# homeward
	"U+498d":   [wn.synset("homeward.s.01")],

	# iris
	"U+4992":   [wn.synset("iris.n.01"),
				wn.synset("iris.n.02"),
				wn.synset("iris.n.03")],

	# labyrinth, maze
	"U+4993":   [wn.synset("maze.n.01")],

	# Lapps, Lapplander, Sami
	"U+4994":   [wn.synset("lapp.n.01"),
				wn.synset("lapp.n.02"),
				wn.synset("patch.n.03")],

	# Latvia
	"U+4996":   [wn.synset("latvia.n.01")],

	# Latvian
	"U+499a":   [wn.synset("latvian.n.01"),
				wn.synset("latvian.n.02")],

	# lick
	"U+499d":   [wn.synset("lick.v.02")],

	# lower leg, shank, shin
	"U+499f":   [wn.synset("bet.n.02"),
				wn.synset("tibia.n.01"),
				wn.synset("shin.n.03"),
				wn.synset("shank.n.08"),
				wn.synset("shin.n.02"),
				wn.synset("shank.n.05"),
				wn.synset("shank.n.04"),
				wn.synset("shin.n.01"),
				wn.synset("shank.n.06"),
				wn.synset("shank.n.01"),
				wn.synset("cannon.n.05"),
				wn.synset("shank.n.03"),
				wn.synset("shank.n.02")],

	# magic
	"U+49a0":   [wn.synset("magic_trick.n.01"),
				wn.synset("magic.n.01")],

	# magical
	"U+49a1":   [wn.synset("charming.s.02")],

	# manhole cover
	"U+49a2":   [wn.synset("manhole_cover.n.01")],

	# midnight sun
	"U+49a3":   [wn.synset("midnight_sun.n.01")],

	# milkmaid, dairymaid
	"U+49a4":   [wn.synset("dairymaid.n.01")],

	# millepede
	"U+49a6":   [wn.synset("millipede.n.01")],

	# mother's milk
	"U+49a7":   [wn.synset("mother's_milk.n.01")],

	# myth
	"U+49a9":   [wn.synset("myth.n.01")],

	# northward
	"U+49aa":   [wn.synset("northbound.s.01")],

	# open one's mouth, hold one's mouth open, gape
	"U+49ab":   [wn.synset("goggle.v.01"),
				wn.synset("gape.v.02")],

	# overturn, turn over, tip over
	"U+49ad":   [wn.synset("overturn.v.02"),
				wn.synset("overturn.v.01"),
				wn.synset("roll.v.01"),
				wn.synset("turn_over.v.05"),
				wn.synset("topple.v.02"),
				wn.synset("revoke.v.02"),
				wn.synset("overrule.v.01"),
				wn.synset("pass.v.05"),
				wn.synset("revolutionize.v.01"),
				wn.synset("consider.v.05"),
				wn.synset("turn.v.10"),
				wn.synset("flip.v.08"),
				wn.synset("dig.v.01"),
				wn.synset("overthrow.v.01")],

	# paper clip
	"U+49ae":   [wn.synset("paper_clip.n.01")],

	# polar bear
	"U+49b1":   [wn.synset("ice_bear.n.01")],

	# raindrop
	"U+49b3":   [wn.synset("raindrop.n.01")],

	# sandstorm
	"U+49b7":   [wn.synset("dust_storm.n.01")],

	# way
	"U+49b9":   [wn.synset("way.n.05"),
				wn.synset("means.n.01")],

	# sight, vision, visual sense
	"U+49bd":   [wn.synset("sight.n.03")],

	# sole
	"U+49be":   [wn.synset("sole.n.02"),
				wn.synset("sole.n.03"),
				wn.synset("sole.n.01"),
				wn.synset("sole.n.04")],

	# southward
	"U+49c0":   [wn.synset("southbound.s.01")],

	# sprout, germinate
	"U+49c1":   [wn.synset("shoot.v.19")],

	# summer house, summerhouse
	"U+49c3":   [wn.synset("summer_house.n.01"),
				wn.synset("gazebo.n.01")],

	# thigh, upper leg
	"U+49c8":   [wn.synset("thigh.n.01")],

	# thread, string, cord
	"U+49ca":   [wn.synset("thread.n.01"),
				wn.synset("cord.n.04"),
				wn.synset("string.n.01")],

	# trapeze
	"U+49cd":   [wn.synset("trapeze.n.01")],

	# T shirt, tee shirt, jersey
	"U+49ce":   [wn.synset("jersey.n.03"),
				wn.synset("jersey.n.02"),
				wn.synset("jersey.n.05"),
				wn.synset("jersey.n.04"),
				wn.synset("new_jersey.n.01")],

	# tuft of grass, tussock
	"U+49cf":   [wn.synset("tuft.n.01")],

	# watchdog
	"U+49d0":   [wn.synset("watchdog.n.01"),
				wn.synset("watchdog.n.02")],

	# very much, very many
	"U+49d2":   [wn.synset("a_lot.r.01")],

	# westward
	"U+49d3":   [wn.synset("westbound.s.01")],

	# woodpecker
	"U+49d7":   [wn.synset("woodpecker.n.01")],

	# zigzag
	"U+49d9":   [wn.synset("zigzag.s.01")],

	# beyond, past
	"U+49de":   [wn.synset("past.s.02"),
				wn.synset("past.a.01"),
				wn.synset("beyond.r.02"),
				wn.synset("beyond.r.03"),
				wn.synset("beyond.r.01")],

	# binoculars, field glass
	"U+49df":   [wn.synset("binoculars.n.01")],

	# broadband
	"U+49e2":   [wn.synset("broadband.a.02"),
				wn.synset("broadband.a.01")],

	# control
	"U+49e5":   [wn.synset("control.n.05"),
				wn.synset("control.n.03"),
				wn.synset("control.n.02"),
				wn.synset("control.n.01"),
				wn.synset("command.n.06"),
				wn.synset("dominance.n.02"),
				wn.synset("restraint.n.02")],

	# corruption
	"U+49e6":   [wn.synset("corruption.n.04"),
				wn.synset("corruption.n.05"),
				wn.synset("corruption.n.06"),
				wn.synset("putrescence.n.01"),
				wn.synset("corruption.n.03"),
				wn.synset("bribery.n.01"),
				wn.synset("corruptness.n.02")],

	# Danish
	"U+49e9":   [wn.synset("danish.n.01"),
				wn.synset("danish.n.02")],

	# Denmark
	"U+49ea":   [wn.synset("denmark.n.01")],

	# disability, handicap, impairment
	"U+49eb":   [wn.synset("disability.n.01")],

	# disability benefit
	"U+49ec":   [wn.synset("pension.n.01"),
				wn.synset("disability_benefit.n.01")],

	# disabled, impaired, handicapped, mentally)
	"U+49ed":   [wn.synset("impaired.a.01"),
				wn.synset("disabled.s.01"),
				wn.synset("afflicted.s.02")],

	# intellectual impairment, cognitive impairment, mental impairment
	"U+49ee":   [wn.synset("retarded.a.01")],

	# distance
	"U+49f3":   [wn.synset("distance.n.01"),
				wn.synset("distance.n.03"),
				wn.synset("distance.n.04"),
				wn.synset("distance.n.05"),
				wn.synset("distance.n.06")],

	# empower
	"U+49f4":   [wn.synset("authorize.v.01"),
				wn.synset("mandate.v.03"),
				wn.synset("endow.v.01"),
				wn.synset("empower.v.01"),
				wn.synset("entitle.v.02"),
				wn.synset("accredit.v.02")],

	# empowerment
	"U+49f5":   [wn.synset("authorization.n.04"),
				wn.synset("mandate.n.01")],

	# empowered
	"U+49f6":   [wn.synset("empowered.s.01"),
				wn.synset("authorized.a.01")],

	# eternal
	"U+49f7":   [wn.synset("ageless.s.01")],

	# eternity, infinity
	"U+49f8":   [wn.synset("eternity.n.03"),
				wn.synset("eternity.n.02"),
				wn.synset("eternity.n.01")],

	# infiniteness, boundlessness, limitlessness
	"U+49fa":   [wn.synset("infiniteness.n.01")],

	# fat, thick
	"U+49fe":   [wn.synset("thick.a.01")],

	# gym, gymnasium
	"U+49ff":   [wn.synset("gymnasium.n.02")],

	# gym mat
	"U+4a00":   [wn.synset("mat.n.03")],

	# Halloween, All Saint's Day
	"U+4a01":   [wn.synset("halloween.n.01")],

	# hearing impairment
	"U+4a02":   [wn.synset("hearing_impairment.n.01")],

	# hearing impaired
	"U+4a03":   [wn.synset("hard-of-hearing.s.01")],

	# infinite, limitless
	"U+4a04":   [wn.synset("infinite.a.01")],

	# lacrosse
	"U+4a05":   [wn.synset("lacrosse.n.01")],

	# limited, restricted, confined
	"U+4a06":   [wn.synset("restricted.a.01"),
				wn.synset("limited.a.01")],

	# Loki
	"U+4a07":   [wn.synset("loki.n.01")],

	# long jump
	"U+4a08":   [wn.synset("broad_jump.n.02"),
				wn.synset("long_jump.n.01")],

	# odometer
	"U+4a09":   [wn.synset("odometer.n.01")],

	# placenta
	"U+4a0a":   [wn.synset("placenta.n.02")],

	# speech impaired
	"U+4a0f":   [wn.synset("gruffness.n.01")],

	# speech impairment, dysarthria
	"U+4a10":   [wn.synset("dysarthria.n.01")],

	# table tennis, ping pong
	"U+4a14":   [wn.synset("table_tennis.n.01")],

	# visual impairment
	"U+4a17":   [wn.synset("visual_impairment.n.01")],

	# visually impaired
	"U+4a18":   [wn.synset("dim-sighted.s.01")],

	# uncharted
	"U+4a1b":   [wn.synset("chartless.s.01")],

	# backwater
	"U+4a1c":   [wn.synset("backwater.n.02"),
				wn.synset("backwater.n.01")],

	# unfashionable
	"U+4a1d":   [wn.synset("unfashionable.a.01")],

	# such
	"U+4a1e":   [wn.synset("such.s.01")],

	# chant
	"U+4a1f":   [wn.synset("chant.n.01")],

	# resume
	"U+4a20":   [wn.synset("curriculum_vitae.n.01"),
				wn.synset("sketch.n.03")],

	# testament
	"U+4a22":   [wn.synset("testament.n.03"),
				wn.synset("testament.n.01"),
				wn.synset("will.n.03"),
				wn.synset("testament.n.04")],

	# genesis
	"U+4a24":   [wn.synset("genesis.n.01"),
				wn.synset("genesis.n.02")],
}
'''