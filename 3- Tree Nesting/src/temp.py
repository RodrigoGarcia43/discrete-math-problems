
typedef long long ll;
inline int read(){
	int w=0,x=0;char c=getchar();
	while(!isdigit(c))w|=c=='-',c=getchar();
	while(isdigit(c))x=(x<<3)+(x<<1)+(c^48),c=getchar();
	return w?-x:x;
}


namespace star
{
	const int maxn=1005,mod=1e9+7,maxf=(1<<12);
	int n,m;
	struct tree{
		int n,ecnt,head[maxn],bit[maxn],to[maxn<<1],nxt[maxn<<1];
		vector<int> son[maxn];

		inline void addedge(int a,int b){
			to[++ecnt]=b, nxt[ecnt]=head[a], head[a]=ecnt;
			to[++ecnt]=a, nxt[ecnt]=head[b], head[b]=ecnt;
		}

        inline void init(){
			n=read();
			for(int i=1;i<n;i++)addedge(read(),read());
		}


		void dfs(int x,int fa)
        {
			son[x].clear(); bit[x]=0;
			for(int i=head[x]; i ;i=nxt[i]){
				int u=to[i];
				if(u==fa)continue;
				son[x].push_back(u);
				dfs(u,x);
				bit[x] |= (1<<(u-1));
			}
		}

	}S,T;


	inline ll fpow(ll a,int b){
		ll ans=1;
		for( ;b ; b>>=1, a = a * a%mod ) if(b&1) ans = ans * a%mod;
		return ans;
	}

	ll f[maxn][maxf],ans1,ans2;
	bool vis[maxn][maxf];

	ll dfs(int x,int id,int d){
		if(!id) return !d;

		int u=S.son[x][id-1];

		if(vis[u][d]) return f[u][d];

		vis[u][d]=1;

		ll sum=dfs(x,id-1,d);

		for(int i=0; i<T.n; i++)
			if (d>>i & 1)
			    sum=(sum + dfs(x, id-1, d^(1<<i) ) * dfs(u, S.son[u].size(), T.bit[i+1]) %mod) %mod;

		return f[u][d]=sum;
	}

	inline void work(){
		S.init(),T.init();
		S.dfs(1,0);

		for(int i=1;i<=T.n;i++){
			memset(vis,0,sizeof vis);
			memset(f,0,sizeof f);
			T.dfs(i,0);
			for(int j=1;j<=S.n;j++)
				ans1=(ans1 + dfs(j,S.son[j].size(),T.bit[i]) ) %mod;
		}

		S=T;
		S.dfs(1,0);
		for(int i=1;i<=T.n;i++){
			memset(vis,0,sizeof vis);
			memset(f,0,sizeof f);
			T.dfs(i,0);
			ans2=(ans2+dfs(1,S.son[1].size(),T.bit[i]))%mod;
		}
		printf("%lld\n",ans1*fpow(ans2,mod-2)%mod);
	}
}

signed main(){
	star::work();
	return 0;
}
