function [ ] = SamplePlot( samples,N )
%UNTITLED4 �˴���ʾ�йش˺�����ժҪ

%   ����������ֲ�ͼ
%   ��N���ֲ��������������һ��ͼ��

    for i = 1:N
        plot(samples{i}(:,1),samples{i}(:,2),'r+');
        hold on;
    end

end

