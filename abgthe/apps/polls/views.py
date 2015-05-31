# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, RedirectView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from .models import Poll, Item, SixListRanking, PurchaseAccept
from .forms import ItemsForm, PollSixListForm, PollPurchaseForm, AcceptsForm
from django.core.exceptions import MultipleObjectsReturned, ValidationError
from django.http import HttpResponseRedirect
from django.contrib import messages

class PollListView(LoginRequiredMixin, ListView):
    
    model = Poll

class PollSixListCreateView(LoginRequiredMixin, CreateView):

	model = Poll
	form_class = PollSixListForm
	template_name = 'polls/poll_add.html'

	def  get_success_url(self):
		return reverse('polls:poll_list')

	def get_initial(self):
		return {'poll_type':"sixlistpoll",'create_user': self.request.user}

class PollPurchaseCreateView(LoginRequiredMixin, CreateView):

	model = Poll
	form_class = PollPurchaseForm
	template_name = 'polls/poll_add.html'

	def  get_success_url(self):
		return reverse('polls:poll_list')

	def get_initial(self):
		return {'poll_type':"purchasepoll",'create_user': self.request.user}

class PollPurchaseDetailView(LoginRequiredMixin, DetailView):

	model = Poll
	template_name = 'polls/poll_purchase_detail.html'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(PollPurchaseDetailView, self).get_context_data(**kwargs)

		user = self.object.poll_purchaseaccepts.filter(create_user=self.request.user)
		if user:
			context['user_vote'] = user[0]
		else:
			context['user_vote'] = None
		return context

class PurchaseAcceptCreateView(LoginRequiredMixin, CreateView):

	model = PurchaseAccept
	form_class = AcceptsForm
	template_name = 'polls/purchase_accept_add.html'

	def get_poll(self):
		return get_object_or_404(Poll, pk=self.kwargs['poll_pk'])

	def get(self, request, *args, **kwargs):
			
		if self.get_poll().status != 'aberta':
			messages.error(request, "Não é possivel votar nessa votação")
			return HttpResponseRedirect(reverse('polls:poll_purchase_detail', kwargs={'pk': self.kwargs['poll_pk']}))
		else:
			return super(PurchaseAcceptCreateView, self).get(request, *args, **kwargs)

	def  get_success_url(self):
		return reverse('polls:poll_purchase_detail', kwargs={'pk': self.kwargs['poll_pk']})

	def get_initial(self):
		return {'poll':self.get_poll(),'create_user': self.request.user}

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(PurchaseAcceptCreateView, self).get_context_data(**kwargs)
		context['poll'] = self.get_poll()
		return context

class PurchaseAcceptUpdateView(LoginRequiredMixin, UpdateView):

	model = PurchaseAccept
	form_class = AcceptsForm
	template_name = 'polls/purchase_accept_update.html'

	def get(self, request, *args, **kwargs):
		poll = get_object_or_404(Poll, pk=self.kwargs['poll_pk'])
		
		if poll.status != 'aberta':
			messages.error(request, "Não é possivel alterar votos dessa votação")
			return HttpResponseRedirect(reverse('polls:poll_purchase_detail', kwargs={'pk': self.kwargs['poll_pk']}))
		else:
			return super(PurchaseAcceptUpdateView, self).get(request, *args, **kwargs)

	def  get_success_url(self):
		return reverse('polls:poll_purchase_detail', kwargs={'pk': self.object.poll.pk})

class PurchaseAcceptDeleteView(LoginRequiredMixin, DeleteView):

	model = PurchaseAccept
	template_name = 'polls/purchase_accept_delete.html'

	def get(self, request, *args, **kwargs):
		poll = get_object_or_404(Poll, pk=self.kwargs['poll_pk'])

		if poll.status != 'aberta':
			messages.error(request, "Não é possivel deletar votos dessa votação")
			return HttpResponseRedirect(reverse('polls:poll_purchase_detail', kwargs={'pk': self.kwargs['poll_pk']}))
		else:
			return super(PurchaseAcceptDeleteView, self).get(request, *args, **kwargs)

	def  get_success_url(self):
		return reverse_lazy('polls:poll_purchase_detail', kwargs={'pk': self.object.poll.pk})
		

class ItemListView(LoginRequiredMixin, ListView):

	model = Item
	template_name = 'polls/poll_items_list.html'
	
	def get_queryset(self):
		return Item.objects.filter(poll__pk=self.kwargs['poll_pk'])

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(ItemListView, self).get_context_data(**kwargs)

		poll = get_object_or_404(Poll, pk=self.kwargs['poll_pk'])
		context['poll'] = poll
		user = self.get_queryset().filter(create_user=self.request.user)
		if user:
			context['user_item'] = user[0]
		else:
			context['user_item'] = None
		return context

class PollSixListDetailView(LoginRequiredMixin, DetailView):

	model = Poll
	template_name = 'polls/poll_sixlist_detail.html'


	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(PollSixListDetailView, self).get_context_data(**kwargs)

		if self.object.poll_itens:
			ordered_itens = sorted(self.object.poll_itens.all(), key=lambda a: a.parcial())
		else:
			ordered_itens = None
		context['itens'] = ordered_itens

		user = self.object.poll_itens.filter(create_user=self.request.user)
		if user:
			context['user_item'] = user[0]
		else:
			context['user_item'] = None
		return context

class ItemSixListCreateView(LoginRequiredMixin, CreateView):

	model = Item
	form_class = ItemsForm
	template_name = 'polls/sixlist_item_add.html'

	def get_poll(self):
		return get_object_or_404(Poll, pk=self.kwargs['poll_pk'])

	def get(self, request, *args, **kwargs):
			
		if self.get_poll().status != 'aberta':
			messages.error(request, "Não é possivel indicar item nessa votação")
			return HttpResponseRedirect(reverse('polls:poll_sixlist_detail', kwargs={'pk': self.kwargs['poll_pk']}))
		else:
			return super(ItemSixListCreateView, self).get(request, *args, **kwargs)

	def  get_success_url(self):
		return reverse('polls:poll_sixlist_detail', kwargs={'pk': self.kwargs['poll_pk']})

	def get_initial(self):
		return {'poll':self.get_poll(),'create_user': self.request.user}

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(ItemSixListCreateView, self).get_context_data(**kwargs)
		context['poll'] = self.get_poll()
		return context

class ItemSixListUpdateView(LoginRequiredMixin, UpdateView):

	model = Item
	form_class = ItemsForm
	template_name = 'polls/sixlist_item_update.html'

	def get(self, request, *args, **kwargs):
		poll = get_object_or_404(Poll, pk=self.kwargs['poll_pk'])
		
		if poll.status != 'aberta':
			messages.error(request, "Não é possivel alterar item dessa votação")
			return HttpResponseRedirect(reverse('polls:poll_sixlist_detail', kwargs={'pk': self.kwargs['poll_pk']}))
		else:
			return super(ItemSixListUpdateView, self).get(request, *args, **kwargs)

	def  get_success_url(self):
		return reverse('polls:poll_sixlist_detail', kwargs={'pk': self.object.poll.pk})

class ItemSixListDeleteView(LoginRequiredMixin, DeleteView):

	model = Item
	template_name = 'polls/sixlist_item_delete.html'

	def get(self, request, *args, **kwargs):
		poll = get_object_or_404(Poll, pk=self.kwargs['poll_pk'])

		if poll.status != 'aberta':
			messages.error(request, "Não é possivel deletar item dessa votação")
			return HttpResponseRedirect(reverse('polls:poll_sixlist_detail', kwargs={'pk': self.kwargs['poll_pk']}))
		else:
			return super(ItemSixListDeleteView, self).get(request, *args, **kwargs)

	def  get_success_url(self):
		return reverse_lazy('polls:poll_sixlist_detail', kwargs={'pk': self.object.poll.pk})


class SixListRankingView(View):

	http_method_names=['post']

	def post(self, request, *args, **kwargs):

		poll = get_object_or_404(Poll, pk=self.kwargs['poll_pk'])

		if poll.status != 'ranqueamento':
			messages.error(request, "Não é possivel fazer ranqueamento de votações abertas ou fechadas")
			return HttpResponseRedirect(reverse('polls:poll_sixlist_detail', kwargs={'pk': self.kwargs['poll_pk']}))
		
		itens = request.POST.getlist('itens[]')
		rankings = request.POST.getlist('rankings[]')
		user = self.request.user

		try:
			for index in range(len(itens)):
				i = get_object_or_404(Item,pk=itens[index])
				rank, created  = SixListRanking.objects.get_or_create(item=i, create_user=user, defaults={'ranking': 0})
				rank.ranking = int(rankings[index])
				rank.save()

			return HttpResponseRedirect(reverse('polls:poll_sixlist_detail', kwargs={'pk': self.kwargs['poll_pk']}))

		except  MultipleObjectsReturned:
			messages.error(request, "Não é possivel fazer ranqueamento da lista submetida")
			return HttpResponseRedirect(reverse('polls:poll_sixlist_detail', kwargs={'pk': self.kwargs['poll_pk']}))