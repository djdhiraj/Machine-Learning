import io

def graph(request):
    f = matplotlib.figure.Figure()

    pos = np.arange(10) + 2

    fig = plt.figure(figsize=(8, 3))
    ax = fig.add_subplot(111)

    ax.barh(pos, np.arange(1, 11), align='center')
    ax.set_yticks(pos)
    ax.set_yticklabels(('#hcsm',
                        '#ukmedlibs',
                        '#ImmunoChat',
                        '#HCLDR',
                        '#ICTD2015',
                        '#hpmglobal',
                        '#BRCA',
                        '#BCSM',
                        '#BTSM',
                        '#OTalk',),
                       fontsize=15)
    ax.set_xticks([])
    ax.invert_yaxis()

    ax.set_xlabel('Popularity')
    ax.set_ylabel('Hashtags')
    ax.set_title('Hashtags')

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(f)
    response = HttpResponse(buffer.getvalue(), content_type='image/png')
    return response
